def opciones(nombre,apodo):
    print(f"Bienvenido {nombre} ({apodo}), Seleccione una opcion")
    print("1-SUMAR")
    print("2-RESTAR")
    print("3-MULTIPLICAR")
    print("4-SALIR")
def sumar(n1,n2):
    return n1+n2
def restar(n1,n2):
    return n1-n2
def multiplicar(n1,n2):
    return n1*n2
def accion(OP=0): 
    if OP==1:
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        print(sumar(n1,n2))
    elif OP==2:
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        print(restar(n1,n2))
    elif OP==3:
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        print(multiplicar(n1,n2))
    elif OP==4:
        print("Salioo")
    else:
        print("opcion incorrecta")

validacion=True
while validacion==True:
    opciones("GONZALO","ZALO")
    try:
        op=int(input("Ingrese una opcion: "))
        print(type(op))
        accion(op)
        validacion=False
    except:
        validacion=True
        print("Error")
