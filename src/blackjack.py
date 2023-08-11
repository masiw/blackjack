# Create an application that randomly deals a deck of cards
# to a player. The player can choose to hit or stay by typing
# the letter h or s. If the player hits, deal another card.
# If the player stays, end the game.
# Cards are represented by a 2 character string. The first
# character is the face value (A, 2-9, T, J, Q, K). The second
# character is the suit (H, D, C, S).

import random

# Create a list to define a deck of cards
deck = [
    'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H',
    '9H', 'TH', 'JH', 'QH', 'KH',
    'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D',
    '9D', 'TD', 'JD', 'QD', 'KD',
    'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C',
    '9C', 'TC', 'JC', 'QC', 'KC',
    'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S',
    '9S', 'TS', 'JS', 'QS', 'KS'
]

# Create a list to hold the shoe
shoe = []

# Create a list to hold the player's cards
player_cards = []

# Create a list to hold the dealer's cards
dealer_cards = []

# Create function to shuffle fill the shoe with a shuffled deck
def shuffle():
    global shoe
    shoe = deck.copy()
    random.shuffle(shoe)

# Create function to deal a card to a player
def deal_card():
    player_cards.append(shoe.pop())


# Create a function to display the cards in a player's hand
def show_cards():
    print('Your cards are: ')
    for card in player_cards:
        print(card + ' ', end='')
    print('\n')

# Create a function to handle the player's turn
def player_turn():
    # Display the player's cards
    show_cards()
    
    if len(shoe) == 0:
        return
    
    # Ask the player if they want to hit or stay
    choice = input('Hit or stay? (h/s): ')

    # If the player hits, deal a card
    if choice == 'h':
        deal_card()
        player_turn()

    # If the player stays, end the turn
    elif choice == 's':
        pass

    # If the player enters an invalid choice, ask again
    else:
        print('Invalid choice. Please try again.')
        player_turn()

# Create main function
def main():
    # Shuffle the deck
    shuffle()
    
    # Deal two cards to the player
    deal_card()
    deal_card()
    
    # Handle the player's turn
    player_turn()


if __name__ == "__main__":
    main()

