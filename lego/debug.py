def finde_kanten(a,kanten):
    kanten=[1,3,5,7]
    weisse_kanten=[]
    for i in range (6):
        for l in kanten:
            if a[i][l]==a[0][4]:
                weisse_kanten.append([i,l])
    
    return weisse_kanten
tuplets={
    (0,1):(1,7),
    (0,3):(5,3),
    (0,5):(4,3),
    (0,7):(3,1),
    
    (1,1):(2,7),
    (1,3):(5,7),
    (1,5):(4,1),
    (1,7):(0,1),

    (2,1):(3,7),
    (2,3):(5,5),
    (2,5):(4,5),
    (2,7):(1,1),

    (3,1):(0,7),
    (3,3):(5,1),
    (3,5):(4,7),
    (3,7):(2,1),

    (4,1):(1,5),
    (4,3):(0,5),
    (4,5):(2,5),
    (4,7):(3,5),
    
    (5,1):(3,3),
    (5,3):(0,3),
    (5,5):(2,3),
    (5,7):(1,3),
}
l_tuplets=[
    ((0, 1), (1, 7)), ((0, 3), (5, 3)), ((0, 5), (4, 3)), ((0, 7), (3, 1)),
    ((1, 1), (2, 7)), ((1, 3), (5, 7)), ((1, 5), (4, 1)), ((1, 7), (0, 1)),
    ((2, 1), (3, 7)), ((2, 3), (5, 5)), ((2, 5), (4, 5)), ((2, 7), (1, 1)),
    ((3, 1), (0, 7)), ((3, 3), (5, 1)), ((3, 5), (4, 7)), ((3, 7), (2, 1)),
    ((4, 1), (1, 5)), ((4, 3), (0, 5)), ((4, 5), (2, 5)), ((4, 7), (3, 5)),
    ((5, 1), (3, 3)), ((5, 3), (0, 3)), ((5, 5), (2, 3)), ((5, 7), (1, 3))
]
def cross(x):
    kanten = finde_kanten(x)
    kanten_cross = []
    for i in kanten:
        k = tuple(i)
        if k in tuplets:
            sub = tuplets[k]
            kanten_cross.append((k, sub))
    print(kanten_cross)
    return kanten_cross
def kreuz(x):
    kanten = cross(x)
    moves = []

    if not kanten:
        return moves  # keine passenden weißen Kanten gefunden

    kante = kanten[0]  # nur die erste Kante betrachten
    temp = [row[:] for row in x]  # Kopie vom Würfelzustand

    
    
    if temp[kante[0][0]][kante[0][1]] == temp[0][4]:  # weiße Seite passt
        if temp[kante[1][0]][kante[1][1]] == temp[kante[1][0]][4]:  # Seite stimmt auch
            return moves
        for i in range(3):
            if temp[kante[1][0]][kante[1][1]] == temp[kante[1][0]][4]:  # Seite stimmt auch
                return moves
            temp = F(temp)
            moves.append('F')
    if temp[kante[0][0]][kante[0][1]] == temp[0][4]:
        ...
    kante=kanten[1]
    if temp[kante[0][0]][kante[0][1]] == temp[0][4]:  # weiße Seite passt
            if temp[kante[1][0]][kante[1][1]] == temp[kante[1][0]][4]:
                return moves
            
    return moves



def kreuz_V2(x):
    kanten = cross(x)
    Ziel = [None, None, None, None]
    moves = []
    counter = 0

    # Ziel-Kanten identifizieren
    for kante in kanten:
        if x[kante[1][0]][kante[1][1]] == x[1][4]:
            Ziel[0] = kante
        elif x[kante[1][0]][kante[1][1]] == x[3][4]:
            Ziel[1] = kante
        elif x[kante[1][0]][kante[1][1]] == x[4][4]:
            Ziel[2] = kante
        elif x[kante[1][0]][kante[1][1]] == x[5][4]:
            Ziel[3] = kante

    # Kanten verarbeiten
    for kante in Ziel:
        if kante is None:
            continue
        if x[kante[1][0]][kante[1][1]] == x[kante[1][0]][4]:
            continue  # passt schon

        if kante == ((0, 3), (5, 3)):
            moves.append('F')
            counter += 1
            continue
        elif kante == ((5, 3), (0, 3)):
            moves.extend(['Rr', 'Dr'])
            counter += 1
            continue
        elif kante == ((0, 5), (4, 3)):
            moves.append('Fr')
            counter += 1
            continue
        elif kante == ((4, 3), (0, 5)):
            moves.extend(['L', 'D'])
            counter += 1
            continue
        elif kante == ((0, 7), (3, 1)):
            moves.extend(['F', 'F'])
            counter += 1
            continue
        elif kante == ((3, 1), (0, 7)):
            moves.extend(['U', 'L', 'L', 'L'])
            counter += 1
            continue
        elif kante == ((1, 3), (5, 7)):
            moves.append('D')
            counter += 1
            continue
        elif kante == ((5, 7), (1, 3)):
            moves.extend(['R', 'F'])
            counter += 1
            continue
        elif kante == ((1, 5), (4, 1)):
            moves.extend(['Lr', 'Fr'])
            counter += 1
            continue
        elif kante == ((4, 1), (1, 5)):
            moves.append('D')
            counter += 1
            continue
        elif kante == ((), ()):
            continue

    return moves

            
    