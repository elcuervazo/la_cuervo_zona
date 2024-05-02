sex = (input("ingrese su sexo femenino/masculino :"))
age = int(input("ingrese su edad :"))
# nombramos las variables para conocer la edad y el sexo
if sex == "femenino":
    pulsaciones = (220 * age) /10
    # damos la formula para obtener las pulsaciones
    print("su numero de pulsaiones cada 10 segundos es :", pulsaciones)
elif sex == "masculino":
    pulsaciones = (210 * age) /10  
    print("su numero de pulsaiones cada 10 segundos es :", pulsaciones)
        # damos la formula para obtener las pulsaciones segun la edad 

else:
    print("sexo no valido, seleccione femenino/masculino")