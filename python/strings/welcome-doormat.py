def welcome_line(m):
    line = ''
    for i in range(int((m-7)/2)):
        line += '-'
    print(line + 'WELCOME' + line)

def top_shape(n):
    line = '.|.'
    filler = '---'
    max = int(n/2)
    for i in range(int(n/2)):
        print(filler*max + line + 2*line*i + filler*max)
        max -= 1
    

def bottom_shape(n):
    line = '.|.'
    filler = '---'
    min = 1
    for i in range(int(n/2)-1,-1,-1):
        print(filler*min + line + 2*line*i + filler*min)
        min += 1

if __name__ == '__main__':
    n,m = input().split()
    top_shape(int(n))
    welcome_line(int(m))
    bottom_shape(int(n))