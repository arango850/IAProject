import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import sklearn 
from PIL import Image

st.title('F1')

def load_data():
    data= pd.read_csv(r"data.csv")
    return data

def load_Nombres():
    dataNombres = pd.read_csv(r"dataNombres.csv")
    return dataNombres

def load_equipos():
     dataEquipos= pd.read_csv(r"dataEquipos.csv")
     return dataEquipos
def load_GP():
    dataGP = pd.read_csv(r"dataGP.csv")
    return dataGP
def load_nacionalidades():
    dataNacionalidades= pd.read_csv(r"dataNacionalidades.csv")
    return dataNacionalidades
def load_status():
    dataStatus= pd.read_csv(r"dataStatus.csv")
    return dataStatus

st.text("Indice de Nombres")
dataNombres= load_Nombres()
st.dataframe(dataNombres)

st.text("Indice de equipos")
dataEquipos = load_equipos()
st.dataframe(dataEquipos)

st.text("Indice de Grandes Premios")
dataGP = load_GP()
st.dataframe(dataGP)


dataNacion = load_nacionalidades()
st.dataframe(dataNacion)

dataStatus = load_status()
st.dataframe(dataStatus)

def load_modelD():
    loaded_model = joblib.load("rnDriver.joblib")
    return loaded_model

def load_modelP():
    loaded_model1= joblib.load("dtPoints.joblib")
    return loaded_model1


st.title("Inputs para modelo de piloto")


racerId= st.number_input("racerId")
constructorId= st.number_input("constructorId")
grid= st.number_input("grid")
finish= st.number_input("finish")
points= st.number_input("points")
laps = st.number_input("laps")
timetaken_in_millisec= st.number_input("timetaken_in_millisec")
fastestLap= st.number_input("fastestLap")
max_speed= st.number_input("max_speed")
statusId= st.number_input("statusId")
year= st.number_input("year")
wins= st.number_input("wins")
age= st.number_input("age")
nationalityN= st.number_input("nationalityN")

clicked= st.button("Predecir")
model = load_modelD()

if clicked:
    print("Resolviendo")
    resultado= model.predict(pd.DataFrame({"racerId":[racerId],
                       "constructorId":[constructorId],"grid":[grid],"finish":[finish],
                       "points":[points],"laps":[laps],"timetaken_in_millisec":[timetaken_in_millisec],
                       "fastestLap":[fastestLap],"max_speed":[max_speed],"statusId":[statusId],
                       "year":[year],"wins":[wins],"age":[age],"nationalityN":[nationalityN]}))
    st.text("El resultado del modelo es: {}".format(resultado))

st.title("Inputs para modelo de puntos")

racerIdX= st.number_input("racerIdX")
driverIdX= st.number_input("driverIdX")
constructorIdX= st.number_input("constructorIdX")
gridX= st.number_input("gridX")
finishX= st.number_input("finishX")
lapsX= st.number_input("lapsX")
timetaken_in_millisecX= st.number_input("timetaken_in_millisecX")
fastestLapX= st.number_input("fastestLapX")
max_speedX= st.number_input("max_speedX")
statusIdX= st.number_input("statusIdX")
yearX= st.number_input("yearX")
winsX= st.number_input("winsX")
ageX= st.number_input("ageX")
nationalityNX= st.number_input("nationalityNX")

clicked1= st.button("PredecirX")
model1= load_modelP()
if clicked1:
    print("Resolviendo")
    resultado1= model1.predict(pd.DataFrame({"driverId":[driverIdX],"racerId":[racerIdX],
                       "constructorId":[constructorIdX],"grid":[gridX],"finish":[finishX],
                       "laps":[lapsX],"timetaken_in_millisec":[timetaken_in_millisecX],
                       "fastestLap":[fastestLapX],"max_speed":[max_speedX],"statusId":[statusIdX],
                       "year":[yearX],"wins":[winsX],"age":[ageX],"nationalityN":[nationalityNX]}))
    st.text("El resultado del modelo es: {}".format(resultado1))

