CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}

def get_card_value(card):
    value = card.split()[0]
    return CARD_VALUES[value]

def calculate_hand_value(hand):
    value = sum(get_card_value(card) for card in hand)
    aces = sum(card.startswith('A') for card in hand)  

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value