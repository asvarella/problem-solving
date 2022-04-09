#initializing list:
data = []
n = int(input())
for i in range(n):
    command, *number = input().split()
    match command:
        case 'insert':
            data.insert(int(number[0]), int(number[1]))
        case 'print':
            print(data)
        case 'remove':
            data.remove(int(number[0]))
        case 'append':
            data.append(int(number[0]))
        case 'sort':
            data.sort()
        case 'pop':
            data.pop(-1)
        case 'reverse':
            data.reverse()