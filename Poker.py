import random


class Cards:
    def __init__(self):
        # Empty hand
        self.my_hand = []

    # 52 possible cards
    deck = [
        "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠",
        "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦",
        "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥",
        "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"
    ]

    # Easy to change ranks and number of cards for different variants of poker
    no_cards = 5
    card_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    # Hand should be empty before deal
    def print_hand(self):
        print("Your Hand: ", end=" ")
        if not self.my_hand:
            print("Empty")

    @staticmethod
    def shuffle_cards():
        # Shuffling the cards
        print("Shuffling...", end=" ")
        print("Shuffling...", end=" ")
        print("Shuffling...")

    # 1. Straight Flush: 5 cards of the same suit in sequence
    def straight_flush(self, hand):
        if self.flush(hand) and self.straight(hand):
            return True
        else:
            return False

    # 2. Four of a Kind: 4 cards of the same rank + 1 random card
    def four_of_a_kind(self, hand):
        values = [i[:len(i) - 1] for i in hand]
        for x in range(self.no_cards):
            if values.count(values[x]) == 4:
                return True
        return False

    # 3. Full House: 3 cards of the same rank + 2 cards of another (three of a kind + pair)
    def full_house(self, hand):
        if self.three_of_a_kind(hand) and self.one_pair(hand):
            return True
        else:
            return False

    # 4. Flush: 5 cards of the same suit not in sequence
    def flush(self, hand):
        values = [i[len(i) - 1:] for i in hand]
        if values.count(values[0]) == self.no_cards:
            return True
        return False

    # 5. Straight: 5 cards in sequence
    def straight(self, hand):
        values = [i[:len(i) - 1] for i in hand]
        ranks = []
        for j in range(len(values)):
            ranks.append(self.card_values[values[j]])

        sorted_values = sorted(ranks)
        for x in range(1, self.no_cards):
            if sorted_values[x] != sorted_values[x - 1] + 1:
                return False

        return True

    # 6. Three of a Kind: 3 cards of the same rank + 2 random cards
    def three_of_a_kind(self, hand):
        values = [i[:len(i) - 1] for i in hand]
        for x in range(self.no_cards):
            if values.count(values[x]) == 3:
                return True
        return False

    # 7. Two Pair: 2 cards of one rank + 2 cards of another rank + 1 random card
    def two_pair(self, hand):
        values = [i[:len(i) - 1] for i in hand]
        saved_val = -1
        for x in range(self.no_cards):
            if values.count(values[x]) == 2:
                if saved_val == -1:
                    saved_val = values[x]
                if values.count(values[x]) == 2 and saved_val != values[x]:
                    return True
        return False

    # 8. One Pair: 2 cards of same rank
    def one_pair(self, hand):
        values = [i[:len(i) - 1] for i in hand]
        for x in range(self.no_cards):
            if values.count(values[x]) == 2:
                return True
        return False

    # 9. High Cards: highest card in the hand
    @staticmethod
    def high_cards(self):
        return True


# Inheritance
class Hand(Cards):
    def __init__(self):
        super(Hand, self).__init__()

    def create_hand(self):
        # Random 5 cards
        for x in range(100):
            if len(self.my_hand) == self.no_cards:
                break

            num = random.randint(0, 51)
            if self.deck[num] not in self.my_hand:  
                self.my_hand.append(self.deck[num])

        if not self.check_hand(self.my_hand):
            return False
        else:
            return True

    def check_hand(self, hand):
        # Checking each card is valid
        for h in hand:
            if h not in self.deck:
                return False

        # Checking for duplicates
        if len(hand) != len(set(hand)):
            return False

        return True

    # Polymorphism: method overriding
    def print_hand(self):
        # SAMPLE HAND for testing purposes
        # self.my_hand = ["9♥", "6♦", "5♠", "5♣", "J♠"]

        print("Your Hand: ", end=" ")
        print(self.my_hand)

    # Evaluating the cards in the hand
    def evaluate_hand(self, hand):
        if self.straight_flush(hand):
            return "Straight Flush"
        if self.four_of_a_kind(hand):
            return "Four of a Kind"
        if self.full_house(hand):
            return "Full House"
        if self.flush(hand):
            return "Flush"
        if self.straight(hand):
            return "Straight"
        if self.three_of_a_kind(hand):
            return "Three of a Kind"
        if self.two_pair(hand):
            return "Two Pair"
        if self.one_pair(hand):
            return "One Pair"
        if self.high_cards(hand):
            return "High Cards"
        else:
            return "ERROR"

    def print_eval(self):
        print("You Have: ", end=" ")
        print(self.evaluate_hand(self.my_hand))

