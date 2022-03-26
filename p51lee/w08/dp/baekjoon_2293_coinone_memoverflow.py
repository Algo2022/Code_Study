import sys
from collections import defaultdict

class Case():
    def __init__(self, n, coins=defaultdict(int), sum=0):
        self.n = n
        self.coins = coins
        self.sum = sum

    def isValid(self):
        return self.sum == n

    def addCoin(self, new_coin):
        # print(new_coin)
        ret = [self]
        sum_temp = self.sum + new_coin
        while sum_temp <= self.n:
            self.coins[new_coin] += 1
            # print(self.coins[new_coin])
            ret.append(Case(self.n, self.coins.copy(), sum_temp))
            sum_temp += new_coin
        return ret

    def __str__(self):
        return str(self.coins) + str(self.sum)

flat_map = lambda f, xs: [y for ys in xs for y in f(ys)]

num_coins, n = map(int, sys.stdin.readline().split())

coins = []
for _ in range(num_coins):
    coins.append(int(sys.stdin.readline()))

cases = [Case(n)]
for coin in coins:
    cases = flat_map(lambda c: c.addCoin(coin), cases)

print(len(list(filter(lambda x: x.isValid(), cases))))
