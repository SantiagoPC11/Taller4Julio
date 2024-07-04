import random

def generarDatosProductos():
    Productos=["Musica","TV","Apliaciones","PC","Celulares","Tablets","Accesiorios"]
    datos=[]
    for producto in Productos:
        TipoProducto={}        
        categoria=random.choice(['Plus','Mega','Basic'])
        TipoProducto=[producto,categoria]
        datos.append(TipoProducto)

    return datos

print(generarDatosProductos())