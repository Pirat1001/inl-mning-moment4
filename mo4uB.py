
# Skriver ut vad programmet gör och vad den har för funktion
from glob import escape


print("Programmet finns för att du ska kunna lätt beräkna arean på rektanglar \n för att stoppa programmet mata in 'Q'")
# Skapar en tom lista som ska hålla på värden som användaren matar in 
rektangel_värden = []

# Skapar en while loop som gäller så länge det är sant
while True:
    # Först ställs frågan ifall man vill utföra en beräkning, man kan svara antingen j eller n 
    Q_1 = input("Vill du göra en beräkning? skriv 'J'(ja) eller 'N'(nej)")
    Q_1 = Q_1.lower()
    # Ifall svaret är j kommer följande två frågor att ställas, alltså längden på rektangelns två sidor
    if Q_1 == "j":
        sida_Q1 = int(input("Ange längden på den första sidan: "))
        sida_Q2 = int(input("Ange längden på rektangelns andra sida: "))
        # Arean räknas ut genom att använda svaret på frågan alltså arean för rektangeln är sida * sida
        area = sida_Q2 * sida_Q1

        # Skapar en variabel som håller på en f string därefter skriver ut f stringen och berättar arean och vilka sidorna rektangeln har
        rektangel_length = f"Din rektangel har sidorna {sida_Q1} och {sida_Q2} vilket ger arean {area}"
        print(rektangel_length)
        # Här skickar jag f stringen till den tomma listan "rektangel_värden" som jag sedan skriver ut ifall användaren inte vill utföra någon fler beräkning
        rektangel_värden.append(rektangel_length)

        # skapar en variabel där återigen en f string är värdet, i form av en tabell alltså block sträng som berättar vilka exempel volym skulle rektangeln kunna ha vid exempel höjd
        volym_tabell = f"""
              Höjd    |    Volym   
                1     |     {area*1}
                2     |     {area*2}
                3     |     {area*3}
                4     |     {area*4}
                5     |     {area*5}
                6     |     {area*6}
                7     |     {area*7}
                8     |     {area*8}
                9     |     {area*9}
                10    |     {area*10}   """
        # här skriver jag ut tabellen
        print(volym_tabell) 
    # Skapar en elif sats alltså ifall svaret inte är j kollar programmet ifall svaret är n, om det är de kommer följande att hända:
    elif Q_1 == "n":
        # Skriver ut att användaren inte vill utföra några fler beräkningar
        print("Du ville inte utföra några fler beräkningar")
        #skapar en for loop som loopar igenom listan och skriver ut meningen
        for rektangel in rektangel_värden:
            print(rektangel)
        break
    # här finns även en if sats om vad som händer ifall användaren skriver in något värde som inte finns tillgängligt som svar
    else:
        #Ifall sånt händer skriver den ut att man har endast två möjligheter som svar och ställer frågan igen
        print("Du måste välja en av möjligheterna (J/N)")
