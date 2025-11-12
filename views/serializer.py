from marshmallow import fields
from . import ma

class LibroSchema(ma.Schema):
    id = fields.Int(dump_only=True)  # dump_only = Solo para serialización (salida)
    titulo = fields.Str(required=True)
    autor = fields.Str(required=True)

    class Meta:
        # Campos a incluir en la serialización
        fields = ("id", "titulo", "autor")

# --- Instancias del Schema para uso en las rutas ---
# Se exportan para poder importarlas directamente en los archivos de rutas.
libro_schema = LibroSchema()
libros_schema = LibroSchema(many=True)
