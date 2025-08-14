def finde_kanten(a):
    kanten=[1,3,5,7]
    weisse_kanten=[]
    for i in range (6):
        for l in kanten:
            if a[i][l]==a[0][4]:
                weisse_kanten.append([i,l])
    
    return weisse_kanten
tuplets={
    (0,1):(1,7),
    (0,3):(5,5),
    (0,5):(4,5),
    (0,7):(3,1),
    
    (1,1):(2,7),
    (1,3):(5,1),
    (1,5):(4,7),
    (1,7):(0,1),

    (2,1):(3,7),
    (2,3):(5,3),
    (2,5):(4,3),
    (2,7):(1,1),

    (3,1):(0,7),
    (3,3):(5,7),
    (3,5):(4,1),
    (3,7):(2,1),

    (4,1):(3,5),
    (4,3):(2,5),
    (4,5):(0,5),
    (4,7):(1,5),
    
    (5,1):(1,3),
    (5,3):(2,3),
    (5,5):(0,3),
    (5,7):(3,3),
}
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
l_tuplets=[
    ((0, 1), (1, 7)), ((0, 3), (5, 3)), ((0, 5), (4, 3)), ((0, 7), (3, 1)),
    ((1, 1), (2, 7)), ((1, 3), (5, 7)), ((1, 5), (4, 1)), ((1, 7), (0, 1)),
    ((2, 1), (3, 7)), ((2, 3), (5, 5)), ((2, 5), (4, 5)), ((2, 7), (1, 1)),
    ((3, 1), (0, 7)), ((3, 3), (5, 1)), ((3, 5), (4, 7)), ((3, 7), (2, 1)),
    ((4, 1), (1, 5)), ((4, 3), (0, 5)), ((4, 5), (2, 5)), ((4, 7), (3, 5)),
    ((5, 1), (3, 3)), ((5, 3), (0, 3)), ((5, 5), (2, 3)), ((5, 7), (1, 3))
]

def R(y):
    x=5
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[0][0],y[0][3],y[0][6],  y[1][0],y[1][3],y[1][6], y[2][0],y[2][3],y[2][6], y[3][0],y[3][3],y[3][6]  =y[1][0],y[1][3],y[1][6],y[2][0],y[2][3],y[2][6],y[3][0],y[3][3],y[3][6],y[0][0],y[0][3],y[0][6],
    
    return y
def L(y):
    x=4
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[0][2],y[0][5],y[0][8],  y[1][2],y[1][5],y[1][8], y[2][2],y[2][5],y[2][8], y[3][2],y[3][5],y[3][8]  =  y[3][2],y[3][5],y[3][8], y[0][2],y[0][5],y[0][8],y[1][2],y[1][5],y[1][8], y[2][2],y[2][5],y[2][8], 
   
    return y
def F(y):
    S1=1
    S2=5
    S3=3
    S4=4
    x=0
    y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][5], y[S2][2],     y[S3][2], y[S3][1], y[S3][0],     y[S4][8], y[S4][5], y[S4][2], y[x][0],y[x][1],y[x][2],y[x][3],y[x][5],y[x][6],  y[x][7],  y[x][8]  =         y[S2][8], y[S2][5], y[S2][2],     y[S3][2], y[S3][1], y[S3][0],     y[S4][8], y[S4][5], y[S4][2],y[S1][6], y[S1][7],y[S1][8],  y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    
    return y

def B(y):
    S1=1
    S2=5
    S3=3
    S4=4
    x=2
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[S1][0], y[S1][1],y[S1][2],     y[S2][6], y[S2][3], y[S2][0],     y[S3][6], y[S3][7], y[S3][8],     y[S4][6], y[S4][3], y[S4][0]  =     y[S4][6], y[S4][3], y[S4][0]  , y[S1][6], y[S1][7],y[S1][8],     y[S2][6], y[S2][3], y[S2][0],     y[S3][0], y[S3][1], y[S3][2],       
    
    return y
