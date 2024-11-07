# Pipeline DVC

``` sh
dvc stage add -n transformation -d step_01_transformation.py -d data/raw -o data/processed python step_01_transformation.py
dvc stage add -n normalization -d step_02_normalization.py python step_02_normalization.py

```