def opciones():
    print("Seleccione una opcion")
    print("1-Opcion 1")
    print("2-Opcion 2")
    print("3-Opcion 3")
    print("4-SALIR")
def accion(OP=0):
    if OP==1:
        print("Ingreso a la opcion 1")
    elif OP==2:
        print("Ingreso a la opcion 2")
    elif OP==3:
        print("Ingreso a la opcion 3")
    elif OP==4:
        print("Salioo")
    else:
        print("opcion incorrecta")

validacion=True
while validacion==True:
    opciones()
    try:
        op=int(input("Ingrese una opcion: "))
        print(type(op))
        accion(op)
        validacion=False
    except:
        validacion=True
        print("Error")