def U(y):
    S1=0
    S2=4
    S3=2
    S4=5
    x=3
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[S1][6], y[S1][7],y[S1][8],     y[S2][0], y[S2][1], y[S2][2],     y[S3][0], y[S3][1], y[S3][2],     y[S4][0], y[S4][1], y[S4][2]  =     y[S4][0], y[S4][1], y[S4][2]     , y[S1][6], y[S1][7],y[S1][8],     y[S2][0], y[S2][1], y[S2][2],     y[S3][0], y[S3][1], y[S3][2],     
    
    return y
def D(y):
    S1=2
    S2=4
    S3=0
    S4=5
    x=1
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][7], y[S2][6],     y[S3][0], y[S3][1], y[S3][2],     y[S4][0], y[S4][1], y[S4][2]  =     y[S4][0], y[S4][1], y[S4][2]     , y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][7], y[S2][6],     y[S3][0], y[S3][1], y[S3][2],     
    
    return y

#inverted
def Rr(y):
    x=5
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]=y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]
    
    y[1][0],y[1][3],y[1][6],y[2][0],y[2][3],y[2][6],y[3][0],y[3][3],y[3][6],y[0][0],y[0][3],y[0][6],=y[0][0],y[0][3],y[0][6],  y[1][0],y[1][3],y[1][6], y[2][0],y[2][3],y[2][6], y[3][0],y[3][3],y[3][6]  
    
    return y
def Lr(y):
    x=4
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]=y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]
    y[3][2],y[3][5],y[3][8], y[0][2],y[0][5],y[0][8],y[1][2],y[1][5],y[1][8], y[2][2],y[2][5],y[2][8],=y[0][2],y[0][5],y[0][8],  y[1][2],y[1][5],y[1][8], y[2][2],y[2][5],y[2][8], y[3][2],y[3][5],y[3][8]   
   
    return y
def Fr(y):
    S1=1
    S2=5
    S3=3
    S4=4
    x=0
    y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]=y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]
    y[S2][8], y[S2][5], y[S2][2],     y[S3][2], y[S3][1], y[S3][0],     y[S4][8], y[S4][5], y[S4][2],y[S1][6], y[S1][7],y[S1][8],=y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][5], y[S2][2],     y[S3][2], y[S3][1], y[S3][0],     y[S4][8], y[S4][5], y[S4][2]  
    
    return y

def Br(y):
    S1=1
    S2=5
    S3=3
    S4=4
    x=2
    y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]=y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]
    y[S4][6], y[S4][3], y[S4][0]  , y[S1][6], y[S1][7],y[S1][8],     y[S2][6], y[S2][3], y[S2][0],     y[S3][0], y[S3][1], y[S3][2],=y[S1][0], y[S1][1],y[S1][2],     y[S2][6], y[S2][3], y[S2][0],     y[S3][6], y[S3][7], y[S3][8],     y[S4][6], y[S4][3], y[S4][0]         
    
    return y
def Ur(y):
    S1=0
    S2=4
    S3=2
    S4=5
    x=3
    y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]=y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]
    y[S4][0], y[S4][1], y[S4][2]     , y[S1][6], y[S1][7],y[S1][8],     y[S2][0], y[S2][1], y[S2][2],     y[S3][0], y[S3][1], y[S3][2],     =y[S1][6], y[S1][7],y[S1][8],     y[S2][0], y[S2][1], y[S2][2],     y[S3][0], y[S3][1], y[S3][2],     y[S4][0], y[S4][1], y[S4][2]
    
    return y
def Dr(y):
    S1=2
    S2=4
    S3=0
    S4=5
    x=1
    y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]=y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]
    y[S4][0], y[S4][1], y[S4][2]     , y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][7], y[S2][6],     y[S3][0], y[S3][1], y[S3][2],=y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][7], y[S2][6],     y[S3][0], y[S3][1], y[S3][2],     y[S4][0], y[S4][1], y[S4][2]       
    
    return y



