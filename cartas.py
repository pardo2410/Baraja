import random
palos= ['o','c','e','b']
cartas=['A','2','3','4','5','6','7','S','C','R']


def crea_baraja():

    baraja=[]
    for palo in palos:
        for carta in cartas:
            naipe=carta+palo
            baraja.append(naipe)

    return baraja

def mezclar(b):
    
    baraja_retorno=[]
    
    while len(b) != len(baraja_retorno):
        n = random.randint(0,len(b)-1)
        while b[n] in baraja_retorno:
            n = random.randint(0,len(b)-1)
        baraja_retorno.append(b[n])
    b[:] = baraja_retorno
    return b

def reparte(b, players, cards,metodo=False):
    res = []
    
    if metodo == False:
        p=0
        for p in range(players):
            res.append([])
        for ic in range(cards):
            for ij in range(players):
                carta = b.pop(0)
                res[ij].append(carta)
        return res
    else:
        for p in range(players):
            res.append([])
            for ij in range(players):
                for ic in range(cards):
                    carta = b.pop(0)
                    res[ic].append(carta)
        return res

