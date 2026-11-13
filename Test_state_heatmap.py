from scipy.io import loadmat
import seaborn as sns
import matplotlib.pyplot as plt
from yby import *

index_z = 2
file = r"E:\Data\Paper_2\Data_vl\Predict_ppo_case1\pres.mat"
data = loadmat(file)
data = data['pres'].flatten()
data = Y_mrst(save=False).data2df(data, [25,10,5])

data = data[data['z']==index_z]
data = data.pivot(index='x', columns='y', values='data')

fig = sns.heatmap(data, cmap='jet')
plt.show()