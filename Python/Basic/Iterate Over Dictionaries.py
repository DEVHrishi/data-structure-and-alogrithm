dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)
'''
a juice
b grill
c corn'''

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt:
    print(key, dt[key])
'''
a juice
b grill
c corn'''

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.iteritems():
    print(key, value)
'''
a juice
b grill
c corn'''

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt.keys():
    print(key)

for value in dt.values():
    print(value)

'''
a
b
c
juice
grill
corn'''