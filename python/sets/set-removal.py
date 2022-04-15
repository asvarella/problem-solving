n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    command, *number = input().split()
    if command == 'discard':
        s.discard(int(number[0]))
    elif command == 'pop':
        s.pop()
    elif command == 'remove':
        s.remove(int(number[0]))
print(sum(s))

