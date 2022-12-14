def AutoPartes(ventas: list) -> dict:
    diccionario = {}
    for i in ventas:
        if diccionario.get(i[0]) == None:
            diccionario[i[0]] = []
        diccionario[i[0]].append((i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
    return diccionario



def consultaRegistro(ventas, idProducto) -> str:
    if idProducto in ventas:
        for i in ventas[idProducto]:
            print(f"Producto consultado : {idProducto} Descripcion {i[0]}")
    else:
        print('No hay registro de venta de ese producto')


ventas = [
    (2001, 'rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020'),
    (2010, 'bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2010'),
    (2010, 'bujía', 'ER6523', 9, 36, 'Pedro Montes', 1243, '12/06/2020'),
    (3578, 'tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020'),
    (9251, 'piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020')
]

consultaRegistro(AutoPartes(ventas), 9251)

# print(AutoPartes(ventas))
