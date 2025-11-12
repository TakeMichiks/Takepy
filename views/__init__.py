from flask import Blueprint
from flask_marshmallow import Marshmallow

ma = Marshmallow()

datos_db = Blueprint("views_api", __name__)
datetime_db = Blueprint('datetime_api', __name__)

#import de las rutas
from .datos import data
from .helpers import datetime
