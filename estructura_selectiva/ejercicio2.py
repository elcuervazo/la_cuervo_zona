value = float(input("ingrese le valor de la compra: "))
shoes= int(input("ingrese la cantidad de pares de zapatos que lleva:"))
descuento1 = value * (1 - 0.1)
descuento2 = value * (1 - 0.2)
if shoes >=3:
    valor= value - descuento2
    print("el descuento fue de  20(%)",valor)
else:
    valor= value - descuento1  
    print("el descuento fue de 10(%)",valor)