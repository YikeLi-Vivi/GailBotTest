#!/bin/bash
# @Author: Vivian Li 
# @Date:   2024-04-05 08:41:53
# @Last Modified by:   Vivian Li 
# @Last Modified time: 2024-04-07 10:18:50
conda create --name gb-test python==3.10
conda activate gb-test
python -m pip install --extra-index-url https://test.pypi.org/simple/  GailBot==0.0.2a16
pip install git+https://github.com/m-bain/whisperx.git
