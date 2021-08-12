import seaborn as sns
import numpy as np
x = np.linspace(0, 5, 11)
y = x ** 2
import matplotlib.pyplot as plt
def plot():
    x = np.linspace(0, 5, 11)
    y = x ** 233
    plt.plot(x, y, 'r') 
    plt.xlabel('X Axis Title Here')
    plt.ylabel('Y Axis Title Here')
    plt.title('String Title Here')
    plt.savefig('foo.png')
    #plt.seek(0)
    return plt



