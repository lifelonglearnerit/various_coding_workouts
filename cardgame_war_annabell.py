"""
Card game WAR:
Description: from: https://www.manning.com/livevideo/get-programming-with-python-in-motion
Actions:
  >> Players take a card from one dec and compare the cards.
  >> The one with higher card winds the round and gives their card to the other player.
  >> The winner is determined after numerous rounds, when the deck is empty
  >> The winner is the person with fewer cards in their hand.
Simulater playing the card game:
Create two types of objects:
  >> Player
  >> CardDeck
Write code that simulates a game between two players.
  >> First ask users for their names.
  >> Create two Player objects.
  >> Both players will use the same card deck.
  >> Use methods defined in the Player and CardDeck classes to automatically
     simulate the rounds and determine the winner.
Rules and Definitions:
  >> Spades = S{card number from 2 to 9}. example.:S4
  >> Hearts = H{card number from 2 to 9}. example.:H4
  >> Diamonds = D{card number from 2 to 9}. example.:D4
  >> Clubs = C{card number from 2 to 9}. example.:C4
The Player:
  >> Player has a name (string) and a hand of card (list)
  >> There is a common deck. Each round you add one card to each player's hand
  >> You compare the cards just added to each player, first by NUMBER. If equal then by their suit
  >> SPADES > HEARTS > DIAMONDS > CLUBS
  >> The person with larger card removes the card from their hand, and the person with the smaller card takes the card.
  >> When deck is empty, compare the number of cards the players have - the person with fewer cards WINS!
"""
import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_name(self):
        return self.name

    def add_card_to_hand(self, card):
        if card is not None:
            self.hand.append(card)

    def remove_card_from_hand(self, card):
        self.hand.remove(card)

    def hand_size(self):
        return len(self.hand)


class CardDeck(object):
    def __init__(self):
        self.deck = []
        for suit in ['S', 'H', 'D', 'C']:
            for i in range(1, 9):
                self.deck.append(suit + str(i))

    def get_card(self):
        """
        returns random a card
        removes a card form deck
        returns None if list is empty
        :return: None or Card
        """
        if len(self.deck) < 1:
            return None
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def compare_cards(self, card1, card2):
        """
        Compare cards
        by number
        SPADES > HEARTS > DIAMONDS > CLUBS
        :return: larger in number or in suit
        """
        if card1[1] > card2[1]:
            return card1
        elif card1[1] < card2[1]:
            return card2
        elif card1[0] > card2[0]:
            return card1
        else:
            return card2


p1_name = input('Player1: Enter your name: ')
p2_name = input('Player2: Enter your name: ')
p1 = Player(p1_name)
p2 = Player(p2_name)
deck = CardDeck()
count: int = 1
while True:

    card_1 = deck.get_card()
    card_2 = deck.get_card()
    p1.add_card_to_hand(card_1)
    p2.add_card_to_hand(card_2)

    if deck.compare_cards(card_1, card_2) == card_1:

        p1.remove_card_from_hand(card_1)
        print(f'{p1.get_name()} wins the round {count} and has {p1.hand_size()} cards!')
        p2.add_card_to_hand(card_1)
        print(f'{p2.get_name()} looses the round {count} and has {p2.hand_size()} cards!')

    else:

        p2.remove_card_from_hand(card_2)
        print(f'{p2.get_name()} wins the round {count} and has {p2.hand_size()} cards!')
        p1.add_card_to_hand(card_2)
        print(f'{p1.get_name()} looses the round {count} and has {p1.hand_size()} cards!')

    if deck.get_card() is None:
        input('The Deck is empty! Now we will compare amount of cards each player has in hand!\n'
              'Player with smaller amount WINS! Press ENTER to continue.')
        if p1.hand_size() < p2.hand_size():
            print(f'{p1.get_name()} WON!')
        elif p1.hand_size() > p2.hand_size():
            print(f'{p2.get_name()} WON!')
        else:
            print('A Tie!')
        input('GAME OVER\n'
              'Press enter to exit')
        exit()
    count += 1
    input(f'Press ENTER to start next round! - Good Luck!\n'
          f'####################### ROUND{count} #######################')
