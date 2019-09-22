import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")


def example():
	rs = np.random.RandomState(365)
	values = rs.randn(365, 4).cumsum(axis=0)
	
	print(values)
	print(type(values))
	print(values.shape)

	dates = pd.date_range("1 1 2016", periods=365, freq="D")
	print(dates)

	data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
	data = data.rolling(7).mean()

	# print(data)

	plot = sns.lineplot(data=data, palette="tab10", linewidth=2.5)
	fig = plot.get_figure()
	fig.savefig('line_example.png',dpi=400)

def myplot1():
	values = [[0.363,0.174],
			[0.796,0.695],
			[0.786,0.679],
			[0.772,0.519],
			[0.563,0.350],
			[0.319,0.002]]
	rows = [i for i in range(1,7)]
	data = pd.DataFrame(values, rows, columns=["Acc", "MADGap"])
	plot = sns.lineplot(data=data, palette="rocket", linewidth=2.5)
	plot.set_xlabel('(a) # Model Layer',fontsize=15)
	plot.set_title('Pearson:0.986**',fontsize=15)
	fig = plot.get_figure()
	fig.savefig('introA.png',dpi=400)

def myplot2():
	values = [[0.08,0.0277],
			[0.092,0.1555],
			[0.684,0.4257],
			[0.698,0.5372],
			[0.708,0.5773],
			[0.688,0.5726],
			[0.724,0.6018],
			[0.784,0.6492],
			[0.796,0.6879],
			[0.784,0.693],
			[0.76,0.6642],
			[0.758,0.6422],
			[0.77,0.637],
			[0.79,0.6344],
			[0.788,0.6308],
			[0.792,0.6512],
			[0.784,0.675],
			[0.76,0.6881],
			[0.76,0.6914],
			[0.758,0.6958],
			[0.76,0.7046],
			[0.76,0.7067],
			[0.762,0.6995],
			[0.762,0.6873],
			[0.756,0.6763],
			[0.76,0.6699],
			[0.76,0.6667],
			[0.758,0.6693],
			[0.764,0.6795],
			[0.768,0.6901]]
	rows = [i for i in range(1,31)]
	data = pd.DataFrame(values, rows, columns=["Acc", "MADGap"])
	plot = sns.lineplot(data=data, palette="rocket", linewidth=2.5)
	# plot.title('')
	plot.set_xlabel('(b) Epoch',fontsize=15)
	plot.set_title('Pearson:0.940**',fontsize=15)
	fig = plot.get_figure()
	fig.savefig('introB.png',dpi=400)

def myplot3():
	values = [[8550,71070,194408,381626,589904,780694,918794,1003356,1049666,1074098,1086504,1092498,1095154,1096174,1096500,1096596,1096636,1096656,1096658,1096658],
				[2006,25818,149730,625814,1604668,2803378,3783626,4392094,4723850,4904266,5000862,5048240,5068112,5074706,5076582,5077078,5077168,5077178,5077178,5077178]]
	values2 = [0.8100,0.7335,0.5649,0.3788,0.2688,0.2178,0.1954,0.1860,0.1818,0.1797,0.1785,0.1779,0.1777,0.1776,0.1776,0.1776,0.1776,0.1776,0.1776,0.1776]
	
	values = np.array(values)
	values = values.T
	rows = [int(i) for i in range(1,21)]
	data = pd.DataFrame(values, rows, columns=["Intra", "Inter"])
	data2 = pd.DataFrame(values2, rows, columns=["Rate"])
	plot = sns.lineplot(data=data, palette="tab10", linewidth=2.5)
	ax2 = plt.twinx()
	plot = sns.lineplot(data=data2, palette="rocket", linewidth=2.5,ax=ax2)
	
	plot.set_xlabel('Order',fontsize=15)
	plot.set_title('CORA',fontsize=15)


	fig = plot.get_figure()
	fig.savefig('line31.png',dpi=400)

def myplot4():
	# sns.set(rc={'figure.figsize':(11.7,8.27)})
	values = [[0.810,0.734,0.565,0.379,0.269,0.218,0.195,0.186,0.182,0.180,0.178,0.178,0.178,0.178,0.178,0.178,0.178,0.178,0.178,0.178],
			[0.740,0.741,0.657,0.593,0.520,0.442,0.369,0.307,0.262,0.233,0.215,0.205,0.199,0.195,0.193,0.192,0.191,0.191,0.190,0.190],
			[0.802,0.766,0.697,0.609,0.506,0.421,0.381,0.364,0.359,0.357,0.357,0.357,0.357,0.357,0.357,0.357,0.357,0.357,0.357,0.357]]
	values = np.array(values)
	values = values.T
	print(values.shape)
	rows = [int(i) for i in range(1,21)]
	data = pd.DataFrame(values, rows, columns=["CORA", "CiteSeer",'Pubmed'])
	
	plot = sns.lineplot(data=data, palette="rocket", linewidth=2.5)

	plot.set_xlabel('Order',fontsize=15)
	plot.set_ylabel('Information-to-noise Ratio',fontsize=15)


	plot.xaxis.set_ticks(np.arange(0,22,2))

	fig = plot.get_figure()
	fig.savefig('new_intra_rate3.pdf',dpi=400)

myplot4()