def lectura_de_datos():
 
  dividendo = float(input("Escriba el dividendo: "))
  divisor = float(input("Escriba el divisor: "))
  return dividendo, divisor
 
def proceso_de_datos(dividendo, divisor):
 
  if divisor == 0:
    return "No se puede dividir por cero."
  else:
    if dividendo % divisor == 0.0:
      return f"{dividendo // divisor} "
    else:
      return f"{dividendo // divisor} Resto: {dividendo % divisor}"
 
def mostrar_resultados(resultado):
 
  print(resultado)
 
def ejercicio_1():
 
  dividendo, divisor = lectura_de_datos()
  resultado = proceso_de_datos(dividendo, divisor)
  mostrar_resultados(resultado)
 
ejercicio_1()