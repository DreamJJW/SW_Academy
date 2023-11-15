t = int(input())
for test_case in range(t):
    n = int(input())
    cards = list(map(str, input().split()))
    new_cards = []
    if n % 2 == 0:
        for i in range(n // 2):
            new_cards.append(cards[i])
            new_cards.append(cards[n//2 + i])
    else:
        for i in range(n // 2):
            new_cards.append(cards[i])
            new_cards.append(cards[n//2 + i + 1])
        new_cards.append(cards[n // 2])

    print(f'#{test_case+1}', *new_cards)
