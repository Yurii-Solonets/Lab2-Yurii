with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia, end = '')
    with open("notowania_gieldowe.txt", "a") as plik:
        plik.write("\n ALR, 113")