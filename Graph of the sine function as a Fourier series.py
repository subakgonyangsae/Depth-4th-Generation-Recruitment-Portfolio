import numpy as np
import matplotlib.pyplot as plt

# [x 값을 -2π에서 2π까지 생성]
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# [y 값을 사인 함수로 계산]
y = np.sin(x)

# [그래프 그리기]
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='sin(x)', color='blue')
plt.title('Sine Function')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()
plt.show()