import os, time, csv, msvcrt

pedidos = ["RUT","Cliente","Direccion","Comuna","Cil.5kg","Cil.15kg","Total"]
def registrar_ped():
    while True:
        rut = int(input("Ingrese su rut(sin puntos ni guion y con dígito verificador): "))
        pedidos.append(rut)
        while True:
            nombre = input("Ingrese su nombre: ")
            if len(nombre)>=3:
                print("Su nombre cumple con las 3 letras minimas")
            else:
                ("ERROR! SU NOMBRE DEBE TENER AL MENOS 3 LETRAS")
            break
        pedidos.append(nombre)
        direccion = input("Ingrese su dirección: ")
        pedidos.append(direccion)
        comuna = input("Ingrese su comuna(Santiago, Pirque, Colina): ")
        pedidos.append(comuna)
        cilindros = int(input("Ingrese que cilindro quiere llevar: "))
        
        if cilindros ==5: 
            print("Cilindro agregado con éxito")
            cilindro_5 = cilindro_5 + 12500
            pedidos.append(cilindros)
            time.sleep(1.5)
        elif cilindros == 15:
            print("Cilindro agregado con éxito")
            cilindro_15 = cilindro_15 + 25500
            pedidos.append(cilindros)
            time.sleep(1.5)
        else:
            print("ERROR! PEDIDO NO REGISTRADO, INGRESE EL CILINDOR DE 5 O DE 15")
            
        total = cilindro_5 + cilindro_15
        print("Total",total)
        pedidos.append(total)
        break
            
def listar_ped():
    print(pedidos)
    msvcrt.getch("...presione tecla...")
def buscar_ped_rut():
    rut = input(f"RUT"("Ingrese rut: "))
    if not rut:
        print("NO EXISTEN PEDIDOS PARA ESTE RUT") 
    else:
        ("ERROR! RUT NO REGISTRADO")

def imprimir_hoja_ruta():
    with open("w",pedidos,".csv") as archivo:
        archivo 
def salir():
    print("Gracias por su compra, y gracias a dios, que tenga buen día")
    exit()