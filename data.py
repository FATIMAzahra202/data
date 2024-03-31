# app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
@st.cache  # Cette annotation permet de cacher les données pour accélérer l'application
def load_data():
    data = pd.read_csv('votre_fichier_de_données.csv')
    return data

data = load_data()

# Titre de l'application
st.title('Exploration de Données avec Streamlit')

# Affichage de quelques données
st.write('Voici un aperçu des données :')
st.write(data.head())

# Sélection d'une colonne pour visualiser
col_to_plot = st.selectbox('Quelle colonne souhaitez-vous visualiser ?', data.columns)

# Création d'un histogramme
st.write(f'Histogramme de {col_to_plot}:')
fig, ax = plt.subplots()
sns.histplot(data[col_to_plot], ax=ax)
st.pyplot(fig)
