def busyStudent(startTime, endTime, queryTime):
        return sum([queryTime>=i and queryTime<=j for i, j in zip(startTime, endTime)])

print(busyStudent([1,2,3], [3,2,7], 4))