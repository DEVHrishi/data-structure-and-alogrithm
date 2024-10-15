'''A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.'''

def mostWordsFound(self, sentences) -> int:
        return max(len(word.split()) for word in sentences)


def mostWordsFound(self, sentences) -> int:
        return max(s.count(" ") for s in sentences) + 1