# Pipeline DVC

``` sh
dvc stage add -n transformation -d step_01_transformation.py -d data/raw -o data/processed python step_01_transformation.py
dvc stage add -n normalization -d step_02_normalization.py python -d data/processed step_02_normalization.py
dvc stage add -n gridsearch -d step_03_gridsearch.py -d data/processed -o models/model.pkl python step_03_gridsearch.py
dvc stage add -n train -d step_04_training.py -d data/processed python step_04_training.py
dvc stage add -n evaluate -d step_05_evaluate.py -d data/processed python step_05_evaluate.py
```