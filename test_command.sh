#!/bin/bash
# @Author: Vivian Li 
# @Date:   2024-04-05 08:41:53
# @Last Modified by:   Vivian Li 
# @Last Modified time: 2024-04-05 12:42:41
conda create --name gb-test 
conda activate gb-test
conda install pip
python -m pip install --extra-index-url https://test.pypi.org/simple/  GailBot==0.0.2a13
pip install git+https://github.com/m-bain/whisperx.git
