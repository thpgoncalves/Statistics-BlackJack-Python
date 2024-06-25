from rules.end_game_conditions import check_end_game
from game.deck import initialize_deck
from game.deal import deal_initial_cards, hit
from rules.card_values import calculate_hand_value
from rules.split_rules import can_split

def play_game():
    MAX_SPLITS = 3
    while True:
        deck = initialize_deck()
        player_hand, dealer_hand = deal_initial_cards(deck)
        player_hands = [(player_hand, 0)]  

        current_hand_index = 0

        while current_hand_index < len(player_hands):
            hand, split_count = player_hands[current_hand_index]
            while True:
                print(f"\n\n\nPlayer Hand {current_hand_index + 1}: {hand}, value: {calculate_hand_value(hand)}")
                print(f"Dealer Hand: [{dealer_hand[0]}, ?]")

                action = input("Choose '1. hit', '2. stand' or '3. split': ")
                if action == '1':
                    hit(deck, hand)
                    if calculate_hand_value(hand) > 21:
                        print(f"Player Hand {current_hand_index + 1}: {hand}, value: {calculate_hand_value(hand)}")
                        print("You busted!")
                        break
                elif action == '2':
                    break
                elif action == '3' and can_split(hand) and split_count < MAX_SPLITS:
                    split_card = hand.pop()
                    split_hand = [split_card]
                    player_hands.append((split_hand, split_count + 1)) 
                    hit(deck, hand)
                    hit(deck, split_hand) 
                    print(f"You split. Original hand: {hand}, New hand: {split_hand}")
                    break
                else:
                    print("Invalid action or split not allowed. Please choose 'hit', 'stand' or 'split'.")
            
            current_hand_index += 1

        if len(player_hands) > 1:
            for i, (hand, _) in enumerate(player_hands):
                while calculate_hand_value(hand) <= 21:
                    print(f"Player Hand {i + 1}: {hand}, value: {calculate_hand_value(hand)}")
                    action = input("Choose '1. hit', '2. stand' or '3. split': ")
                    if action == '1':
                        hit(deck, hand)
                        if calculate_hand_value(hand) > 21:
                            print(f"Player Hand {i + 1}: {hand}, value: {calculate_hand_value(hand)}")
                            print("You busted!")
                            break
                    elif action == '2':
                        break
                    elif action == '3' and can_split(hand) and split_count < MAX_SPLITS:
                        split_card = hand.pop()
                        split_hand = [split_card]
                        player_hands.append((split_hand, split_count + 1)) 
                        hit(deck, hand)
                        hit(deck, split_hand) 
                        print(f"You split. Original hand: {hand}, New hand: {split_hand}")
                        break
                    else:
                        print("Invalid action. Please choose 'hit' or 'stand'.")

        while calculate_hand_value(dealer_hand) < 17:
            hit(deck, dealer_hand)

        dealer_hand_value = calculate_hand_value(dealer_hand)
        print(f"Dealer Hand: {dealer_hand}, value: {dealer_hand_value}")

        if dealer_hand_value > 21:
            print("Dealer has busted!")

        for i, (hand, _) in enumerate(player_hands):
            result = check_end_game(hand, dealer_hand)
            print(f"Player Hand {i + 1}: {hand}, value: {calculate_hand_value(hand)}")
            print(f"Dealer Hand: {dealer_hand}, value: {dealer_hand_value}")  # Usando o valor calculado
            print(f"Result for hand {i + 1}: {result}")

        if not play_again():
            print("Thanks for playing!")
            break

def play_again():
    while True:
        answer = input("Do you want to play another hand? (y/n): ").lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        print("Invalid response. Please enter 'y' for yes or 'n' for no.")