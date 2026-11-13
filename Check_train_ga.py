import matplotlib.pyplot as plt
import pandas as pd
import pandasgui as pg
from yby import *

log = y_read(Path(r"E:\Data\Paper_2\Data_vl\Y_train_ga_case1\20231129_215707_Y_ga_paper2_case1_pop2_log.pkl"))
history = pd.DataFrame(log.all_history_Y)
print(history)
plt.plot(history.index, history.min(axis=1))
plt.show()