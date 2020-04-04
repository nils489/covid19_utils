#!/bin/bash

git clone https://github.com/CSSEGISandData/COVID-19
(crontab -l 2>/dev/null; echo "0 */3 * * * $PWD/update.sh") | crontab -
