class Stack:
    def __init__(self):  # Kostruktor
        self.Stack = []
    def Push(self, s):  # Dodawanie elementów
        self.Stack.append(s)
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
x,y=input('podaj liczbe wierzcholkow i krawedzi').split()
x=int(x)
y=int(y)
A=[]
Euler = Stack()
odwiedzone=[]
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
    A[int(v1)][int(v2)]=1
    A[int(v2)][int(v1)] = 1
print('macierz sąsiedztwa:')
for t in A:
    print(t)
for i in range(x):
    odwiedzone.append(False)
    #odwiedzone2.append(False)
'''print('lista sasiedztwa: ')
for i in krawedz:
    print(i)'''
print('Cykl Eulera:')
DFS(0)
#sciezka()

#print(krawedz)
for i in range(Euler.Size()):
    print(Euler.Top())
    Euler.Pop()