# def kreuz(x):
#     kanten = cross(x)
#     moves = []
# 
#     if not kanten:
#         return moves  # keine passenden weißen Kanten gefunden
# 
#     kante = kanten[0]  # nur die erste Kante betrachten
#     temp = [row[:] for row in x]  # Kopie vom Würfelzustand
# 
#     
#     
#     if temp[kante[0][0]][kante[0][1]] == temp[0][4]:  # weiße Seite passt
#         if temp[kante[1][0]][kante[1][1]] == temp[kante[1][0]][4]:  # Seite stimmt auch
#             return moves
#         for i in range(3):
#             if temp[kante[1][0]][kante[1][1]] == temp[kante[1][0]][4]:  # Seite stimmt auch
#                 return moves
#             temp = F(temp)
#             moves.append('F')
#     if temp[kante[0][0]][kante[0][1]] == temp[0][4]:
#         ...
#     kante=kanten[1]
#     if temp[kante[0][0]][kante[0][1]] == temp[0][4]:  # weiße Seite passt
#             if temp[kante[1][0]][kante[1][1]] == temp[kante[1][0]][4]:
#                 return moves
#             
#     return moves


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
        if counter==0:
            if kante==((1,7),(0,1)):
                moves.extend(['D','R','F'])
                continue
            elif kante==((0,3),(5,3)):
                moves.append('F')
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
                moves.extend(['U', 'L',  'Fr'])
                counter += 1
                continue
            elif kante == ((1, 3), (5, 1)):
                moves.extend(['R', 'F'])
                counter += 1
                continue
            elif kante == ((5, 1), (1, 3)):
                moves.append('Dr')
                counter += 1
                continue
            elif kante == ((1, 5), (4, 7)):
                moves.extend(['Lr', 'Fr'])
                counter += 1
                continue
            elif kante == ((4,7), (1, 5)):
                moves.append('D')
                counter += 1
                continue
            elif kante == ((4,1), (3,5)):
                moves.extend(['Ur','F','F'])
                continue
            elif kante==((3,5),(4,1)):
                moves.extend(['L','Fr'])
                continue
            elif kante==((5,7),(3,3)):
                moves.extend(['U','F','F'])
                continue
            elif kante==((3,3),(5,7)):
                moves.extend(['Rr','F'])
                continue

            elif kante==((2,7),(1,1)):
                moves.extend(['D','D'])
                continue
            elif kante==((1,1),(2,7)):
                moves.extend(['Dr','R','Fr'])
                continue
            elif kante==((2,1),(3,7)):
                moves.extend(['U','U','F','F'])
                continue
            elif kante==((3,7),(2,1)):
                moves.extend(['U','Rr','F'])
                continue
            elif kante==((2,3),(5,3)):
               moves.extend(['R','R','F'])
               continue
            elif kante==((5,3),(2,3)):
               moves.extend(['R','Dr'])
               continue
            elif kante==((2,5),(4,3)):
               moves.extend(['L','L','Fr'])
               continue
            elif kante==((4,3),(2,5)):
               moves.extend(['Lr','D'])
               continue
        if counter ==1:
            
            if kante == ((5, 5), (0, 3)):
                moves.extend(['Rr', 'F','Dr','Fr'])
                counter += 1
                continue
            elif kante == ((0, 5), (4, 5)):
                moves.append('L','F','F','Lr','F','F')
                counter += 1
                continue
            elif kante == ((4, 5), (0, 5)):
                moves.extend(['L','F','D','Fr'])
                counter += 1
                continue
            elif kante == ((0, 7), (3, 1)):
                moves.extend(['D', 'F','Dr'])
                counter += 1
                continue
            elif kante == ((3, 1), (0, 7)):
                moves.extend(['Ur', 'Rr',])
                counter += 1
                continue

            elif kante == ((1, 3), (5, 1)):
                moves.append('R')
                counter += 1
                continue
            elif kante == ((5, 1), (1, 3)):
                moves.extend(['F', 'Dr','Fr'])
                counter += 1
                continue
            elif kante == ((1, 5), (4, 7)):
                moves.extend(['F', 'F','Lr','F','F'])
                counter += 1
                continue
            elif kante == ((4, 7), (1, 5)):
                moves.extend(['F','D','Fr'])
                counter += 1
                continue
            elif kante == ((4,1), (3,5)):
                moves.extend(['Fr','Ur','F'])
                continue
            elif kante==((3,5),(4,1)):
                moves.extend(['F','F','L','F','F'])
                continue
            elif kante==((5,7),(3,3)):
                moves.extend(['Fr','U','F'])
                continue
            elif kante==((3,3),(5,7)):
                moves.append('Rr')
                continue

            elif kante==((2,7),(1,1)):
                moves.extend(['B','R','R'])
                continue
            elif kante==((1,1),(2,7)):
                moves.extend(['F','Dr','Fr','R'])
                continue
            elif kante==((2,1),(3,7)):
                moves.extend(['Fr','U','U','F'])
                continue
            elif kante==((3,7),(2,1)):
                moves.extend(['U','Rr'])
                continue
            elif kante==((2,3),(5,3)):
               moves.extend(['R','R'])
               continue
            elif kante==((5,3),(2,3)):
               moves.extend(['R','F','Dr','Fr'])
               continue
            elif kante==((2,5),(4,3)):
               moves.extend(['B','B','R','R'])
               continue
            elif kante==((4,3),(2,5)):
               moves.extend(['Lr','F','D','Fr'])

               continue
        if counter ==2:
            
            
            if kante == ((4, 5), (0, 5)):
                moves.extend(['L','Fr','D','F'])
                counter += 1
                continue
            elif kante == ((0, 7), (3, 1)):
                moves.extend(['U', 'F','Ur','Fr'])
                counter += 1
                continue
            elif kante == ((3, 1), (0, 7)):
                moves.extend(['U', 'L',])
                counter += 1
                continue

            elif kante == ((1, 3), (5, 1)):
                moves.extend(['F','F','R','F','F'])
                counter += 1
                continue
            elif kante == ((5, 1), (1, 3)):
                moves.extend(['Fr', 'Dr','F'])
                counter += 1
                continue
            elif kante == ((1, 5), (4, 7)):
                moves.append('Lr')
                counter += 1
                continue
            elif kante == ((4, 7), (1, 5)):
                moves.extend(['Fr','D','F'])
                counter += 1
                continue
            elif kante == ((4,1), (3,5)):
                moves.extend(['F','Ur','Fr'])
                continue
            elif kante==((3,5),(4,1)):
                moves.append('L')
                continue
            elif kante==((5,7),(3,3)):
                moves.extend(['F','U','Fr'])
                continue
            elif kante==((3,3),(5,7)):
                moves.extend(['F','F','Rr','F','F'])
                continue

            elif kante==((2,7),(1,1)):
                moves.extend(['Br','L','L'])
                continue
            elif kante==((1,1),(2,7)):
                moves.extend(['Fr','D','F','Lr'])
                continue
            elif kante==((2,1),(3,7)):
                moves.extend(['F','U','U','Fr'])
                continue
            elif kante==((3,7),(2,1)):
                moves.extend(['Ur','L'])
                continue
            elif kante==((2,3),(5,3)):
               moves.extend(['B','B','L','L'])
               continue
            elif kante==((5,3),(2,3)):
               moves.extend(['B','Ur','L'])
               continue
            elif kante==((2,5),(4,3)):
               moves.extend(['L','L'])
               continue
            elif kante==((4,3),(2,5)):
               moves.extend(['L','F','Ur','Fr'])
               continue
        if counter ==3:
            
            
            if kante == ((3, 1), (0, 7)):
                moves.extend(['Ur','Fr', 'L','F'])
                counter += 1
                continue

            elif kante == ((1, 3), (5, 1)):
                moves.extend(['F','R','Fr'])
                counter += 1
                continue
            elif kante == ((5, 1), (1, 3)):
                moves.extend(['F','F', 'Dr','F','F'])
                counter += 1
                continue
            elif kante == ((1, 5), (4, 7)):
                moves.extend(['Fr','Lr'])
                counter += 1
                continue
            elif kante == ((4, 7), (1, 5)):
                moves.extend(['F','F','D','F','F'])
                counter += 1
                continue
            elif kante == ((4,1), (3,5)):
                moves.append('Ur')
                continue
            elif kante==((3,5),(4,1)):
                moves.extend(['Fr','L','F'])
                continue
            elif kante==((5,7),(3,3)):
                moves.append('U')
                continue
            elif kante==((3,3),(5,7)):
                moves.extend(['F','Rr','Fr'])
                continue

            elif kante==((2,7),(1,1)):
                moves.extend(['B','B','U','U'])
                continue
            elif kante==((1,1),(2,7)):
                moves.extend(['B','B','U','F','R','Fr'])
                continue
            elif kante==((2,1),(3,7)):
                moves.extend(['U','U'])
                continue
            elif kante==((3,7),(2,1)):
                moves.extend(['U','F','R','Fr'])
                continue
            elif kante==((2,3),(5,3)):
               moves.extend(['B','U','U'])
               continue
            elif kante==((5,3),(2,3)):
               moves.extend(['B','U','F','R','Fr'])
               continue
            elif kante==((2,5),(4,3)):
               moves.extend(['Br','U','U'])
               continue
            elif kante==((4,3),(2,5)):
               moves.extend(['Br','U','F','R','Fr'])
               continue
    return moves


