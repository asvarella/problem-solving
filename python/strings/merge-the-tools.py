import textwrap

def merge_the_tools(string, k):
    t = textwrap.wrap(string,k)
    for i in t:
        print(''.join(sorted(set(i), key = i.index)))
    
if __name__ == '__main__':
    #string, k = input(), int(input())
    string = 'AABCAAADA'
    k = 3
    merge_the_tools(string, k)
