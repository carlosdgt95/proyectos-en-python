import datetime
formato = "%d/%m/%Y"
contador = 0
fecha_reserva = input ("fecha reserva (dd/mm/aaaa):")
fechadesde = input ('Fecha desde (dd/mm/aaaa): ')
fechahasta = input ('Fecha hasta (dd/mm/aaaa): ')
while contador==0 :
    contador+=1
    if fechadesde < fechahasta and fecha_reserva<fechadesde and fecha_reserva<30:
        fechadesde = datetime.strptime (fechadesde= formato)
        fechahasta = datetime.strptime (fechahasta= formato)
        fecha_reserva=datetime.strptime(fecha_reserva=formato)
    else:
        fecha=1
        print ("fecha de inicio:",fechadesde)
        print ("fecha fin de estadia:",fechahasta)
        print("fecha de reserva:",fecha_reserva)


