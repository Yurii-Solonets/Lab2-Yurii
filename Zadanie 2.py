x = float(input("Wpisz x: "))
y = float(input("Wpisz y: "))
z = float(input("Wpisz z: "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print(f"Liczby w kolejności rosnącej: {x}, {y}, {z}")