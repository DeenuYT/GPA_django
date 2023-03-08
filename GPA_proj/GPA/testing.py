def evaluate(x):
    if x == 'O' and 'o':
        return 10
    elif x == 'A+' and 'a+':
        return 9
    elif x == 'A' and 'a':
        return 8
    elif x == 'B+' and 'b+':
        return 7
    elif x == 'B' and 'b':
        return 6
    elif x == 'C' and 'c':
        return 5
    else:
        return int(x)

print(evaluate('O'))
print(evaluate('A+'))
print(evaluate('10'))
print(evaluate('B'))
print(evaluate(str.upper('b+')))