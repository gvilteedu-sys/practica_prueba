band=True
while band:
    try:
        n1=int(input("Ingrese el primer numero: "))
        n2=int(input("Ingrese el segundo numero: "))
        print(n1/n2)
    except ZeroDivisionError as e:
        print(f"Error de division entre cero {e}")
    except ValueError as e:
        print(f"Error de valor {e}")
    else:
        print("Operacion correcta")
        band=False