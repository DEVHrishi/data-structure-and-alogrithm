dict1 = {1: 'a', 2: 'b'}
dict2 = {3: 'c', 4: 'd'}

print(dict1 | dict2)

print({**dict1, **dict2})

dict_3 = dict2.copy()
dict_3.update(dict1)

print(dict_3)