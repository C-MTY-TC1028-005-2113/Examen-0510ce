![Tec de Monterrey](../../images/logotecmty.png)
# Suma números

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def contar_diagnosticos(n):
    pass
    
def main():
    #Leer la cantidad de diagnosticos
    
    #escribe la llamada a la función contar_diagnosticos
    pass
    
if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Lleva a cabo el análisis, diseño y codificación en lenguaje Python de una función llamada  contar_diagnosticos() y
de la función main( )

La función  contar_diagnosticos recibe como parámetro de entrada la cantidad de diagnósticos que se van a procesar,
dentro de la función se ingresan los datos de  los diagnósticos de pacientes de un consultorio médico,
estos datos son de tipo string, la función debe calcular:
* la cantidad de casos de COVID_19,
* la cantidad de casos de DELTA y 
* la cantidad de casos de pacientes SANOS:

Los datos que se ingresan son de tipo string - una sola letra indicando el diagnóstico:
- C o c para un paciente diagnosticado con *COVID_19*
- D o d para un paciente diagnosticado con *DELTA*
- S o s para un paciente *SANO*

La función debe calcular y desplegar:
- total de casos de COVID_19
- total de casos de  DELTA
- total de casos de  SANO(s)

#### Nota importante - en caso de que no existan casos de alguna opción no se muestra nada sobre ese caso.

# Añade tu análisis del problema dentro del archivo
#### Entradas:
#### Salidas:
* Mensajes para ingresar los datos de Entrada:
* Mensajes para desplegar los datos de salida:
#### Procesos:
#### NOTA IMPORTANTE:

Tu programa debe incluir los mensaje para pedir los datos y
la salida deben coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

4 Ejemplos de Ejecución del programa:

```
Ingresa el total de diagnosticos: 6
Ingresa diagnostico: c
Ingresa diagnostico: d
Ingresa diagnostico: s
Ingresa diagnostico: c
Ingresa diagnostico: d
Ingresa diagnostico: s
Casos Delta = 2
Casos Covid-19 = 2
Casos Sanos = 2


Ingresa el total de diagnosticos: 1
Ingresa diagnostico: c
Casos Covid-19 = 1


Ingresa el total de diagnosticos: 8
Ingresa diagnostico: C
Ingresa diagnostico: D
Ingresa diagnostico: S
Ingresa diagnostico: c
Ingresa diagnostico: D
Ingresa diagnostico: s
Ingresa diagnostico: s
Ingresa diagnostico: s
Casos Delta = 2
Casos Covid-19 = 2
Casos Sanos = 4


Ingresa el total de diagnosticos: 0

```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento.
No la vamos a necesitar para este programa, pero es una buena práctica
incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con
`python -m pytest --tb=short -v`, subela a tu repositorio en GitHub,
con el proceso de commit + push.
