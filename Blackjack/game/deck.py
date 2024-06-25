import random

def initialize_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    single_deck = [rank + ' ' + suit for suit in suits for rank in ranks]
    decks = 6 * single_deck  #online cassinos standart pattern of 6 decks
    random.shuffle(decks)
    return decks