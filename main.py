import cartas
b1 = cartas.crea_baraja()
bm = cartas.mezclar(b1)
print(bm)
Jugadores = int(input('Numero de jugadores: '))
cartas_j = int(input('Numero de cartas: '))
metodo_r = input('Desea cambiar el metodo de repartir S/N: ')
if metodo_r =='N':
    metodo_r = False
else:
    metodo_r = True
print(cartas.reparte(bm,Jugadores,cartas_j,metodo_r))
