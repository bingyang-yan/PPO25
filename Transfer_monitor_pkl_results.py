import os
import pandas as pd
import pandasgui as pg
from yby_paper2 import *

file = r"E:\Data\Paper_2\Data_vl\SB\Env12\Monitor_step.pkl"
os.chdir(os.path.dirname(file))
data = read_pkl_v3(file)
data.to_csv('Monitor_step.csv')
