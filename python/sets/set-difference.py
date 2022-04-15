if __name__ == '__main__':
    n = int(input())
    narr = set(map(int, input().split()))
    b = int(input())
    barr = set(map(int, input().split()))
    print(len(narr.difference(barr)))