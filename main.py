pocetLodi = 0
pocetStrel = 0
more2 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
while pocetLodi < 3:
    for i in more2:  # fory na vypis
        for j in i:
            if j == 3:
                print(0, end=" ")
            else:
                print(j, end=" ")
        print()
    x = input()
    y = input()
    if more2[int(x)][int(y)] == 3:
        more2[int(x)][int(y)] = 1
        pocetLodi += 1
        pocetStrel += 1
        print("Střelená loď")
    elif more2[int(x)][int(y)] == 0:
        pocetStrel += 1
        print("Trefená voda")
    elif more2[int(x)][int(y)] == 1 or 3:
        pocetStrel += 1
        print("Sem si již střílel")
print("Sestřelil jsi všechny lodě, zde máš staty: počet střel: " + str(pocetStrel) + ", Počet lodí: " + str(pocetLodi))
