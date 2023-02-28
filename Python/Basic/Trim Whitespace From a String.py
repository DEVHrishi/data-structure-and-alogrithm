my_string = " Python "

print(my_string.strip())  #Python

my_string = " \nPython "

print(my_string.strip(" "))  #Python

import re

my_string  = " Hello Python "
output = re.sub(r'^\s+|\s+$', '', my_string)

print(output)  # Hello python