map0 = {
        ((1, 7), (0, 1)): ['D', 'R', 'F'],
        ((0, 3), (5, 3)): ['F'],
        ((5, 3), (0, 3)): ['Rr', 'Dr'],
        ((0, 5), (4, 3)): ['Fr'],
        ((4, 3), (0, 5)): ['L', 'D'],
        ((0, 7), (3, 1)): ['F', 'F'],
        ((3, 1), (0, 7)): ['U', 'L', 'Fr'],
        ((1, 3), (5, 1)): ['R', 'F'],
        ((5, 1), (1, 3)): ['Dr'],
        ((1, 5), (4, 7)): ['Lr', 'Fr'],
        ((4, 7), (1, 5)): ['D'],
        ((4, 1), (3, 5)): ['Ur', 'F', 'F'],
        ((3, 5), (4, 1)): ['L', 'Fr'],
        ((5, 7), (3, 3)): ['U', 'F', 'F'],
        ((3, 3), (5, 7)): ['Rr', 'F'],
        ((2, 7), (1, 1)): ['D', 'D'],
        ((1, 1), (2, 7)): ['Dr', 'R', 'Fr'],
        ((2, 1), (3, 7)): ['U', 'U', 'F', 'F'],
        ((3, 7), (2, 1)): ['U', 'Rr', 'F'],
        ((2, 3), (5, 3)): ['R', 'R', 'F'],
        ((5, 3), (2, 3)): ['R', 'Dr'],
        ((2, 5), (4, 3)): ['L', 'L', 'Fr'],
        ((4, 3), (2, 5)): ['Lr', 'D'],
    }

