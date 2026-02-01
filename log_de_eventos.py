import logging


logging.basicConfig(
    filename='seguridad_almacen.log', 
    level=logging.INFO, 
    format='%(asctime)s | %(levelname)s | %(message)s', 
    datefmt='%d-%m-%Y %H:%M:%S'
)

usuarios_validos = {
    "Angel Solis": "1234",
    "Sergio Plata": "0000",   
    "Gael Torres": "9999"
}

inventario = {
    "Laptop HP Gamer": 10,
    "iPhone 15 Pro": 15,
    "AirPods Pro": 25,
    "Cargador USB-C": 50
}

usuario_actual = None


def login():
    global usuario_actual
    print("\n" + "="*45)
    print("SISTEMA DE CONTROL DE INVENTARIOS")
    print("="*45)
    
    user = input("Usuario: ")
    password = input("Contraseña: ")
    
    if user in usuarios_validos and usuarios_validos[user] == password:
        usuario_actual = user
        print(f"\nBienvenido {usuario_actual}. Sesión iniciada.")
        logging.info(f"ACCESO: El usuario '{usuario_actual}' ingresó al sistema.")
        return True
    else:
        print("\nCredenciales inválidas.")
        logging.warning(f"INTRUSIÓN: Intento fallido de acceso con usuario '{user}'.")
        return False

def ver_inventario():
    print("\n--- ESTADO DEL ALMACÉN ---")
    print(f"{'PRODUCTO':<20} | {'CANTIDAD':<10}")
    print("-" * 35)
    for prod, cant in inventario.items():
        print(f"{prod:<20} | {cant:<10}")
    
    logging.info(f"CONSULTA: {usuario_actual} revisó el inventario.")

def ajustar_stock():
    print(f"\n--- MÓDULO DE SALIDA DE MERCANCÍA ---")
    print(f"Usuario responsable: {usuario_actual}")
    
    prod = input("Nombre del producto a retirar: ")
    
    if prod in inventario:
        try:
            cantidad_actual = inventario[prod]
            print(f"Stock actual de '{prod}': {cantidad_actual} unidades.")
            
            cantidad_retirar = int(input("¿Cuántas unidades vas a retirar?: "))
            
            if 0 < cantidad_retirar <= cantidad_actual:
                inventario[prod] -= cantidad_retirar
                print(f"Se han retirado {cantidad_retirar} unidades. Quedan {inventario[prod]}.")
                
                logging.warning(f"MOVIMIENTO DE STOCK: {usuario_actual} RESTÓ {cantidad_retirar} unidades de '{prod}'. (Stock restante: {inventario[prod]})")
            
            elif cantidad_retirar > cantidad_actual:
                print("Error: No hay suficiente stock para retirar esa cantidad.")
                logging.error(f"ERROR: {usuario_actual} intentó retirar más {prod} del existente.")
            else:
                print("Cantidad no válida.")
                
        except ValueError:
            print("Error: Debes ingresar un número entero.")
    else:
        print("El producto no existe.")

if login():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver Inventario")
        print("2. Registrar Salida de Mercancía (Baja)")
        print("3. Salir")
        
        opcion = input("Elige: ")
        
        if opcion == '1':
            ver_inventario()
        elif opcion == '2':
            ajustar_stock()
        elif opcion == '3':
            print("Saliendo...")
            logging.info(f"SALIDA: {usuario_actual} cerró sesión.")
            break