import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sbn
import mysql.connector
import matplotlib.pyplot as plt
from PIL import Image


#print aplly name
#bus map network, picture from the web
#print the schedule by lign

mydb = mysql.connector.connect(
host="localhost",
port="3307",
user="admin_bzhbus",
password="BS2SJy69b6tsk2",
database="Breizhibusoff")

mycursor = mydb.cursor()   # Exécution de la requête SQL

mycursor.execute('''SELECT heure, adresse
FROM Horaire h
INNER JOIN Arret A ON A.adresse = h.id''')
result = mycursor.fetchall()   # Création du curseur

st.title("Breizhibus")

image = Image.open('bzhmap.jpg')

st.image(image, caption='Plan du réseau')

st.markdown('''<style>
h1 {
    color:rgb(181 22 87); 
} 
.css-ffhzg2 {

background-image: url(https://www.10wallpaper.com/wallpaper/medium/1712/Yosemite_Jungle_Waterfall_Rivers_iMac_Retina_4K_Ultra_HD_medium.jpg);
background-size: cover;

}
.st-bw {
    background-color: rgb(12 17 61);
}
</style>''', unsafe_allow_html=True)


df = pd.DataFrame(result, columns=mycursor.column_names)
selected_line = st.selectbox('Select a line', df['adresse'].unique())
filtered_df = df[df['adresse'] == selected_line]


st.dataframe(filtered_df)