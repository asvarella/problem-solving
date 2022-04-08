#starting a void list:
students = []

for i in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score]) ##adding info on list

#finding the second lowest score
second_lowest = sorted(set(score for name, score in students))[1]

#printing names of students who scored the second lowest score, sorted by alphabetical order.
print('\n'.join(sorted((name for name, score in students if score == second_lowest))))