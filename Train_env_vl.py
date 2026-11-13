from yby_paper2.env import Y_env_mrst_vl
from yby_paper2 import *

kargs = {'root_case':r"E:\Data\Paper_2\Data_vl\Case2_single",
    'max_iter':20, 'size_pop':10, 'prob_mut':0.2,
    'info':'case2_env_vl'}
env = Y_env_mrst_vl()
cla = Y_ga_paper2_vl(env, **kargs)