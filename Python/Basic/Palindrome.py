x = input("Enter a string: ")
rev_x = x[::-1]

if x == rev_x:
    print('palindrome')
else:
    print('not palindrome')