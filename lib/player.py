from lib.card import Card
from .deck import Deck


class Player:
    def __init__(self, player_name: str, character_name: str) -> None:
        self.player_name: str = player_name
        self.character_name: str = character_name
        self.influence: int = 0
        self.deck = Deck()
        self.build_my_deck()
        self.hand: list[Card] = []
        self.has_emperor: bool = False
        self.deck.shuffle()

    def build_my_deck(self) -> None:
        # the card instance, and then `:` how many of them go in the deck
        count_of_each_card: dict[Card, int] = {
            Card(
                name="Steal an Influence",
                flavor_text="Theif!",
                player_add=1,
                player_subtract=0,
                target_add=0,
                target_subtract=1,
            ): 3,
            Card(
                name="+2 Influence",
                flavor_text="Medium yay!!",
                player_add=2,
                player_subtract=0,
                target_add=0,
                target_subtract=0,
            ): 4,
            Card(
                name="-2 Influence",
                flavor_text="Medium shucks!!",
                player_add=0,
                player_subtract=0,
                target_add=0,
                target_subtract=2,
            ): 2,
            Card(
                name="+3 Influence",
                flavor_text="Big yay!!!",
                player_add=3,
                player_subtract=0,
                target_add=0,
                target_subtract=0,
            ): 1,
            Card(
                name="+2 from Player with Emperor Token",
                flavor_text="Emperor's Wrath!",
                player_add=2,
                player_subtract=0,
                target_add=0,
                target_subtract=2,
            ): 1,
        }
        cards: list[Card] = []

        for card, count in count_of_each_card.items():
            cards += [card] * count

        self.deck.build_deck(cards=cards)

    def draw(self) -> None:
        if len(self.deck.cards) == 0:
            self.deck.shuffle()
        self.hand.append(self.deck.draw())

    def discard(self, card: Card) -> None:
        self.hand.remove(card)
        self.deck.discard(card=card)

    def add_influence(self, influence: int) -> int:
        self.influence += influence
        return self.influence

    def remove_influence(self, influence: int) -> int:
        self.influence -= influence
        if self.influence - influence < 0:
            self.influence = 0
        return self.influence

    def play_card(self, card: Card, target_player=None) -> None:
        if len(self.hand) == 0:
            return
        card.apply(player=self, target_player=target_player)
        self.hand.remove(card)
        self.deck.discard(card=card)

    def __str__(self) -> str:
        return f"{self.character_name} played by {self.player_name} with {self.influence} influence and {len(self.hand)} cards in hand"
