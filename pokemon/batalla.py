import random

def seleccionarPokemones(pokedex):
    ID1, ID2 = random.sample(pokedex.keys(), 2)
    return ID1, ID2

def batallaPokemon(IDpokemon1,IDpokemon2,pokedex,dicTiposPokemon):
    tipo1 = pokedex[IDpokemon1][1].upper()
    tipo2 = pokedex[IDpokemon2][1].upper()
    ataque1 =pokedex[IDpokemon1][2]
    ataque2 =pokedex[IDpokemon2][2]

    if tipo2 in dicTiposPokemon[tipo1][0]:
        ataque1 *= 2
    elif tipo2 in dicTiposPokemon[tipo1][1]:
        ataque1 *= 0.5
    elif tipo2 in dicTiposPokemon[tipo1][2]:
        ataque1 *= 0

    if tipo1 in dicTiposPokemon[tipo2][0]:
        ataque2 *= 2
    elif tipo1 in dicTiposPokemon[tipo2][1]:
        ataque2 *= 0.5
    elif tipo1 in dicTiposPokemon[tipo2][2]:
        ataque2 *= 0

    if ataque1 > ataque2:
        return IDpokemon1
    if ataque2 > ataque1:
        return IDpokemon2
    return 0