# Analyse des Salaires dans la Data & l'IA

Projet d'analyse exploratoire et de traitement de données axé sur les rémunérations dans les métiers de la Data et de l'Intelligence Artificielle.

## Structure du projet

- `data/`
  - `raw/` : Données brutes sources (`jobs_in_data.csv`, `cost_of_living.csv`).
  - `processed/` : Données nettoyées et enrichies (`cleaned_salaries.csv`).
- `figures/` : 5 visualisations générées au format PNG.
- `notebooks/`
  - `01_exploration.ipynb` : Audit du schéma, détection des 4 014 doublons stricts.
  - `02_nettoyage.ipynb` : Pipeline de déduplication, typage, regroupement métier et jointure géographique.
  - `03_analyse.ipynb` : Agrégations statistiques, visualisations et conclusions métier.
- `src/`
  - `nettoyage.py` : Fonctions réutilisables du pipeline de données.
- `requirements.txt` : Dépendances figées du projet.

## Reproduction de l'environnement

```bash
pip install -r requirements.txt


