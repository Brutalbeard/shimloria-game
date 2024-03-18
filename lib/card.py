class Card():
    def __init__(self, name, flavor_text, player_add, player_subtract, target_add, target_subtract) -> None:
        self.name: str = name
        self.flavor_text: str = flavor_text
        self.player_add: int = player_add
        self.player_subtract: int = player_subtract
        self.target_add: int = target_add
        self.target_subtract: int = target_subtract

    def apply(self, player, target_player=None) -> None:
        player.add_influence(influence=self.player_add)
        player.remove_influence(influence=self.player_subtract)

        if target_player is not None:
            target_player.add_influence(influence=self.target_add)
            target_player.remove_influence(influence=self.target_subtract)

    def __str__(self) -> str:
        return f"{self.name} - {self.flavor_text} (me: +{self.player_add}/-{self.player_subtract} them: +{self.target_add}/-{self.target_subtract})"