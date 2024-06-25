from .card_values import calculate_hand_value

def check_end_game(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > 21:
        return "Player has busted! Dealer wins!"
    elif dealer_value > 21:
        return "Dealer has busted! Player wins!"
    elif player_value == 21:
        return "player_21" 
    elif dealer_value == 21:
        return "dealer_21" 
    elif player_value == dealer_value:
        return "It's a tie! Dealer wins."
    elif player_value < dealer_value:
        return "Dealer has a better hand, he wins"
    else:
        return "You got a better hand, you wins" 