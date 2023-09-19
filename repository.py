# repository.py
import csv

ARCHIVO_DATOS = 'sample_grocery.csv'

def cargar_datos():
    with open(ARCHIVO_DATOS, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def guardar_datos(data):
    with open(ARCHIVO_DATOS, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def agregar_articulo(articulo):
    data = cargar_datos()
    data.append(articulo)
    guardar_datos(data)

def eliminar_articulo_por_sku(sku):
    data = cargar_datos()
    data_filtrado = [articulo for articulo in data if articulo['SKU'] != sku]
    guardar_datos(data_filtrado)
