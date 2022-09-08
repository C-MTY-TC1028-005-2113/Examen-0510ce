# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
      (
        ["U","F","10"],
        ["Tipo de cursos: ", "Tipo de alumno: ", "Cantidad de cursos: ", 
         "Colegiatura $65000 DLS", "Descuento $7800 DLS", "Total a pagar $57200 DLS"],
        "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
    (
        ["B","F","10"],
        ["Tipo de cursos: ", "Tipo de alumno: ", "Cantidad de cursos: ",
         "Colegiatura $89000 DLS", "Descuento $24030 DLS", "Total a pagar $64970 DLS"],
        "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
    (
        ["I","F","10"],
        ["Tipo de cursos: ", "Tipo de alumno: ", "Cantidad de cursos: ",
        "Colegiatura $305500 DLS", "Descuento $82485 DLS", "Total a pagar $223015 DLS"],
         "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
         
         
   (
        ["U","L","10"],
        ["Tipo de cursos: ", "Tipo de alumno: ", "Cantidad de cursos: ", 
         "Colegiatura $65000 DLS", "Descuento $19500 DLS","Total a pagar $45500 DLS"],
        "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
    
    (
        ["B","L","10"],
        ["Tipo de cursos: ", "Tipo de alumno: ", "Cantidad de cursos: ",
         "Colegiatura $89000 DLS", "Descuento $26700 DLS", "Total a pagar $62300 DLS"],
        "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
    
    (
        ["I","L","10"],
        ["Tipo de cursos: ", "Tipo de alumno: ", "Cantidad de cursos: ",
         "Colegiatura $305500 DLS", "Descuento $91650 DLS", "Total a pagar $213850 DLS"],
         "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
    
      (
        ["buenisimo","buenisimo"],
        ["Tipo de cursos: ", "Tipo de alumno: ",  "Datos incorrectos"],
         "No debes leer la cantidad de cursos, \
         Revisa que ingresaste los tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
    
      (
       ["cocina","chef"],
        ["Tipo de cursos: ", "Tipo de alumno: ",  "Datos incorrectos"],
         "No debes leer la cantidad de cursos, \
         Revisa que ingresaste los tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
       (
       ["I","L","-10"],
        ["Tipo de cursos: ", "Tipo de alumno: ",  "Cantidad de cursos: ","Cantidad de cursos incorrecta"],
         "La cantidad de cursos debe ser mayor a 0, \
         Revisa que ingresaste los tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
    
     (
       ["I","L","0"],
        ["Tipo de cursos: ", "Tipo de alumno: ",  "Cantidad de cursos: ","Cantidad de cursos incorrecta"],
         "La cantidad de cursos debe ser mayor a 0, \
         Revisa que ingresaste los tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    )
    
    
]
