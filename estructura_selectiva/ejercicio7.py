cantTires = int(input("Ingrese la  cantidad de llantas a comprar: "))
# asignamos la variable para saber la cantidad de llantas se compran 
if cantTires < 5:
    valueTires = 300
elif 5 <= cantTires <= 10:
    valueTires = 250
else:
    valueTires = 200
    # asignamos valores dependiendo la cantidad de llantas y asi conocer el valor total
totalPay = cantTires * valueTires
print("El precio por cada llanta es:", valueTires)
print("El total a pagar es:", totalPay)