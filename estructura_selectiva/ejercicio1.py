primerNota=float(input("Escriba la primer nota: "))
#almacena la primer nota
segundaNota=float(input("Escriba la segunda nota: "))
#almaceana  la segunda nota
tercerNota=float(input("Escriba la tercer nota: "))
#almacena la tercer nota
prom= (primerNota+segundaNota+tercerNota)/3
#realiza el calculo para obtener el promedio
print ("Aprobado mi rey, paso con",prom) if prom > 70  else print("paila mi rey, perdio con",prom,)