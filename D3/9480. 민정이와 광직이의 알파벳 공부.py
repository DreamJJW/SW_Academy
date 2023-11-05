# t = int(input())
# alp = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
#        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
# for test_case in range(t):
#     n = int(input())
#     words = []
#     set_cnt = 0
#     for _ in range(n):
#         s = input()
#         for i in s:
#             alp[i] += 1
#
#     print(alp)
#     cnt = 0
#     for i, j in alp.items():
#         if j != 0:
#             j -= 1
#             cnt += 1
#             if cnt == 26:
#                 set_cnt += 1
#
#     print(f'#{test_case + 1} {set_cnt}')
