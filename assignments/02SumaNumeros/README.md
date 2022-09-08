![Tec de Monterrey](../../images/logotecmty.png)
# Suma números

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def colegiatura_antes_descuento(tipo_curso, cantidad_cursos):
    pass
    
def descuento_colegiatura(colegiatura, tipo_alumno):
    pass
    
def main():
    #Leer 
    
    # Llamar a las funciones
    pass
    
    # Desplegar los resultados
    
if __name__ == '__main__':
    main()
```
Lleva a cabo el análisis, diseño y codificación en lenguaje Python.

En una secundaria se ofrecen 3 tipos de cursos: 
- U - UF
- B - BLOQUES
- I - INTERCAMBIO

Tiene 2 tipos de alumnos: 
- L - Locales 
- F - Foraneos.

El precio es el siguiente para cada tipo de curso:
- UF  $6,500  DLS c/u
- BLOQUES $8,900 DLS c/u
- INTERCAMBIO $30,550  DLS c/u

Por este regreso a clases la Secundaria ha decidido dar un descuento del 30% a los <b>alumnos Locales</b>

Además ha decidido aplicar la siguiente política de descuentos a los
<b> alumnos Foraneos </b>:
- Si su colegiatura es superior o igual a $21,000 e inferior a $70,000 tendrá un 12% de descuento en la colegiatura.
- Si su colegiatura es superior o igual a $70,000  tendrán un 27% de descuento en la colegiatura.

Escribe un programa que lea el tipo de curso (que es una letra mayúscula que puede ser U, B, I),
el tipo de alumno(que es una letra mayúscula que puede ser L o F) si los datos ingresados son correctos también 
se debe leer la cantidad de cursos en los que se va a inscribir (que es un número entero). 
Supón que solo se va a inscribir en un mismo tipo de curso.

Si se ingresan datos incorrectos en el tipo de curso o en el tipo de alumno el programa
debe desplegar "Datos Incorrectos" y no debe leer la cantidad de cursos.

####  El programa debe tener las siguientes funciones:

- Función llamada __colegiatura_antes_descuento__ que recibe como parámetros: tipo_curso y la cantidad_cursos:  
La función retorna el monto de la colegiatura a pagar antes del descuento.

- Función llamada __descuento_colegiatura__ que recibe como parámetros: el colegiatura antes del descuento y el tipo_alumno:  
La función retorna el monto del descuento que se le hará al alumno.

Si los datos ingresados son adecuados el programa debe calcular   
y mostrar los datos de salida en formato entero.


La salida del programa debe de ser exactamente de la siguiente forma:

```
Tipo de cursos: U
Tipo de alumno: F
Cantidad de cursos: 10
Colegiatura $65000 DLS
Descuento  $7800 DLS
Total a pagar $57200 DLS

Tipo de cursos: B
Tipo de alumno: F
Cantidad de cursos: 10
Colegiatura $89000 DLS
Descuento  $24030 DLS
Total a pagar $64970 DLS

Tipo de cursos: U
Tipo de alumno: L
Cantidad de cursos: 10
Colegiatura $65000 DLS
Descuento  $19500 DLS
Total a pagar $45500 DLS

Tipo de cursos: I
Tipo de alumno: L
Cantidad de cursos: 10
Colegiatura $305500 DLS
Descuento  $91650 DLS
Total a pagar $213850 DLS

Tipo de cursos: juego
Tipo de alumno: inteligente
Datos incorrectos



**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`python -m pytest --tb=short -v`, subela a tu repositorio en GitHub,
con el proceso de commit + push.
