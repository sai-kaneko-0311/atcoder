import math


def get_most_appeared_num(S):
    num = {}
    for s in S[n]:
        if s in num.keys():
            num[s] += 1
        else:
            num[s] = 1
    k, v = sorted(num.items(), key=lambda x: -x[1])[0]
    return k


id, N, K = input().split()
S = []
num = {}
for n in range(int(N)):
    S.append(list(map(int, input())))
most_appeared_num = get_most_appeared_num(S)
ope_list = []
for nf in range(1, int(N)+1):
    prev_n = -1
    if nf % 2 == 0:
        for ns in range(1, int(N)+1):
            if ns == prev_n + 3:
                ope_list.append(str(nf) + ' ' + str(ns) + ' ' + str(most_appeared_num))
                prev_n = ns
print(len(ope_list))
for ope in ope_list:
    print(ope)
