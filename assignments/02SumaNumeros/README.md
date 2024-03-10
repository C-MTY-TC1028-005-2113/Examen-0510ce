![Tec de Monterrey](../../images/logotecmty.png)
# Secundaria X - condicionales y funciones

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def calcula_colegiatura_con_descuento(tipo_curso, cantidad_cursos, tipo_alumno):
    # función que calcula el total a pagar en base a los datos recibidos en los parámetros

    # La función retorna el total a pagar ya con el descuento aplicado(solo si aplica)
    pass


def main():
    # 1. Leer los datos de entrada

    # 2. Validar datos de entrada

         # 3. si si son correctos llamar a  calcula_colegiatura_con_descuento(...)

            # 4. Desplegar los resultados
    pass

if __name__ == '__main__':
    main()
```
Lleva a cabo el análisis, diseño y codificación en lenguaje Python.

En una secundaria se ofrecen 2 tipos de cursos:
- UF - UNIDAD_FORMACION
- BL - BLOQUE

La secundaria tiene 2 tipos de alumnos:
- L - Locales
- F - Foraneos.

El precio es el siguiente para cada tipo de curso:
- UF  $6,500  DLS c/u
- BL  $8,900 DLS c/u

Por este regreso a clases la Secundaria ha decidido  dar el siguiente descuento a foráneos :

<b> alumnos Foraneos </b>:
- Si su colegiatura es superior o igual a $15,500 e inferior a $65,000 tendrá un 15% de descuento en la colegiatura.
- Si su colegiatura es superior o igual a $65,000  tendrán un 30% de descuento en la colegiatura.


# Dentro de la función main() se debe hacer lo siguiente

1. leer el tipo de curso (que son 2 letras mayúsculas, puede ser : UF, BL),
2. ler el tipo de alumno(que es una letra mayúscula, puede ser L o F)
3. Verificar si se ingresan datos incorrectos en el tipo de curso o en el tipo de alumno  

   el programa debe desplegar "Datos Incorrectos" y no debe leer la cantidad de cursos.  

   Si todos los datos son correctos:  

     leer la cantidad de cursos en los que se va a inscribir (entero).   

     Si la cantidad de cursos es inferior a 1 el programa debe desplegar   

            "Cantidad de cursos incorrecta"   

Si todos los datos ingresados son correctos el programa debe llamar a la función
calcula_colegiatura_con_descuento( ...) que calcula y retorna el total a pagar de colegiatura(ya con despuento si es que aplica)
el valor de retorno se debe desplegar en formato entero usando la función *round( )* sin decimales.

La salida del programa debe de ser exactamente de la siguiente forma:
Casos de ejecución del programa:
```
Caso 1:
Cursos: UF
Alumno: F
Cantidad: 10
Total $45500 DLS

Caso 2:
Cursos: BL
Alumno: F
Cantidad: 10
Total $62300 DLS

Caso 3:
Cursos: UF
Alumno: L
Cantidad: 10
Total $65000 DLS

Caso 4:
Cursos: juego
Alumno: inteligente
Datos Incorrectos

Caso 5:
Cursos: UF
Alumno: L
Cantidad: 0
Cantidad de cursos incorrecta
``````

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`python -m pytest --tb=short -v`, subela a tu repositorio en GitHub,
con el proceso de commit + push.
ef main():
