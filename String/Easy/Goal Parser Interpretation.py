'''You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.'''

def interpret(self, command: str) -> str:
        char_to_replace = { '()': 'o', '(al)': 'al' }
        for key, value in char_to_replace.items():
            command = command.replace(key, value)
        return command

# Replace multiple characters in a string using the translate ()

def interpret(self, command: str) -> str:
        char_to_replace = { '()': 'o', '(al)': 'al' }
        command = command.translate(str.maketrans(char_to_replace))
        return command