# funciones_intermedias_1.py

# 1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambios solicitados:
matriz[1][0] = 6  # cambia 3 por 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"  # cambia "Cancún" por "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

# 2. Función para iterar una lista de diccionarios e imprimir sus llaves y valores
def iterarDiccionario(lista):
    for diccionario in lista:
        # BONUS: formato solicitado
        salida = []
        for llave, valor in diccionario.items():
            salida.append(f"{llave} - {valor}")
        print(", ".join(salida))

# 3. Función para imprimir valores de una llave en lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# 4. Función para imprimir información de diccionario con listas
def imprimirInformacion(diccionario):
    for llave, lista_valores in diccionario.items():
        print(f"{len(lista_valores)} {llave.upper()}")
        for valor in lista_valores:
            print(valor)
        print()  # línea en blanco para separar secciones


# --- Ejemplos de uso ---

if __name__ == "__main__":
    print("Matriz actualizada:")
    print(matriz)
    print("\nCantantes actualizados:")
    print(cantantes)
    print("\nCiudades actualizadas:")
    print(ciudades)
    print("\nCoordenadas actualizadas:")
    print(coordenadas)

    # Prueba iterarDiccionario con cantantes extendidos
    cantantes.extend([
        {"nombre": "José José", "pais": "México"},
        {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
    ])
    print("\nIterar Diccionario:")
    iterarDiccionario(cantantes)

    print("\nIterar Diccionario 2 - Nombres:")
    iterarDiccionario2("nombre", cantantes)

    print("\nIterar Diccionario 2 - Países:")
    iterarDiccionario2("pais", cantantes)

    costa_rica = {
       "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
       "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }
    print("\nImprimir Información:")
    imprimirInformacion(costa_rica)