map1 = {
        ((5, 5), (0, 3)): ['Rr', 'F', 'Dr', 'Fr'],
        ((0, 5), (4, 5)): ['L', 'F', 'F', 'Lr', 'F', 'F'],
        ((4, 5), (0, 5)): ['L', 'F', 'D', 'Fr'],
        ((0, 7), (3, 1)): ['D', 'F', 'Dr'],
        ((3, 1), (0, 7)): ['Ur', 'Rr'],
        ((1, 3), (5, 1)): ['R'],
        ((5, 1), (1, 3)): ['F', 'Dr', 'Fr'],
        ((1, 5), (4, 7)): ['F', 'F', 'Lr', 'F', 'F'],
        ((4, 7), (1, 5)): ['F', 'D', 'Fr'],
        ((4, 1), (3, 5)): ['Fr', 'Ur', 'F'],
        ((3, 5), (4, 1)): ['F', 'F', 'L', 'F', 'F'],
        ((5, 7), (3, 3)): ['Fr', 'U', 'F'],
        ((3, 3), (5, 7)): ['Rr'],
        ((2, 7), (1, 1)): ['B', 'R', 'R'],
        ((1, 1), (2, 7)): ['F', 'Dr', 'Fr', 'R'],
        ((2, 1), (3, 7)): ['Fr', 'U', 'U', 'F'],
        ((3, 7), (2, 1)): ['U', 'Rr'],
        ((2, 3), (5, 3)): ['R', 'R'],
        ((5, 3), (2, 3)): ['R', 'F', 'Dr', 'Fr'],
        ((2, 5), (4, 3)): ['B', 'B', 'R', 'R'],
        ((4, 3), (2, 5)): ['Lr', 'F', 'D', 'Fr'],
    }

