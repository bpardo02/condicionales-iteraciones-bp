#datos a ingresar por usuario
peso = float(input('Ingrese peso en kilogramos (kg): '))
altura = float(input('Ingrese altura en metros (m)'))

#formula
imc = peso/(altura**2)

#condiciones
if imc<18.5:
    print("El resultado del imc es: bajo peso")
elif 18.5<=imc<25:
    print("El resultado del imc es: peso normal")
elif 25<=imc<30:
    print("El resultado del imc es: sobrepeso")
elif 30<=imc<35:
    print("El resultado del imc es: obesidad grado I")
elif 35<=imc<40:
    print("EL resultado del imc es: obesidad grado II")
else:
    print("El resultado del imc es: obesidad grado III")
