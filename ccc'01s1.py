def pokers():
    cards = 'C258TJKD69QAHSTJA'
    clubs = []
    diamonds = []
    hearts = []
    spades = []
    for i in cards:
        if i == 'C':
            clubs.append()
            if i == 'D':
                break
        if i == 'D':
            diamonds.append()
            if i == 'H':
                break
    print(clubs)
    print(diamonds)

pokers()
