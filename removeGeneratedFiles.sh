#!/bin/bash
HOME="/root/checkonchain"
BTC_ONCHAIN_PATH="${HOME}/hosted_charts/btconchain"
DCR_ONCHAIN_PATH="${HOME}/hosted_charts/dcronchain"

export PYTHONPATH=/root/

# Remove old files
echo "Removing old files ..."
cd ${BTC_ONCHAIN_PATH}
for dir in `find . -mindepth 1 -maxdepth 1 -type d` ; do
    cd ${dir}
    rm ${dir}* 2> /dev/null
    cd - 2>&1 > /dev/null
done

cd ${DCR_ONCHAIN_PATH}
for dir in `find . -mindepth 1 -maxdepth 1 -type d` ; do
    cd ${dir}
    rm ${dir}* 2> /dev/null
    cd - 2>&1 > /dev/null
done
