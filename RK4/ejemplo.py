#!/usr/bin/env python3
"""Ejemplo del uso del programa


Se importan los modulos necesarios para realizar la operación

    >>> import numpy as np
    >>> from RK4 import rk4
    >>> import matplotlib.pyplot as plt

Se crean dos arreglos, uno que contiene el estado inicial del sistema y otro el estado inicial del operador

    >>> oOper = np.array([[0, 1], [1, 0]])
    >>> yInit = np.array([[1, 0], [0, 0]])

Se crea un arreglo que contendrá todas las subdiviciones del período de tiempo especificado

    >>> times = np.linspace(0,10,100).astype(float)

Se crean dos arreglos que contendran los valores de las variaciones para los dos posbiles estados

    >>> stateQuant00 = np.zeros(times.size)
    >>> stateQuant11 = np.zeros(times.size)

Se identifica la variación temporal que hay entre cada medición y este valor se le asiga a una variable

    >>> h = times[1]-times[0]

Se realiza un ciclo for para evaluar la variación de los estados con forme el tiempo avanza, y se almacenan los valores de la matriz en posicion [0,0] y [1,1] en los arreglos

    >>> for tt in range(times.size):
        >>> stateQuant00[tt] = yInit[0,0].real
        >>> stateQuant11[tt] = yInit[1,1].real

Se le asignan a una variable el estado actual de la matriz evaluada en las dos [funciones principales](reference.md), y luego este valor se le asiga a la variable que almacena el valor de la función $f(y,t)$

        >>> yN = rk4.rk4(rk4.dyn_generator,oOper,yInit,h)
        >>> yInit = yN

El siguiente código permite crear una gráfica con la evolución de los dos diferentes estados a lo largo del tiempo

    >>> plt.figure(figsize=(4, 2), dpi=300)
    >>> plt.plot(times, stateQuant00, label='Estado (0,0)', color='g')
    >>> plt.plot(times, stateQuant11, label='Estado (1,1)', color ="b")
    >>> plt.xlabel('Tiempo')
    >>> plt.ylabel('Valor del estado')
    >>> plt.legend()
    >>> plt.show()

![Evolucion temporal](Images/grafico.png)

"""
