def sistema_ecuaciones( ):
    a = int(input( 'a = ') )
    b = int(input( 'b = ') )
    c = int(input( 'c = ') )
    d = int(input( 'd = ') )
    e = int(input( 'e = ') )
    f = int(input( 'f = ') )

    y = (a * f - c * d) / (a * e - b * d)
    x = (c * e - b * f) / (a * e - b * d)

    print('x =', x)
    print('y =', y)


def main():
  #escribe tu código abajo de esta línea
  sistema_ecuaciones( )


if __name__=='__main__':
    main()
