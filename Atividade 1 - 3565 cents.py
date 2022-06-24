print("Informe o valor que deseja receber em centavos")
valor = int ( input())

real = int ( (valor / 100) )
print (real ,"Moedas de R$ 1")
restoUm = (valor % 100)
print(restoUm)

cinquenta = int ( (restoUm / 50))
print (cinquenta,"Moedas de 50 cent")
restoCinquenta = (restoUm % 50)
print(restoCinquenta)

vinteCinco = int ( (restoCinquenta / 25) )
print (vinteCinco,"Moedas de 25 cent")
restoVinteCinco = int ( (vinteCinco % 25))

dez = int ((restoVinteCinco / 10) )
print(dez,"Moedas de 10 cent")
restoDez = int ((restoVinteCinco % 10))

cinco = int ((restoDez / 5))
print(cinco,"Moedas de 5 cent")
restoCinco = int ((restoDez % 5))





