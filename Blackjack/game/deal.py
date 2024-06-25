def deal_initial_cards(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand

def hit(deck, hand):
    hand.append(deck.pop())