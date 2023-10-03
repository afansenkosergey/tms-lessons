num = int(input())
answer = 0

while num > 0:
    ost = num % 10
    num //= 10
    answer = answer + ost
print(answer)