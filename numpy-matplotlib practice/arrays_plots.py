#### Act 1 ####

import numpy as np


A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)
F = np.arange(3).reshape(3, 1)
D = A @ B @ C
E = np.divide(np.sqrt(D), 2)
x = np.linalg.solve(E, F)


print(f'A is\n{A}')
print('\n')
print(f'B is\n{B}')
print('\n')
print(f'C is\n{C}')
print('\n')
print(f'F is\n{F}')
print('\n')
print(f'D is\n{D.T}')
print('\n')
print(f'E is\n{E}')
print('\n')
print(f'X is\n{x}')
print('\n')

#### Act 2 ####
#### Parabola ####
import matplotlib.pyplot as plt
import numpy as np

plt.suptitle('Parabola')
x = np.linspace(-2, 2, 100)
f1, f2 = 2.0, 6.0

plt.plot(x, (1 / (4 * f1)) * x**2, 'r-', lw=2.0, label='F = 2')

plt.plot(x, (1 / (4 * f2)) * x**2, 'b-', lw=6.0, label="F = 6")

plt.axis([-2.0, 2.0, 0.0, 0.5])

plt.legend(shadow=True, loc="lower left")

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
