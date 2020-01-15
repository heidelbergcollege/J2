from random import randint

class Bestellung:
    def __init__(self, pBestellnummer, pTisch, pGericht):
        self.bestellnummer = pBestellnummer
        self.tisch = pTisch
        self.gericht = pGericht

zubereitungsschlange = []

# Kontrollvariable zum Beenden des
# Programms
programmRunning = True

while programmRunning:
    action = input("Was wollen Sie tun? Bestellung [A]nlegen, [Z]ubereitungsliste anzeigen oder [B]eenden? ").upper()
    if action not in "AZB" or len(action) != 1:
        print("Keine Ahnung, was Sie tun wollen.")
        continue
    # Buch anlegen
    if action == 'A':
        bestellnummer = randint(1,1000000)
        tischnummer = input("Bitte Tischnummer eingeben: ")
        gericht = input("Bitte Gericht eingeben: ")
        neueBestellung = Bestellung(bestellnummer, tischnummer, gericht)
        zubereitungsschlange.append(neueBestellung)
    elif action == 'Z':
        for sBestellung in zubereitungsschlange:
            print(str(sBestellung.bestellnummer) +" "+ str(sBestellung.tisch) + " " + sBestellung.gericht)
    elif action == 'B':
        programmRunning = False