map2 = {
        ((4, 5), (0, 5)): ['L', 'Fr', 'D', 'F'],
        ((0, 7), (3, 1)): ['U', 'F', 'Ur', 'Fr'],
        ((3, 1), (0, 7)): ['U', 'L'],
        ((1, 3), (5, 1)): ['F', 'F', 'R', 'F', 'F'],
        ((5, 1), (1, 3)): ['Fr', 'Dr', 'F'],
        ((1, 5), (4, 7)): ['Lr'],
        ((4, 7), (1, 5)): ['Fr', 'D', 'F'],
        ((4, 1), (3, 5)): ['F', 'Ur', 'Fr'],
        ((3, 5), (4, 1)): ['L'],
        ((5, 7), (3, 3)): ['F', 'U', 'Fr'],
        ((3, 3), (5, 7)): ['F', 'F', 'Rr', 'F', 'F'],
        ((2, 7), (1, 1)): ['Br', 'L', 'L'],
        ((1, 1), (2, 7)): ['Fr', 'D', 'F', 'Lr'],
        ((2, 1), (3, 7)): ['F', 'U', 'U', 'Fr'],
        ((3, 7), (2, 1)): ['Ur', 'L'],
        ((2, 3), (5, 3)): ['B', 'B', 'L', 'L'],
        ((5, 3), (2, 3)): ['B', 'Ur', 'L'],
        ((2, 5), (4, 3)): ['L', 'L'],
        ((4, 3), (2, 5)): ['L', 'F', 'Ur', 'Fr'],
    }

map3 = {
        ((3, 1), (0, 7)): ['Ur', 'Fr', 'L', 'F'],
        ((1, 3), (5, 1)): ['F', 'R', 'Fr'],
        ((5, 1), (1, 3)): ['F', 'F', 'Dr', 'F', 'F'],
        ((1, 5), (4, 7)): ['Fr', 'Lr'],
        ((4, 7), (1, 5)): ['F', 'F', 'D', 'F', 'F'],
        ((4, 1), (3, 5)): ['Ur'],
        ((3, 5), (4, 1)): ['Fr', 'L', 'F'],
        ((5, 7), (3, 3)): ['U'],
        ((3, 3), (5, 7)): ['F', 'Rr', 'Fr'],
        ((2, 7), (1, 1)): ['B', 'B', 'U', 'U'],
        ((1, 1), (2, 7)): ['B', 'B', 'U', 'F', 'R', 'Fr'],
        ((2, 1), (3, 7)): ['U', 'U'],
        ((3, 7), (2, 1)): ['U', 'F', 'R', 'Fr'],
        ((2, 3), (5, 3)): ['B', 'U', 'U'],
        ((5, 3), (2, 3)): ['B', 'U', 'F', 'R', 'Fr'],
        ((2, 5), (4, 3)): ['Br', 'U', 'U'],
        ((4, 3), (2, 5)): ['Br', 'U', 'F', 'R', 'Fr'],
    }


