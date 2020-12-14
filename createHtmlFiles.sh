#!/bin/bash
HOME="/root/checkonchain"
BTC_ONCHAIN_PATH="${HOME}/hosted_charts/btconchain"
DCR_ONCHAIN_PATH="${HOME}/hosted_charts/dcronchain"

export PYTHONPATH=/root/

# Remove old files
${HOME}/removeGeneratedFiles.sh

# Generate base charts
echo "Generating BTC charts ..."
cd ${HOME}/btconchain/charts
python3 ./btc_charts_plotting.py > /dev/null

# Add navigation bar and description
cd ${BTC_ONCHAIN_PATH}
for dir in `find . -mindepth 1 -maxdepth 1 -type d` ; do
    cp -f ../../navbar_template.html ${dir} 2>&1 > /dev/null
    cd ${dir}
    cat "${dir}_light.html" >> navbar_template.html 2> /dev/null
    cat description.html >> navbar_template.html 2> /dev/null
    cp navbar_template.html "${dir}_light.html" 2>&1 > /dev/null
    rm navbar_template.html
    cd - 2>&1 > /dev/null
done

echo "Generating DCR charts ..."
cd ${HOME}/dcronchain/charts
python3 ./dcr_charts_plotting.py > /dev/null

cd ${DCR_ONCHAIN_PATH}
for dir in `find . -mindepth 1 -maxdepth 1 -type d` ; do
    cp -f ../../navbar_template.html ${dir} 2>&1 > /dev/null
    cd ${dir}
    cat "${dir}_light.html" >> navbar_template.html 2> /dev/null
    cat description.html >> navbar_template.html 2> /dev/null
    cp navbar_template.html "${dir}_light.html" 2>&1 > /dev/null
    rm navbar_template.html
    cd - 2>&1 > /dev/null
done
cd ${HOME}