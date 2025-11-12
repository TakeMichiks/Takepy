from flask import Blueprint
from flask_marshmallow import Marshmallow

ma = Marshmallow()

datos_db = Blueprint("views_api", __name__)
datetime_db = Blueprint('datetime_api', __name__)

from .datos import routes
from .helpers import datetime
