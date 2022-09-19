import unittest
import Poker


class TestStraightFlush(unittest.TestCase):
    def test_normal(self):
        card = Poker.Cards()
        hand = ["10♥", "J♥", "8♥", "Q♥", "9♥"]
        self.assertEqual(card.straight_flush(hand), True, "Incorrect classification (straight flush)")

    def test_false(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "4♠", "5♣", "J♠"]
        self.assertEqual(card.straight_flush(hand), False, "Incorrect classification (not straight flush)")


class TestFourOfAKind(unittest.TestCase):
    def test_normal(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "5♠", "5♣", "J♠"]
        self.assertEqual(card.four_of_a_kind(hand), True, "Incorrect classification (four of a kind)")

    def test_false(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "4♠", "5♣", "J♠"]
        self.assertEqual(card.four_of_a_kind(hand), False, "Incorrect classification (not four of a kind)")


class TestFullHouse(unittest.TestCase):
    def test_normal(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "5♠", "J♣", "J♠"]
        self.assertEqual(card.full_house(hand), True, "Incorrect classification (full house)")

    def test_false(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "4♠", "5♣", "J♠"]
        self.assertEqual(card.full_house(hand), False, "Incorrect classification (not full house)")


class TestFlush(unittest.TestCase):
    def test_normal(self):
        card = Poker.Cards()
        hand = ["5♥", "8♥", "9♥", "7♥", "2♥"]
        self.assertEqual(card.flush(hand), True, "Incorrect classification (flush)")

    def test_false(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "4♠", "5♣", "J♠"]
        self.assertEqual(card.flush(hand), False, "Incorrect classification (not flush)")


class TestStraight(unittest.TestCase):
    def test_normal(self):
        card = Poker.Cards()
        hand = ["J♥", "A♦", "10♠", "K♣", "Q♠"]
        self.assertEqual(card.straight(hand), True, "Incorrect classification (straight)")

    def test_false(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "4♠", "5♣", "J♠"]
        self.assertEqual(card.straight(hand), False, "Incorrect classification (not straight)")


class TestThreeOfAKind(unittest.TestCase):
    def test_normal(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "4♠", "5♣", "J♠"]
        self.assertEqual(card.three_of_a_kind(hand), True, "Incorrect classification (three of a kind)")

    def test_false(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "4♠", "10♣", "J♠"]
        self.assertEqual(card.three_of_a_kind(hand), False, "Incorrect classification (not three of a kind)")


class TestTwoPair(unittest.TestCase):
    def test_normal(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "10♠", "10♣", "J♠"]
        self.assertEqual(card.two_pair(hand), True, "Incorrect classification (two pair)")

    def test_false(self):
        card = Poker.Cards()
        hand = ["5♥", "5♦", "4♠", "5♣", "J♠"]
        self.assertEqual(card.two_pair(hand), False, "Incorrect classification (not two pair)")


class TestOnePair(unittest.TestCase):
    def test_normal(self):
        card = Poker.Cards()
        hand = ["5♥", "6♦", "A♠", "A♣", "J♠"]
        self.assertEqual(card.one_pair(hand), True, "Incorrect classification (one pair)")

    def test_false(self):
        card = Poker.Cards()
        hand = ["5♥", "9♦", "4♠", "10♣", "J♠"]
        self.assertEqual(card.one_pair(hand), False, "Incorrect classification (not one pair)")


class TestCheckHand(unittest.TestCase):
    def test_normal(self):
        card = Poker.Hand()
        hand = ["5♥", "9♦", "4♠", "10♣", "J♠"]
        self.assertEqual(card.check_hand(hand), True, "Incorrectly checked hand")

    def test_invalid(self):
        card = Poker.Hand()
        hand = ["15♥", "9♦", "1♠", "10♣", "J♠"]
        self.assertEqual(card.check_hand(hand), False, "Card not in deck")

    def test_duplicates(self):
        card = Poker.Hand()
        hand = ["5♥", "7♥", "4♠", "5♥", "J♠"]
        self.assertEqual(card.check_hand(hand), False, "Duplicate cards not allowed")


class TestEvalHand(unittest.TestCase):
    def test_straight_flush(self):
        card = Poker.Hand()
        hand = ["10♥", "J♥", "8♥", "Q♥", "9♥"]
        self.assertEqual(card.evaluate_hand(hand), "Straight Flush", "Incorrect classification (straight flush)")

    def test_four_of_a_kind(self):
        card = Poker.Hand()
        hand = ["5♥", "5♦", "5♠", "5♣", "J♠"]
        self.assertEqual(card.evaluate_hand(hand), "Four of a Kind", "Incorrect classification (four of a kind)")

    def test_full_house(self):
        card = Poker.Hand()
        hand = ["5♥", "5♦", "5♠", "J♣", "J♠"]
        self.assertEqual(card.evaluate_hand(hand), "Full House", "Incorrect classification (full house)")

    def test_flush(self):
        card = Poker.Hand()
        hand = ["5♥", "8♥", "9♥", "7♥", "2♥"]
        self.assertEqual(card.evaluate_hand(hand), "Flush", "Incorrect classification (flush)")

    def test_straight(self):
        card = Poker.Hand()
        hand = ["J♥", "A♦", "10♠", "K♣", "Q♠"]
        self.assertEqual(card.evaluate_hand(hand), "Straight", "Incorrect classification (straight)")

    def test_three_of_a_kind(self):
        card = Poker.Hand()
        hand = ["5♥", "5♦", "4♠", "5♣", "J♠"]
        self.assertEqual(card.evaluate_hand(hand), "Three of a Kind", "Incorrect classification (three of a kind)")

    def two_pair(self):
        card = Poker.Hand()
        hand = ["5♥", "5♦", "10♠", "10♣", "J♠"]
        self.assertEqual(card.evaluate_hand(hand), "Two Pair", "Incorrect classification (two pair)")

    def one_pair(self):
        card = Poker.Hand()
        hand = ["5♥", "6♦", "A♠", "A♣", "J♠"]
        self.assertEqual(card.evaluate_hand(hand), "One Pair", "Incorrect classification (one pair)")

    def high_card(self):
        card = Poker.Hand()
        hand = ["5♥", "6♦", "2♠", "A♣", "J♠"]
        self.assertEqual(card.evaluate_hand(hand), "High Cards", "Incorrect classification (high card)")
