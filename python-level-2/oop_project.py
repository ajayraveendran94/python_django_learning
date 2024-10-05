from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Create an ordered Deck")
        self.all_cards = [(s,r) for s in SUITE for r in RANKS]
    def shuffle(self):
        print("shuffling all cards")
        shuffle(self.all_cards)
    def split_card(self):
        return (self.all_cards[:26], self.all_cards[26:])
    

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards
    def __str__(self):
        return f"Contain {len(self.cards)} cards"
    def add_card(self, added_cards):
        self.cards.extend(added_cards)
    def remove_card(self):
        return self.cards.pop()
class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has played a {drawn_card}")
        print("\n")
        return drawn_card
    def remove_war_card(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
    def still_has_cards(self):
        """
        Returns True if player still has cards
        """
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create New Deck and split in half
deck = Deck()
deck.shuffle()
half1,half2 = deck.split_card()

#Create players
computer = Player("Computer", Hand(half2))
your_name = input("Enter your name: ")
user = Player(your_name, Hand(half1))

total_count = 0
war_count = 0
while user.still_has_cards() and computer.still_has_cards():
    total_count += 1
    print(f"Lets begin round {total_count}")
    print("Current Standings")
    print(f"{user.name} has {str(len(user.hand.cards))} cards")
    print(f"Computer has {str(len(computer.hand.cards))} cards")
    print("Both players play a card")

    table_card = []
    comp_card = computer.play_card()
    user_card = user.play_card()
    table_card.append(comp_card)
    table_card.append(user_card)
    if comp_card[1] == user_card[1]:
        war_count += 1
        print("It is a War")
        table_card.extend(user.remove_war_card())
        table_card.extend(computer.remove_war_card())
        comp_card = computer.play_card()
        user_card = user.play_card()
        table_card.append(comp_card)
        table_card.append(user_card)
        if RANKS.index(comp_card[1]) < RANKS.index(user_card[1]):
            print(f"{user.name} has the highest Card")
            user.hand.add_card(table_card)
        else:
            print("Computer has the higher card")
            computer.hand.add_card(table_card)
    else:
        if RANKS.index(comp_card[1]) < RANKS.index(user_card[1]):
            print(f"{user.name} has the highest Card")
            user.hand.add_card(table_card)
        else:
            print("Computer has the higher card")
            computer.hand.add_card(table_card)

print(f"Game Over!!! - Number of rounds {str(total_count)}")
print(f" Number of war rounds {str(war_count)}")