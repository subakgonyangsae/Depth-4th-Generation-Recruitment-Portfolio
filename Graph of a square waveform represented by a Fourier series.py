import numpy as np
import matplotlib.pyplot as plt

# [사각파의 파라미터]
A = 1
T = 2 * np.pi
n_terms = 10

# [시간 배열 생성]
t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# [Fourier 급수 계산]
fourier_series = np.zeros_like(t)

for n in range(1, n_terms + 1):
    if n % 2 == 1:
        fourier_series += (4 * A / (np.pi * n)) * np.sin(n * (2 * np.pi / T) * t)

# [그래프 그리기]
plt.figure(figsize=(12, 6))
plt.plot(t, fourier_series, label='Fourier Series Approximation', color='blue')
plt.title('Fourier Series Representation of a Square Wave')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.legend()
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.ylim(-1.5, 1.5)
plt.show()