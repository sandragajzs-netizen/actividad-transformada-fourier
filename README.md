# Actividad Formativa 2 — Simulación y análisis de señales con la Transformada de Fourier

## Descripción

Este proyecto implementa en Python una simulación básica para analizar señales en el dominio del tiempo y de la frecuencia mediante la Transformada Discreta de Fourier (DFT), utilizando la FFT.

Se estudian:

- Pulso rectangular.
- Función escalón.
- Señal senoidal de 10 Hz.
- Magnitud del espectro.
- Fase del espectro.
- Propiedad de linealidad.
- Propiedad de desplazamiento temporal.
- Escalamiento en frecuencia.

## Requisitos

- Python 3.x
- NumPy
- Matplotlib

## Instalación de librerías

```bash
pip install numpy matplotlib
```

## Ejecución

Desde la carpeta del proyecto:

```bash
python transformada_fourier.py
```

El programa genera las gráficas de las señales y sus espectros directamente en pantalla.

## Estructura

```text
Proyecto_Transformada_Fourier/
│
├── transformada_fourier.py
├── README.md
│
└── graficas/
    ├── 01_dominio_tiempo.png
    ├── 02_magnitud_espectro.png
    ├── 03_fase_espectro.png
    ├── 04_linealidad.png
    ├── 05_desplazamiento_tiempo.png
    ├── 06_desplazamiento_magnitud.png
    └── 07_escalamiento_frecuencia.png
```

## Descripción de los resultados

El pulso rectangular presenta un espectro distribuido alrededor de bajas frecuencias. La función escalón contiene un conjunto amplio de componentes frecuenciales. La señal senoidal de 10 Hz concentra sus componentes principales en +10 Hz y -10 Hz.

La propiedad de linealidad se observa al combinar señales senoidales de diferentes frecuencias. El desplazamiento temporal conserva esencialmente la magnitud del espectro y modifica la fase. Finalmente, al cambiar una señal de 10 Hz a 20 Hz, sus componentes principales se desplazan hacia ±20 Hz.

## Aplicaciones

La Transformada de Fourier se utiliza en procesamiento de audio, telecomunicaciones, procesamiento de imágenes, análisis de vibraciones, radar, comunicaciones digitales y otras áreas de ingeniería.

## Autor

Nombre del estudiante: ______________________________

Actividad Formativa 2 — Señales y Sistemas.
