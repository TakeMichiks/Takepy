from marshmallow import fields
from . import ma

class LibroSchema(ma.Schema):
    id = fields.Int(dump_only=True)  # dump_only = Solo para serialización (salida)
    titulo = fields.Str(required=True)
    autor = fields.Str(required=True)

    class Meta:
        # Campos a incluir en la serialización
        fields = ("id", "titulo", "autor")


class DataTeachersSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Str(required=True)
    phone = fields.Int(required=True)
    direction = fields.Str(required=True)
    yearasigned = fields.Str(required=True)
    titledoc = fields.Str(required=True)
    disability = fields.Str(allow_none=True)

    class Meta:
        fields = ("id","name","age","phone","direction","yearasigned","titledoc","disability")

# --- Instancias del Schema para uso en las rutas ---
# Se exportan para poder importarlas directamente en los archivos de rutas.
libro_schema = LibroSchema()
libros_schema = LibroSchema(many=True)
dataTeachers_schema = DataTeachersSchema(many=True)
