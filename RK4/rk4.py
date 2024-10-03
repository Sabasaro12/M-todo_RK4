#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def dyn_generator(oper, state):
    """ Esta es la función $f(t,y)= −i[𝐎,𝐲(𝑡)]$, la cual se puede expresar como: $−i[𝐎,y(t)]= −i(𝐎 \cdot y(t) - y(t) \cdot 𝐎 )$.

    Examples:
        >>> dyn_generator(np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]))
        array([[0.-0.j, 0.+1.j],[0.-1.j, 0.-0.j]])

    Args:
        oper (array): Es un array que representa al operador lineal 𝐎.
        state (array): Es un array que representa el estado de la función y(t).

    Returns:
        (array): Es un array que representa la conmutación $−i[𝐎,𝐲(t)]$.
    """
    return -1.0j*(np.dot(oper,state)-np.dot(state,oper))

def rk4(func, oper, state, h):
    """
    Esta función implementa el [método RK4](explanation.md).

    Examples:
        >>> rk4(dyn_generator,np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0,     0]],),1)
        array([[0.25+0.j,0.-0.75j],[0.+0.75j,0.75+0.j]])

    Args:
         func (function): Toma una función en la cual se va a evaluar cada uno de los argumentos según que subindice de k se este determinando.
         oper (array): Es un array que representa al operador lineal 𝐎.
         state (array): Es un array que representa el estado de la función y(t).
         h (float): Es una variable que contiene el paso temporal homogéneo

    Returns:
        (array): Es un array que representa la solución estimada por el método RK4 a un punto temporal $𝑦_𝑛+1$.
    """
    k1 = h*func(oper,state)
    k2 =h* func(oper + h/2, state + k1/2)
    k3 =h* func(oper + h/2, state + k2/2)
    k4 =h* func(oper+h,state+k3)
    return state + (1/6)*(k1+2*k2+2*k3+k4)

