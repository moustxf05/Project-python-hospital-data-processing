import pandas as pd
from datetime import datetime

# Fonction pour enregistrer les changements dans un fichier de log
def log_change(change):
    """
    Enregistre une modification dans un fichier de log.
    
    Args:
    change (str): Le texte décrivant la modification effectuée.
    """
    with open("modifications_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(change + "\n")

# Charger les données CSV dans des DataFrames
df = pd.read_csv("hospital_data.csv")
df2 = pd.read_csv("additional_hospital_data.csv")

log_change("Chargement des données CSV dans les DataFrames.")

# Supprimer les lignes où "Diagnosis" ou "TreatmentCost" est manquant
df = df.dropna(subset=["Diagnosis", "TreatmentCost"])
df2 = df2.dropna(subset=["Diagnosis", "TreatmentCost"])

log_change("Suppression des lignes avec des valeurs manquantes dans 'Diagnosis' ou 'TreatmentCost'.")

# Nettoyer et uniformiser la colonne "Diagnosis"
df["Diagnosis"] = df["Diagnosis"].str.upper().str.strip()
df2["Diagnosis"] = df2["Diagnosis"].str.upper().str.strip()

log_change("Nettoyage et uniformisation des valeurs de la colonne 'Diagnosis'.")

# Convertir les colonnes de dates en format datetime et reformater en DD/MM/YYYY
df["DOB"] = pd.to_datetime(df["DOB"], errors="coerce").dt.strftime("%d/%m/%Y")
df["LastVisit"] = pd.to_datetime(df["LastVisit"], errors="coerce").dt.strftime("%d/%m/%Y")
df2["DOB"] = pd.to_datetime(df2["DOB"], errors="coerce").dt.strftime("%d/%m/%Y")
df2["LastVisit"] = pd.to_datetime(df2["LastVisit"], errors="coerce").dt.strftime("%d/%m/%Y")

log_change("Conversion des colonnes de dates au format DD/MM/YYYY.")

# Remplir les valeurs manquantes dans "Diagnosis" par "Inconnu"
df["Diagnosis"] = df["Diagnosis"].fillna("Inconnu")
df2["Diagnosis"] = df2["Diagnosis"].fillna("Inconnu")

log_change("Remplissage des valeurs manquantes dans 'Diagnosis' par 'Inconnu'.")

# Remplir les valeurs manquantes dans "TreatmentCost" par la moyenne de la colonne
df["TreatmentCost"] = df["TreatmentCost"].fillna(df["TreatmentCost"].mean())
df2["TreatmentCost"] = df2["TreatmentCost"].fillna(df2["TreatmentCost"].mean())

log_change("Remplissage des valeurs manquantes dans 'TreatmentCost' par la moyenne.")

# Remplir les valeurs manquantes dans "LastVisit" par une date par défaut
df["LastVisit"] = df["LastVisit"].fillna("2024-12-31")
df2["LastVisit"] = df2["LastVisit"].fillna("2024-12-31")

log_change("Remplissage des valeurs manquantes dans 'LastVisit' par la date par défaut '2024-12-31'.")

# Sauvegarder les résultats nettoyés dans de nouveaux fichiers CSV
df.to_csv("hospital_data_cleaned.csv", index=False)
df2.to_csv("additional_hospital_data_cleaned.csv", index=False)

log_change("Sauvegarde des DataFrames nettoyés dans 'hospital_data_cleaned.csv' et 'additional_hospital_data_cleaned.csv'.")

# Ajouter une colonne Age calculée à partir de la date de naissance (DOB)
current_date = datetime.now()  # Obtenir la date actuelle

df["Age"] = pd.to_datetime(df["DOB"], errors="coerce", format="%d/%m/%Y").apply(
    lambda x: current_date.year - x.year if pd.notnull(x) else None
)
df2["Age"] = pd.to_datetime(df2["DOB"], errors="coerce", format="%d/%m/%Y").apply(
    lambda x: current_date.year - x.year if pd.notnull(x) else None
)

log_change("Ajout de la colonne 'Age' calculée à partir de 'DOB'.")

# Sauvegarder les DataFrames avec la colonne "Age" ajoutée
df.to_csv("hospital_data_cleaned.csv", index=False)
df2.to_csv("additional_hospital_data_cleaned.csv", index=False)

log_change("Sauvegarde des DataFrames avec la colonne 'Age' ajoutée.")

# Ajouter la colonne "Statut" pour df et df2
df["Statut"] = df["Diagnosis"].apply(lambda x: "Sain" if x == "HEALTHY" else "Malade")
df2["Statut"] = df2["Diagnosis"].apply(lambda x: "Sain" if x == "HEALTHY" else "Malade")

log_change("Ajout de la colonne 'Statut' en fonction du 'Diagnosis'.")

# Sauvegarder les deux fichiers avec les nouvelles colonnes
df.to_csv("hospital_data_cleaned.csv", index=False)
df2.to_csv("additional_hospital_data_cleaned.csv", index=False)

log_change("Sauvegarde des fichiers avec la nouvelle colonne 'Statut'.")

# Fusionner les deux DataFrames en supprimant les doublons sur la base de la colonne PatientID
merged_df = pd.merge(df, df2, on="PatientID", how="outer", suffixes=('_df1', '_df2'))

log_change("Fusion des deux DataFrames sur la base de la colonne 'PatientID'.")

# Combinaison des colonnes doublon : garder celles de df1 (ou df2) uniquement
merged_df["Name"] = merged_df["Name_df1"].fillna(merged_df["Name_df2"])
merged_df["DOB"] = merged_df["DOB_df1"].fillna(merged_df["DOB_df2"])
merged_df["Diagnosis"] = merged_df["Diagnosis_df1"].fillna(merged_df["Diagnosis_df2"])
merged_df["LastVisit"] = merged_df["LastVisit_df1"].fillna(merged_df["LastVisit_df2"])
merged_df["TreatmentCost"] = merged_df["TreatmentCost_df1"].fillna(merged_df["TreatmentCost_df2"])
merged_df["Age"] = merged_df["Age_df1"].fillna(merged_df["Age_df2"])
merged_df["Statut"] = merged_df["Statut_df1"].fillna(merged_df["Statut_df2"])

log_change("Combinaison des colonnes doublon et conservation des valeurs des colonnes principales.")

# Supprimer les anciennes colonnes doublons
merged_df = merged_df.drop(columns=["Name_df1", "DOB_df1", "Diagnosis_df1", "LastVisit_df1", "TreatmentCost_df1", "Age_df1", "Statut_df1",
                                    "Name_df2", "DOB_df2", "Diagnosis_df2", "LastVisit_df2", "TreatmentCost_df2", "Age_df2", "Statut_df2"])

log_change("Suppression des colonnes doublons après la fusion.")

# Sauvegarder le DataFrame fusionné dans un nouveau fichier CSV
merged_df.to_csv("fusion_hospital_data.csv", index=False)

log_change("Sauvegarde du fichier fusionné dans 'fusion_hospital_data.csv'.")
