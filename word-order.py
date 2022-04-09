words = []
wo = {}

for i in range(int(input())):
    words.append(input())

for p in words:
    if p in wo:
        wo[p] += 1
    else:
        wo[p] = 1


print(len(wo))
for wr,freq in wo.items():
    print(freq, end = ' ')
