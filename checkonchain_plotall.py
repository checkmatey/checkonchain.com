from checkonchain_v2.apis.checkonchain_api import *

#Run unified API to update csvs
Checkonchain_api().return_df(1)

from checkonchain_v2.modules.adoption import Adoption
from checkonchain_v2.modules.cointime import Cointime
from checkonchain_v2.modules.pricing import Pricing
from checkonchain_v2.modules.supply import Supply

print('Checkonchain v2 Chart Output Complete!')