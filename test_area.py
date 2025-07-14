from primer_proceto import * #Importamos las funciones de el archivo principal

def test_area_cuadrado(): #Función para calcular el área del cuadrado y probarlo
  assert calcular_area_cuadrado(7) == 49
  assert calcular_area_cuadrado(5.5) == 30.25
  assert calcular_area_cuadrado(0) == 0