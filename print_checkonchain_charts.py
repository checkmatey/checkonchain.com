import os
#Print Public Charts    = 1
#Print Private charts   = 0
public  = 0

#BITCOIN
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../btconchain/charts')
import checkonchain.btconchain.charts.btc_charts_plotting

#DECRED
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../dcronchain/charts')
import checkonchain.dcronchain.charts.dcr_charts_plotting

#MONERO
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../xmronchain')
import checkonchain.xmronchain.xmr_charts

#ALTCOINS
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../altonchain')
import checkonchain.altonchain.alt_add_metrics

#STABLECOINS
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../stableonchain')
import checkonchain.stableonchain.charts.stable_charts_plotting

#Print Research Paper Charts
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../dcronchain/charts')
import checkonchain.dcronchain.charts.chart_dcr_unforgeablecostliness

#Print Research Paper Charts
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../dcronchain/charts')
import checkonchain.dcronchain.charts.chart_dcr_useradoption

#STABLECOINS
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../stableonchain/charts')
import checkonchain.stableonchain.charts.stable_charts_plotting


#Print Last Valid Timestamp
from checkonchain.btconchain.btc_add_metrics import *
df = btc_add_metrics().btc_coin()
i = df.apply(pd.Series.last_valid_index)['date']
print("")
print("")
print("LAST VALID TIMESTAMP")
print(df.loc[i,'date'])

print('CHECKONCHAIN CHART PRODUCTION COMPLETE!')