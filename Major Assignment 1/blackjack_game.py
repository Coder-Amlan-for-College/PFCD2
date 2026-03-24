import random
from enum import Enum

class Suit(Enum):
    HEARTS="Hearts"
    DIAMONDS="Diamonds"
    CLUBS="Clubs"
    SPADES="Spades"

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def value(self):
        if self.rank in ['J','Q','K']:
            return 10
        elif self.rank=='A':
            return 11
        else:
            return int(self.rank)
    
    def __str__(self):
        return f"{self.rank} of {self.suit.value}"

class Deck:
     def __init__(self):
         self.cards=[]
         self.build_deck()

     def build_deck(self):
         ranks=['2','3','4','5','6','7','8','9','10','J','Q','K', 'A']

         for suit in Suit:
             for rank in ranks:
                 self.cards.append(Card(suit,rank))

     def shuffle(self):
         random.shuffle(self.cards)

     def draw_card(self):
         return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.standing = False

    def add_card(self, card):
        self.hand.append(card)

    def calculate_total(self):
        total = sum(card.value() for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == 'A')

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

class BlackjackGame:
    def __init__(self, num_players):
        self.deck = Deck()
        self.deck.shuffle()

        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players:
                player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

    def player_turns(self):
        for player in self.players:
            while True:
                print(f"\n{player.name}'s Hand: {player.show_hand()} (Total: {player.calculate_total()})")

                if player.calculate_total() > 21:
                    print(f"{player.name} BUSTED!")
                    break

                choice = input("Hit or Stand? (h/s): ").lower()

                if choice == 'h':
                    player.add_card(self.deck.draw_card())
                else:
                    player.standing = True
                    break


    def dealer_turn(self):
        print(f"\nDealer's Hand: {self.dealer.show_hand()} (Total: {self.dealer.calculate_total()})")

        while self.dealer.calculate_total() <= 16:
            print("Dealer hits...")
            self.dealer.add_card(self.deck.draw_card())

        print(f"Dealer stands with total: {self.dealer.calculate_total()}")


    def determine_winner(self):
        dealer_total = self.dealer.calculate_total()

        if dealer_total > 21:
            print("\nDealer BUSTED! All players win!")
            return

        for player in self.players:
            player_total = player.calculate_total()

            print(f"\n{player.name}: {player_total} vs Dealer: {dealer_total}")

            if player_total > 21:
                print(f"{player.name} loses (busted).")
            elif player_total > dealer_total:
                print(f"{player.name} wins!")
            elif player_total < dealer_total:
                print(f"{player.name} loses.")
            else:
                print(f"{player.name} -> Push (tie).")


    def play(self):
        self.deal_initial_cards()

        self.player_turns()
        self.dealer_turn()
        self.determine_winner()


if __name__ == "__main__":
    num_players = int(input("Enter number of players: "))
    game = BlackjackGame(num_players)
    game.play()
            