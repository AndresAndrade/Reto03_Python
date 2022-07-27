# ventas = [
#     (5489, 'tornillo', 'RS8512', 2, 33, 'Julio Perez', 3654213, '13/06/2020'),
#     (3215, 'zocalo', 'UM8587', 2, 125, 'Laura Macias', 1256321, '13/06/2020'),
#     (3698, 'biela', 'PT3218', 1, 78, 'Luis Peña', 14565487, '13/06/2020'),
#     (8795, 'cilindro', 'AZ8794', 2, 96, 'Carlos Casio', 5612405, '13/06/2020')]


# ---------------------------------------------------------------------------------
def AutoPartes(ventas):
    dctKeys = ["idProducto", "dProducto", "pnProducto", "cvProducto", "sProducto", "nComprador", "cComprador", "fVenta"]
    lstVentas = []
    for i in ventas:
        dctVentas = dict(zip(dctKeys, i))
        lstVentas.append(dctVentas)
    # print(lstVentas)
    return lstVentas


def consultaRegistro(AutoPartes, idProducto):
    respuesta = ""
    for i in AutoPartes:
        if idProducto == i["idProducto"]:
            respuesta += f"Producto consultado : {i['idProducto']}  Descripción  {i['dProducto']}  #Parte  {i['pnProducto']}  " \
                         f"Cantidad vendida  {i['cvProducto']}  Stock  {i['sProducto']}  Comprador {i['nComprador']}  " \
                         f"Documento  {i['cComprador']}  Fecha Venta  {i['fVenta']}\n"

    if respuesta == "":
        respuesta = "No hay registro de venta de ese producto"
    print(respuesta)


# -------------------------------------------------------------------------------

consultaRegistro(AutoPartes([
    (9852, 'Culata', 'XC9875', 2, 165, 'Luis Molero', 3455846, '14/06/2020'),
    (9852, 'Culata', 'XC9875', 2, 165, 'Jose Mejia', 1355846, '14/06/2020'),
    (2564, 'Cárter', 'PT29872', 2, 32, 'Peter Cerezo', 8545436, '14/06/2020'),
    (5412, 'válvula', 'AZ8798', 2, 11, 'Juan Peña', 568975, '14/06/2020')]), 9852)
print()