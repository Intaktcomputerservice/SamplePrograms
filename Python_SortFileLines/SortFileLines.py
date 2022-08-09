# Nutzung: python SortFileLines.py < inputTest.py
# Man könnte das auch lösen, indem man eine Datei direkt ausliest.
# Vielleicht ist das eine gute Übung, herauszufinden, was man ändern muss,
# damit direkt aus der Datei gelesen werden kann...

import sys

# Lese Eingabe aus Kommandozeile
text = sys.stdin.read()

# Spalte gelesene Eingabe in Zeilen
lines = text.splitlines()

# Sortiere (das ist wohl der einfachste Sortieralgorithmus)... (Komplexität: O = n^2)
for i in range(len(lines)):
    for j in range(len(lines)):
        if lines[i] < lines[j]:
            tmp = lines[i]
            lines[i] = lines[j]
            lines[j] = tmp

# Gebe jede Zeile in der Kommandozeile aus
for line in lines:
    print(line)