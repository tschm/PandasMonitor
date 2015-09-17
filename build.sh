#!/bin/bash
FOLDER="$(cd "$(dirname "$0")" && pwd)"
rm -rf ${FOLDER}/env
conda create --yes -p ${FOLDER}/env python=3.4.3 pandas=0.16.2 pyqt=4.11.3 matplotlib=1.4.3




