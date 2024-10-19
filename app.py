from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
productos = []

# Ruta para crear un producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nuevo_producto = {
        "id": len(productos) + 1,
        "nombre": data['nombre'],
        "descripcion": data['descripcion'],
        "precio": data['precio']
    }
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

# Ruta para obtener la lista de productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos), 200

# Ruta para obtener un producto por ID
@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = next((prod for prod in productos if prod["id"] == id), None)
    if producto:
        return jsonify(producto), 200
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

# Ruta para actualizar un producto
@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = next((prod for prod in productos if prod["id"] == id), None)
    if producto:
        data = request.get_json()
        producto.update({
            "nombre": data.get('nombre', producto['nombre']),
            "descripcion": data.get('descripcion', producto['descripcion']),
            "precio": data.get('precio', producto['precio'])
        })
        return jsonify(producto), 200
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

# Ruta para eliminar un producto
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    global productos
    productos = [prod for prod in productos if prod["id"] != id]
    return jsonify({"mensaje": "Producto eliminado"}), 200

if __name__ == '__main__':
    app.run(debug=True)



