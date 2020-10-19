import re
import operator
 
 
def roman_ar(data):
    first = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9}
    second = {'X':10, 'XX':20, 'XXX':30, 'XL':40, 'L':50}
    rang = re.findall(r' [A-Z]+', data)[0][1:]
    number = 0
    try:
        number = first[rang]
    except:
        pass
    try:
        number = second[rang]
    except:
        pass
    if number == 0:
        for i in ['XL', 'L', 'XXX', 'XX', 'X']:
            main_d = re.findall(i, rang)
            if len(main_d)!=0:
                number = second[main_d[0]]
                break
        rang = rang.replace(main_d[0], '', 1)
        number += first[rang]
    return number
 
N = int(input())
kings = []
for i in range(N):
    king = input()
    kings.append([re.findall(r'[A-z]+ ', king)[0],roman_ar(king), king])
for i in sorted(kings, key=operator.itemgetter(0, 1)):
    print(i[2])
    