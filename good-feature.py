import numpy as np

rabbits = 500
rats = 500

rabbit_length = 15 + 4 * np.random.randn(rabbits)
rar_length = 10 + 4 * np.random.randn(rats)

import matplotlib.pyplot as plot

plot.hist([rabbit_length, rat_length], stacked = True, color=['r', 'b'])
plot.show()
