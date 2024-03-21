import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns


df = pd.read_csv('comptage-velo-donnees-compteurs.csv', sep = ';')

st.title("Comment analyser et prédire le trafic cycliste Parisien")
st.write("Par Anne Levet-Figueredo, Karine Mahmri, Kaity Kone")
st.write("Cohorte DA septembre 2023")
st.image('bis.jpg')


st.sidebar.image("velo.png", width= None)
st.sidebar.title("Sommaire")

pages=["Présentation du projet", "Exploration des données", "DataVizualization", "Modélisation"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0]:
    st.write("### Présentation du projet")
    st.write("A part pour Karine qui a spécifiquement sélectionné ce thème, ce projet a été attribué à Anne et Kaity. Il ne concerne pas nos entreprises actuelles et nous nous sommes donc imprégnées des données et du contexte chacune en même temps.")
    st.write("Dans un contexte d'environnement climatique tendu, nous sommes tous sensibilisés à l’enjeu des moyens de transport éco responsable depuis plusieurs années, dont le vélo est largement préconisé.")
    st.write("En effet, d’après le site du gouvernement.fr, l’utilisation du vélo est mise en avant grâce à 6 principales raisons :")
    st.write("- réduire de 30% le risque de maladie")
    st.write("- moins de risque d’être blessés qu’en voiture")
    st.write("- économiser 650 kilogrammes de CO2 par personne/an")
    st.write("- c’est le moyen de déplacement le plus performant pour les trajets de moins de 5km")
    st.write("- le coût des dépenses est de 100€/an à vélo contre 1 000€/an en voiture")
    st.write("- plus de problèmes de stationnement")


st.write("Pour des trajets travail/maison ainsi que les balades dominicales, surtout à Paris, 42ème ville la plus polluée d’après https://www.iqair.com/fr/world-air-quality-ranking, le vélo est un moyen de transport majeur.") 

st.write("Plusieurs primes à destination des employeurs et des particuliers sont d’ailleurs mises en place afin de pousser à l’utilisation des mobilités douces et durables comme le FMD.")

st.write("A partir du dataset de bornes de comptage de passages de vélos qui nous a été fourni, nous réalisons une étude qui consiste à identifier les corrélations entre la variable cible de fréquentation et les autres variables catégorielles et explicatives. Nous souhaitons principalement mettre en avant l’utilisation des bornes Velibs à Paris afin de faciliter leur travaux d’amélioration (augmentation du nombre de velibs disponibles aux stations) en fonction des prédictions que nous effectuerons grâce au Machine Learning sur les 7/8/9/10 prochains jours en temps réel.")

st.write("L’objectif de cette étude est de prédire la fréquentation cycliste afin de faciliter la mobilité dans la ville de Paris grâce à l’amélioration de deux axes : amélioration des plans des pistes cyclables en fonction des lieux culturels et événementiels à Paris prédictions de la quantité de vélos disponibles aux différentes stations de velibs à J+1. Le Dataset étant sur une année réelle de octobre 2022 à novembre 2023, nous pourrons aussi envisager de prédire les fréquentations sur les zones des stations de velibs. Cette étude permettra de visualiser si les capacités des bornes de velibs sont cohérentes en fonction du nombre de passages de la zone afin d’envisager des travaux de réaménagement..")

st.write("Nous notons que les compteurs de passage horaire quantifient le passage de tous types de velos : usagers, velibs, electriques…")


if page == pages[1] : 
  st.write("### Exploration des données")
  st.dataframe(df.head(10))
  st.write('La dimension du dataset est :', df.shape)
  st.dataframe(df.describe())
  if st.checkbox("Afficher les NA") :
    st.dataframe(df.isna().sum())

if page == pages[2] : 
  st.write("### DataVizualization")


if page == pages[3] : 
  st.write("### Modélisation")