from sys import stdin

n, m = map(int, stdin.readline().split())
t, *truth_men = map(int, stdin.readline().split())
truth_men = set(truth_men)

party_list = []
for _ in range(m):
    party_num, *party = map(int, stdin.readline().split())
    party_list.append(set(party))

while True:
    prev = truth_men.copy()
    for party in party_list:
        if truth_men.intersection(party):
            truth_men.update(party)
    if prev == truth_men:
        break

ans = 0
for party in party_list:
    if not truth_men.intersection(party):
        ans += 1

print(ans)

