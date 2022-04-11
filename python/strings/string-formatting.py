def print_formatted(number):
    max_width = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(max_width) + oct(i)[2:].rjust(max_width + 1) + hex(i)[2:].rjust(max_width + 1).upper() + bin(i)[2:].rjust(max_width + 1))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)