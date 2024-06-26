hard_hand_strategy = {
    # 2
    (5, 2): 'H', (6, 2): 'H', (7, 2): 'H', (8, 2): 'H', (9, 2): 'H', (10, 2): 'H', (11, 2): 'H', (12, 2): 'H', (13, 2): 'H', (14, 2): 'H', (15, 2): 'H', (16, 2): 'H',
    (17, 2): 'S', (18, 2): 'S', (19, 2): 'S', (20, 2): 'S', (21, 2): 'S',
    # 3
    (5, 3): 'H', (6, 3): 'H', (7, 3): 'H', (8, 3): 'H', (9, 3): 'H', (10, 3): 'H', (11, 3): 'H', (12, 3): 'H', (13, 3): 'S', (14, 3): 'S', (15, 3): 'S', (16, 3): 'S',
    (17, 3): 'S', (18, 3): 'S', (19, 3): 'S', (20, 3): 'S', (21, 3): 'S',
    # 4
    (5, 4): 'H', (6, 4): 'H', (7, 4): 'H', (8, 4): 'H', (9, 4): 'H', (10, 4): 'H', (11, 4): 'H', (12, 4): 'S', (13, 4): 'S', (14, 4): 'S', (15, 4): 'S', (16, 4): 'S',
    (17, 4): 'S', (18, 4): 'S', (19, 4): 'S', (20, 4): 'S', (21, 4): 'S',
    # 5
    (5, 5): 'H', (6, 5): 'H', (7, 5): 'H', (8, 5): 'H', (9, 5): 'H', (10, 5): 'H', (11, 5): 'H', (12, 5): 'S', (13, 5): 'S', (14, 5): 'S', (15, 5): 'S', (16, 5): 'S',
    (17, 5): 'S', (18, 5): 'S', (19, 5): 'S', (20, 5): 'S', (21, 5): 'S',
    # 6
    (5, 6): 'H', (6, 6): 'H', (7, 6): 'H', (8, 6): 'H', (9, 6): 'H', (10, 6): 'H', (11, 6): 'H', (12, 6): 'S', (13, 6): 'S', (14, 6): 'S', (15, 6): 'S', (16, 6): 'S',
    (17, 6): 'S', (18, 6): 'S', (19, 6): 'S', (20, 6): 'S', (21, 6): 'S',
    # 7
    (5, 7): 'H', (6, 7): 'H', (7, 7): 'H', (8, 7): 'H', (9, 7): 'H', (10, 7): 'H', (11, 7): 'H', (12, 7): 'H', (13, 7): 'H', (14, 7): 'H', (15, 7): 'H', (16, 7): 'H',
    (17, 7): 'S', (18, 7): 'S', (19, 7): 'S', (20, 7): 'S', (21, 7): 'S',
    # 8
    (5, 8): 'H', (6, 8): 'H', (7, 8): 'H', (8, 8): 'H', (9, 8): 'H', (10, 8): 'H', (11, 8): 'H', (12, 8): 'H', (13, 8): 'H', (14, 8): 'H', (15, 8): 'H', (16, 8): 'H',
    (17, 8): 'S', (18, 8): 'S', (19, 8): 'S', (20, 8): 'S', (21, 8): 'S',
    # 9
    (5, 9): 'H', (6, 9): 'H', (7, 9): 'H', (8, 9): 'H', (9, 9): 'H', (10, 9): 'H', (11, 9): 'H', (12, 9): 'H', (13, 9): 'H', (14, 9): 'H', (15, 9): 'H', (16, 9): 'H',
    (17, 9): 'S', (18, 9): 'S', (19, 9): 'S', (20, 9): 'S', (21, 9): 'S',
    # 10
    (5, 10): 'H', (6, 10): 'H', (7, 10): 'H', (8, 10): 'H', (9, 10): 'H', (10, 10): 'H', (11, 10): 'H', (12, 10): 'H', (13, 10): 'H', (14, 10): 'H', (15, 10): 'H', (16, 10): 'H',
    (17, 10): 'S', (18, 10): 'S', (19, 10): 'S', (20, 10): 'S', (21, 10): 'S',
    # A
    (5, 'A'): 'H', (6, 'A'): 'H', (7, 'A'): 'H', (8, 'A'): 'H', (9, 'A'): 'H', (10, 'A'): 'H', (11, 'A'): 'H', (12, 'A'): 'H', (13, 'A'): 'H', (14, 'A'): 'H', (15, 'A'): 'H', (16, 'A'): 'H',
    (17, 'A'): 'S', (18, 'A'): 'S', (19, 'A'): 'S', (20, 'A'): 'S', (21, 'A'): 'S',
}

def get_hard_hand_strategy(player_total, dealer_card):
    action = hard_hand_strategy.get((player_total, dealer_card), 'H') 
    if action == 'H':
        return 'hit'
    elif action == 'S':
        return 'stand'
    return action