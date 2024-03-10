![Tec de Monterrey](../../images/logotecmty.png)
# Sistema de Ecuaciones - básico

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Lleva a cabo el análisis, diseño y codificación en lenguaje Python de un programa que
leea los valores de los coeficientes de las 2 ecuaciones:
# - a,b,c,d,e y f  

![Tec de Monterrey](../../images/ecuaciones.png)

El programa debe calcular los valores de  y ,  x con las 2 fórmulas anteriores.
*  posteriormente  el programa debe desplegar el valor de *x, y*

#### Entradas:
los coeficinetes de las 2 ecuaciones : a,b,c,d,e y f
#### Salidas:
* Mensajes para ingresar los datos de Entrada
* Mensajes para desplegar x, y
#### Procesos:

#### NOTA IMPORTANTE:
* Tu programa debe incluir los mensaje para pedir los datos y
* la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

2 Ejemplos de Ejecución del programa:


```
Caso 1:
a = 3
b = 1
c = 22
d = 4
e = -3
f = -1
x = 5.0
y = 7.0



Caso 2:
a = 2
b = 3
c = 5
d = 5
e = 6
f = 4
x = -6.0
y = 5.666666666666667


```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`python -m pytest --tb=short -v`, subela a tu repositorio en GitHub,
con el proceso de commit + push.
