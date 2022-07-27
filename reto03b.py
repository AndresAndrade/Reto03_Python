ventas = [
    (5489, 'tornillo', 'RS8512', 2, 33, 'Julio Perez', 3654213, '13/06/2020'),
    (3215, 'zocalo', 'UM8587', 2, 125, 'Laura Macias', 1256321, '13/06/2020'),
    (3698, 'biela', 'PT3218', 1, 78, 'Luis Peña', 14565487, '13/06/2020'),
    (8795, 'cilindro', 'AZ8794', 2, 96, 'Carlos Casio', 5612405, '13/06/2020')]


# ---------------------------------------------------------------------------------
def AutoPartes(ventas: list):
    dctKeys = ["idProducto", "dProducto", "pnProducto", "cvProducto", "sProducto", "nComprador", "cComprador", "fVenta"]
    lstVentas = []
    for i in ventas:
        dctVentas = dict(zip(dctKeys, i))
        lstVentas += (dctVentas,)
    return lstVentas


def consultaRegistro(ventas, idProducto):
    ventas = AutoPartes(ventas)
    respuesta = ""
    for i in ventas:
        if idProducto == i["idProducto"]:
            respuesta += f"Producto consultado : {i['idProducto']} Descripción {i['dProducto']} #Parte {i['pnProducto']} " \
                         f"Cantidad vendida {i['cvProducto']} Stock {i['sProducto']} Comprador {i['nComprador']} " \
                         f"Documento {i['cComprador']} Fecha Venta {i['fVenta']}\n"

    if respuesta == "":
        respuesta = "No hay registro de venta de ese producto"
    print(respuesta)


# --------------------------------------------------------------------------------
print(consultaRegistro([
    (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
    (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
    (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
    (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')], 2001))
# print(AutoPartes(ventas))
