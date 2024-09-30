# Sistemas dinámicos y el método RK4

Para encontrar la documentación completa visite el siguiente enlace:  [github.com](https://github.com/Sabasaro12/Metodo_RK4.git).

Los sistemas dinámicos son modelos de suma importancia en las ciencias. En general, un modelo dinámico intenta resolver la trayectoria temporal de alguna cantidad física como función de algún generador dinámico; este último usualmente representado de forma funcional.


En algunos casos, podemos modelar la dinámica de un estado genérico 𝑦
mediante la ecuación dinámica

$$\frac{dy}{dt}=f(t,y);\hspace{3mm} $$

La cuál se encuentra sujeta a la siguiente condición inicial:

$$y(t_0)=y_0$$
En esta notación, 𝑦 corresponde a un estado del sistema. Este estado puede ser representado mediante diferentes objetos matemáticos: desde cantidades escalares hasta matrices que representan cierto operador lineal. En la ecuación anterior, 𝑡

corresponde a la variable temporal.

El problema dinámico descrito anteriormente es usualmente conocido en el campo de las matemáticas aplicadas como problema de condición inicial. 

La herramienta que se esta implementando en estos casos perminte resolver \textbf{únicamente el caso donde no existe dependencia explı́cita temporal en la función}
