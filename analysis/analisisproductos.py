from generators.generadorApple import generarDatosProductos
import pandas as pd

def analizarDatos():
    datos=generarDatosProductos()
    tabla=pd.DataFrame(datos,columns=['Tipo Producto','categoria'])
    tabla.to_csv("./data/ProductosApple.csv",index=False)
analizarDatos()