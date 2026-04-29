#include <Servo.h>

// Pines del sensor ultrasónico HC-SR04
const int trigPin = 8;
const int echoPin = 9;

// Pin del servo
const int servoPin = 10;

Servo miServo;

long duracion;
float distanciaCm;

void setup() {
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  miServo.attach(servoPin);

  Serial.println("Radar con Servo y HC-SR04");
  Serial.println("Angulo,Distancia_cm");
}

void loop() {
  // Barrido de 0 a 180 grados
  for (int angulo = 0; angulo <= 180; angulo++) {
    miServo.write(angulo);
    delay(30); // Tiempo para que el servo se mueva

    distanciaCm = medirDistancia();

    Serial.print(angulo);
    Serial.print(",");
    Serial.println(distanciaCm);
  }

  // Barrido de 180 a 0 grados
  for (int angulo = 180; angulo >= 0; angulo--) {
    miServo.write(angulo);
    delay(30);

    distanciaCm = medirDistancia();

    Serial.print(angulo);
    Serial.print(",");
    Serial.println(distanciaCm);
  }
}

// Función para medir distancia con el HC-SR04
float medirDistancia() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Timeout de 30 ms para evitar bloqueos
  duracion = pulseIn(echoPin, HIGH, 30000);

  // Si no detecta eco, regresa 0
  if (duracion == 0) {
    return 0;
  }

  // Calcular distancia en centímetros
  float distancia = duracion * 0.0343 / 2;

  return distancia;
}
