import string
#string.ascii_lowercase

def print_rangoli(size):
    #top section
    for i in range(size-1,0,-1):
        print('--'*i + '-'.join(string.ascii_lowercase[size-1:i-1:-1] + string.ascii_lowercase[i+1:size]) + '--'*i )
    
    #center line
    print('-'.join(string.ascii_lowercase[size-1::-1] + string.ascii_lowercase[1:size]))

    #bottom section
    for i in range(size-1):
        print('--'*(i+1) + '-'.join(string.ascii_lowercase[size-1:i:-1] + string.ascii_lowercase[i+2:size]) + '--'*(i+1))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)