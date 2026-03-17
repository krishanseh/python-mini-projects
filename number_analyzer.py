largest = None 
smallest = None
summe = 0
anzahl = 0

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    num = float(num)
# Maximum prüfen
    if largest is None or num > largest :
        largest = num
# Minimum prüfen
    if smallest is None or num < smallest :
        smallest = num
# Summe und Anzahl aktualisieren
    summe += num
    anzahl += 1

# Durchschnitt berechen
durchschnitt = summe / anzahl
print("Maximum is", largest)
print("Minimum is", smallest)
print("Average is", durchschnitt)
