input_str = input().lower()


count = 0
for i in input_str:
    if 'a' in i:
        count += 1
print(count)