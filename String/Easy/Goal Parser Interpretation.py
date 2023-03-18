'''You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"'''

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