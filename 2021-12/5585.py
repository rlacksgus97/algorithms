n = int(input())
coin = [500, 100, 50, 10, 5, 1]
exchange = 1000-n

count = 0
for c in coin:
    if exchange // c > 0:
        count += exchange // c
        exchange = exchange % c

print(count)