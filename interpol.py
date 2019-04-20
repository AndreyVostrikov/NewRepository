import matplotlib.pyplot as plt
import function as fun
import numpy as np


cx, cy = fun.openFile('coord')
yarray = np.array(cy, dtype=float)
xarray = np.array(cx, dtype=float)
xnew = np.linspace(np.min(xarray), np.max(yarray))
ynew = [fun.funLagranz(xarray, yarray, i) for i in xnew]
plt.plot(xnew, ynew, 'red')
plt.scatter(cx, cy, color='black')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(("Interpol F(x)", "F(x)"))
plt.show()
