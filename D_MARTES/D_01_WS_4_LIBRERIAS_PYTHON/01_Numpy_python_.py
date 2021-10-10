# -*- coding: utf-8 -*-
"""Introducción a Python .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1puahiVBmVDiA8uoLfC14zfO8t4ruoXdK

# Programación con Python - Numpy


NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.

Incorpora una nueva clase de objetos llamados arrays que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación.

La clase de objetos array
Un array es una estructura de datos de un mismo tipo organizada en forma de tabla o cuadrícula de distintas dimensiones.

Las dimensiones de un array también se conocen como ejes.

### Actividad 1

Crear un vector con valores dentro del rango 10 a 49
"""

import numpy as np
a = np.arange(10,50)
a

"""### Actividad 2
Crear una matriz 3x3 con valores de 0 a 8
"""

np.arange(0,9).reshape(3,3)

"""### Actividad 3

Encontrar los indices que no son ceros del arreglo [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]

"""

a = np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])
np.argwhere( a!=0 )

"""### Actividad 4 

Crear una matriz identidad de 6x6
"""

np.identity(6)

"""###Actividad 5

Crear una matriz con valores al azar con forma 3x3
"""

r = np.random.random((3,3))
r