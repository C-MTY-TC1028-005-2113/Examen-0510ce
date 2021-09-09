# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["3","1","22","4","-3","-1"],
        ["a = ","b = ","c = ","d = ","e = ","f = ", "x = 5.0","y = 7.0"],
        "Debe salir x = 5.0 y = 7.0  revisa la division - añadiste  ( )/ ( )?"
    ),
    # Test case 2
    (
        ["2","3","5","5","6","4"],
        ["a = ","b = ","c = ","d = ","e = ","f = ","x = -6.0","y = 5.666666666666667"],
        "Debe salir x = -6.0  y = 5.666666666666667 revisa la division - añadiste  ( )/ ( )?"

    )

]
