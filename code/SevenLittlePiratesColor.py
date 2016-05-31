# Seven Little Pirates CMDL  ALPHA 1.0 by Al3X V3GAS
# This software is licensed under the GNU GPL v3.0
# COPYRIGHT Al3X V3GAS 2016 (C) under open conditions.
# ********************NOTE*********************
# THIS PROGRAM WILL ONLY WORK ON PYTHON 2!!!
# ********************NOTE*********************

#<startsettings>
import time
import colorama
colorama.init()
#</startsettings>

#<main>
print (colorama.Fore.MAGENTA + "Hola! Mi nombre es Blaise!" + colorama.Fore.RESET)
username = raw_input(colorama.Fore.MAGENTA + "Y tu? Como te llamas? " + colorama.Fore.RESET)
print ("Hola, " + str(username))
promptname = (colorama.Fore.MAGENTA + "[" + str(username) + "]" + colorama.Fore.RESET)
time.sleep(1)
print (colorama.Fore.MAGENTA + "[BLAISE] Yo tengo una problema poca.." + colorama.Fore.RESET)
print (str(promptname) + " Que es eso?" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.MAGENTA + "[BLAISE] Mi novia, Matilde, es en los manos de unos piratas" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.MAGENTA + "muy males y estos quieren, que yo resolvo siete preguntas y" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.MAGENTA + "las respuestas a esta preguntas dirigen a la ciudad 'El Dorado'!" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.MAGENTA + "Yo no se las respuestas para estas preguntas! Ayudas me?" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.MAGENTA + str(promptname) + " Si, naturalmente! Donde son los piratas?" + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "[BLAISE] En la isla de los muertos." + colorama.Fore.RESET)
print (str(promptname) + " Vamos a esta isla!" + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "======================================" + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "En la isla de los muertos..." + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "======================================" + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "[ALEJO] ALTO!" + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "[ALEJO] QUIEN VA?" + colorama.Fore.RESET)
time.sleep(1)
print (colorama.Fore.MAGENTA + str(promptname) + " Tenga cuidado! Es " + str(username) + " y Blaise!" + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "Tenga cuidado Alejo! Ahh los estupidos estan aqui amigos!" + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + str(promptname) + " Silencio, cachito de mierda. Danos tu misterio y Matilde" + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "si Blaise responsa todas de tus preguntas con la respuesta correcta!" + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "[ALEJO] Vale..." + colorama.Fore.RESET)
print (colorama.Fore.MAGENTA + "La pregunta una es 'Que animal tenia pies, pero es un animal peligroso ahora?" + colorama.Fore.RESET)
answerone = raw_input(colorama.Fore.CYAN + "Tu respuesta: " + colorama.Fore.RESET)
if answerone == "serpiente":
    print (colorama.Fore.GREEN + "Muy bien! Dos preguntas se dejan!" + colorama.Fore.RESET)
    print (colorama.Fore.GREEN + "La pregunta dos es 'Que animal es majestuosamente, vive lejos de aqui y es un icono de la Fuerza?" + colorama.Fore.RESET)
    answertwo = raw_input(colorama.Fore.CYAN + "Tu respuesta: " + colorama.Fore.RESET)
    print (colorama.Fore.GREEN + "Tus puntos: 1 " + colorama.Fore.RESET)
    if answertwo == "leon":
        print (colorama.Fore.GREEN + "Muy bien! Una preguntas se deja!" + colorama.Fore.RESET)
        print (colorama.Fore.GREEN + "Tus puntos: 2 " + colorama.Fore.RESET)
        print (colorama.Fore.GREEN + "La pregunta dos es 'Que animal es extinguido y temido?" + colorama.Fore.RESET)
        answerthree = raw_input(colorama.Fore.CYAN + "Tu respuesta: " + colorama.Fore.RESET)
        if answerthree == "T-Rex":
            print (colorama.Fore.GREEN + "Muchas Gracias! Ahora podemos buscar la prenda con estos indicaciones!" + colorama.Fore.RESET)
            print (colorama.Fore.GREEN + "Tus puntos: 3 " + colorama.Fore.RESET)
        else:
            print (colorama.Fore.RED + "[ALEJO] Matad Matilde y los dos!" + colorama.Fore.RESET)
            print (colorama.Fore.RED + "Tus puntos: 2 " + colorama.Fore.RESET)
    else:
        print (colorama.Fore.RED + "[ALEJO] Matad Matilde y los dos!" + colorama.Fore.RESET)
        print (colorama.Fore.RED + "Tus puntos: 1 " + colorama.Fore.RESET)
else:
    print (colorama.Fore.RED + "[ALEJO] Matad Matilde y los dos!" + colorama.Fore.RESET)
    print (colorama.Fore.RED + "Tus puntos: 0 " + colorama.Fore.RESET)

print (colorama.Fore.CYAN + "=======================================================" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.CYAN + "THANK YOU FOR PLAYING SEVEN LITTLE PIRATES!" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.CYAN + "IT HAS BEEN A PLEASURE WORKING WITH YOU!" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.CYAN + "SEVEN LITTLE PIRATES 2016 (C) BY AL3X V3GAS 2016 (C)" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.CYAN + "FURTHER INFO: GITHUB:COM/AL3XV3GAS/SEVENLITTLEPIRATES" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.CYAN + "=======================================================" + colorama.Fore.RESET)
time.sleep(2)
print (colorama.Fore.RED + "===EXITING===" + colorama.Fore.RESET)
exit()
#</main>
