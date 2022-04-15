a = int(input())
arr = set(map(int, input().split()))
n = int(input())
for i in range(n):
    command, *number = input().split()
    number = int(number[0])
    new_arr = set(map(int, input().split()))
    if command == 'update':
        arr.update(new_arr)
    elif command == 'intersection_update':
        arr.intersection_update(new_arr)
    elif command == 'difference_update':
        arr.difference_update(new_arr)
    elif command == 'symmetric_difference_update':
        arr.symmetric_difference_update(new_arr)
print(sum(arr))