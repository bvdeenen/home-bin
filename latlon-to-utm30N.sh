#!/usr/bin/env bash

set -e
DIR=$(dirname $(readlink -f $0))
source ~/py314/bin/activate

python $DIR/latlon-to-utm30N.py

