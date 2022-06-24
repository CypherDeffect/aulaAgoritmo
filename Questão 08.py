valorFabrica = float(input("Informe o valor de fábrica do carro:"))

distribuidor = float ((valorFabrica * 28)/100)
imposto = float ((valorFabrica * 45)/100)

print("O Carro custará R$ ", distribuidor + imposto + valorFabrica, " ao consumidor")

