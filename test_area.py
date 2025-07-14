from primer_proceto import * #Importamos las funciones de el archivo principal

def test_area_cuadrado(): #Función para calcular el área del cuadrado y probarlo
  assert calcular_area_cuadrado(7) == 49
  assert calcular_area_cuadrado(5.5) == 30.25
  assert calcular_area_cuadrado(25) == 625

def test_area_circulo():
  assert calcular_area_circulo(5) == 78.54
  assert calcular_area_circulo(5.5) == 95.0334

def test_area_triangulo():
  assert calcular_area_triangulo(5,3) == 7.5
  assert calcular_area_triangulo(8.93,25.35) == 113.18775