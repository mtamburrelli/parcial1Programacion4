import sqlite3

DB = "inventario.db"


# Todas las funciones necesarias

def addProducto(producto, descripcion):
    con = obtener_conexion()
    cursor = con.cursor()
    sentencia = "INSERT INTO inventario(producto, descripcion) VALUES (?, ?)"
    cursor.execute(sentencia, [producto, descripcion])
    con.commit()


def update(producto, nueva_descripcion):
    con = obtener_conexion()
    cursor = con.cursor()
    sentencia = "UPDATE inventario SET descripción = ? WHERE producto = ?"
    cursor.execute(sentencia, [nueva_descripcion, producto])
    con.commit()


def delProd(producto):
    con = obtener_conexion()
    cursor = con.cursor()
    sentencia = "DELETE FROM inventario WHERE producto = ?"
    cursor.execute(sentencia, [producto])
    con.commit()


def getProductos():
    con = obtener_conexion()
    cursor = con.cursor()
    consulta = "SELECT producto FROM inventario"
    cursor.execute(consulta)
    return cursor.fetchall()


def descProd(producto):
    con = obtener_conexion()
    cursor = con.cursor()
    consulta = "SELECT descripcion FROM inventario WHERE producto = ?"
    cursor.execute(consulta, [producto])
    return cursor.fetchone()


def obtener_conexion():
    return sqlite3.connect(DB)


def crearInventario():
    tablas = [
        """
        CREATE TABLE IF NOT EXISTS inventario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            descripcion TEXT NOT NULL
        );
        """
    ]
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    for tabla in tablas:
        cursor.execute(tabla)


# Menu principal
def inventario():
    crearInventario()
    menu = """
\n--------¡Bienvenido al inventario del Restaurante UIP!--------\n
1) Agregar al inventario
2) Editar producto 
3) Eliminar producto del inventario
4) Ver lista de productos
5) Ver la descripción de un producto
6) Salir
\nSeleccione una opción: """
    opt = ""
    while opt != "6":
        opt = input(menu)
        if opt == "1":
            producto = input("\nIngrese el producto: ")
            posible_descripcion = descProd(producto)
            if posible_descripcion:
                print(f"El producto'{producto}' ya existe")
            else:
                descripcion = input("Ingresa la descripcion: ")
                addProducto(producto, descripcion)
                print("¡Producto agregado exitosamente!")
        if opt == "2":
            producto = input("\nIngresa el producto que desea editar: ")
            nueva_descripcion = input("Ingresa la descripcion: ")
            productos = getProductos()
            if producto in productos:
                update(producto, nueva_descripcion)
                print("¡Producto actualizado exitosamente!")
            else:
                print(f"El producto '{producto}' no fue encontrado")
        if opt == "3":
            producto = input("\n¿Qué producto desea eliminar?: ")
            delProd(producto)
        if opt == "4":
            productos = getProductos()
            print("\n--------Inventario del Restaurante UIP--------\n")
            for producto in productos:
                print(producto[0])
        if opt == "5":
            producto = input(
                "\n¿De cuál producto quieres saber la descripción?: ")
            descripcion = descProd(producto)
            if descripcion:
                print(f"La descripción de '{producto}' es:\n{descripcion[0]}")
            else:
                print(f"La descripción del producto '{producto}' no fue encontrada")
        if opt == "6":
            print("¡Hasta luego!")
            exit()


# Inicialización
if __name__ == '__main__':
    inventario()
