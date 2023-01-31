import numpy as np
#import tensorflow as tf
import matplotlib.pyplot as plt
plt.style.use("ggplot")
x=np.linspace(1,50,51)
y=x+10*np.random.random(len(x))
plt.scatter(x,y,label="generated Data")
plt.xlabel("x")
plt.ylabel("y")
