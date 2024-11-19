import random

class Deck:
    def __init__(self):
        # Create a standard deck of 52 cards
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]
        self.reset_deck()

    def reset_deck(self):
        # Reset and shuffle the deck
        self.current_deck = self.deck.copy()
        random.shuffle(self.current_deck)

    def draw_card(self):
        # Draw a card from the deck
        if len(self.current_deck) == 0:
            return None
        return self.current_deck.pop()

    def calculate_probability(self, condition):
        """
        Calculate probability of drawing a card meeting a specific condition
        condition: function that takes a card tuple (rank, suit) and returns boolean
        """
        matching_cards = sum(1 for card in self.current_deck if condition(card))
        total_cards = len(self.current_deck)
        return matching_cards / total_cards if total_cards > 0 else 0

# Example usage
deck = Deck()

# Draw a random card
card = deck.draw_card()
print(f"Drawn card: {card[0]} of {card[1]}")

# Calculate probabilities for different scenarios
def is_heart(card):
    return card[1] == 'Hearts'

def is_face_card(card):
    return card[0] in ['Jack', 'Queen', 'King']

def is_ace(card):
    return card[0] == 'Ace'

# Print probabilities
print(f"\nProbabilities from remaining deck:")
print(f"Drawing a heart: {deck.calculate_probability(is_heart):.2%}")
print(f"Drawing a face card: {deck.calculate_probability(is_face_card):.2%}")
print(f"Drawing an ace: {deck.calculate_probability(is_ace):.2%}")

# Example of drawing multiple cards
print("\nDrawing 5 cards:")
for i in range(5):
    card = deck.draw_card()
    if card:
        print(f"Card {i+1}: {card[0]} of {card[1]}")
        print(f"Probability of drawing an ace now: {deck.calculate_probability(is_ace):.2%}")