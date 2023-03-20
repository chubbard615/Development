#Bot that plays you in Danish
from enum import Enum
import pygame
import random

number_of_players = int(input("How many people are playing? "))
Decks_used = 1

#classes (tutorial)

class Suits(Enum):
           CLUB = 0
           SPADE = 1
           HEART = 2
           DIAMOND = 3
class Card:
    suit = None
    value = None
    special = None
#class special(Enum):
#    2 = #reset pile face
#    10 = #wipe pile count
#    7 = #pile face must be lower
#    8 = #skip next player


    def __init__(self, suit, value, special):
        self.suit = suit
        self.value = value
        self.special = special
class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for suit in Suits:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)
        def deal(self):
            return self.cards.pop()
        def length(self):
            return len(self.cards)
class Pile:
    cards = None
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def peek(self):
        if (len(self.cards) > 0):
            return self.cards[-1]
        else:
            return None
    def popAll(self):
        return self.cards

    def clear(self):
        self.cards = []

    def isWipe(self):
       if (len(self.cards) > 1):
            return (self.cards[-1].value == self.cards[-2].value == self.cards[-3].value == self.cards[-4].value)
       else:
        return False
class Player:
    hand = None
    flipKey = None
    snapKey = None
    name = None
    def __init__(self, name, flipkey, snapkey):
        self.hand = []
        self.flipkey = flipkey
        self.snapkey = snapkey
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.deal())

    def play(self):
        return self.hand.pop(0)

class GameState(Enum):
    PLAYING = 0
    ENDED = 1

class DanishEngine:
    deck = None
    player1 = None
    player2 = None
    pile = None
    state = None
    currentPlayer = None
    result = None

    def __init__(self): ##### NOT SURE HOW TO ADD A VARIABLE NUMBER OF PLAYERS
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player("Player 1", pygame.k_q, pygame.K_w)
        self.player2 = Player("Player 2", pygame.K_o, pygame.K_p)
        self.pile = Pile()
        self.deal()
        self.currentPlayer = self.player1
        self.state = GameState.PLAYING

    def deal(self):
        half = self.deck.length() // 2
        for i in range(0, half):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)


#main

if int(number_of_players) < 2 or number_of_players > 12:
    print('You have too many friends, or not enough sorry :(')
elif int(number_of_players) > 6:
    use_two_decks = input("Would you like to use two decks? Y or N ")
    print(use_two_decks)
    if use_two_decks.find('Y'):
        Decks_used = 2
        print('Using 2 decks')
    elif use_two_decks.find('N'):
        print('Using 1 deck')
else:
    print('Using 1 deck')
if number_of_players == 2:
    player_1 = Player()
    player_2 = Player()
    player_list = [player_1, player_2]


print('Done :)')