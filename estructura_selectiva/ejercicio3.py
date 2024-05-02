totalPay = float(input("Ingrese el monto total de la compra: "))
#almacena el total de la compra
if totalPay > 500000:
    #condiciona para la toma de desicion
    mineMoney = totalPay * 0.55
    #   el dinero propoio de la empresa
    bankMoney = totalPay * 0.30
    #el dinero que el banco presta
    credit = (totalPay * 0.15) 
    #el credito que los fabricantes nos ofrecen 
    interes = (credit) + (credit * 0.2)
else:
    mineMoney = totalPay * 0.70
    credit = (totalPay * 0.3)
    interes = (credit) + (credit * 0.2)
    bankMoney = 0
    #asignacion de valores a cada uno
print("Valor invertido de dinero propio: $", mineMoney)
print("Valor prestado al banco: $", bankMoney)
print("Valor del crédito solicitado al fabricante: $", credit)