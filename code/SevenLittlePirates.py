# Seven Little Pirates CMDL  ALPHA 1.0 by Al3X V3GAS
# This software is licensed under the GNU GPL v3.0
# COPYRIGHT Al3X V3GAS 2016 (C) under open conditions.
# ********************NOTE*********************
# THIS PROGRAM WILL ONLY WORK ON PYTHON 2!!!
# ********************NOTE*********************

#<startsettings>
import time
#</startsettings>

#<main>
print ("Hola! Mi nombre es Blaise!")
username = raw_input("Y tu? Como te llamas? ")
print ("Hola, " + str(username))
promptname = ("[" + str(username) + "]")
time.sleep(1)
print ("[BLAISE] Yo tengo una problema poca..")
print (str(promptname) + " Que es eso?")
time.sleep(2)
print ("[BLAISE] Mi novia, Matilde, es en los manos de unos piratas")
time.sleep(2)
print ("muy males y estos quieren, que yo resolvo siete preguntas y")
time.sleep(2)
print ("las respuestas a esta preguntas dirigen a la ciudad 'El Dorado'!")
time.sleep(2)
print ("Yo no se las respuestas para estas preguntas! Ayudas me?")
time.sleep(2)
print (str(promptname) + " Si, naturalmente! Donde son los piratas?")
print ("[BLAISE] En la isla de los muertos.")
print (str(promptname) + " Vamos a esta isla!")
print ("======================================")
print ("En la isla de los muertos...")
print ("======================================")
print ("[ALEJO] ALTO!")
print ("[ALEJO] QUIEN VA?")
time.sleep(1)
print (str(promptname) + " Tenga cuidado! Es " + str(username) + " y Blaise!")
print ("Tenga cuidado Alejo! Ahh los estupidos estan aqui amigos!")
print (str(promptname) + " Silencio, cachito de mierda. Danos tu misterio y Matilde")
print ("si Blaise responsa todas de tus preguntas con la respuesta correcta!")
print ("[ALEJO] Vale...")
print ("La pregunta una es 'Que animal tenia pies, pero es un animal peligroso ahora?")
answerone = raw_input("Tu respuesta: ")
if answerone == "serpiente":
    print ("Muy bien! Dos preguntas se dejan!")
    print ("La pregunta dos es 'Que animal es majestuosamente, vive lejos de aqui y es un icono de la Fuerza?")
    answertwo = raw_input("Tu respuesta: ")
    print ("Tus puntos: 1 ")
    if answertwo == "leon":
        print ("Muy bien! Una preguntas se deja!")
        print ("Tus puntos: 2 ")
        print ("La pregunta dos es 'Que animal es extinguido y temido?")
        answerthree = raw_input("Tu respuesta: ")
        if answerthree == "T-Rex":
            print ("Muchas Gracias! Ahora podemos buscar la prenda con estos indicaciones!")
            print ("Tus puntos: 3 ")
        else:
            print ("[ALEJO] Matad Matilde y los dos!")
            print ("Tus puntos: 2 ")
    else:
        print ("[ALEJO] Matad Matilde y los dos!")
        print ("Tus puntos: 1 ")
else:
    print ("[ALEJO] Matad Matilde y los dos!")
    print ("Tus puntos: 0 ")

print ("=======================================================")
time.sleep(2)
print ("THANK YOU FOR PLAYING SEVEN LITTLE PIRATES!")
time.sleep(2)
print ("IT HAS BEEN A PLEASURE WORKING WITH YOU!")
time.sleep(2)
print ("SEVEN LITTLE PIRATES 2016 (C) BY AL3X V3GAS 2016 (C)")
time.sleep(2)
print ("FURTHER INFO: GITHUB:COM/AL3XV3GAS/SEVENLITTLEPIRATES")
time.sleep(2)
print ("=======================================================")
time.sleep(2)
print ("===EXITING===")
exit()
#</main>
