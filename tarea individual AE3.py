def calcular_descuento(num_productos, num_compras_previas, total_compra, es_promocion_especial):
    descuento = 0  # Inicializar el descuento a 0

    # Descuento por cantidad de productos
    if num_productos > 10:
        descuento += 10
    
    # Descuento por ser cliente frecuente
    if num_compras_previas > 5:
        descuento += 5

    # Descuento por monto de compra
    if total_compra > 500:
        descuento += 7
    
    # Descuento por promoción especial
    if es_promocion_especial:
        descuento += 15
    
    # Limitar el descuento a un máximo de 30%
    if descuento > 30:
        descuento = 30
    
    return descuento


def main():
    # Entradas del usuario
    num_productos = int(input("¿Cuántos productos compró? "))
    num_compras_previas = int(input("¿Cuántas compras previas ha realizado? "))
    total_compra = float(input("¿Cuál es el total de su compra en dólares? "))
    es_promocion_especial = input("¿Es un día de promoción especial? (sí/no) ").strip().lower() == 'sí'

    # Calcular el descuento
    descuento = calcular_descuento(num_productos, num_compras_previas, total_compra, es_promocion_especial)

    # Mostrar el descuento aplicado
    print(f"El descuento aplicado es: {descuento}%")

    # Calcular el total a pagar
    total_a_pagar = total_compra - (total_compra * descuento / 100)
    print(f"El total a pagar después del descuento es: ${total_a_pagar:.2f}")


if __name__ == "__main__":
    main()
