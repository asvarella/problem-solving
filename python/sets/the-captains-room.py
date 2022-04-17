k = int(input())
arr = list(map(int, input().split()))
setarr = set(arr)
print(((sum(setarr)*k)-(sum(arr)))//(k-1))