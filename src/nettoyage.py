"""Module de nettoyage et de standardisation des données de salaires."""

from nbclient import execute
import pandas as pd


def categorize_role(title: str) -> str:
    """Regroupe un intitulé de poste en grande famille métier."""
    t = str(title).lower()
    if any(
        k in t
        for k in [
            "machine learning",
            "ml",
            "ai",
            "artificial intelligence",
            "deep learning",
        ]
    ):
        return "IA & Machine Learning"
    if any(k in t for k in ["data engineer", "etl", "database", "pipeline"]):
        return "Data Engineering"
    if any(
        k in t for k in ["data scientist", "research", "applied scientist"]
    ):
        return "Data Science"
    if any(k in t for k in ["analyst", "analytics", "bi", "business intelligence"]):
        return "Data Analytics"
    return "Autre Data"


def clean_salaries_pipeline(
    df_salaries: pd.DataFrame, df_geo: pd.DataFrame
) -> pd.DataFrame:
    """Exécute l'ensemble du pipeline de nettoyage des salaires."""
    df = df_salaries.copy()

    # 1. Harmonisation du niveau d'expérience
    level_map = {
        "EN": "Entry-level",
        "MI": "Mid-level",
        "SE": "Senior",
        "EX": "Lead / Executive",
        "Entry-level": "Entry-level",
        "Mid-level": "Mid-level",
        "Senior": "Senior",
        "Lead / Executive": "Lead / Executive",
    }
    df["experience_level"] = df["experience_level"].map(level_map).fillna(
        df["experience_level"]
    )

    # 2. Catégorisation des intitulés de poste
    df["job_group"] = df["job_title"].apply(categorize_role)

    # 4. Jointure géographique
    cols_geo = ["CLDR display name", "Continent", "Sub-region Name"]
    geo_clean = (
        df_geo[cols_geo]
        .dropna(subset=["CLDR display name"])
        .drop_duplicates(subset=["CLDR display name"])
    )
    df = df.merge(
        geo_clean,
        left_on="employee_residence",
        right_on="CLDR display name",
        how="left",
    )

    return df
