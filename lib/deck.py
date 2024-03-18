import random
from .card import Card

class Deck():
    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.discards: list[Card] = []

    def build_deck(self, cards: list[Card]) -> None:
        self.cards = cards

    def draw(self) -> Card:
        return self.cards.pop(0)

    def shuffle(self) -> None:
        self.cards = self.cards + self.discards
        random.shuffle(x=self.cards)

    def add(self, card: Card) -> None:
        self.cards.append(card)

    def remove(self, card: Card) -> None:
        self.cards.remove(card)

    def discard(self, card: Card) -> None:
        self.discards.append(card)

    def add_to_discard(self, card: Card) -> None:
        self.discards.append(card)

    def __str__(self) -> str:
        return f"Deck with {len(self.cards)} cards and {len(self.discards)} discards"