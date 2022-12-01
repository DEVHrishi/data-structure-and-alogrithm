'''A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.'''

# TC = O(N)


def sortSentence(self, s: str) -> str:
    words = s.split()
    n = len(words)

    sent = [None] * n

    for i in range(n):
        sent[int(words[i][-1]) - 1] = words[i][:-1]

    return " ".join(sent)


def sortSentence(self, s: str) -> str:

    dic = {}
    for i in s.split():
        dic[i[-1]] = i[:-1]

    final = []
    for num, word in sorted(dic.items()):
        final.append(word)
    return " ".join(final)

# (runtime / memory)
#  24 ms / 14.3 MB


def sortSentence(self, s: str) -> str:

    dic = {}
    for i in s.split():
        dic[i[-1]] = i[:-1]

    final = [word for num, word in sorted(dic.items())]
    return " ".join(final)

# (runtime / memory)
#  28 ms / 14.4 MB


def sortSentence(self, s: str) -> str:

    words = s[::-1].split()
    result = [word[1:][::-1] for word in sorted(words)]
    return ' '.join(result)

# (runtime / memory)
#  32 ms / 14.1 MB
