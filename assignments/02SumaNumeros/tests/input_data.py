# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
      (
        ["UF","F","10"],
        ["Cursos: ", "Alumno: ", "Cantidad: ", "Total $45500 DLS"],
        "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
    (
        ["BL","F","10"],
        ["Cursos: ", "Alumno: ", "Cantidad: ", "Total $62300 DLS"],
        "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),



   (
        ["UF","L","10"],
        ["Cursos: ", "Alumno: ", "Cantidad: ", "Total $65000 DLS"],
        "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),

    (
        ["BL","L","10"],
        ["Cursos: ", "Alumno: ", "Cantidad: ", "Total $89000 DLS"],
        "Revisa que ingresastelos tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),



      (
        ["buenisimo","buenisimo"],
        ["Cursos: ", "Alumno: ",  "Datos Incorrectos"],
         "No debes leer la cantidad de cursos, \
         Revisa que ingresaste los tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),

      (
       ["cocina","chef"],
        ["Cursos: ", "Alumno: ",  "Datos Incorrectos"],
         "No debes leer la cantidad de cursos, \
         Revisa que ingresaste los tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),
       (
       ["UF","L","-10"],
        ["Cursos: ", "Alumno: ", "Cantidad: ","Cantidad de cursos incorrecta"],
         "La cantidad de cursos debe ser mayor a 0, \
         Revisa que ingresaste los tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    ),

     (
       ["UF","L","0"],
        ["Cursos: ", "Alumno: ", "Cantidad: ","Cantidad de cursos incorrecta"],
         "La cantidad de cursos debe ser mayor a 0, \
         Revisa que ingresaste los tipos de datos correctos, revisa que los datos de salida sean enteros\
        revisa los espacios"
    )


]
