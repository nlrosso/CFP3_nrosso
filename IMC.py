def calcular_imc(peso,altura):
    return peso / (altura ** 2)

peso=float(input("Ingrese su peso en kilogramos     "))
altura=float(input("Ingrese su altura en metros     "))

print(f"Su indice de masa corporal es {calcular_imc(peso,altura)}")



