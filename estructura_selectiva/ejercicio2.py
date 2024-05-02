totalValue = float(input("ingrese le valor de la compra: "))
# almacena el valor de la compra
cantidadShoes= int(input("ingrese la cantidad de pares de zapatos que lleva:"))
# almacena la cantidad de zapatillas 
descuento1 = totalValue * (1 - 0.1)
# realiza el calculo para la primer descuento 
descuento2 = totalValue * (1 - 0.2)
# realiza el calculo para la segunda posibilidad de calculo 
if cantidadShoes >=3:
    # compara la cantidad de zapatos para tomar una desicion 
    valor= totalValue - descuento2
    print("el descuento fue de  20(%)",valor)
else:
    valor= totalValue - descuento1  
    print("el descuento fue de 10(%)",valor)