gol = int(input("Podaj liczbę zdobytych bramek: "))
bonus = int(input("Podaj liczbę dodatkowych punktów bonusowych: "))

wynik = gol * 10

if gol > 10:
    wynik += 10
if gol > 5:
    wynik += 5

wynik += bonus

print("Całkowity wynik drużyny: ", wynik)