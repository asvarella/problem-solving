n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split() #collects person's name and grades and splits by ' '
    scores = list(map(float, line)) #catches floats from line and creates a list of scores
    student_marks[name] = scores #links the list of scores to names in dictionary
query_name = input() #

name_scores = list(student_marks[query_name]) #creates a list with query_name's scores
average = sum(name_scores)/len(name_scores)

print(f'{average:.2f}')