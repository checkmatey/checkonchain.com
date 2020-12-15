import os
os.chdir('../dcronchain/charts')
import checkonchain.dcronchain.charts.dcr_charts_plotting
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../btconchain/charts')
import checkonchain.btconchain.charts.btc_charts_plotting
#Print Research Paper Charts
os.chdir(os.path.dirname(__file__)) #reset dir to this file
os.chdir('../dcronchain/charts')
import checkonchain.dcronchain.charts.chart_dcr_unforgeablecostliness