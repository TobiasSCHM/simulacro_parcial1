
inventario = [
    
    ]

lista_caro = []
lista_barato = []

constinuar = True


def agregar_producto():
    """
    Función para agregar nombre, cantidad y precio del producto nuevo en forma de lista a la lista inventario 
    """
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    precio = int(input("Ingrese el precio del producto: "))

    cantidad = int(input("Ingrese la cantidad disponible del producto: "))
    
    inventario.append([nombre, precio, cantidad])
    
def buscar_producto(producto: str):
    """
    escanea la lista buscando el valor str que se le impuso y la compara con cada i[0]
    """
    for i in inventario:
        if i[0] == producto:
            print(f"NOMBRE DEL PRODUCTO: {i[0]}, PRECIO: {i[1]}, CANTIDAD: {i[2]}")

def producto_milqui():
    """
    te genera una lista con los productos con i[1] mayor a 1500 pero como que no funciona
    """
    producto_milqui = []
    for i in inventario:
        if i[1] > 1500:
            producto_milqui += i
    print(producto_milqui)
            

def mas_caro_producto(inventario: list):
    """
    te muestra el producto con el i[1] mas grande
    """
    contador_caro = 0
    for i in inventario:
        if i[1] > contador_caro:
            contador_caro = i[1]
            lista_caro = i

    print(f"NOMBRE DEL PRODUCTO MAS CARO: {lista_caro[0]}, PRECIO: {lista_caro[1]}, CANTIDAD: {lista_caro[2]}")
            
def mas_barato_producto(inventario: list):
    """
    te muestra el producto con el i[1] mas grande
    """
    contador_barato = float("inf")
    for i in inventario:
        if i[1] < contador_barato:
            contador_barato = i[1]
            lista_barato = i
    print(f"NOMBRE DEL PRODUCTO MAS BARATO: {lista_barato[0]}, PRECIO: {lista_barato[1]}, CANTIDAD: {lista_barato[2]}")
    
def ord_burbuja(arreglo):
    """
    bubble sort visto en clase
    """
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j][1] > arreglo[j+1][1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]



  
def menu() -> str:
    """
    printea el menu, pregunta la seleccion y valida que no sea otro valor que no sea requerido.
    """
    print("que desea?: \n agregar un producto[1] \n mostrar la lista de productos[2] \n ordenar el inventario[3] \n mostrar productos mas caros y mas barato[4] \n mostrar productos mayores a 1500[5] \n salir[6] ")
    
    seleccion = input("ingrese su seleccion:")
    
    while seleccion !="1" and seleccion != "2" and seleccion != "3" and seleccion != "4" and seleccion != "5" and seleccion != "6":
        seleccion = int(input("Error. Ingrese el numero de su elección: ")) 
    return seleccion


    

while constinuar == True:
    seleccion = menu()
    match seleccion:
        case ("1"):
            agregar_producto()
            
        case("2"):
            for i in inventario:
                print(f"NOMBRE DEL PRODUCTO: {i[0]}, PRECIO: {i[1]}, CANTIDAD: {i[2]}")
            
        case("3"):
            ord_burbuja(inventario)
            
        case("4"):
            mas_caro_producto(inventario)
            mas_barato_producto(inventario)
            
        case("5"):
            producto_milqui()
            
        case("6"):
            print("Hasta luego!")
            constinuar = False