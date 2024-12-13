# Python Cheatsheet

## Grundlegende Datentypen

### Zahlen
```python
# Integer (Ganzzahlen)
x = 5
y = -17
großezahl = 1_000_000  # Unterstriche für bessere Lesbarkeit

# Float (Gleitkommazahlen)
pi = 3.14159
wissenschaftlich = 2.5e-4  # 0.00025

# Komplexe Zahlen
c = 3 + 4j
```

### Strings
```python
# String-Erstellung
text = "Hallo Welt"
mehrzeilig = """Dies ist ein
mehrzeiliger String"""

# String-Operationen
name = "Python"
print(name[0])      # Erstes Zeichen: 'P'
print(name[-1])     # Letztes Zeichen: 'n'
print(name[0:2])    # Slice: 'Py'
print(len(name))    # Länge: 6

# String-Formatierung
name = "Max"
alter = 25
# f-Strings (modern, empfohlen)
ausgabe = f"{name} ist {alter} Jahre alt"
# .format() Methode
ausgabe = "{} ist {} Jahre alt".format(name, alter)
```

### Listen
```python
# Listen-Erstellung
zahlen = [1, 2, 3, 4, 5]
gemischt = [1, "text", 3.14, [1, 2]]

# Listen-Operationen
zahlen.append(6)        # Am Ende hinzufügen
zahlen.insert(0, 0)    # An Position einfügen
zahlen.extend([7, 8])  # Liste erweitern
zahlen.remove(1)       # Element entfernen
erster = zahlen.pop(0) # Element entfernen und zurückgeben

# List Comprehension
quadrate = [x**2 for x in range(10)]
gerade = [x for x in range(10) if x % 2 == 0]
```

### Dictionaries
```python
# Dictionary-Erstellung
person = {
    "name": "Max",
    "alter": 25,
    "stadt": "Berlin"
}

# Zugriff und Modifikation
name = person["name"]           # Direkter Zugriff
alter = person.get("alter")     # Sicherer Zugriff
person["beruf"] = "Entwickler"  # Neuer Eintrag
del person["stadt"]            # Eintrag löschen

# Dictionary Comprehension
quadrate = {x: x**2 for x in range(5)}
```

### Sets
```python
# Set-Erstellung
zahlen = {1, 2, 3, 4, 5}
unique = set([1, 2, 2, 3, 3, 4])  # Duplikate werden entfernt

# Set-Operationen
zahlen.add(6)           # Element hinzufügen
zahlen.remove(1)        # Element entfernen
zahlen.discard(10)      # Entfernt Element, wenn vorhanden

# Set-Mathematik
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b          # Vereinigung
schnitt = a & b        # Schnittmenge
differenz = a - b      # Differenz
```

## Kontrollstrukturen

### If-Anweisungen
```python
# Grundlegende if-Struktur
if bedingung:
    # Code
elif andere_bedingung:
    # Code
else:
    # Code

# Ternärer Operator
ergebnis = "ja" if bedingung else "nein"
```

### Schleifen
```python
# For-Schleife
for i in range(5):
    print(i)

# For mit enumerate
for index, wert in enumerate(liste):
    print(f"Index {index}: {wert}")

# While-Schleife
while bedingung:
    # Code
    if abbruch_bedingung:
        break
    if überspringen:
        continue
```

## Funktionen

### Funktionsdefinitionen
```python
# Einfache Funktion
def grüße(name):
    return f"Hallo {name}!"

# Funktion mit Standardwerten
def addiere(a, b=0):
    return a + b

# Funktion mit variabler Argumentanzahl
def summe(*args):
    return sum(args)

# Funktion mit Keyword-Argumenten
def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### Lambda-Funktionen
```python
quadrat = lambda x: x**2
summe = lambda a, b: a + b
```

## Fehlerbehandlung

```python
try:
    # Risikobehafteter Code
    ergebnis = 10 / 0
except ZeroDivisionError:
    # Behandlung spezifischer Fehler
    print("Division durch Null!")
except Exception as e:
    # Allgemeine Fehlerbehandlung
    print(f"Fehler: {e}")
else:
    # Code bei erfolgreicher Ausführung
    print("Erfolgreich!")
finally:
    # Wird immer ausgeführt
    print("Aufräumen...")
```

## Klassen und Objektorientierung

```python
class Person:
    # Klassenattribut
    species = "Homo Sapiens"
    
    # Konstruktor
    def __init__(self, name, alter):
        # Instanzattribute
        self.name = name
        self.alter = alter
    
    # Methode
    def vorstellen(self):
        return f"Ich bin {self.name}, {self.alter} Jahre alt."
    
    # Statische Methode
    @staticmethod
    def ist_erwachsen(alter):
        return alter >= 18
    
    # Klassenmethode
    @classmethod
    def von_geburtsjahr(cls, name, geburtsjahr):
        alter = 2024 - geburtsjahr
        return cls(name, alter)
```

## Module und Pakete

```python
# Modul importieren
import math

# Spezifische Funktionen importieren
from datetime import datetime, timedelta

# Alias verwenden
import numpy as np

# Alle Funktionen importieren (nicht empfohlen)
from math import *
```

## Dateioperationen

```python
# Datei lesen
with open('datei.txt', 'r') as f:
    inhalt = f.read()
    zeilen = f.readlines()

# Datei schreiben
with open('ausgabe.txt', 'w') as f:
    f.write('Hallo Welt')

# CSV-Dateien
import csv
with open('daten.csv', 'r') as f:
    reader = csv.reader(f)
    for zeile in reader:
        print(zeile)
```

## Nützliche Eingebaute Funktionen

```python
# Listen-Operationen
länge = len(liste)
maximum = max(liste)
minimum = min(liste)
summe = sum(liste)
sortiert = sorted(liste, reverse=True)

# Typ-Konvertierung
string = str(42)
ganzzahl = int("42")
gleitkomma = float("3.14")

# Sequenz-Funktionen
aufzählung = list(range(10))
reißverschluss = list(zip([1, 2, 3], ['a', 'b', 'c']))
gefiltert = list(filter(lambda x: x > 0, liste))
transformiert = list(map(lambda x: x**2, liste))
```

## Best Practices

1. **PEP 8 Style Guide**
   - 4 Leerzeichen für Einrückung
   - Maximal 79 Zeichen pro Zeile
   - Leerzeilen zwischen Funktionen und Klassen
   - Snake_case für Funktionen und Variablen
   - PascalCase für Klassen

2. **Dokumentation**
   - Docstrings für Module, Klassen und Funktionen
   - Inline-Kommentare für komplexe Logik
   - Aussagekräftige Variablennamen

3. **Fehlerbehandlung**
   - Spezifische Exceptions fangen
   - Context Manager (with) für Ressourcen
   - Logging statt print für Debugging

4. **Performance**
   - List Comprehensions statt Schleifen wo möglich
   - Generator-Expressions für große Datensätze
   - Vermeidung globaler Variablen
