'''
card[0] : 끝수 = face
card[1] : shape
card[2] : value
'''
import random
FACES = list(range(1, 11)) + ["Jack", "Queen", "King", "Ace"]
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

def hand_value(hand):
    total = 0
    for card in hand:
        total += card.value()
    return total


class Card(object):
    """A Blackjack Card."""

    def __eq__(self, other):
        return (self.face == other.face and self.suit == other.suit)

    def __ne__(self, other):
        return not self == other

    def __init__(self, face, suit):
        assert face in FACES and suit in SUITS
        self.face = face
        self.suit = suit

    """__str__ 은 클래스를 좀 더 간편하게 출력 할 수 있도록 해준다."""
    def __str__(self):
        article = "a "
        if self.face in [8, "Ace"]:
            article = "an "
        return article + str(self.face) + " of " + self.suit

    def value(self):
        if type(self.face) == int:
            return self.face
        elif self.face == "Ace":
            return 11
        else:
            return 10

class Deck(object):
    """A deck of Cards"""
    def __init__(self):
        """create a deck of 52 cards and shuffle them"""
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(Card(face, suit))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


"""============================================================="""
num_players = 3
num_cards = 5
deck = Deck()
hands = []
'hands에 3개의 리스트 추가'
for i in range(num_players):
    hands.append([])

'3명에게 카드 5장씩 나눠주기'
for i in range(num_cards):
    for j in range(num_players):
        hands[j].append(deck.draw())

'각 사람이 들고 있는 카드의 합과 카드의 종류 알려주기'
for i in range(num_players):
    print("Player {}'s hand value is".format(hand_value(hands[i])))
    for j in range(num_cards):
        print("Player {}'s hand card is {}".format(i+1, hands[i][j]))
