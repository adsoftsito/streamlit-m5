import streamlit as st 
import datetime
import pandas as pd 
import matplotlib.pyplot as ptl
import numpy as np

titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = pd.read_csv(titanic_link)

st.title("Mi primera App con Streamlit")

sidebar = st.sidebar
sidebar.title("Esto es la barra lateral")
sidebar.write("Aqui van los elementos de entrada")

sidebar.title("Información sobre el conjunto de datos")
st.header("Descripción de los datos")
st.write("Este es un simple ejemplo de una App para predecir datos")

today = datetime.date.today()
today_date = sidebar.date_input('Cual es tu cumple : ', today)

st.success(f'tu cumple es: {today_date} felicidades...') 

st.header("Titanic Dataset")

agree = sidebar.checkbox("Desea ver la data ? ")
if agree:
  st.dataframe(titanic_data)

st.header("Class Description")
selected_class = sidebar.radio("Select Class", titanic_data['class'].unique())


st.success(f'Selected Class: {selected_class}') 

st.markdown("___")

selected_sex = sidebar.selectbox("Select Sex", titanic_data['sex'].unique())

st.success(f'Selected sex: {selected_sex}') 

optionals = sidebar.expander("Optional Configurations", True)

fare_select = optionals.slider( 
  "Select the age",
  min_value = float(titanic_data['age'].min()),
  max_value = float(titanic_data['age'].max())
)

subset_fare = titanic_data[(titanic_data['age'] >= fare_select)]

st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")
st.dataframe(subset_fare)

fig, ax = ptl.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)

fig2, ax2 = ptl.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')
st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)

st.markdown("___")
fig3, ax3 = ptl.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Grafica -de - Dispersión del Titanic")
st.pyplot(fig3)

map_data = pd.DataFrame( np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])

st.tittle("san fracisco map")
st.header("using streamlit an Mapbox")
st.map(map_data)