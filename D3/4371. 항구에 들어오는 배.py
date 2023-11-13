T = int(input())
answer = []
for t in range(1, T+1):
    n = int(input())
    day = []
    for _ in range(n):
        day.append(int(input()))
    ship = set()
    cnt = 0
    for i in range(1, len(day)):
        if day[i] in ship:
            continue
        gap = day[i] - 1
        for j in range(1+gap, day[-1]+1, gap):
            ship.add(j)
        cnt += 1

    answer.append(f'#{t} {cnt}')
print(*answer, sep='\n')

