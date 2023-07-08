'''You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

 

Example 1:

Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:

Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"'''

class Solution:
    def maximumTime(self, time: str) -> str:
        hours = list(time[:2])
        minutes = list(time[3:])

        if hours[0] == '?':
            if hours[1] == '?' or int(hours[1]) <= 3 :
                hours[0] = '2'
            else:
                hours[0] = '1'
        if hours[1] == '?':
            if hours[0] == '?' or hours[0] == '2':
                hours[1] = '3'
            else:
                hours[1] = '9'
        if minutes[0] == '?':
            minutes[0] = '5'
        if minutes[1] == '?':
            minutes[1] = '9'

        return ''.join(hours)+':'+''.join(minutes)