import os, msvcrt, csv

#lista
registro = []
#tupla
productos = ("LAPTOP","SMARTPHONE","TABLET","SMARTWATCH","HEADPHONES","SPEAKER")
#csv

def limpiar():#Espera una tecla y limpia la pantalla
    print("|PRESS ANY KEY|")
    msvcrt.getch()
    os.system("cls")

def printR(texto):#COLOR ROJO
    print(f"\033[31m{texto}\033[0m")
def printV(texto):#COLOR VERDE
    print(f"\033[32m{texto}\033[0m")
def printA(texto):#COLOR AMARILLO
    print(f"\033[34m{texto}\033[0m")
def printM(texto):#COLOR MAGENTA
    print(f"\033[35m{texto}\033[0m")
def menu():#Genera el menú del sistema
    printA("Sistema Gestión de TechStore [💻]")
    printA("════════════════════════════════")
    print("1) AGREGAR PRODUCTOS")
    print("2) LISTAR PRODUCTOS")
    print("3) VENDER PRODUCTO")
    print("4) GUARDAR REGISTRO EN CSV")
    print("5) CARGAR INVENTARIO")
    print("0) SALIR.")
    printA("════════════════════════════════")
def validarNombre(nombre):#Valida el nombre como variable
    for i in range(len(registro)):
        if registro[i][0]==nombre:
            return 1 #Retorno la posición si encontramos la patente
    return -1 #Retorno negativo si no lo encuentro
def validarCantidad(cantidad):#Valida la cantidad como variable
    for i in range(len(registro)):
        if registro[i][2]<=cantidad and cantidad<0:
            return i 
    return -1 
def seleccionProducto():
    print("PRODUCTOS DISPONIBLES")
    for i in range(len(productos)):
        printA(f"{i+1}.- {productos[i]}")
    seleccion = int(input("Seleccione : "))-1
    if seleccion>=0 and seleccion<len(productos):
        return productos[seleccion]
    else:
        return None #Valor invalido
def listar():
    if len(registro)>0:
        for i in range(len(registro)):
            printM(f"{i+1}.- NOMBRE: {registro[i][0]}| PRECIO: ${registro[i][1]}| CANTIDAD: {registro[i][2]}")
    else:
        printR("No hay vehículos registrados")
def agregarProducto(nombre,precio,cantidad):
    if validarNombre(nombre)==-1:
        if precio>0:
            if cantidad>=0:
                registro.append([nombre,precio,cantidad])
                printV("PRODUCTO REGISTRADO CORRECTAMENTE")
            else:
                printR("CANTIDAD NO VALIDA")
        else:
            printR("PRECIO NO VALIDO")
    else:
        printR("PRODUCTO YA AGREGADO")
def venderProducto(nombre,cantidad):
    if len(registro)>0:
        centinels = False
        for i in range(len(registro)):
            if nombre==registro[i][0]:
                if cantidad<=registro[i][2]:
                    total=0
                    precio = registro[i][1]
                    total=cantidad*precio
                    printV(F"COMPRA REALIZADA WITH EXITO {cantidad} VALOR: ${total}")
                    registro[i][2]-=cantidad
                else:
                    printR("CANTIDAD INSUFICIENTE [X]")
                centinels =True
        if not centinels:
            printR("PRODUCTO NO REGISTRADO")
    else:
        printR("NO HAY PRODUCTOS REGISTRADOS")
def imprimirReporteCSV(nombreReporte):
    if len(registro)>0:
        with open(f'{nombreReporte}.csv','w',newline='',encoding='utf-8') as a:
            escribir = csv.writer(a,delimiter=",")
            registro.insert(0,["NOMBRE","PRECIO","CANTIDAD"])
            escribir.writerows(registro)
            registro.pop(0)
            printV(F"REPORTE {nombreReporte}.csv GENERADO EXITOSAMENTE ")
    else:
        printR("NO HAY PRODUCTOS [X]")
def cargarInventario(ruta):
    with open(f'{ruta}.csv','r',newline='',encoding='utf-8') as f:
        leer = csv.reader(f,delimiter=",".upper())
        for i in leer:
            registro.append(i)
            printV(','.join(i))
            