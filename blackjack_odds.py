import random

def create_deck():
    deck = {}
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    for a in suit_names:
        for b, c in zip(rank_names, range(13)):
            if c == 0:
                deck[b+' of '+a] = []
                deck[b+' of '+a].append(1)
                deck[b+' of '+a].append(11)
            elif c >= 10:
                deck[b+' of '+a] = 10
            else:
                deck[b+' of '+a] = c+1
    return deck

def check_value(hand):
    total = 0
    aceTotal = 0
    for card in hand:
        if type(hand[card]) == int:
            total += hand[card]
            aceTotal += hand[card]
        else:
            total += 1
            aceTotal += 11
    if aceTotal == total:
        return total
    else:
        return total, aceTotal

def check_odds(hand, deck):
    odds = 0
    total = len(deck)
    points = check_value(hand)
    for c in deck.keys():
        if type(points) == int:
            if type(deck[c]) == int:
                if deck[c] + points <= 21:
                    odds += 1
            else:
                for d in deck[c]:
                    if d + points <= 21:
                        odds += 1
        else:
            for score in points: 
                if type(deck[c]) == int:
                    if deck[c] + score <= 21:
                        odds += 1
                else:
                    for d in deck[c]:
                        if d + score <+ 21:
                            odds += 1

    chance = (odds/total) * 100
    if chance > 100:
        return '{0:.2f}'.format(100.00)
    else:
        return '{0:.2f}'.format(chance)

class Person():
    def __init__(self):
        self.hand = {}

    def draw(self, deck):
        cards = random.sample(deck.keys(), 1)
        for card in cards:
            self.hand[card] = deck[card]
            del deck[card]
        return deck

    def start(self, deck):
        cards = random.sample(deck.keys(), 2)
        for card in cards:
            self.hand[card] = deck[card]
            del deck[card]
        return deck

deck = create_deck()

player = Person()
dealer = Person()

deck = player.start(deck)
deck = dealer.start(deck)

# while True:
#     if check_value(player.hand) < 21 and check_value(dealer.hand) < 21:
#         if check_value(dealer.hand) <= 16:
#             dealer.draw(deck)
#             print(check_value(dealer.hand))
#         if check_odds(player.hand, deck) > 50:
#             player.draw(deck)
#             print(check_value(player.hand))
#     else:
#         if check_value(dealer.hand) <= 16:
#             dealer.draw(deck)
#             print(check_value(dealer.hand))
#         if check_odds(player.hand, deck) > 50:
#             player.draw(deck)
#             print(check_value(player.hand))

# print(check_odds(player.hand, deck))