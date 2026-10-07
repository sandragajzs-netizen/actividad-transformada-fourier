# ============================================================
# ACTIVIDAD FORMATIVA 2
# Simulación y análisis de señales con la Transformada de Fourier
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. CONFIGURACIÓN DEL TIEMPO
# ------------------------------------------------------------
Fs = 1000  # Frecuencia de muestreo en Hz
t = np.arange(-1, 1, 1 / Fs)

# ------------------------------------------------------------
# 2. DEFINICIÓN DE SEÑALES
# ------------------------------------------------------------
# Pulso rectangular
pulso = np.where((t >= -0.2) & (t <= 0.2), 1, 0)

# Función escalón
escalon = np.where(t >= 0, 1, 0)

# Señal senoidal de 10 Hz
f0 = 10
senoidal = np.sin(2 * np.pi * f0 * t)

# ------------------------------------------------------------
# 3. FUNCIÓN PARA CALCULAR LA FFT
# ------------------------------------------------------------
def calcular_fft(señal, Fs):
    N = len(señal)

    # Transformada Discreta de Fourier
    X = np.fft.fft(señal)

    # Centrar frecuencias negativas y positivas
    X_shift = np.fft.fftshift(X)

    # Vector de frecuencias
    frecuencias = np.fft.fftshift(np.fft.fftfreq(N, 1 / Fs))

    # Magnitud normalizada
    magnitud = np.abs(X_shift) / N

    # Fase
    fase = np.angle(X_shift)

    return frecuencias, magnitud, fase

# ------------------------------------------------------------
# 4. FFT DE LAS SEÑALES
# ------------------------------------------------------------
f_pulso, mag_pulso, fase_pulso = calcular_fft(pulso, Fs)
f_escalon, mag_escalon, fase_escalon = calcular_fft(escalon, Fs)
f_senoidal, mag_senoidal, fase_senoidal = calcular_fft(senoidal, Fs)

# ------------------------------------------------------------
# 5. SEÑALES EN EL DOMINIO DEL TIEMPO
# ------------------------------------------------------------
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, pulso)
plt.title("Pulso rectangular - Dominio del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, escalon)
plt.title("Función escalón - Dominio del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, senoidal)
plt.title("Señal senoidal - Dominio del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 6. MAGNITUD DEL ESPECTRO
# ------------------------------------------------------------
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(f_pulso, mag_pulso)
plt.xlim(-30, 30)
plt.title("Espectro de magnitud - Pulso rectangular")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(f_escalon, mag_escalon)
plt.xlim(-30, 30)
plt.title("Espectro de magnitud - Función escalón")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(f_senoidal, mag_senoidal)
plt.xlim(-30, 30)
plt.title("Espectro de magnitud - Señal senoidal")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid(True)

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 7. FASE DEL ESPECTRO
# ------------------------------------------------------------
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(f_pulso, fase_pulso)
plt.xlim(-30, 30)
plt.title("Espectro de fase - Pulso rectangular")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (rad)")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(f_escalon, fase_escalon)
plt.xlim(-30, 30)
plt.title("Espectro de fase - Función escalón")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (rad)")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(f_senoidal, fase_senoidal)
plt.xlim(-30, 30)
plt.title("Espectro de fase - Señal senoidal")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (rad)")
plt.grid(True)

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 8. PROPIEDAD DE LINEALIDAD
# ------------------------------------------------------------
f1 = 5
f2 = 15

x1 = np.sin(2 * np.pi * f1 * t)
x2 = 0.5 * np.sin(2 * np.pi * f2 * t)

a = 2
b = 3

combinacion = a * x1 + b * x2

f_comb, mag_combinacion, _ = calcular_fft(combinacion, Fs)

plt.figure(figsize=(12, 6))
plt.plot(f_comb, mag_combinacion)
plt.xlim(-30, 30)
plt.title("Propiedad de linealidad de la Transformada de Fourier")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()

# ------------------------------------------------------------
# 9. PROPIEDAD DE DESPLAZAMIENTO TEMPORAL
# ------------------------------------------------------------
x_original = np.sin(2 * np.pi * 10 * t)

desplazamiento = 0.2
x_desplazada = np.sin(2 * np.pi * 10 * (t - desplazamiento))

f_original, mag_original, fase_original = calcular_fft(x_original, Fs)
f_desplazada, mag_desplazada, fase_desplazada = calcular_fft(
    x_desplazada, Fs
)

plt.figure(figsize=(12, 6))
plt.plot(t, x_original, label="Señal original")
plt.plot(t, x_desplazada, label="Señal desplazada")
plt.xlim(-0.5, 0.5)
plt.title("Propiedad de desplazamiento temporal")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(f_original, mag_original, label="Señal original")
plt.plot(f_desplazada, mag_desplazada, "--", label="Señal desplazada")
plt.xlim(-30, 30)
plt.title("Desplazamiento temporal: comparación del espectro")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.grid(True)
plt.show()

# ------------------------------------------------------------
# 10. ESCALAMIENTO EN FRECUENCIA
# ------------------------------------------------------------
x_10 = np.sin(2 * np.pi * 10 * t)
x_20 = np.sin(2 * np.pi * 20 * t)

f_10, mag_10, _ = calcular_fft(x_10, Fs)
f_20, mag_20, _ = calcular_fft(x_20, Fs)

plt.figure(figsize=(12, 6))
plt.plot(f_10, mag_10, label="Señal de 10 Hz")
plt.plot(f_20, mag_20, label="Señal de 20 Hz")
plt.xlim(-40, 40)
plt.title("Escalamiento en frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.legend()
plt.grid(True)
plt.show()

# ------------------------------------------------------------
# 11. RESUMEN
# ------------------------------------------------------------
print("=" * 55)
print("ANÁLISIS DE LA TRANSFORMADA DE FOURIER")
print("=" * 55)

print("\n1. Pulso rectangular:")
print("Su espectro presenta componentes distribuidas alrededor de 0 Hz.")

print("\n2. Función escalón:")
print("Presenta un contenido amplio de frecuencias.")

print("\n3. Señal senoidal:")
print("Presenta componentes principales en +10 Hz y -10 Hz.")

print("\n4. Linealidad:")
print("La transformada conserva la combinación lineal de las señales.")

print("\n5. Desplazamiento temporal:")
print("El desplazamiento modifica principalmente la fase,")
print("mientras que la magnitud del espectro se conserva.")

print("\n6. Escalamiento en frecuencia:")
print("Al aumentar la frecuencia, las componentes espectrales")
print("se desplazan hacia frecuencias mayores.")

print("\n" + "=" * 55)
print("FIN DE LA SIMULACIÓN")
print("=" * 55)
