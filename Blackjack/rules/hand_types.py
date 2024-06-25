from .card_values import get_card_value

def is_soft_hand(hand):
  aces = sum(card.startswith('A') for card in hand)
  total = sum(get_card_value(card) for card in hand if not card.startswith('A')) + 11 * aces
  return aces > 0 and total <= 21

def is_hard_hand(hand):
  return not is_soft_hand(hand) and not is_pair(hand)

def is_pair(hand):
  return len(hand) == 2 and hand[0] == hand[1]