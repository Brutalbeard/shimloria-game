from lib.player import Player
import random

player_names: list[str] = [
    "Colin",
    "Bre",
    "Heather",
    "John",
]

character_names: list[str] = [
    "The General",
    "Heir Apparent",
    "The Princess",
    "The Emperor",
]


class Game:
    def __init__(self, number_of_players: int) -> None:
        self.players: list[Player] = []
        self.active_player = None
        self.number_of_rounds = 0
        self.winner = None
        self.create_players(number_of_players=number_of_players)

    def round(self) -> Player | None:
        self.number_of_rounds += 1
        for player in self.players:
            self.active_player: Player = player
            self.players.remove(player)
            self.player_turn(player=player)
            self.players.append(player)
            self.active_player = None
            if self.winner:
                return self.winner

    def player_turn(self, player: Player) -> None:
        player.draw()
        player.play_card(
            card=player.hand[0], target_player=random.choice(seq=self.players)
        )

        if player.influence >= 15:
            self.winner: Player = player
            return

    def create_players(self, number_of_players: int) -> list[Player]:
        players: list[Player] = []
        random.shuffle(x=character_names)
        random.shuffle(x=player_names)
        for i in range(number_of_players):
            players.append(
                Player(player_name=player_names[i], character_name=character_names[i])
            )
        self.players = players
