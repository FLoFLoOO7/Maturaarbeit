x=[['Gel','Wei','Gel','Wei','Gel','Wei','Gel','Wei','Gel'],
['Gre','Blu','Gre','Blu','Gre','Blu','Gre','Blu','Gre'],
['Wei','Gel','Wei','Gel','Wei','Gel','Wei','Gel','Wei'],
['Blu','Gre','Blu','Gre','Blu','Gre','Blu','Gre','Blu'],
['Rot','Ora','Rot','Ora','Rot','Ora','Rot','Ora','Rot'],
['Ora','Rot','Ora','Rot','Ora','Rot','Ora','Rot','Ora']
]
y=[['Gel','Wei','Gel',
    'Wei','Gel','Wei',
    'Gel','Wei','Gel'],

   ['Gre','Blu','Gre',
    'Blu','Gre','Blu',
    'Gre','Blu','Gre'],

   ['Wei','Gel','Wei',
    'Gel','Wei','Gel',
    'Wei','Gel','Wei'],

   ['Blu','Gre','Blu',
    'Gre','Blu','Gre',
    'Blu','Gre','Blu'],

   ['Rot','Ora','Rot',
    'Ora','Rot','Ora',
    'Rot','Ora','Rot'],

   ['Ora','Rot','Ora',
    'Rot','Ora','Rot',
    'Ora','Rot','Ora']
]

def rechts_drehen(y):
    x=4
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][1],y[x][8],y[x][7],y[x][7],y[x][1],y[x][3]
    y[0][2],y[0][5],y[0][8],  y[1][2],y[1][5],y[1][8], y[2][2],y[2][5],y[2][8], y[3][2],y[3][5],y[3][8]  =y[3][2],y[3][5],y[3][8],y[0][2],y[0][5],y[0][8],y[1][2],y[1][5],y[1][8],y[2][2],y[2][5],y[2][8]
    
    return y
def links_drehen(y):
    x=5
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][1],y[x][8],y[x][7],y[x][7],y[x][1],y[x][3]
    y[0][0],y[0][3],y[0][6],  y[1][0],y[1][3],y[1][6], y[2][0],y[2][3],y[2][6], y[3][0],y[3][3],y[3][6]  =  y[1][0],y[1][3],y[1][6], y[2][0],y[2][3],y[2][6], y[3][0],y[3][3],y[3][6], y[0][0],y[0][3],y[0][6]
    
    return y
def front_drehen(Y):
    S1=1
    S2=4
    S3=3
    S4=5
    pos_1=0
    pos_2=1
    pos_3=2
    x=0
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][1],y[x][8],y[x][7],y[x][7],y[x][1],y[x][3]
    y[S1][pos_1], y[S1][pos_2],y[S1][pos_3],     y[S2][pos_1], y[S2][pos_2], y[S2][pos_3],     y[S3][pos_1], y[S3][pos_2], y[S3][pos_3],     y[S4][pos_1], y[S4][pos_2], y[S4][pos_3]  =     y[S2][pos_1], y[S2][pos_2], y[S2][pos_3],     y[S3][pos_1], y[S3][pos_2], y[S3][pos_3],     y[S4][pos_1], y[S4][pos_2], y[S4][pos_3],y[S1][pos_1], y[S1][pos_2],y[S1][pos_3], 
    print(y)
    return y

def back_drehen(y):
    S1=1
    S2=4
    S3=3
    S4=5
    pos_1=6
    pos_2=7
    pos_3=8
    x=2
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][1],y[x][8],y[x][7],y[x][7],y[x][1],y[x][3]
    y[S1][pos_1], y[S1][pos_2],y[S1][pos_3],     y[S2][pos_1], y[S2][pos_2], y[S2][pos_3],     y[S3][pos_1], y[S3][pos_2], y[S3][pos_3],     y[S4][pos_1], y[S4][pos_2], y[S4][pos_3]  =      y[S4][pos_1], y[S4][pos_2], y[S4][pos_3],y[S1][pos_1], y[S1][pos_2],y[S1][pos_3], y[S2][pos_1], y[S2][pos_2], y[S2][pos_3],     y[S3][pos_1], y[S3][pos_2], y[S3][pos_3],    
    print(y)
    return y
