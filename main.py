from flask import Flask
from funciones import crear_tarea
#aqui vamos a importar los modulos de funciones.py para organizar mejor el codigo, y usaremos el framework de flask para crear una pagina.

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Bienvenido a la página de inicio!'

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'¡Hola, {nombre}!'

if __name__ == '__main__':
    app.run(debug=True)