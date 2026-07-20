from os import system
from examen import *

juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
'IronGate'],
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}

while True:
    opc = leer_opcion()
    match opc:
        case 1:
            plataforma = input("ingrese plataformar a consultar: ")
            stock_plataforma(juegos, inventario, plataforma)
        case 2:
            while True:
                try:
                    p_min = int(input("ingrese precio minimo"))
                    p_max = int(input("ingrese precio maximo"))
                    break
                except:
                    print("debe ingresar valores enteros")
            busqueda_precio(juegos, inventario, p_min, p_max)
        case 3:
            while True:
                codigo = input("ingrese codigo del juego")
                try:
                    nuevo_precio = int(input("ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        if actualizar_precio(juegos, inventario, codigo, nuevo_precio):
                            print("precio actualizado")
                        else:
                            print("el codigo no existe")
                    else:
                        print("error, el precio debe ser mayor a cero")
                except:
                    print("debe ingresar un valor entero para el precio")
                resp = input("¿desea actualizar otro precio (s/n)?: ")
                if resp.lower() != "s":
                    break
        case 4:
            codigo = input("ingrese codigo del juego")
            if validar_codigo(juegos,codigo):
                titulo = input("ingrese titulo: ")
                if validar_titulo(titulo):
                    plataforma = input("ingrese plataforma: ")
                    if validar_plataforma(plataforma):
                        genero = input("ingrese genero")
                        if validar_genero(genero):
                            clasificacion = input("ingrese clasificacion")
                            if validar_clasificacion(clasificacion):
                                multiplayer = input("¿es multiplayer? (s/n)")
                                if validar_multiplayer(multiplayer):
                                    editor = input("ingrese editor")
                                    if validar_editor(editor):
                                        try:
                                            precio = int(input("ingrese precio: "))
                                            if validar_precio_registro(precio):
                                                stock = int(input("ingrese stock: "))
                                                if validar_stock_registro(stock):
                                                    if agregar_juego(juegos, inventario, codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
                                                        print("juego agregado")
                                                    else:
                                                        print("el juego ya existe")
                                        except:
                                            print("error, precio y stock deben ser numeros enteros")
        case 5:
            codigo = input("ingrese el codigo del juego que quiera eliminar")
            if eliminar_juegos(juegos, inventario,codigo):
                print("juego eliminado")
            else:
                print("el codigo no existe")
        case 6:
            print("programa finalizado")
            break      
