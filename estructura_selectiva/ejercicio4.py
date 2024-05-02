import random
#importamos random para poder hacer una accion aleatoria 

totalValue = float(input("Ingrese el valor de la compra: $ "))
colorBall = ["verde", "amarillo", "rojo", "blanco"]
colorBalota = random.choice(colorBall)
#nombramos y damos color a cada variable 

if colorBalota == "verde":
    descuento = 0.2
    print ("su descuento es del 20%")
    
elif colorBalota == "amarillo":
    descuento = 0.0
    print ("su descuento es del 0%")
elif colorBalota == "rojo":
    descuento = 0.15
    print ("su descuento es del 15%")
elif colorBalota == "blanco":
    descuento = 0.0
    print ("su descuento es del 0%")
    # damos las condiciones segun cada color de balota 

valorPay = (totalValue *  descuento) 
valorDiscount = totalValue - valorPay
#asignamos formulas para dar el valor en total

print("Valor de la compra:" , totalValue)
print("Color de la balota:" , colorBalota)
print("Valor a pagar:", valorDiscount)