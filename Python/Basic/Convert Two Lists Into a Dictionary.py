index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = dict(zip(index, languages))
print(dictionary)  #{1: 'python', 2: 'c', 3: 'c++'}

index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = {k: v for k, v in zip(index, languages)}
print(dictionary)  # {1: 'python', 2: 'c', 3: 'c++'}