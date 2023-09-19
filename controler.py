# controller.py
from flask import Flask, request, jsonify
import repository

app = Flask(__name__)

@app.route('/item', methods=['GET'])
def obtener_articulos():
    datos = repository.cargar_datos()
    return jsonify(datos)

@app.route('/item', methods=['POST'])
def agregar_articulo():
    articulo = request.json
    repository.agregar_articulo(articulo)
    return jsonify({"mensaje": "Artículo agregado exitosamente!"}), 201

@app.route('/item/<string:sku>', methods=['DELETE'])
def eliminar_articulo(sku):
    repository.eliminar_articulo_por_sku(sku)
    return jsonify({"mensaje": f"Artículo con SKU {sku} eliminado exitosamente!"})

if __name__ == '__main__':
    app.run(debug=True)
