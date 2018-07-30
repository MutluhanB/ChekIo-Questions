''''
Mutluhan Boz 30.7.2018
Solution for finding the percantage challenge on hackerrank (https://www.hackerrank.com/challenges/finding-the-percentage)
'''
#Function to return the average of desired student's grades.
def findTheGuy(name):
    return sum(marks[name])/len(marks[name])

n = int(input()) #Desired entry count.
marks={} #Marks stored in a dictionary
for n in range (n):
    name, *points = input().split(" ") #Reading names and grades of students whic provided in a line and splitted by spaces.
    scores = list(map(float, points)) #Converting points to float as desired in the challenge.
    marks[name]=scores
name=str(input())
print("{0:.2f}".format(findTheGuy(name)))
