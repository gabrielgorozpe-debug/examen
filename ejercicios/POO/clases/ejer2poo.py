class Ejercicio2():
  
    def  __init__ (self):
        self.a = 0
        self.b = 0
        self.resultado = ""  

def lectura_de_datos_ecuacion(self):
  print('ECUACIÓN A X + B = 0')
  while True:
    try:
      self.a = float(input('Escriba el valor del coeficiente a: '))
      self.b = float(input('Escriba el valor del coeficiente b: '))
      return self.a, self.b
    except ValueError:
      print("Entrada inválida. Por favor, ingrese números.")

def proceso_de_datos_ecuacion(self):
  if self.a == 0 and self.b == 0:
    return 'Todos los números son solución'
  elif self.a == 0:
    return 'La ecuación no tiene solución'
  else:
    x = -self.b / self.a
    return f'La ecuación tiene una solución: {x}'

def mostrar_resultados_ecuacion(self):
  print(self.resultado)