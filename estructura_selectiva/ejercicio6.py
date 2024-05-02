tuPromedio=float(input("ingrese su promedio: "))
pensionValue=float(input("ingrese el valor de su pension: "))
#nombramos variables para saber el promedio y el valor de la pension
if tuPromedio >= 9:
    descuento = 0.3 * pensionValue
    totalValue = pensionValue - descuento
    #asignamos la formula para conocer el total a pagar dependiendo de su promedio
    print("se te aplico un descuento de 30%, valor total: ", totalValue)
else:
    totalValue = pensionValue*1.1
    print("valor total a pagar", totalValue)


