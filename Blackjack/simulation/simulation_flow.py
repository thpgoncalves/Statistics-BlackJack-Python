import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import initialize_deck, deal_initial_cards, hit
from strategy import get_hard_hand_strategy, get_soft_hand_strategy, get_pair_strategy, dealer_should_hit
from rules.hand_types import is_soft_hand, is_hard_hand, is_pair
from rules.card_values import get_card_value, calculate_hand_value
from rules.split_rules import can_split

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_card_value_for_strategy(card):
    value_str = card.split(" ")[0]
    if value_str in ["J", "Q", "K", "10"]:
        return 10
    elif value_str == "A":
        return 'A'
    else:
        return int(value_str)

def simulate_game_rounds(num_rounds):
    statistics = {
        'total_wins': 0,
        'total_games': 0,
        'strategy_wins': {'hard': 0, 'soft': 0, 'pair': 0},
        'strategy_usage': {'hard': 0, 'soft': 0, 'pair': 0}
    }

    for round_num in range(num_rounds):
        if round_num % 1000 == 0:
            logging.info(f"Rodada {round_num} de {num_rounds}")
        deck = initialize_deck()
        player_hand, dealer_hand = deal_initial_cards(deck)
        player_hands = [(player_hand, 0)] 

        current_hand_index = 0
        MAX_SPLITS = 3
        strategy_identified = None

        while current_hand_index < len(player_hands):
            hand, split_count = player_hands[current_hand_index]
            hand_finished = False
            while not hand_finished:
                strategy, action = determine_strategy_and_action(hand, dealer_hand, split_count, MAX_SPLITS)
                if strategy_identified is None:
                    strategy_identified = strategy
                    statistics['strategy_usage'][strategy] += 1

                if action == 'hit':
                    hit(deck, hand)
                    if calculate_hand_value(hand) > 21:
                        hand_finished = True
                elif action == 'split':
                    new_hands = split(deck, hand)
                    player_hands[current_hand_index] = (new_hands[0], split_count + 1)
                    player_hands.append((new_hands[1], split_count + 1))
                    break
                elif action == 'stand':
                    hand_finished = True

            current_hand_index += 1

        dealer_final_hand = dealer_play(deck, dealer_hand, hand)
        evaluate_results(player_hands, dealer_final_hand, statistics, strategy_identified)

    calculate_statistics(statistics)
    return statistics

def determine_strategy_and_action(hand, dealer_hand, split_count, MAX_SPLITS):
    dealer_card = get_card_value_for_strategy(dealer_hand[0])
    player_total = calculate_hand_value(hand)
    if is_pair(hand) and can_split(hand) and split_count < MAX_SPLITS:
        action = get_pair_strategy(player_total, dealer_card)
        strategy = 'pair'
    elif is_soft_hand(hand):
        action = get_soft_hand_strategy(player_total, dealer_card)
        strategy = 'soft'
    else:
        action = get_hard_hand_strategy(player_total, dealer_card)
        strategy = 'hard'
    return strategy, action

def split(deck, hand):
    assert len(hand) == 2, "Can only split a hand with two cards."
    return [(hand[:1] + [deck.pop()]), (hand[1:] + [deck.pop()])]

def dealer_play(deck, dealer_hand, hand):
    player_total = calculate_hand_value(hand)
    while dealer_should_hit(calculate_hand_value(dealer_hand), is_soft_hand(dealer_hand), player_total):
        hit(deck, dealer_hand)
    return dealer_hand

def evaluate_results(player_hands, dealer_final_hand, statistics, strategy):
    dealer_total = calculate_hand_value(dealer_final_hand)
    for hand, _ in player_hands:
        player_total = calculate_hand_value(hand)
        statistics['total_games'] += 1 
        if player_total > 21:
            continue 
        if dealer_total > 21 or player_total > dealer_total:
            statistics['total_wins'] += 1
            statistics['strategy_wins'][strategy] += 1

def calculate_statistics(statistics):
    if statistics['total_games'] > 0:
        statistics['win_rate'] = (statistics['total_wins'] / statistics['total_games']) * 100
    else:
        statistics['win_rate'] = 0 
    for strategy in statistics['strategy_wins']:
        if statistics['strategy_usage'][strategy] > 0:
            statistics['strategy_wins'][strategy] = (statistics['strategy_wins'][strategy] / statistics['strategy_usage'][strategy]) * 100
