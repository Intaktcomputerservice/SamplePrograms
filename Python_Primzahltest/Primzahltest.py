# Eine Primzahl ist eine Zahl, die nur durch sich selbst und durch eins Teilbar ist
#
# Dieses Programm nimmt eine Zahl als Kommandozeilenargument entgegen und prüft,
# auf zwei Arten, ob essich um eine Primzahl handelt

# Importieren der Library, um Kommandozeilenparameter auslesen zu können
from array import array
import sys

# Auslesen des Kommandozeilenarguments und Abfangen möglicher Fehler
try:
    maybePrime = int(sys.argv[1]);
# Falls es kein Element mit Index 1 in der Liste sys.argv gibt:
except IndexError:
    print("You have to pass one number as argument!")
# Falls jemand eine Zeichenkette oder Kommazahl eingibt:
except ValueError:
    print("Your argument must be an integer value!")

# 1: Iterativer Ansatz (mit Schleife)
# Hier wird eine Funktion deklariert, um sie unten übersichtlich aufrufen zu
# können
def checkPrimeIterative(checkNumber):
    # Da es auch negative Primzahlen gibt, müssen auch diese überprüft werden
    # Überprüfen, ob checkNumber negativ ist:
    if checkNumber < 0:
        # Wenn negativ, dann mache eine positive Zahl daraus (positive und
        # negative Zahlen können gleich behandelt werden).
        # Da beim Teilen durch -1 eine Kommazahl vom Python-Interpreter
        # generiert wird, sagen wir ihm mit int(), dass wir eine Ganzzahl
        # brauchen
        checkNumber = int(checkNumber / -1)

    # Überprüfe, ob checkNumber kleiner ist als zwei. Die eins ist keine
    # Primzahl!
    if checkNumber < 2:
        return False

    # range(2, checkNumber) erstellt eineListe von 2 bis checkNumber-1 und i 
    # wird bei jedem Schleifendurchlauf aus dieser Liste genommen, bis das
    # Ende der Liste erreicht wurde
    for i in range(2, checkNumber):
        # % ist der Modulus-Operator. Dieser gibt den Rest einer Division zurück.
        # Wenn checkNumber durch irgendwas außer eins und sich selbst restlos
        # teilbar ist - also durch i -, ist checkNumber keine Primzahl
        if checkNumber % i == 0:
            return False

    # Alle Zahlen, die keine Teiler außer eins und sich selbst haben, sorgen dafür,
    # dass das Programm bis hier unten ausgeführt wird
    return True

# 2: Rekursiver Ansatz (die Funktion ruft sich selbst immer wieder auf)
# Hier wird eine Funktion deklariert, um sie unten übersichtlich aufrufen zu
# können.
# divisor ist eine Hilfsvariable
def checkPrimeRecursive(checkNumber, divisor = None):
    # Wenn eingegebene Zahl neagtiv ist, mache sie positiv
    if checkNumber < 0:
        return checkPrimeRecursive(int(checkNumber / -1))
    # Wenn divisor nicht gesetzt ist (beim ersten Aufruf unten), setze es
    # auf die zu testende Zahl minus eins
    elif divisor == None:
        return checkPrimeRecursive(checkNumber, checkNumber - 1)
    # Wenn divisor größer als eins ist (die Eins soll ja nicht getestet werden,
    # weil sie Teiler von jeder Zahl ist) und der divisor kein Teiler von
    # checkNumber ist, wiederhole die Funktion mit dem nächstkleineren
    # möglichen Teiler
    elif divisor > 1 and checkNumber % divisor != 0:
        return checkPrimeRecursive(checkNumber, divisor - 1)
    # Wenn alle Teiler, die größer als eins sind getestet wurden, muss checkNumber
    # eine Primzahl sein
    elif divisor == 1:
        return True
    # Wenn keine Bedingung zutrifft, ist checkNumber keine Primzahl
    else:
        return False

# Man kann die zweite Funktion auch deutlich kürzer fassen, was den Quelltext
# aber auch sehr unverständlich macht:
def checkPrimeRecursive2(checkNumber, divisor = -1):
    if checkNumber == 0: return False
    return (
        checkNumber < 0 and checkPrimeRecursive2(int(checkNumber / -1))
        or divisor == -1 and checkPrimeRecursive2(checkNumber, checkNumber - 1)
        or divisor > 1 and checkNumber % divisor != 0 and checkPrimeRecursive2(checkNumber, divisor - 1)
        or divisor == 1
    )
        

# Boilerplate-Code. Lese https://stackoverflow.com/a/419185, um zu erfahren, wofür if __name__... steht
if __name__ == "__main__":
    if checkPrimeIterative(maybePrime):
        print("Iterative:  " + str(maybePrime) + " is a prime number")
    else:
        print("Iterative:  " + str(maybePrime) + " is not a prime number")

    if checkPrimeRecursive(maybePrime):
        print("Recursive:  " + str(maybePrime) + " is a prime number")
    else:
        print("Recursive:  " + str(maybePrime) + " is not a prime number")
    
    if checkPrimeRecursive2(maybePrime):
        print("Recursive2: " + str(maybePrime) + " is a prime number")
    else:
        print("Recursive2: " + str(maybePrime) + " is not a prime number")