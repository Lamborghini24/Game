import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_attempts = 10
fallos = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
Dificultad=int(input("""Ingrese el numero correspondiente a la dificultad que usted desea:
1)_ Facil
2)_ Normal
3)_ Dificil
 """))
while (Dificultad != 1 and Dificultad != 2 and Dificultad != 3):
    Dificultad=int(input("""Numero invalido, por favor, ingrese el numero correspondiente a la dificultad que desea:
1)_ Facil
2)_ Normal
3)_ Dificil
 """))
    print(Dificultad)
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
if Dificultad == 1:
    word_displayed = ""
    for c in secret_word:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'á' or c == 'é' or c == 'í' or c =='ó' or c == 'ú':
            word_displayed = word_displayed+c
            guessed_letters.append(c)
        else:
            word_displayed = word_displayed + "_"
elif Dificultad == 2:
    inicio = (secret_word[0])
    fin = (secret_word[-1])
    aux = ""
    for i in range(1, len(secret_word)-1):
        aux=aux+secret_word[i]
    secret_word=aux
    word_displayed = inicio + ("_" * len(secret_word) ) + fin

elif Dificultad == 3:
    word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
while fallos < max_attempts:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si la letra ya ha sido adivinada
    if letter == "":
        print("Error, asegurese de ingresar una letra")
        continue
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fallos = fallos +1
        print(f"Has fallado {fallos} veces, Te quedan {max_attempts- fallos} intentos")
    
        # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    if Dificultad != 2:
        print(f"Palabra: {word_displayed}")
    else:
        print(f"Palabra: {inicio+word_displayed+fin}")
        # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        if Dificultad!=2:
            print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        else:
            print(f"¡Felicidades! Has adivinado la palabra secreta: {inicio+secret_word+fin}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")  
    if Dificultad!=2:
        print(f"La palabra secreta era: {secret_word}")
    else:
        print(f"La palabra secreta era: {inicio+secret_word+fin}")

### Made in argentina



