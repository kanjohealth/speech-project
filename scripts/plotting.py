from matplotlib import pyplot as plt
from matplotlib.pyplot import figure


def feature_time_scatter(time_values,feature_values):

    plt.scatter(time_values, feature_values, c ='red',marker='x')
    plt.title('Sample Lengths Over Time')
    plt.ylabel('Feature Value')
    plt.xlabel('Sample Publishing Date')
    plt.show()


