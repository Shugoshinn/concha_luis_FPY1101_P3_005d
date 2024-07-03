import os, time, csv, msvcrt

pedidos = ["RUT","Cliente","Direccion","Comuna","Cil.5kg","Cil.15kg","Total"]
def registrar_ped():
    while True:
        rut = int(input("Ingrese su rut(sin puntos ni guion y con dígito verificador): "))
        pedidos.append(rut)
        nombre = input("Ingrese su nombre: ")
        pedidos.append(nombre)
        direccion = input("Ingrese su dirección: ")
        pedidos.append(direccion)
        comuna = input("Ingrese su comuna(Santiago, Pirque, Colina): ")
        pedidos.append(comuna)
        cilindros = int(input("Ingrese que cilindro quiere llevar: "))
        while True:
            if cilindros >=5 and cilindros <=15:
                print("Cilindro agregado con éxito")
                pedidos.append(cilindros)
                time.sleep(1.5)
            else:
                print("ERROR! PEDIDO NO REGISTRADO, INGRESE EL CILINDOR DE 5 O DE 15")
            
            total = cilindros + cilindros
            print("Total",total)
            pedidos.append(total)
            break
            
def listar_ped():
    print(pedidos)
    msvcrt.getch("...presione tecla...")
def buscar_ped_rut():
    pass

def imprimir_hoja_ruta():
    pass

def salir():
    print("Gracias por su compra")
    exit()