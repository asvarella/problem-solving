def symmetric_difference(marr,narr):
    result = marr.difference(narr)
    for i in narr:
        if i in narr.difference(marr):
            result.add(i)
    print('\n'.join(str(i) for i in sorted(result)))

if __name__ == '__main__':
    m = int(input())
    marr = set(map(int, input().strip().split()))
    n = int(input())
    narr = set(map(int, input().strip().split()))
    symmetric_difference(marr,narr)