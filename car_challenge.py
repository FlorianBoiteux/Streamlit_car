import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title = "Car Study")

# Header section

with st.container():
    st.title("Bienvenue")
    st.write("Dans cette page, nous allons étudier une base de données qui reprend 261 voitures, sorties entre 1971 et 1983 et nous concentrer sur la colonne accélération de 0 à 100km/h.")


# Importation du DF + nettoyage :

with st.container():
    st.write("---") # divider
    st.header("Aperçu du DataFrame : ")
    link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
    df_car = pd.read_csv(link)
    df_car["continent"] = df_car["continent"].str[:-1]
    st.dataframe(df_car)
    
# Affichage de la correlation_heatmap :

with st.container():
    st.write("---") # divider
    st.header("Analyse de corrélation :")
    viz_correlation = sns.heatmap(df_car.corr(), center = 0, cmap = sns.color_palette("vlag", as_cmap = True))
    st.pyplot(viz_correlation.figure)
    st.write("Les cases en bleu et en rouge montrent les corrélations (positives ou négatives) entre les colonnes.")
    st.markdown(""" * **Exemple de corrélation positive (en rouge) :**'Cylinders'/'hp' : plus il y a de cylindres dans la voiture, plus
              la puissance en chevaux du véhicule est importante.""")
    st.markdown(""" * **Exemple de corrélation négative (en bleu) :** 'hp'/'time-to-60' : plus la puissance en chevaux de la voiture est importante,
             moins la durée de 0 à 100kmh/ est importante.""")


# Graphique

with st.container():
    st.write("---") # divider
    st.header("Représentation graphique des données, par continent : ")

    continent = df_car["continent"].unique()
    select_continent = st.selectbox("Choisir un continent : ", continent, index=0)

  


    st.subheader("Moyenne de la valeur 0 à 100km/h, par année de sortie :")
    pvt_car = df_car.loc[df_car["continent"] == select_continent].pivot_table(values = "time-to-60", index = "year", aggfunc = "mean")
    fig2 = plt.figure(figsize=(10, 3))
    plt.plot(pvt_car)
    st.pyplot(fig2)

    st.subheader("Rapport entre la puissance en chevaux du véhicule et le temps de 0 à 100km/h :")
    fig3 = plt.figure(figsize=(10, 3))
    plt.scatter(data = df_car.loc[df_car["continent"] == select_continent], x = "hp", y= "time-to-60")
    st.pyplot(fig3)






     
    