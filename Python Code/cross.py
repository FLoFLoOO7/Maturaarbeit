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
z=[
['Blu', 'Gel', 'Blu', 'Blu', 'Gel', 'Blu', 'Blu', 'Gel', 'Blu'], 
['Wei', 'Gre', 'Wei', 'Wei', 'Gre', 'Wei', 'Wei', 'Gre', 'Wei'], 
['Gre', 'Wei', 'Gre', 'Gre', 'Wei', 'Gre', 'Gre', 'Wei', 'Gre'], 
['Gel', 'Blu', 'Gel', 'Gel', 'Blu', 'Gel', 'Gel', 'Blu', 'Gel'], 
['Ora', 'Ora', 'Ora', 'Rot', 'Rot', 'Rot', 'Ora', 'Ora', 'Ora'], 
['Rot', 'Rot', 'Rot', 'Ora', 'Ora', 'Ora', 'Rot', 'Rot', 'Rot']]
O=[['Blu', 'Gel', 'Blu', 'Blu', 'Gel', 'Blu', 'Gre', 'Wei', 'Gre'], 
   ['Wei', 'Gre', 'Wei', 'Wei', 'Gre', 'Wei', 'Wei', 'Gre', 'Wei'], 
   ['Blu', 'Gel', 'Blu', 'Gre', 'Wei', 'Gre', 'Gre', 'Wei', 'Gre'], 
   ['Gel', 'Blu', 'Gel', 'Gel', 'Blu', 'Gel', 'Gel', 'Blu', 'Gel'], 
   ['Ora', 'Ora', 'Ora', 'Rot', 'Rot', 'Rot', 'Rot', 'Rot', 'Rot'], 
   ['Ora', 'Ora', 'Ora', 'Ora', 'Ora', 'Ora', 'Rot', 'Rot', 'Rot']]
def rechts_drehen(y):
    x=4
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[0][0],y[0][3],y[0][6],  y[1][0],y[1][3],y[1][6], y[2][0],y[2][3],y[2][6], y[3][0],y[3][3],y[3][6]  =y[3][0],y[3][3],y[3][6],y[0][0],y[0][3],y[0][6],y[1][0],y[1][3],y[1][6],y[2][0],y[2][3],y[2][6]
    
    return y
def links_drehen(y):
    x=5
    #1->3 2->6 3->9 4->2 6->8 9->7 7->1 8->4
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[0][2],y[0][5],y[0][8],  y[1][2],y[1][5],y[1][8], y[2][2],y[2][5],y[2][6], y[3][2],y[3][5],y[3][8]  =  y[1][2],y[1][5],y[1][8], y[2][2],y[2][5],y[2][8], y[3][2],y[3][5],y[3][8], y[0][2],y[0][5],y[0][8]
   
    return y
def front_drehen(y):
    S1=1
    S2=4
    S3=3
    S4=5
    x=0
    y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][5], y[S2][2],     y[S3][2], y[S3][1], y[S3][0],     y[S4][8], y[S4][5], y[S4][2], y[x][0],y[x][1],y[x][2],y[x][3],y[x][5],y[x][6],  y[x][7],  y[x][8]  =         y[S2][8], y[S2][5], y[S2][2],     y[S3][2], y[S3][1], y[S3][0],     y[S4][8], y[S4][5], y[S4][2],y[S1][6], y[S1][7],y[S1][8],  y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    print(y)
    return y

def back_drehen(y):
    S1=1
    S2=4
    S3=3
    S4=5
    x=2
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[S1][6], y[S1][7],y[S1][8],     y[S2][6], y[S2][3], y[S2][0],     y[S3][0], y[S3][1], y[S3][2],     y[S4][6], y[S4][3], y[S4][0]  =     y[S4][6], y[S4][3], y[S4][0]  , y[S1][6], y[S1][7],y[S1][8],     y[S2][6], y[S2][3], y[S2][0],     y[S3][0], y[S3][1], y[S3][2],       
    
    return y
def up_drehen(y):
    S1=0
    S2=5
    S3=2
    S4=4
    x=3
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][7], y[S2][6],     y[S3][0], y[S3][1], y[S3][2],     y[S4][0], y[S4][1], y[S4][2]  =     y[S4][0], y[S4][1], y[S4][2]     , y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][7], y[S2][6],     y[S3][0], y[S3][1], y[S3][2],     
    
    return y
def down_drehen():
    S1=2
    S2=4
    S3=0
    S4=5
    x=1
    y[x][0],y[x][1],y[x][2],  y[x][3],y[x][5],y[x][6],y[x][7],y[x][8]=y[x][2],y[x][5],y[x][8],y[x][1],y[x][7],y[x][0],y[x][3],y[x][6]
    y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][7], y[S2][6],     y[S3][0], y[S3][1], y[S3][2],     y[S4][0], y[S4][1], y[S4][2]  =     y[S4][0], y[S4][1], y[S4][2]     , y[S1][6], y[S1][7],y[S1][8],     y[S2][8], y[S2][7], y[S2][6],     y[S3][0], y[S3][1], y[S3][2],     
    
    return y
front_drehen(z)

ü=[['Wei', 'Wei', 'Wei', 'Gel', 'Gel', 'Gel', 'Wei', 'Wei', 'Wei'], 
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
