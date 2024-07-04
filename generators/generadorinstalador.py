import random

def generarDatosInstaladores():
    instaladores=["Jhon Doe","Pedro Perez","Ana Rubio","Carlos Zapata","Martha Builes"]
    datos=[]
    for instalador in instaladores:
        responsable={}        
        edad=random.randint(25,50)
        zona=random.choice(['Zona A','Zona B','Zona C'])
        experiencia=random.randint(1,20)
        instalaciones=random.randint(20,50)
        responsable=[instalador,edad,zona,experiencia,instalaciones]
        datos.append(responsable)

    return datos

print(generarDatosInstaladores())

