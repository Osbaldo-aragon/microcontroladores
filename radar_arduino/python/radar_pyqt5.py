import sys
import math
import serial
import serial.tools.list_ports

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QHBoxLayout
)


# ==========================
# CONFIGURACIÓN GENERAL
# ==========================

BAUD_RATE = 9600
MAX_DISTANCE_CM = 200  # Distancia máxima que se dibuja en el radar


# ==========================
# HILO PARA LEER EL SERIAL
# ==========================

class SerialReader(QThread):
    data_received = pyqtSignal(int, float)
    status_changed = pyqtSignal(str)

    def __init__(self, port, baudrate=9600):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.running = False
        self.serial_connection = None

    def run(self):
        try:
            self.serial_connection = serial.Serial(
                self.port,
                self.baudrate,
                timeout=1
            )

            self.running = True
            self.status_changed.emit(f"Conectado a {self.port}")

            while self.running:
                line = self.serial_connection.readline().decode(errors="ignore").strip()

                if not line:
                    continue

                # Se espera formato: angulo,distancia
                # Ejemplo: 90,35.6
                try:
                    parts = line.split(",")

                    if len(parts) != 2:
                        continue

                    angle = int(float(parts[0]))
                    distance = float(parts[1])

                    if 0 <= angle <= 180:
                        self.data_received.emit(angle, distance)

                except ValueError:
                    # Ignora encabezados como: Angulo,Distancia_cm
                    continue

        except Exception as e:
            self.status_changed.emit(f"Error: {e}")

        finally:
            if self.serial_connection and self.serial_connection.is_open:
                self.serial_connection.close()

            self.status_changed.emit("Desconectado")

    def stop(self):
        self.running = False
        self.wait()


# ==========================
# WIDGET DEL RADAR
# ==========================

class RadarWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 500)

        self.current_angle = 90
        self.current_distance = 0

        # Diccionario para guardar la última distancia medida por ángulo
        self.points = {}

    def update_data(self, angle, distance):
        self.current_angle = angle
        self.current_distance = distance

        if 0 < distance <= MAX_DISTANCE_CM:
            self.points[angle] = distance

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()

        painter.fillRect(self.rect(), QColor(5, 10, 10))

        center_x = width // 2
        center_y = height - 40

        radar_radius = min(width // 2 - 40, height - 80)

        self.draw_grid(painter, center_x, center_y, radar_radius)
        self.draw_points(painter, center_x, center_y, radar_radius)
        self.draw_sweep_line(painter, center_x, center_y, radar_radius)
        self.draw_info(painter)

    def draw_grid(self, painter, center_x, center_y, radar_radius):
        grid_pen = QPen(QColor(0, 180, 80), 2)
        painter.setPen(grid_pen)

        # Arcos de distancia
        for i in range(1, 5):
            r = int(radar_radius * i / 4)

            painter.drawArc(
                center_x - r,
                center_y - r,
                2 * r,
                2 * r,
                0,
                180 * 16
            )

            distance_label = int(MAX_DISTANCE_CM * i / 4)

            painter.setFont(QFont("Arial", 9))
            painter.drawText(
                center_x + 10,
                center_y - r + 5,
                f"{distance_label} cm"
            )

        # Líneas angulares cada 30 grados
        for angle in range(0, 181, 30):
            rad = math.radians(angle)

            x = center_x + radar_radius * math.cos(rad)
            y = center_y - radar_radius * math.sin(rad)

            painter.drawLine(center_x, center_y, int(x), int(y))

            label_x = center_x + (radar_radius + 20) * math.cos(rad)
            label_y = center_y - (radar_radius + 20) * math.sin(rad)

            painter.drawText(
                int(label_x) - 15,
                int(label_y) + 5,
                f"{angle}°"
            )

        # Línea base
        painter.drawLine(
            center_x - radar_radius,
            center_y,
            center_x + radar_radius,
            center_y
        )

    def draw_points(self, painter, center_x, center_y, radar_radius):
        point_pen = QPen(QColor(255, 60, 60), 6)
        painter.setPen(point_pen)

        for angle, distance in self.points.items():
            if distance <= 0 or distance > MAX_DISTANCE_CM:
                continue

            rad = math.radians(angle)
            scaled_radius = (distance / MAX_DISTANCE_CM) * radar_radius

            x = center_x + scaled_radius * math.cos(rad)
            y = center_y - scaled_radius * math.sin(rad)

            painter.drawPoint(int(x), int(y))

    def draw_sweep_line(self, painter, center_x, center_y, radar_radius):
        sweep_pen = QPen(QColor(0, 255, 100), 3)
        painter.setPen(sweep_pen)

        rad = math.radians(self.current_angle)

        x = center_x + radar_radius * math.cos(rad)
        y = center_y - radar_radius * math.sin(rad)

        painter.drawLine(center_x, center_y, int(x), int(y))

    def draw_info(self, painter):
        painter.setPen(QPen(QColor(0, 255, 100)))
        painter.setFont(QFont("Arial", 14))

        painter.drawText(
            20,
            30,
            f"Ángulo: {self.current_angle}°"
        )

        painter.drawText(
            20,
            60,
            f"Distancia: {self.current_distance:.2f} cm"
        )

        painter.setFont(QFont("Arial", 10))
        painter.drawText(
            20,
            90,
            f"Escala máxima: {MAX_DISTANCE_CM} cm"
        )


# ==========================
# VENTANA PRINCIPAL
# ==========================

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Radar Ultrasónico con Arduino, HC-SR04 y PyQt5")
        self.resize(900, 600)

        self.serial_thread = None

        self.radar = RadarWidget()

        self.port_combo = QComboBox()
        self.refresh_ports()

        self.connect_button = QPushButton("Conectar")
        self.disconnect_button = QPushButton("Desconectar")
        self.disconnect_button.setEnabled(False)

        self.status_label = QLabel("Estado: Desconectado")

        self.connect_button.clicked.connect(self.connect_serial)
        self.disconnect_button.clicked.connect(self.disconnect_serial)

        top_layout = QHBoxLayout()
        top_layout.addWidget(QLabel("Puerto COM:"))
        top_layout.addWidget(self.port_combo)
        top_layout.addWidget(self.connect_button)
        top_layout.addWidget(self.disconnect_button)
        top_layout.addWidget(self.status_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.radar)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)

    def refresh_ports(self):
        self.port_combo.clear()

        ports = serial.tools.list_ports.comports()

        for port in ports:
            self.port_combo.addItem(port.device)

    def connect_serial(self):
        port = self.port_combo.currentText()

        if not port:
            self.status_label.setText("Estado: No se encontró puerto COM")
            return

        self.serial_thread = SerialReader(port, BAUD_RATE)
        self.serial_thread.data_received.connect(self.radar.update_data)
        self.serial_thread.status_changed.connect(self.update_status)
        self.serial_thread.start()

        self.connect_button.setEnabled(False)
        self.disconnect_button.setEnabled(True)

    def disconnect_serial(self):
        if self.serial_thread:
            self.serial_thread.stop()
            self.serial_thread = None

        self.connect_button.setEnabled(True)
        self.disconnect_button.setEnabled(False)
        self.status_label.setText("Estado: Desconectado")

    def update_status(self, message):
        self.status_label.setText(f"Estado: {message}")

    def closeEvent(self, event):
        self.disconnect_serial()
        event.accept()


# ==========================
# EJECUCIÓN DEL PROGRAMA
# ==========================

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
