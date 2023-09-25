lis = [1, 2, 3]
fou = lis.append('four')
tw = lis[1] = 'two'
print(lis)
add_1 = lis.append({5, 6})
add_2 = lis[4] = {5, 6, 7}
add_3 = lis.insert(2, (2.5, 2.6))
print(lis)