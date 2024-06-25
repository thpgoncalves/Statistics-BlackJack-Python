def can_split(hand):
    return len(hand) == 2 and hand[0].split()[0] == hand[1].split()[0]