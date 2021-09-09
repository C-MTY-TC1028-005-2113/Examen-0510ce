# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["6","c","d","s","c","d","s"],
        ["Ingresa el total de diagnosticos: ",
        "Ingresa diagnostico: ","Ingresa diagnostico: ","Ingresa diagnostico: ","Ingresa diagnostico: ","Ingresa diagnostico: ","Ingresa diagnostico: ",
        "Casos Delta = 2", "Casos Covid-19 = 2", "Casos Sanos = 2"],
        "Revisa que hayas inicializado los contadores antes del ciclo, revisa si verificaste si se ingresaron valores de ese diganostico usando condicionales"
    ),
    (
        ["8","C","D","S","c","D","s","s","s"],
        ["Ingresa el total de diagnosticos: ",
        "Ingresa diagnostico: ","Ingresa diagnostico: ","Ingresa diagnostico: ","Ingresa diagnostico: ",
        "Ingresa diagnostico: ","Ingresa diagnostico: ",
        "Ingresa diagnostico: ","Ingresa diagnostico: ","Casos Delta = 2", "Casos Covid-19 = 2", "Casos Sanos = 4"],
        "Revisa que hayas inicializado los contadores antes del ciclo, revisa si verificaste si se ingresaron valores de ese diganostico usando condicionales"
    ),
    (
        ["0"],
        ["Ingresa el total de diagnosticos: "],
        "Revisa que hayas inicializado los contadores antes del ciclo, revisa si verificaste si se ingresaron valores de ese diganostico usando condicionales"

    ),
    (
        ["1","c"],
        ["Ingresa el total de diagnosticos: ", "Ingresa diagnostico: ","Casos Covid-19 = 1"],
        "Revisa que hayas inicializado los contadores antes del ciclo, revisa si verificaste si se ingresaron valores de ese diganostico usando condicionales"

    )
]
