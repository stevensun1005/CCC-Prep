def score1():
    s = 'C258TJKD69QAH'
    card_lst = []
    for i in range(len(s)):
        if s[i] == 'C':
            a = []
        elif i == len(s)-1 and s[i]=='S':
            card_lst.append(a)
            a = []
            #a.append(s[i])
            card_lst.append(a)
            break
        elif i == len(s)-1:
            a.append(s[i])
            card_lst.append(a)
            break
        elif s[i] == 'D' or s[i] =='H' or s[i] =='S':
            card_lst.append(a)
            a = []
        else:
            a.append(s[i])
    print(s,card_lst)

score1()