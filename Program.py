from random import randint

class Bestellung:
    def __init__(self, pBestellnummer, pTisch, pGericht):
        self.bestellnummer = pBestellnummer
        self.tisch = pTisch
        self.gericht = pGericht

zubereitungsschlange = []
servierschlange = []
alleBestellungen = []

# Kontrollvariable zum Beenden des
# Programms
programmRunning = True

while programmRunning:
    action = input("Was wollen Sie tun? Bestellung [A]nlegen, [Z]ubereitungsliste anzeigen, Gericht [F]ertig, [S]ervierliste anzeigen, Gericht ser[V]ieren, [R]echnung oder [B]eenden? ").upper()
    if action not in "AZBFSVR" or len(action) != 1:
        print("Keine Ahnung, was Sie tun wollen.")
        continue
    # Buch anlegen
    if action == 'A':
        bestellnummer = randint(1,1000000)
        tischnummer = input("Bitte Tischnummer eingeben: ")
        gericht = input("Bitte Gericht eingeben: ")
        neueBestellung = Bestellung(bestellnummer, tischnummer, gericht)
        zubereitungsschlange.append(neueBestellung)
        alleBestellungen.append(neueBestellung)
    elif action == 'Z':
        for sBestellung in zubereitungsschlange:
            print(str(sBestellung.bestellnummer) +" "+ str(sBestellung.tisch) + " " + sBestellung.gericht)
    elif action == 'F':
        bestellung = zubereitungsschlange.pop(0)
        servierschlange.append(bestellung)
    elif action == 'S':
        for sBestellung in servierschlange:
            print(str(sBestellung.bestellnummer) +" "+ str(sBestellung.tisch) + " " + sBestellung.gericht)
    elif action == 'V':
        servierschlange.pop(0)
    elif action == 'R':
        tisch = input("Für welchen Tisch soll die Rechnung erstellt werden? ")
        offeneBestellungen = False
        # Check Zubereitungsschlange

        # Check Servierschlange

        if offeneBestellungen == False:
            # Rechnung erstellen
            continue
    elif action == 'B':
        programmRunning = False
