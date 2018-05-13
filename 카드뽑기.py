class Card:
    def __init__(self,pattern,number):
        self.pattern = pattern
        self.number = number

    def __str__(self):
        return self.pattern + " " + self.number

class Deck:
    patternList = ["클럽", "스페이드", "하트","다이아몬드"]
    numberList = ["에이스", "2","3","4","5","6","7","8","9","10","잭","퀸","킹"]

    def __init__(self):
        self.Cards = []
        for p in self.patternList:
            for n in self.numberList:
                self.Cards.append(Card(p,n))

    def __str__(self):
        strList = [str(c) for c in self.Cards]
        return str(strList)

deck = Deck()
print(deck)