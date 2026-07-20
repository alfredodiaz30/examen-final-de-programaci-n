from os import system
system("cls")

def leer_opcion():
    try:
        while True:
            print("menu principal")
            print("1.- stock por plataforma")
            print("2.- busqueda de juegos por rango de precio")
            print("3.- actualizar precio de juego")
            print("4.- agregar juego")
            print("5.- eliminar juego")
            print("6.- salir")
            opc = int(input("ingrese opcion: "))
            if 1 <= opc <= 6:
                return opc
            print("debe seleccionar una opcion valida")
    except:
        print("debe seleccionar una opcion valida")
def stock_plataforma(juegos, inventario, plataforma):
    total_stock = 0
    for codigo in juegos:
        datos_juego = juegos[codigo]
        if datos_juego[1].lower() == plataforma.lower():
            total_stock = total_stock + inventario[codigo][1]
        print(f"el total de stock disponible es: {total_stock}")
def busqueda_precio(juegos, inventario, p_min, p_max):
    lista_encontrados = []
    for codigo in inventario:
        precio_juego = inventario[codigo][0]
        stock_juego = inventario[codigo][1]
        if p_min <= precio_juego <= p_max and stock_juego > 0:
            titulo_juego = juegos[codigo][0]
            formato = f"{titulo_juego}--{codigo}"
            lista_encontrados.append(formato)
    if len(lista_encontrados) == 0:
        print("no hay juegos en ese rango de precios")
    else:
        lista_encontrados()
        print(f"los juegos encontrados son: {lista_encontrados}")
def buscar_codigo(juegos, codigo):
    for cod in juegos:
        if cod.lower() == codigo.lower():
            return True
    return False
def actualizar_precio(juegos, inventario, codigo, nuevo_precio):
    if buscar_codigo(juegos, codigo):
        for cod_real in inventario:
            if cod_real.lower() == codigo.lower():
                inventario[cod_real][0] = nuevo_precio
                return True
    return False
def validar_codigo(juegos, codigo):
    if codigo == "":
        print("error, el codigo no puede estar vacio")
        return False
    if buscar_codigo(juegos, codigo):
        print("error, el codigo ya existe en los diccionarios")
        return False
    return True
def validar_titulo(titulo):
    if titulo == "":
        print("error, el titulo no puede estar vacio")
        return False
    return True
def validar_plataforma(plataforma):
    if plataforma == "":
        print("error, la plataforma no puede estar vacia")
        return False
    return True
def validar_genero(genero):
    if genero == "":
        print("error, el genero no puede estar vacio")
        return False
    return True
def validar_clasificacion(clasificacion):
    if clasificacion == "E" or clasificacion == "T" or clasificacion == "M":
        return True
    print("error, la clasificacion debe ser exactamente 'E', 'T', 'M'")
    return False
def validar_multiplayer(multiplayer):
    if multiplayer.lower() == "s" or multiplayer.lower == "n":
        return True
    print("error, debe ingresar 's' o 'n'")
    return False
def validar_editor(editor):
    if editor == "":
        print("error, el editor no puede estar vacio")
        return False
    return True
def validar_precio_registro(precio):
    if precio >= 0:
        return True
    print("error, el precio debe ser un numero entero mayor a cero")
    return False
def validar_stock_registro(stock):
    if stock >= 0:
        return True
    print("error, el stock debe ser un numero entero mayor o igual a cero")
    return False
def agregar_juego(juegos, inventario, codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    if buscar_codigo(juegos, codigo):
        return False
    if multiplayer.lower() == "s":
        es_multi = True
    else:
        es_multi = False
    
    juegos[codigo] = [
        titulo,
        plataforma,
        genero,
        clasificacion,
        es_multi,
        editor
    ]
    inventario[codigo] = [
        precio,
        stock
    ]
    return True
def eliminar_juegos(juegos, inventario, codigo):
    if buscar_codigo(juegos, codigo):
        clave_eliminar = ""
        for cod_real in juegos:
            if cod_real.lower() == codigo.lower():
                clave_eliminar = cod_real
        del juegos[clave_eliminar]
        del inventario[clave_eliminar]
        return True
    return False