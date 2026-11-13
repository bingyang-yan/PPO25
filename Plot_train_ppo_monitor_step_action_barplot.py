# step [1,5] as the x axis
# figure listed in row

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from yby import *
from yby_paper2 import *

pd.set_option('display.max_columns', None)
plt.rcParams['font.size']=16

outdir = Path(r'D:\YAN\Research\Paper\Paper_2\Figure\Element_vl')
data = read_pkl_v4(Path(r"E:\Data\Paper_2\Data_vl\SB\Env12\Monitor_step.pkl"))

data['Episodes'] = np.repeat(list(range(int(len(data)/5))), 5)
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

sns.set_style('ticks')
pal = sns.color_palette('dark:red')
fig = sns.PairGrid(data, x_vars='Episodes', hue='Steps',
                   y_vars=['Position', 'Length (m)', 'Height (m)', 'Width (m)',
                           'Porosity', 'Permeability (mD)'],
                   height=1.7, aspect=9, palette=pal)
fig.map(sns.barplot, saturation=1., errcolor='none', dodge=0.01, linewidth=0.2)
fig.add_legend()
sns.despine(offset=5)
plt.gca().set_xticks(np.arange(0,201,10))
# plt.tight_layout()
import os
import pickle
with open(os.path.join(outdir, 'Train_ppo_monitor_step_action_barplot.pkl'), 'wb') as fp:
    pickle.dump(data,fp)
fig.savefig(outdir / 'Train_ppo_monitor_step_action_barplot.png', dpi=1200)
plt.show()


