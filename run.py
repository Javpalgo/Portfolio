#importar
from flask import Flask

#Crear app mediante instancia
app = Flask(__name__)

#Crear rutas con sus correspondientes funciones
@app.route('/')
def holamundo ():
    return 'Hola Mundo!'

@app.route('/mis-proyectos')
def mostrarproyectos ():
    return 'Aqui se mostraran mis proyectos'    

#Ejecutar nuestra app cuando ejecutemos este archivo run.py

if __name__=='__main__':
    app.run(debug=True)