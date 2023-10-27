import pandas as pd
from funcionsumar import sumarArboles

#Analizar una lista de datos
ciudades=["Medallo","Bogota","Cali","Barranquilla"]

#Analizar una lista de diccionarios
estudiantes=[
    {"id":1,"nombre":"el juli liverpool","promedio":2.8},
    {"id":2,"nombre":"Maria soy del DIM","promedio":2.5},
    {"id":3,"nombre":"Pipe","promedio":2.94},
    {"id":4,"nombre":"Andy","promedio":2.7},
    {"id":5,"nombre":"cata descansos","promedio":2.76}
]

arbolesporMunicipio=[
    {"municipio":"Carolina del principe", "tipo":"guayacanes","cantidad":1500}
]

#conviertiendo listas y listas de diccionarios en DATAFRAMES
dataframe1=pd.DataFrame(ciudades)
dataframe2=pd.DataFrame(estudiantes)

print(dataframe1)
print(dataframe2)

numeroArbolesOriente=1200000
numeroArbolesSuroeste=3000000
numeroArbolesNorte=4000000

sumatoriaorientenorte=sumarArboles(numeroArbolesNorte,numeroArbolesOriente)
sumatoriasuroesteoriente=sumarArboles(numeroArbolesSuroeste,numeroArbolesOriente)

#Analizar un CSV