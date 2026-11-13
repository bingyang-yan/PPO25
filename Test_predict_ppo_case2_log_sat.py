from yby import *

log = y_read(Path(r"E:\Data\Paper_2\Data_vl\Predict_ppo_case2\log.pkl"))
sat = log.loc[0,'state'][1250:2500]
df = Y_mrst.data2df(sat, [25,10,5])
Y_krige.plot_field(df, column='data')