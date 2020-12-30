@ echo off
set BTC_ONCHAIN_PATH=hosted_charts\btconchain
set DCR_ONCHAIN_PATH=hosted_charts\dcronchain
set PYTHONPATH=C:\GitHub\

::Generate base charts
python btconchain\charts\btc_charts_plotting.py
python dcronchain\charts\dcr_charts_plotting.py


:: Add navigation bar and description
for /f %%d in ('dir /ad /b %BTC_ONCHAIN_PATH%') do (
	copy /Y navbar_template.html %BTC_ONCHAIN_PATH%\%%d > NUL
	pushd %BTC_ONCHAIN_PATH%\%%d
	type %%d_light.html >> navbar_template.html
	type description.html >> navbar_template.html
	copy navbar_template.html %%d_light.html > NUL
	del navbar_template.html
	popd)

for /f %%d in ('dir /ad /b %DCR_ONCHAIN_PATH%') do (
	copy /Y navbar_template.html %DCR_ONCHAIN_PATH%\%%d > NUL
	pushd %DCR_ONCHAIN_PATH%\%%d
	type %%d_light.html >> navbar_template.html
	type description.html >> navbar_template.html
	copy navbar_template.html %%d_light.html > NUL
	del navbar_template.html
	popd)