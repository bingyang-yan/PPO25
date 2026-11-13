# step [1,5] as the x axis
# figure listed in row

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from yby import *
from yby_paper2 import *

pd.set_option('display.max_columns', None)

outdir = Path(r'D:\YAN\Research\Paper\Paper_2\Figure\Element_vl')
data = read_pkl_v4(Path(r"E:\Data\Paper_2\Data_vl\SB\Env12\Monitor_step.pkl"))

data['Total_steps'] = list(range(len(data)))
data['Position'] = data.action.apply(lambda x:x[0])
data['Length (m)'] = data.action.apply(lambda x:x[1])
data['Height (m)'] = data.action.apply(lambda x:x[2])
data['Width (m)'] = data.action.apply(lambda x:x[3])
data['Porosity'] = data.action.apply(lambda x:x[4])
data['Permeability (mD)'] = data.action.apply(lambda x:x[5])
data['Permeability (mD)'] = Y_unit().convert_to(data['Permeability (mD)'],
                                                Y_unit().unit['milli'] * Y_unit().unit['darcy'])

data['Position'] = round(data['Position'])

sns.set(font_scale=1.25)
sns.set_style('ticks')
fig, ax = plt.subplots(2,3,figsize=(15,6))
kargs = {'color':'darkred'}
sns.histplot(data, x='Steps', y='Position', ax=ax[0,0], **kargs)
sns.histplot(data, x='Steps', y='Length (m)', ax=ax[0,1], **kargs)
sns.histplot(data, x='Steps', y='Height (m)', ax=ax[0,2], **kargs)
sns.histplot(data, x='Steps', y='Width (m)', ax=ax[1,0], **kargs)
sns.histplot(data, x='Steps', y='Porosity', ax=ax[1,1], **kargs)
sns.histplot(data, x='Steps', y='Permeability (mD)', ax=ax[1,2], **kargs)
for i in ax[0]:
    i.set_xticklabels([])
    i.set_xlabel('')

import os
import pickle
with open(os.path.join(outdir, 'Train_ppo_monitor_step_action_histplot.pkl'), 'wb') as fp:
    pickle.dump(data,fp)
sns.despine(offset=5)
plt.tight_layout()
fig.savefig(outdir / 'Train_ppo_monitor_step_action_histplot.png', dpi=1200)
plt.show()


