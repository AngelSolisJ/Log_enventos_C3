import logging
import datetime

# --- CONFIGURACIÓN DEL SISTEMA DE LOGS ---
# Esto crea el archivo 'seguridad_almacen.log' automáticamente
logging.basicConfig(
    filename='seguridad_almacen.log',
    level=logging.INFO,
    format='%(asctime)s | NIVEL: %(levelname)s | %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

# --- BASE DE DATOS SIMULADA ---
inventario = {
    "Laptop Gamer HP": 5,
    "Monitor Samsung 24": 12,
    "Teclado Mecánico": 8,
    "Mouse Logitech": 20
}

def mostrar_menu():
    print("\n" + "="*40)
    print(" SISTEMA DE GESTIÓN DE INVENTARIO v2.0")
    print("="*40)
    print("1. Ver Inventario Actual")
    print("2. DAR DE BAJA Producto (Requiere Firma)")
    print("3. Salir")

def ver_inventario():
    print("\n--- STOCK EN ALMACÉN ---")
    for producto, cantidad in inventario.items():
        print(f" > {producto}: {cantidad} unidades")
    # Registramos que alguien vio el stock (evento de bajo riesgo)
    logging.info("Consulta general de inventario realizada.")

def eliminar_producto():
    print("\n--- ¡ALERTA! ESTÁ EN ZONA DE EDICIÓN ---")
    # Simulamos el login pidiendo el nombre
    usuario_responsable = input("Ingrese su NOMBRE DE USUARIO para firmar la baja: ")
    prod_a_borrar = input("Nombre exacto del producto a eliminar: ")

    if prod_a_borrar in inventario:
        # Lógica de eliminación
        del inventario[prod_a_borrar]
        print(f"\n[ÉXITO] El producto '{prod_a_borrar}' ha sido eliminado de la BD.")
        
        # --- AQUÍ OCURRE LA MAGIA DEL LOG ---
        mensaje_log = f"USUARIO: {usuario_responsable} --> ELIMINÓ EL PRODUCTO: '{prod_a_borrar}'"
        logging.warning(mensaje_log) # Usamos WARNING porque es una acción delicada
    else:
        print("\n[ERROR] Producto no encontrado.")
        logging.error(f"Fallo de operación: {usuario_responsable} intentó borrar algo inexistente ({prod_a_borrar}).")

# --- EJECUCIÓN DEL PROGRAMA ---
logging.info("--- SISTEMA INICIADO ---")

while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        ver_inventario()
    elif opcion == '2':
        eliminar_producto()
    elif opcion == '3':
        print("Cerrando sistema...")
        logging.info("--- SISTEMA APAGADO ---")
        break
    else:
        print("Opción no válida.")