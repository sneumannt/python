# bucle_for_basico1.py

# 1. Básico: imprime todos los números enteros del 0 al 100.
print("1. Números del 0 al 100:")
for i in range(0, 101):
    print(i)

# 2. Múltiplos de 2 entre 2 y 500
print("\n2. Múltiplos de 2 entre 2 y 500:")
for i in range(2, 501, 2):
    print(i)

# 3. Contando Vanilla Ice
print("\n3. Contando Vanilla Ice:")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# 4. Wow. Número gigante a la vista
print("\n4. Suma de los números pares del 0 al 500000:")
suma_total = 0
for i in range(0, 500001, 2):
    suma_total += i
print("Suma total:", suma_total)

# 5. Regrésame al 3
print("\n5. Cuenta regresiva desde 2024 en pasos de 3:")
for i in range(2024, 0, -3):
    print(i)

# 6. Contador dinámico
print("\n6. Contador dinámico:")
num_inicial = int(input("Ingresa el número inicial: "))
num_final = int(input("Ingresa el número final: "))
multiplo = int(input("Ingresa el múltiplo: "))

print(f"Números entre {num_inicial} y {num_final} que son múltiplos de {multiplo}:")
for i in range(num_inicial, num_final + 1):
    if i % multiplo == 0:
        print(i)

