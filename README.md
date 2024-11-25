# Examen DVC et Dagshub

Je me suis inspiré de ce que j'ai vu en cours pour faire mon examen. 
J'ai utilisé une partie des scripts du repo suivant :
https://github.com/DataScientest/overview_mlops_wine_quality_student


```txt       
├── data                        dossier contenant les données
├── logs                        logs des scripts python
├── metrics                     metrics du modèle
├── models                      dossier contenant les modèles
├── notes
├── src                         source des scripts
├── venv
├── README.md
├── custom_logger.py
├── dvc.lock
├── dvc.yaml
├── models.dvc
├── requirements.txt
├── step_01_transformation.py
├── step_02_normalization.py
├── step_03_gridsearch.py
├── step_04_training.py
└── step_05_evaluate.py
```

## Todo
- [x] compléter le dvc.yaml (schéma qui n'apparaît pas)
- [ ] Votre dossier src manque les dossiers data et models avec les scripts bien rangés
- [ ] Il manque le dossier .dvc/config config contenant les informations par rapport au stockage distant. 
- [ ] Il manque le dossier models avec le model entraîné sous format .pkl. 
- [ ] Le fichier dvc.lock ne contient pas l'information du stockage de chaque étape de la pipeline. 
- [ ] Puis votre onglet data n'affiche pas les données. 
- [ ] Et enfin il n'y a pas de fichier csv avec les prédictions. 