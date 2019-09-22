#sns.heatmap(cm, annot=True, cmap='Reds', fmt='.1f', square=True);
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(12345)

sns.set()


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def example():
    sns.set()


    flights = sns.load_dataset("flights")
    print(flights)
    print(type(flights))

    flights = flights.pivot("month", "year", "passengers")

    print(flights)
    print(type(flights))

    hm = sns.heatmap(flights, annot=True, fmt="d")

    figure = hm.get_figure()

    figure.savefig('sample1.png',dpi=400)


def mysample():

    sns.set()

    mydata = pd.read_csv('hetmap.csv')
    print(mydata)
    print(type(mydata))

    hm = sns.heatmap(mydata, annot=True)

    figure = hm.get_figure()

    figure.savefig('my.png',dpi=400)

def mysample2():
    sns.set()

    mydata = pd.read_csv('heat2.csv')

    mydata = mydata.pivot("Input Time", "Pred Delay", "F1")

    # print(mydata)
    # print(type(mydata))
    #
    hm = sns.heatmap(mydata, annot=True,fmt='.1f',linewidths=.5,vmin=60,vmax=75)

    figure = hm.get_figure()

    # plt.suptitle('USD-JPY')

    figure.savefig('USD-JPY.pdf',dpi=400)

def mysample3():
    sns.set()

    mydata = pd.read_csv('smooth1.csv')

    mydata = mydata.pivot("Model", "#Model Layer", "MAD")

    # print(mydata)
    # print(type(mydata))
    #
    hm = sns.heatmap(mydata, annot=True,fmt='.3f',linewidths=.5,vmin=-0.2,vmax=1,cmap="YlGnBu")

    figure = hm.get_figure()
    figure.subplots_adjust(left=0.3)
    # plt.suptitle('USD-JPY')

    figure.savefig('smooth_cora.pdf',dpi=400)


if __name__ == '__main__':
    # mydata()
    mysample3()