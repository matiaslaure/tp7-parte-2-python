import time

hora = time.strftime('%H') 
minutos = time.strftime('%M') 

if int(hora) >= 19:
	print ("Es hora de descansar y disfrutar la familia") 
else:
	print ("Fuerzas que solo quedan {} horas y {} minutos para salir del trabajo".format(18- int(hora), 59-int(minutos)))