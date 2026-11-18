# DM2 - AdaBoost sur MNIST

Ce dépôt contient les expériences du devoir de machine learning sur la
classification des chiffres manuscrits MNIST avec AdaBoost. Plusieurs
classifieurs faibles sont comparés (perceptron, stump et arbres de décision),
dans l'espace des pixels et dans un embedding de dimension réduite.

## Organisation

- `0_classification chiffre à chiffre/` : expériences de classification paire
  par paire, résultats et figures associées.
- `1_Un chiffre contre tous/` : notebook et modèles sauvegardés pour les dix
  problèmes « un chiffre contre tous ».
- `2_Par tranches/` : classification des tranches `0--4` contre `5--9`.
- `src/` : fonctions utilitaires, notamment le chargement de MNIST.
- `data/` : données téléchargées ou mises en cache par OpenML.
  rapport.
- `Rapport.pdf` et `Sujet.pdf` : rapport final et énoncé du devoir.
- `requirement.txt` : dépendances Python du projet.

## Installation
dans un venv:
```bash
pip install -r requirement.txt
```

Les expériences sont exécutées dans les notebooks Jupyter présents dans les
répertoires correspondants.