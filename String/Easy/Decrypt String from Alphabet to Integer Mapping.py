'''You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"'''

def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = len(s)-1
        while i>=0:
            if s[i]=="#":
                ans = ans + chr(int(s[i-2:i])+96)
                i=i-2
            else:
                ans = ans + chr(int(s[i])+96)
            i -= 1
        return ans[::-1]