maps = [map0, map1, map2, map3]
def kreuz_V3(x):
    all_moves = []       # Gesamte Liste aller Moves
    move_funcs = {
        'F': F, 'Fr': Fr,
        'R': R, 'Rr': Rr,
        'L': L, 'Lr': Lr,
        'U': U, 'Ur': Ur,
        'D': D, 'Dr': Dr,
        'B': B, 'Br': Br
    }

    farben = [x[1][4], x[5][4], x[4][4], x[3][4]]  # Ziel: vorne, rechts, links, hinten
    counter = 0

    while counter < 4:
        executed_moves = []  # Nur für diesen Schleifendurchlauf

        kanten = cross(x)
        Ziel = [None, None, None, None]  # 0: vorne, 1: rechts, 2: links, 3: hinten

        for kante in kanten:
            ziel_farbe = x[kante[1][0]][kante[1][1]]
            if ziel_farbe == farben[0]:
                Ziel[0] = kante
            elif ziel_farbe == farben[1]:
                Ziel[1] = kante
            elif ziel_farbe == farben[2]:
                Ziel[2] = kante
            elif ziel_farbe == farben[3]:
                Ziel[3] = kante

        print(Ziel)
        
        for kante in Ziel:
            current_map = maps[counter]

            if kante is None:
                continue
            if kante[0][0] == 0 and x[kante[0][0]][kante[0][1]] == x[0][4] and x[kante[1][0]][kante[1][1]] == x[kante[1][0]][4]:
                counter+=1
                continue  # Kante bereits richtig
            if kante in current_map:
                for move in current_map[kante]:
                    x=move_funcs[move](x)
                    executed_moves.append(move)
                counter += 1
                break  # Nach einem korrigierten Stück → zurück in while

        all_moves.extend(executed_moves)  # Speichere die aktuellen Moves

        # Hier kannst du die aktuellen Moves separat nutzen:
    print("Ausgeführte Moves:",all_moves)
        # executed_moves wird automatisch geleert im nächsten Durchlauf

    return all_moves


def kreuz_V4(x):
    all_moves = []
    move_funcs = {
        'F': F, 'Fr': Fr,
        'R': R, 'Rr': Rr,
        'L': L, 'Lr': Lr,
        'U': U, 'Ur': Ur,
        'D': D, 'Dr': Dr,
        'B': B, 'Br': Br
    }

    farben = [x[1][4], x[5][4], x[4][4], x[3][4]]  # Ziel: vorne, rechts, links, hinten
    counter = 0

    while counter < 4:
        executed_moves = []
        done =False
        numbre=0

        kanten = cross(x)
        Ziel = [None, None, None, None]  # 0: vorne, 1: rechts, 2: links, 3: hinten

        # Zielkanten zuweisen
        for kante in kanten:
            ziel_farbe = x[kante[1][0]][kante[1][1]]
            if ziel_farbe == farben[0]:
                Ziel[0] = kante
            elif ziel_farbe == farben[1]:
                Ziel[1] = kante
            elif ziel_farbe == farben[2]:
                Ziel[2] = kante
            elif ziel_farbe == farben[3]:
                Ziel[3] = kante

        

        # Für alle Kanten die Moves sammeln
        while not done:
            kante=Ziel[counter]
            current_map = maps[counter]
            if kante is None:
                break
            if x[kante[1][0]][kante[1][1]] == x[kante[1][0]][4]:
                counter+=1
                break  # Bereits richtig
            if kante in current_map:
                executed_moves.extend(current_map[kante])
                done=True

        # Jetzt alle gesammelten Moves ausführen
        for move in executed_moves:
            move_funcs[move](x)
            all_moves.append(move)

        print(f"Durchlauf {counter+1}: ausgeführte Moves:", executed_moves)

        counter += 1  # Nur 1 Schritt weiter, egal wie viele Kanten behandelt wurden

    return all_moves

            
