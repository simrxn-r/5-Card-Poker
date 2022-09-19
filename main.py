import Poker
import unittest
import test_Poker

if __name__ == "__main__":
    # Acquire deck of cards
    thisDeck = Poker.Cards()
    # Initial hand is empty
    thisDeck.print_hand()
    # Shuffle cards
    thisDeck.shuffle_cards()

    myHand = Poker.Hand()
    # Get dealt cards
    if myHand.create_hand():
        # Show player's hand
        myHand.print_hand()
        # Evaluate player's hand
        myHand.print_eval()

    print()
    print("===================================")
    print("Running unit tests...")
    suite = unittest.TestLoader().loadTestsFromModule(test_Poker)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # How to run unit tests??
