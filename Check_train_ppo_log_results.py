import matplotlib.pyplot as plt
from yby import *
from yby_paper2 import *

log = read_pkl_v3(Path(r"E:\Data\Paper_2\Data_vl\SB\env12_v1\Monitor_step.pkl"))
#print(log.df_episode)
log['Reward ($)'].plot()
plt.show()