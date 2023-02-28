list_1 = [1, 'a']
list_2 = [3, 4, 5]

list_joined = list_1 + list_2

list_joined = [*list_1, *list_2]

list_joined = list(set(list_1 + list_2))

list_2.extend(list_1)