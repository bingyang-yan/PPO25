import pandas as pd

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from yby_paper2 import *
from yby import *

pd.set_option('display.max_columns', None)

log = read_pkl(Path(r"E:\Data\Paper_2\Data_vl\SB\Code_v5_test6\Monitor_step.pkl"))
log = log[:-4]
log.dropna(how='any', inplace=True)
log['x'] = list(range(len(log) /5))
log
print(log)
sns.scatterplot(log, x='')
