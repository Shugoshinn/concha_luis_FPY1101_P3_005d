import os, time, csv
from funciones import *


while True:
    os.system('cls')
    print("1. Registrar pedido")
    print("2. Listar pedidos")
    print("3. Buscar pedido por RUT")
    print("4. Imprimir hoja de ruta")
    print("5. Salir")
    opc = input("Ingrese opcion: ")
    os.system('cls')

    if opc == '1':
        registrar_ped()
    elif opc == '2':
        listar_ped()
    elif opc == '3':
        buscar_ped_rut()
    elif opc == '4':
        imprimir_hoja_ruta()
    elif opc == '5':
        salir()