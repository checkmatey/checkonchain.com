# deᴄʀᴇᴅucation - Decred Charts

The following document specifies the input calculations and provides sample charts for a number of Decred specific metrics for implementation into a Decred charting suite.

***Disclaimer***

*These models shall be considered work in progress and informational only and shall not be considered financial or investment advice of any form. The author bears no responsibility for decisions made utilising any resources in this repository or associated material.*

## Charting Suite Menu

**Realised Cap and MVRV Ratio**
- [Realised Cap and MVRV Ratio](#realised-cap-and-mvrv-ratio)
- [Relative Realised Cap and MVRV Ratio](#relative-realised-cap-and-mvrv-ratio)
- [Market-Realised Gradient Oscillator](#market-realised-gradient-oscillator)
- [Unrealised Profit and Loss](#unrealised-profit-and-loss)


**Network Valuation Models**
- [Mayer Multiple](#mayer-multiple)
- [Stock-to-Flow Model (USD)](# -stock-to-flow-model)
- [Stakeholder Commitments](#stakeholder-commitments)
- [142-Day Ticket Sum](#142-day-ticket-sum)


**Proof-of-Work Mining Metrics**
- [Difficulty Ribbon](# -difficulty-ribbon)
- [Puell Multiple](# -puell-multiple)
- [Mining Pulse](# -mining-pulse)


**Proof-of-Stake Ticket Metrics**
- [Hodler Conversion Rate](# -hodler-conversion-rate)
- [Ticket Volume Weighted Average Price](# -ticket-volume-weighted-average-price-tvwap-(usd))
- [Strongest Hand](# -strongest-hand)


**Performance and Transaction Metrics**
- [NVT and RVT Ratio](#nvt-and-rvt-ratio)


## List of Metric Tags

    - USD
    - BTC

    - Pricing Model
    - Momentum Model

    - Realised Valuation
    - Network Valuation
    - Oscillator

    - Ticket Metric
    - Mining Metric
    - Performance Metric


# **Realised Cap and MVRV Ratio**

**Tags:**

    USD
    Pricing Model
    Realised Valuation
    Oscillator

**Checkonchain Code:**

    checkonchain.dcrcharts.charts.dcr_chart_suite(theme).mvrv(x).show()

        theme = 'light' or 'dark'
        x = 0 for Network Valuation (e.g. Market Cap)
        x = 1 for Pricing model (e.e. Price)

**JSON Files**

Valuation - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/mvrv_valuation_usd

Pricing - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/mvrv_pricing_usd

**Blurb:**

    The Realised Cap is the aggregate USD value of all UNSPENT UTXOs, priced at the time they were last transacted. Due to the constant flow of DCR on-chain in Proof-of-Stake tickets, the Decred Realised Cap tends to follow the Market Cap more closely than its Bitcoin equivalent. Realised value is 'attracted' to the spot price during periods of high transaction demand as more DCR gets 'repriced'. This metric tends to create a psychological level of support in bull markets and resistance in bear markets, representing the last time the aggregate market 'interacted' with their coins.

    The MVRV Ratio measures the relative distance between the market cap and the realised cap. For Decred, this behaves as an oscillator and is ideal identifying periods of extreme under/overvaluation (tops and bottoms) and for support/resistance signals. An MVRV ratio of 1.0 indicates price is at psychological support in bull markets and, conversely, a resistance in bear markets.

    Data Source: Coinmetrics.io

**References:**

[Paper by Checkmate for Decred](https://medium.com/decred/decred-on-chain-realised-cap-mvrv-ratio-and-gradient-oscillators-a36ed2cc8182)

[paper by CoinMetrics on the Realised Cap](https://coinmetrics.io/realized-capitalization/)

[paper by David Puell on Bitcoin MVRV Ratio](https://medium.com/adaptivecapital/bitcoin-market-value-to-realized-value-mvrv-ratio-3ebc914dbaee)

**Inputs:**

    Primary Y-Axis
        Market Cap      = Coin supply * Coin PriceUSD (Daily close)
        Realised Cap    = Sum of Each unspent UTXO priced at the time it last moved

    Secondary Y-Axis
        MVRV Ratio      = Market Cap / Realised Cap
        ZONES           = [1.8,5.0] Red
                        = [1.0,1.0] Orange Line (Unity)
                        = [0.0,0.7] Green 

**Chart Description:**

    X-axis      
        Range   = Genesis to present
        Type    = date

    Y-axis-Left = Network Valuation (USD)
        Range   = 1e5 to 1e10
        Type    = log

    Y-axis-Right = MVRV Ratio
        Range   = 0.3 to 1e4
        Type    = log 

**Sample Chart**

![MVRV Ratio](_images/dcronchain/01_dcr_mvrv_ratio_dark.png)
![MVRV Ratio](_images/dcronchain/01_dcr_mvrv_ratio_light.png)


# **Stakeholder Commitments**

**Tags**

    USD
    BTC
    Pricing Model
    Network Valuation
    Ticket Metric

**Checkonchain Code:**

    checkonchain.dcrcharts.charts.dcr_chart_suite(theme).commitment_usd(x)
    checkonchain.dcrcharts.charts.dcr_chart_suite(theme).commitment_btc(x)

        theme = 'light' or 'dark'
        x = 0 for Network Valuation (e.g. Market Cap)
        x = 1 for Pricing model (e.e. Price)

**JSON Files**

Valuation (USD) - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/commitments_valuation_usd

Pricing (USD) - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/commitments_pricing_usd

Valuation (BTC) - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/commitments_valuation_btc

Pricing (BTC) - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/commitments_pricing_btc


**Blurb:** 

    The block subsidy models were developed by @permabullnino to capture the aggregate income cost basis for all Decred blockchain block reward stakeholders. These models consider the cumulative value issued by the Decred blockchain in Total (blue),
    to Proof-of-Work miners (red), Proof-of-Stake Stakeholders (purple) and the Decred Treasury
    and Contractor base (yellow). Additionally, the cumulative value bound in Decred tickets (turqoise) represents a psychological level of maximum conviction for Decred stakeholders and interstingly alignes with the Supply Issued Cap which Calculates 10x the issued USD value discounting the reduction in coin issuance.
    
    These models are priced in both USD and BTC providing key psychological levels and income cost basis for each set of stakeholders. Where price falls below a block subsidy model, it indicates that on aggregate, that supply side group is underwater on their income stream. In general, miners, contractors and investors with cost basis denominated in USD are more sensitive to fluctuations in the DCR/USD exchange rate. Investors and stakeholders with a cost basis denominated in BTC are more sensitive to the DCR/BTC exchange rate.

    Data Source: Coinmetrics.io and explorer.dcrdata.org

**References:**

[Block subsidy models paper](https://medium.com/@permabullnino/decred-on-chain-a-look-at-block-subsidies-6f5180932c9b)

[Decred ticket cap paper](https://medium.com/decred/decred-the-resilient-stronghold-4038dc64dd2a)

**Inputs:**

    Primary Y-Axis (USD Chart)
        Market Cap          = Coin supply * Coin PriceUSD (Daily close)
        Realised Cap        = Sum of Each unspent UTXO priced at the time it last moved
        Total-USD           = Cumulative total block reward paid in USD (DailyIssuedNtV * PriceUSD + FeeTotUSD)_cumsum
        POW-USD             = Cumulative PoW Miner block reward paid in USD 
                                (DailyIssuedNtV * PriceUSD)_cumsum * 0.6 + FeeTotUSD_cumsum
        POS-USD             =   Cumulative PoS Stakeholder block reward paid in USD 
                            (DailyIssuedNtV * PriceUSD)_cumsum * 0.3
        Treasury-USD        =   Cumulative Treasury block reward paid in USD 
                                (DailyIssuedNtV * PriceUSD)_cumsum * 0.1
        Tickets Bound Cap   = Cumulative sum of USD value bound in Tickets
        Supply Issued Cap   = Metric that calculates the 10x total USD issuance corrected for block reward reduction
                                (DailyIssuedNtv * PriceUSD)_cumsum * 10 * (101/100)**(np.floor(block_height/6144))

    For BTC chart - change all PriceUSD to Price BTC

**Chart Description:**

    X-axis      
        Range   = Genesis to present
        Type    = date

    Y-axis-Left = Price (USD)
        Range   = 1e5 to 1e10
        Type    = log

    Y-axis-Left = Price (BTC)
        Range   = 1e2 to 2e6
        Type    = log

Sample Chart
![Block Subsidy Model (USD)](_images/dcronchain/02a_dcr_blksub_usd_dark.png)
![Block Subsidy Model (USD)](_images/dcronchain/02a_dcr_blksub_usd_light.png)
![Block Subsidy Model (BTC)](_images/dcronchain/02b_dcr_blksub_btc_dark.png)
![Block Subsidy Model (BTC)](_images/dcronchain/02b_dcr_blksub_btc_light.png)


# **NVT and RVT Ratio**

**Tags**

    USD
    Oscillator
    Performance Metric

**Checkonchain Code:**

    checkonchain.dcrcharts.charts.dcr_chart_suite(theme).nvt_rvt(x)

        theme = 'light' or 'dark'
        x = 0 Uses Coinmetrics TxTfrValUSD metric as denominator
        x = 1 Uses Coinmetrics TxTfrValAdjUSD metric as denominator

**JSON Files**

https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/nvtrvt_oscillator_usd

**Blurb:** 

    The NVT and RVT Ratio are inverse velocity metrics that compare daily volume settled on-chain relative to network market cap (NVT) or Realised Cap (RVT). Where there is significant demand for transferring of value on-chain relative to the respective network value, the NVT or RVT ratio will be low or in a downtrend, suggesting undervaluation and increasing utilisation of the network. Conversely, a high or uptrending NVT or RVT Ratio suggest low relative utilisation and potential overvaluation.
    
    Another way to think about these ratios is that an NVT Ratio of 10 means Decred is transferring its market cap worth of value every 10 days. Demand for Decred transactions have historically been dominated by staking tickets, with additional demand arising from privacy mixing and transferring payments or stored value. As such, the NVT and RVT tend to follow each other more closely than the Bitcoin counterpart.
    
    The 28-day and 90-day moving averages are applicable for short and long term signals, respectively with the longer term 90-day average being a higher conviction signal. The NVTS and RVTS apply a 28-day moving average only to the transaction volume (denominator) providing faster signals for short-term traders as it retains daily pricing signals.

    Data Source: Coinmetrics.io and explorer.dcrdata.org

**References:**

[paper on NVT Signal](https://woobull.com/nvt-signal-a-new-trading-indicator-to-pick-tops-and-bottoms/)

[paper on RVT Ratio](https://medium.com/@_Checkmatey_/the-bitcoin-rvt-ratio-a-high-conviction-macro-indicator-615b68715b77)

**Inputs:**

    Primary Y-Axis
        Market Cap      = Coin supply * Coin PriceUSD (Daily close)
        Realised Cap    = Sum of Each unspent UTXO priced at the time it last moved

    Secondary Y-Axis
        NVT (28DMA)     = (Market Cap / TxTfrValAdjUSD)_28sma
        NVT (90DMA)     = (Market Cap / TxTfrValAdjUSD)_90sma
        NVTS            =  Market Cap / (TxTfrValAdjUSD)_28sma
        RVT (28DMA)     = (Realised Cap / TxTfrValAdjUSD)_28sma
        RVT (90DMA)     = (Realised Cap / TxTfrValAdjUSD)_90sma
        RVTS            =  Realised Cap / (TxTfrValAdjUSD)_28sma
        ZONES           = [175,250] = Red
                          [100,175] = Orange
                          [50,100]  = Yellow
                          [0,50]    = Green

        Note - setting code input `mode` to 0 will use Coinmetrics input of TxTfrValUSD and divide ZONES values by a factor of 5

**Chart Description:**

    X-axis      
        Range   = Genesis to present
        Type    = date

    Y-axis-Left = Network Valuation (USD)
        Range   = 1e5 to 1e10
        Type    = log

    Y-axis-Right = MVRV Ratio
        Range   = 0 to 750
        Type    = linear 

Sample Chart
![NVT and RVT Ratios](_images/dcronchain/03_dcr_nvtrvt_dark.png)
![NVT and RVT Ratios](_images/dcronchain/03_dcr_nvtrvt_light.png)


# **Mayer Multiple**

**Tags:**

    USD
    Pricing Model
    Network Valuation

**Checkonchain Code:**

    checkonchain.dcrcharts.charts.dcr_chart_suite(theme).mayer_multiple()

        theme = 'light' or 'dark'

**JSON Files**

https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/mayermultiple_pricing_usd

**Blurb:**

    The Mayer Multiple is a simple oscillator calculated by taking the ratio of the current DCR/USD Price to its 200-day moving average. The 200-day moving average is a very common indicator in technical analysis and is often used to calibrate macro bull/bear bias. The Mayer Multiple is a metric that presents the deviation of price from this long term mean as an oscillator with historically relevant probabilities of occurence shown as follows:

    Mayer Multiple 0.4 = 10% occurence
    Mayer Multiple 0.6 = 25% occurence
    Mayer Multiple 2.0 = 25% occurence
    Mayer Multiple 2.8 = 10% occurence

    Data Source: Coinmetrics.io

**References:**
    
    The Mayer Multiple - https://www.theinvestorspodcast.com/bitcoin-mayer-multiple/

**Inputs:**

    Primary Y-Axis
        DCR Price (USD)     = Coin PriceUSD (Daily close)
        200-Day MA          = 200-day moving average of Price
        Strong Sell (2.8)   = 2.8 * PriceUSD_200sma
        Sell (2.0)          = 2.0 * PriceUSD_200sma
        Buy (0.6)           = 0.6 * PriceUSD_200sma
        Strong Buy (0.4)    = 0.4 * PriceUSD_200sma

    Secondary Y-Axis
        Mayer Multiple      = PriceUSD / PriceUSD_200sma
        ZONES               = [2.8,15]  = Red
                              [2.0,2.8] = Orange
                              [0.4,0.6] = Yellow
                              [0,0.4]   = Green

**Chart Description:**

    X-axis      
        Range   = Genesis to present
        Type    = date

    Y-axis-Left = Network Valuation (USD)
        Range   = 1e-2 to 1e3
        Type    = log

    Y-axis-Right = Mayer Multiple
        Range   = 0.2 to 1e5
        Type    = log 

**Sample Chart:**

![Mayer Multiple](_images/dcronchain/04_dcr_mayer_multiple_dark.png)
![Mayer Multiple](_images/dcronchain/04_dcr_mayer_multiple_light.png)




# **142-day Ticket Sum**

**Tags:**

    USD
    Pricing Model
    Network Valuation
    Ticket Metric

**Checkonchain Code:**

    checkonchain.dcrcharts.charts.dcr_chart_suite(theme).tic_vol_sum_142day()

        theme = 'light' or 'dark'

**JSON Files**

https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/142dayticsum_pricing_usd


**Blurb:**

    The 142-day sum of USD bound in tickets was a metric developed by @permabullnino that calculates the 142-day rolling sum of USD value bound in Decred Tickets, divided by circulating supply (red). 142-days is selected as it represents the maximum time-frame for all tickets within the pool to either vote, or expire, and thus captures an entire ticket holder 'cycle'.
    
    Interestingly, this metric has shown to act as a point of price resistance during bullish markets, and taking Fibonacci ratios (61.8%, 50.0%, 38.2% and 26.3%) creates additional levels where price has historically found support and resistance. In general, price above the 100% 142-day ticket sum tends to be a local top signal whilst price below the 26.3% ratio is a local bottom signal. The ratio is taken between price and the 50% ratio to generate an oscillator which aides with identifying where price enters these key key levels. 

    Data Source: Coinmetrics.io and explorer.dcrdata.org

**References:**
    
    None

**Inputs:**

    Primary Y-Axis
        DCR Price (USD)                  = Coin PriceUSD (Daily close)
        142-Day Ticket USD Sum           = (tic_usd_cost_142sum)_sum(142) / SplyCur
        142-Day Ticket USD Sum * 61.8%   = 61.8% * (tic_usd_cost_142sum)_sum(142) / SplyCur
        142-Day Ticket USD Sum * 50.0%   = 50.0% * (tic_usd_cost_142sum)_sum(142) / SplyCur
        142-Day Ticket USD Sum * 38.2%   = 38.2% * (tic_usd_cost_142sum)_sum(142) / SplyCur
        142-Day Ticket USD Sum * 23.6%   = 23.6% * (tic_usd_cost_142sum)_sum(142) / SplyCur

    Secondary Y-Axis
        142-day Ticket Multiple (50%)   = PriceUSD / ((tic_usd_cost_142sum)_sum(142) / SplyCur)
        ZONES                           = [2.000,5.000]  = Red
                                          [1.236,2.000]  = Orange
                                          [0.472,0.764]  = Yellow
                                          [0.000,0.472]  = Green

**Chart Description:**

    X-axis      
        Range   = Genesis to present
        Type    = date

    Y-axis-Left = Network Valuation (USD)
        Range   = 1e-2 to 1e3
        Type    = log

    Y-axis-Right = Mayer Multiple
        Range   = 0.2 to 1e5
        Type    = log 

**Sample Chart:**

![142-day Ticket Sum](_images/dcronchain/05_dcr_142dticsum_dark.png)
![142-day Ticket Sum](_images/dcronchain/05_dcr_142dticsum_light.png)



# Relative BTC Realised Cap and MVRV Ratio

**Tags:**

    BTC
    Pricing Model
    Realised Valuation
    Oscillator

**Checkonchain Code:**

    checkonchain.dcrcharts.charts.dcr_chart_suite(theme).mvrv_relative_btc(x).show()

        theme = 'light' or 'dark'
        x = 0 for Network Valuation (e.g. Market Cap)
        x = 1 for Pricing model (e.e. Price)

**JSON Files**

Valuation - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/mvrv_valuation_btc

Pricing - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/mvrv_pricing_btc


**Blurb:**

    The Relative Realised Caps present a series of pricing models derived from both spot prices and onchain signatures of the DCR/BTC exchange pair. The following realised valuation models are denominated in BTC and attempt to capture a range of methods for valuing across volatile assets of different size, scale and liquidity.

    Realised Cap (BTC)          - Traditional method for realised cap, pricing each Decred UTXO at the BTC value when it was last spent.

    Relative On-chain Cap (BTC) - Ratio between DCR Realised Cap and Bitcoin Realised Cap giving a relative on-chain pricing model. This metric tends to act as a support level, or lower bound pricing band. When the Decred Realised Cap (numerator) appreciates in price or experiences increased transaction momentum compared to Bitcoin, the pricing metric will increase. Conversely, where the Bitcoin Realised Cap (denominator) appreciates, or where Decred sells off relative to Bitcoin, the metric will shed value.

    Relative MVRV Cap (BTC)     - Presents the DCR/BTC value where the ratio of Decred is equal to the MVRV Ratio of BTC. This is the price at which both coins are trading an equal premium or discount relative to their respective Realised Cap. This model tends to act as an upper bound pricing band which on contact, can be interpreted as the point where Decred has amplified the returns of a BTC only position.

    Mid Relative Realised Cap   - The midpoint between the Relative On-chain Cap and the Relative MVRV Cap. This metric, by design, captures a mean pricing level and can be used as a support or resistance signal in all market cycles.

    The Realtive MVRV Ratio Oscillator presents is a representation of the relative premium or discount between Decred and Bitcoin. High oscillator values signal that both coins are trading at a premium and Decred has provided amplified returns over a BTC only position and may singal overvaluation. Conversely, low values signify that DCR has lost value relative to BTC and may signal undervaluation.

    Data Source: Coinmetrics.io and explorer.dcrdata.org

**References:**

    Paper by @permabullnino - https://medium.com/@permabullnino/decred-on-chain-mini-pub-1-relative-mvrv-ratio-ea2564ca420f

**Inputs:**

    Primary Y-Axis
        Market Cap                  = Coin supply * Coin PriceUSD (Daily close)
        Realised Cap                = Sum of Each unspent UTXO priced in BTC at the time it last moved
        Relative Onchain Cap        = Onchain DCRBTC Price (DCR Realised Cap / BTC Realised Cap)
        Relative MVRV Cap           = Relative DCRBTC MVRV Ratio, Compares premium / discount of Market Price vs Realized Price coins
        Relative MVRV Cap           = Relative MVRV Price (1.0 means MVRV Ratio is equal between BTC and DCR)
        Mid Relative Realised Cap   = Relative Mid-point between PriceBTC_onchain and Price_DCRBTC_MVRV
        28-DMA                      = 28-day Average of Relative MVRV Ratio (DCRBTC_MVRV)
        142-DMA                     = 142-day Average of Relative MVRV Ratio (DCRBTC_MVRV)

    Secondary Y-Axis
        Relative MVRV Ratio     = Decred Realised Cap / Bitcoin Realised Cap
        ZONES                   = [1.0,2.0] Red
                                = [0.0,0.45] Green 

**Chart Description:**

    X-axis      
        Range   = Genesis to present
        Type    = date

    Y-axis-Left = Network Valuation (BTC)
        Range   = 1e2 to 1e6
        Type    = log

    Y-axis-Right = Relative MVRV Ratio
        Range   = 0.2 to 1e2
        Type    = log 

**Sample Chart:**

![Realtive MVRV Ratio](_images/dcronchain/06_dcr_relative_realised_mvrv_dark.png)
![Relative MVRV Ratio](_images/dcronchain/06_dcr_relative_realised_mvrv_light.png)


# Market-Realised Gradient Oscillator

**Tags:**

    USD
    Momentum Model
    Realised Valuation
    Oscillator

**Checkonchain Code:**

    checkonchain.dcrcharts.charts.dcr_chart_suite(theme).fig_dcr.mrkt_real_gradient_usd(x).show()

        theme = 'light' or 'dark'
        x = 28 for 28-day metric
        x = 142 for 142-day metric

**JSON Files**

28day (USD) - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/mrktrealgrad28day_oscillator_usd

142day (USD) - https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/mrktrealgrad142day_oscillator_usd


**Blurb:**

    The Market-Realised Gradient Oscillator is a metric that aims to capture periods where the momentum and sentiment of spot markets begins to shift in advance of a slower reaction on-chain. It considers the rate of change (gradient) of the market cap (fast, noisy metric) over a 28-day or 142-day period, and compares it to the equivalent gradient of the realised cap (slow but higher conviction metric). Standard periods used are 28-day and 142-day, coincident with average and maximum vote periods of the Decred ticket pool.

    The Delta Gradient metric is calculated as the difference between the Market and Realised gradients. Where this metric breaks above zero from below, it signifies spot pricing is reversing trend to the upside faster than the on-chain realised response. Conversely, a break below zero signifies spot price trend reversal to the downside faster than the on-chain realised response.

    This metric can also provide market momentum and divergence signals, similar to those commonly used in technical analysis. The height and sequential change in height of oscillator peaks provides insight into the volume of coins moving within, or counter to the prevailing trend.

    Data Source: Coinmetrics.io and explorer.dcrdata.org

![Market-Gradient Oscillator Character](_images/dcronchain/07_dcr_gradient_character.png)

**References:**
    
    Paper by @_checkmatey_ on the Market-Realised Gradient Oscillator - https://medium.com/decred/decred-on-chain-realised-cap-mvrv-ratio-and-gradient-oscillators-a36ed2cc8182

    Video presentation - https://www.youtube.com/watch?v=HbquQIv9EYw&t=2155s

**Inputs:**

    Primary Y-Axis
        Market Cap                  = Coin supply * Coin PriceUSD (Daily close)
        Realised Cap                = Sum of Each unspent UTXO priced in BTC at the time it last moved
        Regular Tx Volume           = Volume spent in regular transactions (USD)
        Ticket Purchase Volume      = Volume spent in ticket purchase transactions (USD)
        CoinShuffle++ Mix Volume    = Volume spent in CoinShuffle++ Privacy Mixing transactions

    Secondary Y-Axis
        Market Gradient             = Gradient of market cap over specified period
        Realised Gradient           = Gradient of realised cap over specified period
        Delta Gradient              = Difference between Market and Realised Gradients


**Chart Description:**

    X-axis      
        Range   = Genesis to present
        Type    = date

    Y-axis-Left = Network Valuation (USD)
        Range   = 1e-2 to 1e3
        Type    = log

    Y-axis-Right = Market-Realised Gradient
        Range   = -3 to 5 for 28-day
                = -1 to 2 for 142-day
        Type    = linear

**Sample Chart:**

![Market-Realised Gradient Oscillator 28-day (light)](_images/dcronchain/07_dcr_market_realised_gradient_28day_light.png)
![Market-Realised Gradient Oscillator 142-day (light)](_images/dcronchain/07_dcr_market_realised_gradient_142day_light.png)
![Market-Realised Gradient Oscillator 28-day (dark)](_images/dcronchain/07_dcr_market_realised_gradient_28day_dark.png)
![Market-Realised Gradient Oscillator 142-day (dark)](_images/dcronchain/07_dcr_market_realised_gradient_142day_dark.png)


# Unrealised Profit and Loss

**Tags:**

    USD
    Momentum Model
    Realised Valuation
    Oscillator

**Checkonchain Code:**

    checkonchain.dcrcharts.charts.dcr_chart_suite(theme).unrealised_PnL().show()

        theme = 'light' or 'dark'

**JSON Files**

https://github.com/checkmatey/checkonchain/tree/master/hosted_charts/dcronchain/unrealisedpnl_oscillator_usd

**Blurb:**

    The Unrealised Profit and Loss metric calculates the net Profit of Loss of the aggregate market by taking the difference between the Market Cap and the Realised cost basis (normalised by Market Cap to form an oscillator). For Decred, coins are constantly on the move in tickets and in CoinShuffle++ mix transactions. Each time DCR is moved on chain, there is an explicit decision and opportunity cost to sell the coins, or not. Therefore, this metric should be interpreted to capture the profit and loss incurred since the last time DCR holders, on aggregate, interacted with their coins.

    Where the metric is positive, it indicates that market pricing is above the aggregate 'recency bias' level of the Realised Cap and conversely, when the metric is negative, market pricing is below the aggregate 'recency bias' level. Periods of extreme diversion from the Realised Cap mean (+- 50% PnL) are highlighted as Euphoria and Capitulation respectively. 

    Data Source: Coinmetrics.io

**References:**

    Adamant Capital introducing the Unrealised PnL for Bitcoin - https://medium.com/@adamant_capital/a-primer-on-bitcoin-investor-sentiment-and-changes-in-saving-behavior-a5fb70109d32

    Glassnode Revisiting the Unrealised PnL for Bitcoin - https://medium.com/glassnode-insights/dissecting-bitcoins-unrealised-on-chain-profit-loss-73e735020c8d

**Inputs:**

    Primary Y-Axis
        Market Cap      = Coin supply * Coin PriceUSD (Daily close)
        Realised Cap    = Sum of Each unspent UTXO priced at the time it last moved

    Secondary Y-Axis
        Unrealised PnL  = Normalised Unrealised Profit and Loss Oscillator
                        = Capitulation      --> UnrealisedPnL_Net < -0.50
                        = Hope Fear         --> -0.50 < UnrealisedPnL_Net < -0.25
                        = Optimism-Anxiety  --> -0.25 < UnrealisedPnL_Net < -0.25
                        = Belief-Denial     --> -0.25 < UnrealisedPnL_Net < -0.50
                        = Euphoria          --> UnrealisedPnL_Net > 0.50

**Chart Description:**

    X-axis      
        Range   = Genesis to present
        Type    = date

    Y-axis-Left = Network Valuation (USD)
        Range   = 1e5 to 1e10
        Type    = log

    Y-axis-Right = Unrealised PnL
        Range   = -1.5 to 3.5
        Type    = linear

**Sample Chart**

![Unrealised PnL](_images/dcronchain/08_dcr_unrealised_pnl_light.png)
![Unrealised PnL](_images/dcronchain/08_dcr_unrealised_pnl_dark.png)