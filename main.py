import collections
import enum
import itertools
import random


class Suit (enum.Enum):
    HEART = 1
    DIAMOND = 2
    CLUB = 3
    SPADE = 4



def create_deck():
    suits = [Suit.HEART, Suit.DIAMOND, Suit.CLUB, Suit.SPADE]
    numbers = list(range(1, 14))
    cards = []
    for suit, number in itertools.product(suits, numbers):
        cards.append(Card(suit=suit, number=number))
    return cards

class Game:

    def __init__(self, players): # list of (player_name, team_id)
        # Create and shuffle deck
        deck = create_deck()
        random.shuffle(deck)
        hands = []
        for i in range(4):
            hands.append(deck[i*12:(i+1)*12])
        table = deck[-4:]

        # assign teams and hands
        player_count = 0
        teams = collections.defaultdict(list)
        self.players = []
        for player_name, team_id in players:
            player = Player(name=player_name, cards=hands[player_count])
            self.players.append(player)
            player_count += 1
            teams[team_id].append(player)

        self.teams = []
        for team_id, team_players in teams.items():
            self.teams.append(Team(players=team_players, id=team_id))

        # Distribute remaining cards to board
        self.board = Board()
        for card in table:
            self.board.add_free_card(card=card)

    def play_game(self):
        for round in range(12):
            for player in self.players():
                self.play_turn(player)

    def play_turn(self, player):
        card = player.select_card()

        player.remove_card(card)


class Board:
    def __init__(self):
        self.free_cards = []
        self.piles = []

    def add_free_card(self, card):
        self.free_cards.append(card)

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

class Pile:
    def __init__(self, number):
        self.number = number
        self.puca = False
        self.cards = []
        self.owners = []

    def add_cards(self, cards, player):
        assert self.number >= 9
        assert sum([card.number for card in cards]) == self.number
        self.cards += cards

class Team:
    def __init__(self, players, id):
        self.players = players
        self.id = id
        for player in players:
            player.team = self

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.hand = cards # initial hand
        self.groups = []
        self.partner_groups = []

    def make_move(self):

    def select_card(self):
        return random.choice(self.hand)

    def remove_card(self, card):
        self.hand.remove(card)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
