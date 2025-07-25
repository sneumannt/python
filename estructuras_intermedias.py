# estructuras_intermedias.py

# ========================================
# PARTE 1: Actualizar valores
# ========================================

# 1.1 Modificar valor en matriz
matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6  # Cambiar 3 por 6

# 1.2 Cambiar nombre del primer cantante
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"

# 1.3 Reemplazar "Cancún" por "Monterrey"
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"

# 1.4 Cambiar latitud en coordenadas
coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]
coordenadas[0]["latitud"] = 9.9355431

# Mostrar resultados de la parte 1
print("=== Parte 1: Actualización de estructuras ===")
print("Matriz:", matriz)
print("Cantantes:", cantantes)
print("Ciudades:", ciudades)
print("Coordenadas:", coordenadas)
print("-" * 50)

# ========================================
# PARTE 2: Recorrer lista de diccionarios
# ========================================

print("=== Parte 2: Recorrido de cantantes ===")
for cantante in cantantes:
    print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")
print("-" * 50)

# ========================================
# PARTE 3: Obtener valores específicos
# ========================================

print("=== Parte 3: Claves 'nombre' y 'pais' ===")

print("Nombres de cantantes:")
for cantante in cantantes:
    print(cantante["nombre"])

print("\nPaíses de cantantes:")
for cantante in cantantes:
    print(cantante["pais"])

print("-" * 50)

# ========================================
# PARTE 4: Recorrer diccionario con listas
# ========================================

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("=== Parte 4: Recorrer diccionario de listas ===")
for clave, lista in costa_rica.items():
    print(f"{len(lista)} - {clave.upper()}")
    for item in lista:
        print(item)
    print()  # Separación entre secciones
