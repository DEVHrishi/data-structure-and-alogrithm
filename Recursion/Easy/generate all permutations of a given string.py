def generate_permutations(s, start=0):
    # If the start index is at the end of the string, print the permutation
    if start == len(s) - 1:
        print("".join(s))
        return

    # Recursively generate permutations for each character at the start index
    for i in range(start, len(s)):
        # Swap the characters at positions start and i
        s[start], s[i] = s[i], s[start]

        # Recursively generate permutations for the remaining characters
        generate_permutations(s, start + 1)

        # Undo the swap for backtracking
        s[start], s[i] = s[i], s[start]

# Example usage:
input_string = "abc"
generate_permutations(list(input_string))
