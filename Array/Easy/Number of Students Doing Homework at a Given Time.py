'''Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

'''

def busyStudent(startTime, endTime, queryTime):
        return sum([queryTime>=i and queryTime<=j for i, j in zip(startTime, endTime)])

print(busyStudent([1,2,3], [3,2,7], 4))