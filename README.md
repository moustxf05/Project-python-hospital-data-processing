# 🏥🐍 Traitement et Fusion de Données Hospitalières (Python)

Ce projet se concentre sur le **nettoyage**, le **traitement** et la **fusion** de deux ensembles de données hospitalières distincts (`hospital_data.csv` et `additional_hospital_data.csv`).  
L'objectif principal est de **créer un jeu de données unifié et propre** (`fusion_hospital_data.csv`) prêt pour l'analyse.

---

## 🎯 Objectif

Préparer et consolider des données hospitalières brutes provenant de **sources multiples** en un seul fichier CSV propre et structuré.

---

## 🗂️ Structure des Données

### 📥 Données Brutes (Input)
- `hospital_data.csv`  
- `additional_hospital_data.csv`

### 🧹 Données Nettoyées (Intermédiaires)
- `hospital_data_cleaned.csv`  
- `additional_hospital_data_cleaned.csv`

### 📤 Données Finales (Output)
- `fusion_hospital_data.csv`

---

## ⚙️ Méthodologie et Processus

La logique principale de traitement est implémentée dans le script **`projet.py`**.  
Les étapes clés incluent :

### 1. Chargement des données brutes  
### 2. Nettoyage des données (*Data Cleaning*) :
- Gestion des valeurs manquantes  
- Correction des types de données  
- Standardisation des formats  
- Traitement des incohérences ou erreurs spécifiques  
  *(voir `modifications_log.txt` pour le détail des changements appliqués)*  

### 3. Sauvegarde des versions nettoyées intermédiaires  
### 4. Fusion des données (*Data Merging*) :
- Combinaison des deux jeux de données nettoyés (`hospital_data_cleaned.csv`, `additional_hospital_data_cleaned.csv`) sur une ou plusieurs **clés communes**  
- Sauvegarde du fichier final `fusion_hospital_data.csv`

> Le fichier **`modifications_log.txt`** documente les étapes spécifiques de nettoyage et les transformations effectuées sur les données brutes.

---

## 🛠️ Outils Utilisés

- **Langage :** Python 3.x  
- **Bibliothèque principale :** Pandas (pour la manipulation et le nettoyage des données)

---

## ▶️ Comment Exécuter

1. Assurez-vous que **Python** et la bibliothèque **Pandas** sont installés.  
2. Placez les fichiers CSV d'entrée (`hospital_data.csv`, `additional_hospital_data.csv`) dans le même répertoire que le script `projet.py`.  
3. Exécutez le script depuis votre terminal :

```bash
python projet.py
