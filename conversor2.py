dolar = input('cuantos dolares americanos tienes?: ')
dolar = float(dolar)
valor_peso = 0.22 
peso = dolar / valor_peso
peso = round(peso, 2)
peso = str(peso)
print('tienes $' + peso + 'peso')