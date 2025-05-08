from pymongo import MongoClient
from datetime import datetime

# Conexión al servidor de MongoDB (local o en contenedor)
client = MongoClient("mongodb://localhost:27017/")

# Accede o crea la base de datos
db = client["cinedb"]

# Accede o crea la colección
reservas = db["reservas"]

# Crear un índice en el campo "cliente" (opcional)
reservas.create_index("cliente")

# Documento de prueba para insertar si la colección está vacía
reserva = {
    "cliente": "Juan Pérez",
    "fecha": datetime.now(),
    "pelicula_nombre": "Inception",
    "peliculaId": 1,
    "usuarioId": 42
}

# Verifica si la colección está vacía
if reservas.count_documents({}) == 0:
    reservas.insert_one(reserva)
    print("Colección 'reservas' inicializada con un documento de ejemplo.")
else:
    print("ℹ️ La colección 'reservas' ya tiene documentos. No se insertó ninguno nuevo.")

# Cierra la conexión
client.close()
