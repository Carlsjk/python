def conversor(tipo_pesos, valor_dolar):
    pesos = input('cuantos pesos ' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(' tienes $ ' + dolares + ' dolares ')






menu = """
bienvenido al conversor de moneda 

1 - pesos colombianos
2 - pesos mexicanos
3 - pesos argentinos

elige una opcion: """

opcion = input(menu)

if opcion == '1':
    conversor('colombianos', 4323)
    
elif opcion == '2':
    conversor('mexicanos', 20)
    
elif opcion == '3':
    conversor('argentinos', 130)
    
else:
    print('escoge una opcion correcta')

