from checkonchain.btconchain.btc_add_metrics import *
import checkonchain.dcronchain.charts.chart_dcr_useradoption
import checkonchain.dcronchain.charts.chart_dcr_unforgeablecostliness
import checkonchain.stableonchain.charts.stable_charts_plotting
import checkonchain.altonchain.alt_add_metrics
import checkonchain.xmronchain.xmr_charts
import checkonchain.dcronchain.charts.dcr_charts_plotting
import checkonchain.btconchain.charts.btc_charts_plotting
import os
# Print Public Charts    = 1
# Print Private charts   = 0
public = 0

# BITCOIN
os.chdir(os.path.dirname(__file__))  # reset dir to this file
os.chdir('../btconchain/charts')

# DECRED
os.chdir(os.path.dirname(__file__))  # reset dir to this file
os.chdir('../dcronchain/charts')

# MONERO
os.chdir(os.path.dirname(__file__))  # reset dir to this file
os.chdir('../xmronchain')

# ALTCOINS
os.chdir(os.path.dirname(__file__))  # reset dir to this file
os.chdir('../altonchain')

# STABLECOINS
os.chdir(os.path.dirname(__file__))  # reset dir to this file
os.chdir('../stableonchain')

# Print Research Paper Charts
os.chdir(os.path.dirname(__file__))  # reset dir to this file
os.chdir('../dcronchain/charts')

# Print Research Paper Charts
os.chdir(os.path.dirname(__file__))  # reset dir to this file
os.chdir('../dcronchain/charts')


# Print Last Valid Timestamp
df = btc_add_metrics().btc_coin()
i = df.apply(pd.Series.last_valid_index)['date']
print("")
print("")
print("LAST VALID TIMESTAMP")
print(df.loc[i, 'date'])

print('CHECKONCHAIN CHART PRODUCTION COMPLETE!')
