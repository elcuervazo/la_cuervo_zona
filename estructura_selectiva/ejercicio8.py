edad = float(input("Ingresa tu edad en años: "))
sexo = input("Ingresa tu sexo (M para masculino, F para femenino): ")
nivel_hemoglobina = float(input("Ingresa tu nivel de hemoglobina en g%: "))
# Determinar el rango de hemoglobina basado en la edad y el sexo
if edad <= 0.0833: 
    rango_hemoglobina = (13, 26)
elif 0.0833 < edad <= 0.5: 
    rango_hemoglobina = (10, 18)
elif 0.5 < edad <= 1: 
    rango_hemoglobina = (11, 15)
elif 1 < edad <= 5: 
    rango_hemoglobina = (11.5, 15)
elif 5 < edad <= 10:
    rango_hemoglobina = (12.6, 15.5)
elif 10 < edad <= 15:
    rango_hemoglobina = (13, 15.5)
elif sexo == "F" or sexo == "f":
    rango_hemoglobina = (12, 16)
else: 
    rango_hemoglobina = (14, 18)
    # Determinar el rango de hemoglobina basado en la edad y el sexo
if nivel_hemoglobina < rango_hemoglobina[0] or nivel_hemoglobina > rango_hemoglobina[1]:
    resultado = "positivo"
else:
    resultado = "negativo"
    # Determinar si la persona tiene anemia o no
print("El resultado del análisis es:", resultado)
