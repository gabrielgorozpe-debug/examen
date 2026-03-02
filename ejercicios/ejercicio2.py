def lectura_de_datos_ecuacion():
  print('ECUACIÓN A X + B = 0')
  while True:
    try:
      a = float(input('Escriba el valor del coeficiente a: '))
      b = float(input('Escriba el valor del coeficiente b: '))
      return a, b
    except ValueError:
      print("Entrada inválida. Por favor, ingrese números.")

def proceso_de_datos_ecuacion(a, b):
  if a == 0 and b == 0:
    return 'Todos los números son solución'
  elif a == 0:
    return 'La ecuación no tiene solución'
  else:
    x = -b / a
    return f'La ecuación tiene una solución: {x}'

def mostrar_resultados_ecuacion(resultado):
  print(resultado)

def ejercicio_2():
  a, b = lectura_de_datos_ecuacion()
  resultado = proceso_de_datos_ecuacion(a, b)
  mostrar_resultados_ecuacion(resultado)

ejercicio_2()