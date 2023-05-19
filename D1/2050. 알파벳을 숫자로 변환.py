from string import ascii_uppercase

N = str(input())
alp = list(ascii_uppercase)

for i in N:
    if i in alp:
        print(alp.index(i) + 1, end= " ")
