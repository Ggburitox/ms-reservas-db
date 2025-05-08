from pymongo import MongoClient
from datetime import datetime

# Configuración de conexión
client = MongoClient("mongodb://localhost:27017/")
db = client["cinedb"]
reservas = db["reservas"]

# Crear un índice de ejemplo (opcional)
reservas.create_index("cliente")

# Insertar un documento de prueba
reserva = {
    "cliente": "Juan Pérez",
    "fecha": datetime.now(),
    "pelicula_nombre": "Inception",
    "peliculaId": 1,
    "usuarioId": 42
}

if reservas.count_documents({}) == 0:
    reservas.insert_one(reserva)
    print("✅ Colección 'reservas' inicializada.")
else:
    print("ℹ️ La colección 'reservas' ya esta creada.")

client.close()
