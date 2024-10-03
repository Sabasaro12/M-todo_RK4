#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def dyn_generator(oper, state):
    """ Esta es la función $f(t,y)= −i[𝐎,𝐲(𝑡)]$, la cual se puede expresar como: $−i[𝐎,y(t)]= −i(𝐎 \cdot y(t) - y(t) \cdot 𝐎 )$.

    Examples:
        >>> dyn_generator(np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]))
        array([[0.-0.j, 0.+1.j],\\[0.-1.j, 0.-0.j]])

    Args:
        oper (array): Es un array que representa al operador lineal 𝐎.
        state (array): Es un array que representa el estado de la función y(t).

    Returns:
        (array) :Es un array que representa la conmutación $−i[𝐎,𝐲(t)]$.
    """
    return -1.0j*(np.dot(oper,state)-np.dot(state,oper))

def rk4(func, oper, state, h):
    k1 = h*func(oper,state)
    k2 =h* func(oper + h/2, state + k1/2)
    k3 =h* func(oper + h/2, state + k2/2)
    k4 =h* func(oper+h,state+k3)
    return state + (1/6)*(k1+2*k2+2*k3+k4)

oOper = np.array([[0, 1], [1, 0]])
yInit = np.array([[1, 0], [0, 0]])
times = np.linspace(0,10,100).astype(float)

stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)
h = times[1]-times[0]

for tt in range(times.size):
    # Guarde el valor de las entradas (0,0) y (1,1) en los arreglos que definimos
    # Obtenga estos valores de las entradas de yInit
    # Código aquí ->
    stateQuant00[tt] = yInit[0,0].real
    stateQuant11[tt] = yInit[1,1].real
    # Invoque rk4 operando sobre yInit
    # y devuelva el resultado a un nuevo yN
    # Código aquí ->
    yN=rk4(dyn_generator,oOper,yInit,h)
    # Ahora asignamos yN a yInit
    # De esta manera, en la siguiente iteración, el operador de esta iteración se convierte en el inicial
    # de la siguiente iteración
    yInit = yN

plt.figure(figsize=(4, 2), dpi=300)
plt.plot(times, stateQuant00, label='Estado (0,0)', color='g')
plt.plot(times, stateQuant11, label='Estado (1,1)', color ="b")

plt.xlabel('Tiempo')
plt.ylabel('Valor del estado')
plt.legend()
plt.show()
