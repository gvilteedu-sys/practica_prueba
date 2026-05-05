salario_inicial=1500
incremento=0.10
anio=6
for i in range(1,anio+1):
    print(f"El salario en el año {i} ")
    salario_inicial+=(salario_inicial*incremento)
    print(f"Es: {salario_inicial:.2f}")