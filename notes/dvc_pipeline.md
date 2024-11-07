# Pipeline DVC

``` sh
dvc stage add -n transformation -d step_01_transformation.py -d data/raw -o data/processed python step_01_transformation.py
```