import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

x = np.array([1,2,4])
y = np.array([12,10,4,1,4,1])

sns.kdeplot(y,shade=True)
plt.show()

