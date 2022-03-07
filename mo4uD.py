

# Skriver ut vad programmet gör och vad den har för funktion
from glob import escape


print("Programmet finns för att du ska kunna lätt beräkna arean på rektanglar \n för att stoppa programmet mata in 'Q'")
# Skapar en tom lista som ska hålla på värden som användaren matar in 
rektangel_värden = []
rektangel_dimensioner = []

# Skapar en while loop som gäller så länge det är sant
while True:
    # Först ställs frågan ifall man vill utföra en beräkning, man kan svara antingen j eller n 
    Q_1 = input("Vill du göra en beräkning? skriv 'J'(ja) eller 'N'(nej)")
    Q_1 = Q_1.lower()
    # Ifall svaret är j kommer följande två frågor att ställas, alltså längden på rektangelns två sidor
    if Q_1 == "j":
        # Även här använder jag mig av listor iställer för variabler
        sida_Q1 = int(input("Ange längden på den första sidan: "))
        rektangel_dimensioner.append(sida_Q1)
        sida_Q2 = int(input("Ange längden på rektangelns andra sida: "))
        rektangel_dimensioner.append(sida_Q2)
        # Arean räknas ut genom att använda svaret på frågan alltså arean för rektangeln är sida * sida
        area = rektangel_dimensioner[0] * rektangel_dimensioner[1]

        # Skapar en variabel som håller på en f string därefter skriver ut f stringen och berättar arean och vilka sidorna rektangeln har
        rektangel_length = f"Din rektangel har sidorna {rektangel_dimensioner[0]} och {rektangel_dimensioner[1]} vilket ger arean {area}"
        print(rektangel_length)
        # Här skickar jag f stringen till den tomma listan "rektangel_värden" som jag sedan skriver ut ifall användaren inte vill utföra någon fler beräkning
        rektangel_värden.append(rektangel_length)

        # Skapar en till input som frågar efter vilken höjd användaren vill kolla igenom 
        rektangel_höjd = int(input("Skriv in rektangelns höjd"))
        rektangel_dimensioner.append(rektangel_höjd)
        # Skriver ut början på tabellen för att annars skulle det skrivas ut för varje x i for loopen
        print("          Höjd   |   Volym   ")

        # SKapar ett antal if satser som kollar igenom flera villkor ifall höjden är större än 10 eller mindre än 1 ifall det är det ändrar det värdet till det närmsta 1 eller 10 
        # jag ändrar användning av variabler, iställer använder jag mig av listan rektangel_dimensioner och de specifika indexen för specifika dimensioner
        if rektangel_dimensioner[-1] > 10: 
            rektangel_dimensioner[-1] = 10
        elif rektangel_dimensioner[-1] < 1:
            rektangel_dimensioner[-1] = 1
        # Här skapar jag elif-satsen som utför hela utskriften alltså den kommer att skriva ut varje höjd från 1 till den inmatade höjden 
        elif rektangel_dimensioner[-1] >= 1 or rektangel_dimensioner[-1] == 10:
            # for loop som tittar igenom varje värde, eftersom jag vill ha en intigere behöver jag även mata in en tredje range alltså hur många steg alltså 1 dessutom skriver jag fram till rektangel_höjd + 1 eftersom den indexen som det skrivet ut fram till skrivs annars inte ut
            for x in range (1,rektangel_dimensioner[-1] + 1,1):
                volym = f"""            {x}    |     {area*x}   """ # här skapar jag endast strukturen inuti en f string
                print(volym)

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

    