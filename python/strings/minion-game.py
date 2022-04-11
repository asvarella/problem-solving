def minion_game(string):
    #the method count() won't work here due to overlapping strings. use regex or the solution below:
    stringsize = len(string)
    stuart = kevin = 0
    #counting points
    for i in range(stringsize):
        if string[i] in 'AEIOU':
            kevin += stringsize - i
        else:
            stuart += stringsize - i
    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif kevin < stuart:
        print(f'Stuart {stuart}')
    else:
        print('Draw')
    


if __name__ == '__main__':
    s = input()
    minion_game(s)
    