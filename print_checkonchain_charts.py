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

#Print Research Paper Charts
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../dcronchain/charts')
import checkonchain.dcronchain.charts.chart_dcr_unforgeablecostliness

#Print Research Paper Charts
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../dcronchain/charts')
import checkonchain.dcronchain.charts.chart_dcr_useradoption


print('CHECKONCHAIN CHART PRODUCTION COMPLETE!') 