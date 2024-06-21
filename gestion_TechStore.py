from funciones_Tech import listar,agregarProducto,menu,limpiar,printR,printA,venderProducto,imprimirReporteCSV,cargarInventario

while True:
    limpiar()
    menu()
    opc = input("SELECCIONE : ")
    if opc == "0":
        break
    elif opc == "1":
        printA("AGREGAR PRODUCTOS")
        nombre = input("INGRESE NOMBRE DEL PRODUCTO : ").upper()
        precio = int(input("INGRESE PRECIO DEL PRODUCTO : "))
        cantid = int(input("INGRESE CANTIDAD EN STOCK : "))
        agregarProducto(nombre,precio,cantid)
    elif opc == "2":
        printA("LISTAR PRODUCTOS")
        listar()
    elif opc == "3":
        printA("VENDER PRODUCTOS")
        nombre = input("INGRESE NOMBRE DEL PRODUCTO : ").upper()
        cantidad = int(input("INGRESE CANTIDAD A COMPRAR : "))
        venderProducto(nombre,cantidad)
    elif opc == "4":
        printA("GUARDAR REGISTRO DE PRODUCTOS")
        reporte = input("INGRESE NOMBRE DEL REPORTE : ")
        imprimirReporteCSV(reporte)
    elif opc == "5":
        printA("CARGAR INVENTARIO")
        nombre=input("INGRESE EL NOMBRE DEL CSV : ").lower()
        cargarInventario(ruta=nombre)   
        
    else:
        printR("OPCION NO VALIDA")