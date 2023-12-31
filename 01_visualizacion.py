import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if st.checkbox('mostrar texto'): #si esto es true, si la cacilla se activa(se selecciona)
    st.write('hola')           #se realizara esata accion

fields = ['country','points','price','variety']

df = pd.read_csv('wine_reviews.csv', usecols=fields)
df.dropna(inplace=True)
if st.checkbox('Mostrar df'):
    st.dataframe(df)

if st.checkbox('vista de datos Head o Tail'):
    if st.button('Mostrar Head'):
        st.write(df.head())
    if st.button('mostrar Tail'):
        st.write(df.tail())

dim = st.radio('Dimension a mostrar:',('Filas','Columnas'),horizontal = True)
if dim == 'Filas':
    st.write('Cantidad de filas:', df.shape[0])
else:
    st.write('Cantidad de columnas:', df.shape[1])

precio_liminte= st.slider('Definir precio maximo', 0, 400, 250)

fig = plt.figure(figsize=(6,4))
sns.scatterplot(x='price',y ='points',data=df[df['price']<precio_liminte])
st.pyplot(fig)
#seleccion multiple:
countries_list = df['country'].unique().tolist()
countries = st.multiselect('seleccione un/unos pais/es a analizar:', countries_list, default=('Argentina','Chile','Spain'))
df_countries = df[df['country'].isin(countries)]

fig = plt.figure(figsize=(6,4))
sns.scatterplot(x='price',y ='points',hue='country',data=df_countries)
st.pyplot(fig)


col1, col2 = st.columns(2)
with col1:
    df_countries= df [df['country']== 'Argentina']
    fig = plt.figure()
    sns.scatterplot(x='price',y='points',data=df_countries)
    plt.title('Puntajes segun precio para Argentina')
    st.pyplot(fig)

with col2:
    df_countries= df [df['country']== 'Chile']
    fig = plt.figure()
    sns.scatterplot(x='price',y='points',data=df_countries)
    plt.title('Puntajes segun precio para Chile')
    st.pyplot(fig)