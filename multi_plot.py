"""
Plotting a three-way ANOVA
==========================

_thumb: .42, .5
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



def example():
    sns.set(style="whitegrid")

    # Load the example exercise dataset
    df = sns.load_dataset("exercise")

    print(df)

    #palette “point”, “bar”, “strip”, “swarm”, “box”, “violin”, or “boxen”.
    # Draw a pointplot to show pulse as a function of three categorical factors
    ##capsize=.1,
    g = sns.catplot(x="time", y="pulse", hue="kind", col="diet",capsize=.2,
                    palette="YlGnBu_d", height=6, aspect=0.75,
                    kind="point", data=df,ci=None)
    g.despine(left=True)

    g.savefig('varience2.png',dpi=400)


def my_pic1():
    sns.set(style="whitegrid")
    mydata = pd.read_csv('info_noise.csv')
    print(mydata)

    with sns.plotting_context("notebook",font_scale=1.5):
    
        g = sns.catplot(x="Information-to-noise Ratio", y="value", hue="type", col="model",
                        palette="rocket", height=5, aspect=1.25,linewidth=2.5,
                        kind="point", data=mydata,ci=None)
    # plt.setp(g._legend.get_title(), fontsize=20)

    # print(g.__dict__.keys())
    # print(g._legend.__dict__.keys())
    # print(dir(g))
    # print(dir(g._legend))
        # g.grid()
        g.despine(left=True)

        g.savefig('io_cora2.pdf',dpi=400)

def my_pic2():
    # sns.set(style="whitegrid")
    mydata = pd.read_csv('rm_rate.csv')
    print(mydata)

    with sns.plotting_context("notebook",font_scale=1.5):
    
        g = sns.catplot(x="rm_rate", y="value", hue="type", col="model",
                        palette="rocket", height=5, aspect=1.25,linewidth=2.5,
                        kind="bar", data=mydata,ci=None)
 
        g.despine(left=True)

        g.savefig('rm6.pdf',dpi=400)

def my_pic3():
    # sns.set(style="whitegrid")
    mydata = pd.read_csv('add_rate.csv')
    print(mydata)

    with sns.plotting_context("notebook",font_scale=1.5):
    
        g = sns.catplot(x="add_rate", y="value", hue="type", col="model",
                        palette="rocket", height=5, aspect=1.25,linewidth=2.5,
                        kind="bar", data=mydata,ci=None)
 
        g.despine(left=True)

        g.savefig('add2.pdf',dpi=400)

def my_pic4():
    # sns.set(style="whitegrid")
    mydata = pd.read_csv('new.csv')
    print(mydata)

    with sns.plotting_context("notebook",font_scale=1.5):
    
        g = sns.catplot(x="dataset", y="value", hue="training", col="model",
                        palette="rocket", height=4, aspect=1,linewidth=2.5,
                        kind="boxen", data=mydata)
 
        g.despine(left=True)

        g.savefig('toy4.png',dpi=400)

def my_pic5():
    # sns.set(style="whitegrid")
    mydata = pd.read_csv('huge_233.csv')
    print(mydata)

    with sns.plotting_context("notebook",font_scale=1.5):
    
        g = sns.catplot(x="item", y="value", hue="training", col="model",
                        palette="rocket", height=5, aspect=1,linewidth=2.5,
                        kind="bar", data=mydata)
 
        g.despine(left=True)

        g.savefig('huge_233.png',dpi=400)

def my_pic6():
    # sns.set(style="whitegrid")
    mydata = pd.read_csv('huge_three.csv')
    print(mydata)

    with sns.plotting_context("notebook",font_scale=1.5):
    
        g = sns.catplot(x="item", y="value", hue="training", col="model",
                        palette="rocket", height=5, aspect=1,linewidth=2.5,
                        kind="boxen", data=mydata)
 
        g.despine(left=True)

        g.savefig('axis_boxen.pdf',dpi=400)

def my_pic7():
    # sns.set(style="whitegrid")
    mydata = pd.read_csv('huge_acc.csv')
    print(mydata)


    with sns.plotting_context("notebook",font_scale=1.5):
    
        g = sns.catplot(x="dataset", y="Acc", hue="training", col="model",
                        palette="rocket", height=5, aspect=0.75,linewidth=2.5,
                        kind="boxen", data=mydata)
 
        g.despine(left=True)
        g.savefig('accA2.png',dpi=200)
def my_pic8():
    # sns.set(style="whitegrid")
    mydata = pd.read_csv('huge_madgap2.csv')
    print(mydata)

    with sns.plotting_context("notebook",font_scale=1.5):
    
        g = sns.catplot(x="dataset", y="MADGap", hue="training", col="model",
                        palette="rocket", height=5, aspect=0.75,linewidth=2.5,
                        kind="boxen", data=mydata,ci='sd')
 
        g.despine(left=True)

        g.savefig('gapB.png',dpi=200)

my_pic1()


