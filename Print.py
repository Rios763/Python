# Este programa deve imprimir de zero até o numero inserido em y, 
# sendo que devera possuir x numeros (tambem inseridos pelo usuario) em
# cada linha 

x, y = map(int, input().split())

for i in range(1, y+1):
    if i % x == 0:
        print(i)
    else:
        print(i, end=" ")