def kreuz_V4(x):
    executed = []
    counter = 0

    # Mittelsteinfarben der vier Seiten: vorne, rechts, links, hinten
    farben = [x[1][4], x[5][4], x[4][4], x[3][4]]

    # Mapping von Zugstrings zu deinen Funktionsnamen
    move_map = {
        "F": F, "Fr": Fr,
        "R": R, "Rr": Rr,
        "L": L, "Lr": Lr,
        "B": B, "Br": Br,
        "U": U, "Ur": Ur,
        "D": D, "Dr": Dr
    }

    while counter < 4:
        kanten = cross(x)
        Ziel = [None, None, None, None]

        # Ziel-Zuweisung auf Basis der farbigen Seite
        for kante in kanten:
            ziel_farbe = x[kante[1][0]][kante[1][1]]
            if ziel_farbe == farben[0]:
                Ziel[0] = kante
            elif ziel_farbe == farben[1]:
                Ziel[1] = kante
            elif ziel_farbe == farben[2]:
                Ziel[2] = kante
            elif ziel_farbe == farben[3]:
                Ziel[3] = kante

        # Wenn keine Kante für das aktuelle Ziel vorhanden ist, skip
        if Ziel[counter] is None:
            counter += 1
            continue

        kante = Ziel[counter]

        # Prüfen, ob Kante korrekt platziert ist
        if (
            kante[0][0] == 0 and  # Weiße Seite liegt oben
            x[kante[0][0]][kante[0][1]] == x[0][4] and  # wirklich weiß
            x[kante[1][0]][kante[1][1]] == farben[counter]  # farbige Seite stimmt
        ):
            counter += 1
            continue
        print(kante)

        # Richtige Map-Funktion auswählen
        if counter == 0:
            moves = map0[kante]
        elif counter == 1:
            moves = map1[kante]
        elif counter == 2:
            moves = map2[kante]
        elif counter == 3:
            moves = map3[kante]

        # Züge ausführen
        for move in moves:
            x=move_map[move](x)
        executed += moves
        counter += 1

    return executed
    

x=[
['Blu', 'Gel', 'Blu',
'Blu', 'Gel', 'Blu', 
'Blu', 'Gel', 'Blu'], 

['Wei', 'Gre', 'Wei', 
'Wei', 'Gre', 'Wei', 
'Wei', 'Gre', 'Wei'], 

['Gre', 'Wei', 'Gre', 
'Gre', 'Wei', 'Gre', 
'Gre', 'Wei', 'Gre'], 

['Gel', 'Blu', 'Gel', 
'Gel', 'Blu', 'Gel', 
'Gel', 'Blu', 'Gel'], 

['Ora', 'Ora', 'Ora', 
'Rot', 'Rot', 'Rot', 
'Ora', 'Ora', 'Ora'], 

['Rot', 'Rot', 'Rot', 
'Ora', 'Ora', 'Ora', 
'Rot', 'Rot', 'Rot']]

x=[
['Blu', 'Gel', 'Blu', 'Blu', 'Gel', 'Blu', 'Blu', 'Gel', 'Blu'], 
['Wei', 'Gre', 'Wei', 'Wei', 'Gre', 'Wei', 'Wei', 'Gre', 'Wei'], 
['Gre', 'Wei', 'Gre', 'Gre', 'Wei', 'Gre', 'Gre', 'Wei', 'Gre'], 
['Gel', 'Blu', 'Gel', 'Gel', 'Blu', 'Gel', 'Gel', 'Blu', 'Gel'], 
['Ora', 'Ora', 'Ora', 'Rot', 'Rot', 'Rot', 'Ora', 'Ora', 'Ora'], 
['Rot', 'Rot', 'Rot', 'Ora', 'Ora', 'Ora', 'Rot', 'Rot', 'Rot']]
kreuz_V4(x)