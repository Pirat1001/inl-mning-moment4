
# Frågar användaren om hens längd på rektangelns sidor som jag sedan använder i mina uträkningar
sido_Q1 = int(input("Ange längden på ena sidan av din rektangel: "))

sido_Q2 = int(input("Ange längden på den andra sidan av din rektangel: "))

#Här använder jag de inmatade värden av användaren till att beräkna arean på rektangeln
area = sido_Q2 * sido_Q1

#Utskrift som berättar triangelns sidor och vad arean är
print(f"Rektangeln har sidorna {sido_Q1} och {sido_Q2} vilket ger arean {area}")

#Skapar en if sats som kollar efter ifall sidorna är likadana, ifall de är det får användaren utskrivet att rektangeln är en triangel
if sido_Q1 == sido_Q2:
    print("Eftersom båda sidorna är lika långa är rektangeln en kvadrat")

#Skapar en variabel volym_tabell som innehåller en block f-sträng som jag sedan skriver ut
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

print(volym_tabell)
