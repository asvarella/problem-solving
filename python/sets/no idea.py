def happiness(arr,a,b):
    happiness_count = 0
    for i in arr:
        if i in a:
            happiness_count += 1
        if i in b:
            happiness_count -= 1
    print(happiness_count)

if __name__ == '__main__':
    n,m = input().split()
    n,m = int(n),int(m)
    arr = list(map(int, input().split()))
    a = set(map(int, input().strip().split()))
    b = set(map(int, input().strip().split()))
    happiness(arr,a,b)