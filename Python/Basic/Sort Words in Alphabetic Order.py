my_str = "Hello My name is Hrishikesh Roy"

words = [word.lower() for word in my_str.split()]

words.sort()

for word in words:
    print(word)