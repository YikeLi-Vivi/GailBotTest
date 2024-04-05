Test Step 
- run the following command 
  - conda create --name gb-test python==3.10 
  - conda activate gb-test
  - python -m pip install --extra-index-url https://test.pypi.org/simple/  GailBot==0.0.2a12
  - pip install git+https://github.com/m-bain/whisperx.git  
  - python gailbot_sample.py
- check output directory