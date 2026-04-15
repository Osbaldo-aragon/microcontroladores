🔧 Microcontroladores
<div align="center">
![Lenguaje](https://img.shields.io/badge/Lenguaje-C-blue)
![Plataforma](https://img.shields.io/badge/Plataformas-PIC%20%7C%20ESP32-success)
![Compiler](https://img.shields.io/badge/Compiler-CCS%20C-orange)
![Simulación](https://img.shields.io/badge/Simulación-Proteus%208.11-informational)
![Licencia](https://img.shields.io/badge/Licencia-GPL%203.0-lightgrey)
</div>
Repositorio de proyectos y prácticas de microcontroladores orientados al aprendizaje de sistemas embebidos, con ejemplos desarrollados principalmente en PIC con CCS C y apoyo de simulación en Proteus 8.11.  
Incluye ejercicios de comunicación serial, lectura ADC, control de motores, seguimiento de línea y un proyecto adicional de robot RC con ESP32 y Bluetooth.
---
📘 ¿Qué encontrarás en este repositorio?
Este repositorio reúne ejemplos prácticos pensados para estudiantes, docentes y personas interesadas en la programación de microcontroladores. El enfoque está en mostrar implementaciones sencillas, funcionales y útiles como base para desarrollar proyectos más completos.
Contenido destacado
Comunicación serial con PIC18F2550  
Ejemplo básico de envío de mensajes por puerto serial a 9600 baudios, útil para pruebas iniciales de comunicación y depuración.
Lectura ADC y envío serial  
Proyecto en CCS C para adquisición de señales analógicas en múltiples canales y transmisión de lecturas por comunicación serial.
Seguidor de línea simulado  
Implementación de un robot seguidor de línea con PIC16F84A, acompañado de diagrama en Proteus e imagen de referencia.
Robot RC con ESP32  
Proyecto de control remoto mediante Bluetooth Serial, con manejo de velocidad por PWM y control de motores.
---
🗂️ Estructura del repositorio
```text
microcontroladores/
├── Comunicacion Serial/
│   └── Hola_mundo_18f2550.c
├── adc_serial_ccs/
│   └── adc_serial_ccs.c
├── simular seguidor CCS/
│   ├── Seguidor_16F84A.c
│   ├── Seguidor_diagrama_proteus.bmp
│   └── linea2.png
├── Robo_RC/
│   └── Robot_v1
├── LICENSE
└── README.md
```
---
⚙️ Tecnologías y herramientas utilizadas
CCS C Compiler para programación de microcontroladores PIC.
Proteus 8.11 para simulación de circuitos y validación de prácticas.
PIC18F2550 en ejemplos de comunicación serial y adquisición de datos.
PIC16F84A en la práctica de seguidor de línea.
ESP32 en el proyecto de robot RC con Bluetooth.
Puerto serial UART para monitoreo y transmisión de datos.
PWM para control de velocidad de motores.
---
🚀 Objetivo del repositorio
Proporcionar una base práctica para el aprendizaje de microcontroladores, integrando ejercicios que permitan comprender conceptos fundamentales de:
configuración de pines,
comunicación serial,
lectura de sensores,
control de actuadores,
lógica de navegación básica,
y simulación de sistemas embebidos.
Este material puede servir como apoyo en cursos de:
Microcontroladores
Sistemas embebidos
Electrónica digital
Robótica básica
Instrumentación y control
---
🧪 Cómo usar este repositorio
Clona o descarga este repositorio.
Abre el archivo fuente del proyecto que desees revisar.
Compílalo en CCS C si trabajas con PIC.
Si el proyecto incluye simulación, ábrelo en Proteus 8.11.
Para los ejemplos seriales, utiliza un monitor serial a 9600 baudios.
Adapta el código a tu hardware, frecuencia de reloj y conexiones.
---
🖼️ Vista previa
Seguidor de línea
![Seguidor de línea](simular%20seguidor%20CCS/linea2.png)
---
🎥 Material de apoyo
Los tutoriales y explicaciones complementarias se encuentran en el canal de YouTube:
Matemáticas en Corto  
https://www.youtube.com/@MatematicasEnCorto
---
👨‍💻 Autor
Osbaldo Aragón Banderas
Repositorio creado como apoyo para prácticas, demostraciones y aprendizaje en el área de microcontroladores y robótica.
---
📄 Licencia
Este proyecto se distribuye bajo la licencia GPL-3.0.  
Puedes consultar el archivo `LICENSE` para más detalles.
---
⭐ Nota final
Si este repositorio te resulta útil para tus clases, prácticas o proyectos, puedes usarlo como base, adaptarlo y mejorarlo para tus propias aplicaciones.
