"""
Write functions and use data structure to simulate the card game
file name: vegas.py
author: Chen Lin
"""
import random
import cs_queue
import cs_stack


def init_deck(cards):
    """
    a new deck of card
    :param cards: a queue
    :return: a new deck of cards
    """
    empty_queue = cs_queue.make_empty_queue()
    for i in range(1, cards + 1):
        cs_queue.enqueue(empty_queue, i)
    return empty_queue


def random_draw(cards):
    """
    randomly choose a card
    :param cards: a queue
    :return: a randomly-selected card number
    """
    card = random.randint(1, cards.size + 1)
    for i in range(0, card - 1):
        value = cs_queue.front(cards)
        cs_queue.enqueue(cards, value)
        cs_queue.dequeue(cards)
    card = cs_queue.dequeue(cards)
    return card


def play_game(cards):
    """
    deal out the cards
    :param cards: a queue
    :return: card dealt
    """
    for card in range(0, cards.size):
        cards_dealt = random_draw(cards)  # call random_draw function
        return cards_dealt


def implement_card_game(cards):
    """
    make two empty discard piles and one empty victory pile and implement the game
    :param cards: a queue
    """
    discard_1 = cs_stack.make_empty_stack()
    discard_2 = cs_stack.make_empty_stack()
    victory_pile = cs_stack.make_empty_stack()
    cs_stack.push(victory_pile, 0)

    while not cs_queue.is_empty(cards):
        card = random_draw(cards)     # cards is a queue. card is int. Discard_1, discard_2 and victory_pile are stacks.
        if card == 1 or card == cs_stack.top(victory_pile) + 1:
            cs_stack.push(victory_pile, card)

        if cs_stack.is_empty(discard_1) and cs_stack.is_empty(discard_2):
            cs_stack.push(discard_1, card)

        if card < cs_stack.top(discard_1):
            cs_stack.push(discard_1, card)
        else:
            cs_stack.push(discard_2, card)

    while not cs_stack.is_empty(discard_1) and cs_stack.is_empty(discard_2):
        discard_1_top = cs_stack.top(discard_1)
        discard_2_top = cs_stack.top(discard_2)

        if discard_1_top == cs_stack.top(victory_pile) + 1:
            cs_stack.push(victory_pile, discard_1_top)
        else:
            cs_stack.push(discard_1, discard_1_top)

        if discard_2_top == cs_stack.top(victory_pile) + 2:
            cs_stack.push(victory_pile, discard_2_top)
        else:
            cs_stack.push(discard_2, discard_2_top)

    return victory_pile, discard_1, discard_2


def main():
    """
    main function to prompt for input corresponding to the number of cards to use in the deck
    and prompt for input corresponding to the number of games to play. Output the average number of cards
    and max and min on the victory pile.
    """
    deck_size = int(input('Enter deck size:'))
    games = int(input('Enter number of games:'))
    total = 0
    Max = 0
    Min = deck_size
    for i in range(games):
        deck = init_deck(deck_size)
        victory_pile, discard_1, discard_2 = implement_card_game(deck)
        total += cs_stack.size(victory_pile)
        if cs_stack.size(victory_pile) > Max:
            Max = cs_stack.size(victory_pile)
        if cs_stack.size(victory_pile) < Min:
            Min = cs_stack.size(victory_pile)

    average_number = float(total / games)
    print('The average number of cards on the victory pile:', average_number)
    print('The maximum number of cards ever achieved on the victory pile:', Max)
    print('The minimum number of cards ever achieved on the victory pile:', Min)


if __name__ == '__main__':
    main()
