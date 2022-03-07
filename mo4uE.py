
# Skapar inputs för att användaren ska mata in dimensionerna för sin rektangel
Q1 = int(input("Skriv in första sidan på din rektangel:"))
Q2 = int(input("Skriv in andra sidan på din rektangel:"))
Q3 = int(input("Skriv in rektangelns höjd:"))

#Här skapar jag de olika funktionerna för att räkna ut olika saker som t.ex. area med de inmatade värden 
def omkrets(a,b):
    O = (a*a)+(b*b)
    return O

def area(a,b):
    A = a*b
    return A

def volym(a,b,c):
    V = a*b*c
    return V

#Skapar en while loop som är evig så länge man inte skriver in break för att man ska kunna räkna ut flera grejer utan att behöva starta programmet varje gång
while True:
    # Ställer frågan på vad som användaren vill räkna ut 
    Q4 = input("Vad vill du räkna ut volym, area eller omkrets? Du kan stänga programmet genom att skriva in 'quit'")
    Q4 = Q4.lower()

    # Skapar if satserna för fråga 4 för att använda specifik funktion 
    if Q4 == "area":
        # Då användaren skriver in area på fråga 4 kommer följande att skrivas ut, i f-stringen använder jag mig av funktionen för area och jag använder mig av sidorna på rektangeln i Q1 och Q2
        print(f"Du räknar ut arean av sidorna {Q1}cm och {Q2}cm, arean = {area(Q1,Q2)} cm^2")
    # Annars om användaren svarar 'omkrets' på Q4 kommer följande att hända:
    elif Q4 == "omkrets":
        # f-string som räknar ut omkretsen genom att använda sidorna som användaren har matat in i början av programmet och använder funktionen för omkrets i utskriften
        print(f"Du räknar ut omkretsen på rektangeln med sidorna {Q1}cm och {Q2}cm, omkrets = {omkrets(Q1,Q2)}cm")
    #annars om användaren svarar 'volym' på Q4 kommer följande att hända: 
    elif Q4 == "volym":
        # f-string som skriver ut alla tre inmatade dimensioner alltså båda sidorna och höjden på rektangeln, därefter använder volym funktionen för att multiplicera alla värden med varandra
        print(f"Du räknar ut volymen på rektangeln med sidorna {Q1}cm, {Q2}cm och höjden {Q3}cm, volymen = {volym(Q1,Q2,Q3)}cm^3")
    # Annars om svaren på frågan Q4 = quit:
    elif Q4 == "quit":
        # quit används för att stänga programmet, då man är klar med sina beräkningar, break används för att stoppa while loopen och på så sätt stoppa programmet
        print("Programmen stängs av...")
        break
    # else sats för att skriva ut följande ifall svaret på Q4 inte är någon av de ovan
    else:
        print("Det verkar inte finnas sådan möjlighet...")