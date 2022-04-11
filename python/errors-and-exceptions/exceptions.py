x = int(input())
for i in range(x):
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as err:
        print('Error Code:', err)
    except ValueError as vrr:
        print('Error Code:', vrr)