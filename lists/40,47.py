#40, 46

DEBUG = False

def code_split(li, word):

    splitter = ord(word.lower()[0]) - ord('a') + 1
    if splitter > len(li):
        return 'Cannot split'
    l1 = li[:splitter]
    l2 = li[splitter:]
    return l1, l2

def find_odds(li):
    odds = list()
    for ele in li:
        if DEBUG: print('Checking', ele)
        if not ele.isnumeric():
            continue
        #if type(ele) != type(4):
            #if DEBUG: print('Not an int')
            #continue
        ele = int(ele)
        if int(ele) % 2 != 0:
            if DEBUG: print("Found odd", ele)
            odds.append(ele)
            if DEBUG: print('list of odds is now', odds)
    return odds

#Main PROGRAM Q 40
li = input("List: ").split(',')
word = input("Word: ")
print(code_split(li, word))

##Main PROGRAM Q 46
if DEBUG: l1 = [eval(i) for i in li]
l1 = input("List of ints: ").split(',')
print(f'Odd items are {find_odds(l1)}')
