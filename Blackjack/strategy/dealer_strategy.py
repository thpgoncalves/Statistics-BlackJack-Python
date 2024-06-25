def dealer_should_hit(dealer_hand_total, is_soft, hero_hand_total): 
    if dealer_hand_total < 17:
        if hero_hand_total > dealer_hand_total:
            return True
        else:
            return False
    elif dealer_hand_total > 17:
        return False
    else:
        if is_soft:
            return True  
        else:
            return False  