def up_drehen():
    S1=0
    S2=5
    S3=2
    S4=4
    pos_1=6
    pos_2=7
    pos_3=8
    x=1
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][1],y[x][8],y[x][7],y[x][7],y[x][1],y[x][3]
    y[S1][pos_1], y[S1][pos_2],y[S1][pos_3],     y[S2][pos_1], y[S2][pos_2], y[S2][pos_3],     y[S3][pos_1], y[S3][pos_2], y[S3][pos_3],     y[S4][pos_1], y[S4][pos_2], y[S4][pos_3]  =      y[S4][pos_1], y[S4][pos_2], y[S4][pos_3],y[S1][pos_1], y[S1][pos_2],y[S1][pos_3], y[S2][pos_1], y[S2][pos_2], y[S2][pos_3],     y[S3][pos_1], y[S3][pos_2], y[S3][pos_3],    
    print(y)
    return y
def down_drehen():
    S1=1
    S2=4
    S3=3
    S4=5
    pos_1=0
    pos_2=1
    pos_3=2
    x=3
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][1],y[x][8],y[x][7],y[x][7],y[x][1],y[x][3]
    y[S1][pos_1], y[S1][pos_2],y[S1][pos_3],     y[S2][pos_1], y[S2][pos_2], y[S2][pos_3],     y[S3][pos_1], y[S3][pos_2], y[S3][pos_3],     y[S4][pos_1], y[S4][pos_2], y[S4][pos_3]  =      y[S4][pos_1], y[S4][pos_2], y[S4][pos_3],y[S1][pos_1], y[S1][pos_2],y[S1][pos_3], y[S2][pos_1], y[S2][pos_2], y[S2][pos_3],     y[S3][pos_1], y[S3][pos_2], y[S3][pos_3],    
    print(y)
    return y

z=[['Wei', 'Wei', 'Wei', 'Gel', 'Gel', 'Gel', 'Wei', 'Wei', 'Wei'], 
 ['Blu', 'Blu', 'Blu', 'Gre', 'Gre', 'Gre', 'Blu', 'Blu', 'Blu'], 
 ['Gel', 'Gel', 'Gel', 'Wei', 'Wei', 'Wei', 'Gel', 'Gel', 'Gel'], 
 ['Gre', 'Gre', 'Gre', 'Blu', 'Blu', 'Blu', 'Gre', 'Gre', 'Gre'], 
 ['Rot', 'Ora', 'Rot', 'Ora', 'Rot', 'Ora', 'Rot', 'Ora', 'Rot'], 
 ['Ora', 'Rot', 'Ora', 'Rot', 'Ora', 'Rot', 'Ora', 'Rot', 'Ora']]

a=[['Gel', 'Wei', 'Gel', 'Wei', 'Gel', 'Wei', 'Gel', 'Wei', 'Gel'], 
   ['Rot', 'Ora', 'Rot', 'Blu', 'Gre', 'Blu', 'Gre', 'Blu', 'Gre'], 
   ['Wei', 'Gel', 'Wei', 'Gel', 'Wei', 'Gel', 'Wei', 'Gel', 'Wei'], 
   ['Ora', 'Rot', 'Ora', 'Gre', 'Blu', 'Gre', 'Blu', 'Gre', 'Blu'], 
   ['Blu', 'Gre', 'Blu', 'Ora', 'Rot', 'Ora', 'Rot', 'Ora', 'Rot'], 
   ['Gre', 'Blu', 'Gre', 'Rot', 'Ora', 'Rot', 'Ora', 'Rot', 'Ora']]
