n = int(input('Enter a number: '))

print(bin(n), 'is the binary representation' )
print(oct(n), 'is the octal representation' )
print(hex(n), 'is the hexadecimal representation' )

# Function to convert decimal to binary, octal and hexadecimal
def binary_conversion(decimal):
    # binary conversion
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    print("Binary:", binary)

def octal_conversion(decimal):
    # octal conversion
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal = decimal // 8
    print("Octal:", octal)

def hexadecimal_conversion(decimal):
    # hexadecimal conversion
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal = decimal // 16
    print("Hexadecimal:", hexadecimal)

# test the function
binary_conversion(20)
octal_conversion(20)
hexadecimal_conversion(20)
