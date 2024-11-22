# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ln_5CAlmg9HCtTj_G-TtEqKX9sdCej3F
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,6])
y=np.array([0,250])

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Yangi x va y qiymatlari (Heartbeat-like pattern)
x = np.array([0, 1, 2, 3, 4,4.2, 4.4,5,6,7,8,9,10])  # x values showing the time axis
y = np.array([0, 0, 1, 0, 0, 2, 0, -0.5,0,0,1,0,0])  # y values simulating the heartbeat

plt.plot(x, y)
plt.title("Heartbeat Simulation")
plt.xlabel("Time (seconds)")
plt.ylabel("Pulse (Amplitude)")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4,4.2, 4.4,5,6,7,8,9,10])
y = np.array([0, 0, 1, 0, 0, 2, 0, -0.5,0,0,1,0,0])

# plt.plot(x, y)
plt.title("Heartbeat Simulation")
plt.xlabel("Time (seconds)")
plt.ylabel("Pulse (Amplitude)")
plt.grid(True)
plt.plot(y,marker='o')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4,4.2, 4.4,5,6,7,8,9,10])
y = np.array([0, 0, 1, 0, 0, 2, 0, -0.5,0,0,1,0,0])

# plt.plot(x, y)
plt.title("Heartbeat Simulation")
plt.xlabel("Time (seconds)")
plt.ylabel("Pulse (Amplitude)")
plt.grid(True)
plt.plot(y,'o:r')
plt.plot(y,color='red')
plt.show()