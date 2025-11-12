# importaciones principales
from flask import Flask
from flask_cors import CORS
# importacion de rutas
from views import datos_db,datetime_db

# Inicio de la aplicacion
app = Flask(__name__)
CORS(app)

# Seccion de Conexiones
app.register_blueprint(datos_db, url_prefix='/data')
app.register_blueprint(datetime_db, url_prefix='/api')

# App run host
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
