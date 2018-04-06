s=0
t=[]
stop=[]
n=int(input('Liczba wierzcholkow: '))
for a in range(n):
    x=input('wartości wierzchołka:').split()
    t.append(x)
print('Macierz sasiedztwa danego grafu G: ')
for a in t:
    print(a)
for i in range(n):
    c=0
    for j in range(n):
        c+=int(t[i][j])
    stop.append(c)
    print('Stopien wierzcholka: ',i+1,' jest rowny',stop[i])
print('Stopien danego grafu G jest rowny: ',max(stop))
print('Program napisal Michal Laga')
