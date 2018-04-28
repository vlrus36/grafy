class Stack:
    def __init__(self):  # Kostruktor
        self.Stack = []
    def Push(self, s):  # Dodawanie elementów
        self.Stack.append(s)
    def First(self):
        return self.Stack[0]
    def Pop(self):  # Usuwanie elementu
        self.Stack.pop(len(self.Stack) - 1)
    def Size(self):  # Ilość elementów na stosie
        return len(self.Stack)
    def Top(self):  # Zwraca ostatni element
        return self.Stack[len(self.Stack) - 1]
    def Top2(self):  # Zwraca ostatni element
        return self.Stack[len(self.Stack) - 2]
    def Empty(self):  # Sprawdza czy stos jest pusty
        if len(self.Stack) == 0:
            return True
        else:
            return False
def DFS(v):
    for i in range (x):
        while A[v][i]:
            A[v][i]=0
            A[i][v]=0
            DFS(i)
    Euler.Push(v)
def DFS2(v):
    odwiedzone[v] = True
    #print(v + 1)
    for i in range(x):
        if A[v][i] == 1 and odwiedzone[i] == False: DFS2(i)
x,y=input('podaj liczbe wierzcholkow i krawedzi').split()
x=int(x)
y=int(y)
A=[]
Euler = Stack()
odwiedzone=[]
bla=[]
spojny=0
#krawedz=[]
for i in range(x):
    A.append([])
    #krawedz.append([])
    for j in range(x):
        A[i].append([])
for i in range(x):
    for j in range(x):
        A[i][j]=0
for i in range(y):
    v1,v2=input('podaj wierzcholek poczatkowy i koncowy krawedzi ').split()
    #krawedz[i].append(int(v1))
    #krawedz[i].append(int(v2))
    A[int(v1)-1][int(v2)-1]=1
    A[int(v2)-1][int(v1)-1] = 1
print('macierz sąsiedztwa:')
for t in A:
    print(t)
for i in range(x):
    odwiedzone.append(False)
    #odwiedzone2.append(False)
DFS2(0)
#print(odwiedzone)
for i in odwiedzone:
    if i==True:
        spojny+=1
if spojny==x:
    print('graf spojny')
    DFS(0)
    #print(x,' ',Euler.Size(),Euler.Top(),Euler.First())
    if Euler.Size()==y+1 and Euler.First()==0:
        print('graf eulerowski')
    elif Euler.Size()==y+1 and Euler.First()!=0:
        print('graf poleulerowski')
    else:
        print('graf nieeulerowski')
    '''for i in range(Euler.Size()):
        print(Euler.Top())
        Euler.Pop()'''
else:
    print('graf niespojny')

#sciezka()

#print(krawedz)
