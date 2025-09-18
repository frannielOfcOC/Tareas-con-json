from flask import Flask, jsonify, request
from verificador import obtener_tareas_vencidas
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def notificar_vencidas():
    """
    Endpoint de la API para obtener una lista de tareas vencidas.
    """
    try:
        tareas_vencidas = obtener_tareas_vencidas()
        
        if tareas_vencidas:
            return jsonify({
                "status": "success",
                "message": "Se encontraron tareas vencidas.",
                "vencidas": tareas_vencidas
            }), 200
        else:
            return jsonify({
                "status": "success",
                "message": "No hay tareas vencidas para notificar."
            }), 200
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Ocurrio un error en el servidor: {e}"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)