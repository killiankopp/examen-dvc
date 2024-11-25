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
- [x] Votre dossier src manque les dossiers data et models avec les scripts bien rangés
- [x] Il manque le dossier .dvc/config (config contenant les informations par rapport au stockage distant)
- [x] Il manque le dossier models avec le model entraîné sous format .pkl
- [ ] Le fichier dvc.lock ne contient pas l'information du stockage de chaque étape de la pipeline. 
- [ ] Puis votre onglet data n'affiche pas les données. 
- [ ] Et enfin il n'y a pas de fichier csv avec les prédictions. 

## Do
### fichier dvc.yaml
J'ai fait plusieurs tests, j'avais oublié de le remettre au dernier commit. c'est chose faite... mais ça ne change absolument rien ! 
Il est là, complété mais le schéma n'apparaît toujours pas

### Votre dossier src manque les dossiers data et models avec les scripts bien rangés
J'ai rangé les scripts. Les dossers models et data sont ignorés par un gitignore

### il manque le dossier config
Il contient des secrets, il était volontairement absent, j'ai tout de même tenté de l'ajouter mais j'ai un refus de Github
remote: error: GH013: Repository rule violations found for refs/heads/master.        
remote: 
remote: - GITHUB PUSH PROTECTION        
remote:   —————————————————————————————————————————        
remote:     Resolve the following violations before pushing again        
remote: 
remote:     - Push cannot contain secrets        
remote: 
remote:             
remote:      (?) Learn how to resolve a blocked push        
remote:      https://docs.github.com/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line#resolving-a-blocked-push        
remote:             
remote:             
remote:       —— Google OAuth Client ID ————————————————————————————        
remote:        locations:        
remote:          - commit: 7f90089687909cfac146013c5ae79648fa07f746        
remote:            path: .dvc/config:6        
remote:             
remote:        (?) To push, remove secret from commit(s) or follow this URL to allow the secret.        
remote:        https://github.com/killiankopp/examen-dvc/security/secret-scanning/unblock-secret/2pLhO97XeJOMtadHASTvxcR2oSy        
remote:             
remote:             
remote:       —— Google OAuth Client Secret ————————————————————————        
remote:        locations:        
remote:          - commit: 7f90089687909cfac146013c5ae79648fa07f746        
remote:            path: .dvc/config:7        
remote:             
remote:        (?) To push, remove secret from commit(s) or follow this URL to allow the secret.        
remote:        https://github.com/killiankopp/examen-dvc/security/secret-scanning/unblock-secret/2pLhOBpC1VGdUzQ5laXtERbwAnQ        
remote:             
remote: 
remote: 
error: failed to push some refs to 'github.com:killiankopp/examen-dvc.git'
To github.com:killiankopp/examen-dvc.git
!	refs/heads/master:refs/heads/master	[remote rejected] (push declined due to repository rule violations)