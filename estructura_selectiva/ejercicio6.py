tuPromedio=float(input("ingrese su promedio: "))
pensionValue=float(input("ingrese el valor de su pension: "))
if tuPromedio >= 9:
    descuento = 0.3 * pensionValue
    totalValue = pensionValue - descuento
    print("se te aplico un descuento de 30%, valor total: ", totalValue)
else:
    totalValue = pensionValue*1.1
    print("valor total a pagar", totalValue)


