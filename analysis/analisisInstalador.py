from generators.generadorinstalador import generarDatosInstaladores
import pandas as pd

def analizarDatos():
    datos=generarDatosInstaladores()
    tabla=pd.DataFrame(datos,columns=['responsable','edad','zona','experiencia','instalaciones'])
    tabla.to_csv("./data/InstaladoresAburraSur.csv",index=False)
analizarDatos()