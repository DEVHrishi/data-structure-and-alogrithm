'''Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

Example 1:

Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.
Example 2:

Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt.'''

from collections import Counter

class Solution:
    def search(self, pat, txt):
        # Frequency count of characters in the pattern
        freq = Counter(pat)
        l = len(pat)  # Length of the pattern
        window_freq = Counter(txt[:l])  # Frequency count of the first window of text
        count = 0  # Counter to keep track of anagrams found
        
        # Check if the first window is an anagram
        if window_freq == freq:
            count += 1

        # Slide the window across the text
        for i in range(len(txt) - l):
            # Remove the frequency of the outgoing character from the window
            window_freq[txt[i]] -= 1
            if window_freq[txt[i]] == 0:
                del window_freq[txt[i]]  # Remove the character completely if count is zero
            
            # Add the frequency of the incoming character to the window
            window_freq[txt[i + l]] = window_freq.get(txt[i + l], 0) + 1
            
            # Check if the current window is an anagram
            if window_freq == freq:
                count += 1
        
        return count
