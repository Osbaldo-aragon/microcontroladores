# Radar Ultrasónico con Arduino, HC-SR04, Servo y PyQt5

Este proyecto implementa un radar ultrasónico básico utilizando un sensor **HC-SR04**, un **servomotor** y una interfaz gráfica desarrollada en **Python con PyQt5**.  
El sistema realiza un barrido de **0° a 180°**, mide la distancia en cada ángulo y envía los datos por el puerto serial para visualizarlos en una interfaz tipo radar.

## Descripción del Proyecto

El servomotor mueve el sensor ultrasónico HC-SR04 de forma gradual, simulando el funcionamiento de un radar. En cada posición angular, el sensor mide la distancia a los objetos cercanos y Arduino envía la información a la computadora mediante comunicación serial.

La aplicación en Python recibe los datos del puerto COM y dibuja en tiempo real:

- El ángulo actual del sensor.
- La distancia detectada.
- Una línea de barrido.
- Puntos de detección en una gráfica semicircular tipo radar.

## Tecnologías Utilizadas

- Arduino UNO o compatible
- Sensor ultrasónico HC-SR04
- Servomotor SG90 o similar
- Python 3
- PyQt5
- PySerial

## Estructura del Repositorio

```text
radar_arduino/
│
├── arduino/
│   └── radar_hcsr04_servo.ino
│
├── python/
│   └── radar_pyqt5.py
│
├── esquema/
│   └── esquema_conexion.png
│
├── README.md
└── requirements.txt
