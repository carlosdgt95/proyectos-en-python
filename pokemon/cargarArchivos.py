def cargarPokedex(nombreArchivo = 'pokedex.txt'):
    archivo = open(nombreArchivo, 'r')
    archivo.readline()
    diccionario = {}
    for linea in archivo:
        datos = linea.strip().split('|')
        datos[3] = int(datos[3])
        diccionario[int(datos[0])]=datos[1:]
    archivo.close()
    return diccionario

def cargarTipos(nombreArchivo ='tiposPokemon.txt'):
    archivo = open(nombreArchivo, 'r')
    archivo.readline()
    diccionario = {}
    for linea in archivo:
        tipo,doble,mitad,cero = linea.strip().split('|')
        tipo = tipo[:-5]
        diccionario[tipo]=[doble.split('/'),mitad.split('/'),cero.split('/')]
    archivo.close()
    return diccionario