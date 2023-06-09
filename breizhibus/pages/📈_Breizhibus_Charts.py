import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import mysql.connector
import matplotlib.pyplot as plt



mydb = mysql.connector.connect(
host="localhost",
port="3307",
user="admin_bzhbus",
password="BS2SJy69b6tsk2",
database="Breizhibusoff")

mycursor = mydb.cursor()   # Exécution de la requête SQL
#Exercice 1
mycursor.execute("SELECT SUM(f.nbr_passager), l.Nom as nom FROM frequentation f INNER JOIN Horaire h ON f.horaire = h.id INNER JOIN Lignes l ON h.ligne = l.id GROUP BY l.Nom ORDER BY l.Nom")
result1 = mycursor.fetchall()   # Création du curseur
df = pd.DataFrame(result1, columns=["Nbr_Passager","Nom"])



st.markdown('''<style>
.css-ffhzg2 {

background-image: url(https://w.forfun.com/fetch/87/87c93aa33275b4c8c73637ad3fbee836.jpeg?w=1000&r=0.5625);
background-size: cover;}


</style>''', unsafe_allow_html=True)

# Créer un histogramme avec Seaborn
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set_style('whitegrid')
plt.figure(figsize=(8, 5))
sns.barplot(x='Nom', y='Nbr_Passager', data=df)
plt.xlabel('Nom')
plt.ylabel('Nbr_Passager')
plt.title('Nombre de passagers par nom de ligne')
plt.xticks(rotation=45)
#afficher l'histogramme dans Streamlit

st.pyplot()

#Exercice 2
mycursor.execute('SELECT SUM(f.nbr_passager) AS nbr_passager, h.heure FROM frequentation f INNER JOIN Horaire h ON f.horaire = h.id GROUP BY f.horaire ORDER BY h.heure')
result2 = mycursor.fetchall()   # Création du curseur
df = pd.DataFrame(result2, columns=["nbr_passager","heure"])

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(8, 5))
plt.plot(df['heure'], df['nbr_passager'])
plt.xlabel('heure')
plt.ylabel('nbr_passager')
plt.title('Nombre de passagers par nom de ligne')
plt.xticks(rotation=45)
#afficher l'histogramme d

st.pyplot()

st.markdown('<style>h1{color: rgb(131 16 16)}</style>', unsafe_allow_html=True)

#Exercice 3 : pie

mycursor.execute("SELECT jour, SUM(nbr_passager) AS nbr_passager FROM frequentation GROUP BY jour ORDER BY jour ASC")
result = mycursor.fetchall()   # Création du curseur
df = pd.DataFrame(result, columns=mycursor.column_names)
plt.figure(figsize=(6,5),dpi=80)
level_counts = df['nbr_passager'].value_counts()
fig, axe = plt.subplots()
axe.pie(level_counts.index, labels=level_counts.index, autopct='%1.1f%%')
st.pyplot(fig)


