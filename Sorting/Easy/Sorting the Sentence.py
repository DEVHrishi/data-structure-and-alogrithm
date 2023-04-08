'''A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

 

Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
Example 2:

Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.'''

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str

        Runtime complexity: O(1) constant
        Memory complexity: O(len(s)) depends on length of string

        """
        output = ""
        sarray = s.split()

        # Loop through all 9 possible position words
        for i in range(1, 10):

            # Find ith position word in string
            for word in sarray:

                # Insert word to output string
                if word[-1] == str(i):
                    output += " " + word[:-1]

        return output.strip()


class Solution:
    def sortSentence(self, s: str) -> str:
        
        x = s.split()
        dic = {}
        for i in x :
            dic[i[-1]] = i[:-1]
        return ' '.join([dic[j] for j in sorted(dic)])

