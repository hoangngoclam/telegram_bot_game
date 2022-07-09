import random
class GameComputer:
    def __init__(self):
        self.actions = ["rock", "paper", "scissors"]
        self.icons = ["✊", "✋", "✌️"]
        self.computer_action = ""
        self.player_action = ""
    
    def get_computer_action(self):
        return random.choice(self.actions)

    def play(self, player_action):
        self.computer_action = self.get_computer_action()
        self.player_action = player_action

    def get_game_play_message(self, player_action):
        computer_index_icon = self.actions.index(self.computer_action)
        player_index_icon = self.actions.index(player_action)
        computer_icon = self.icons[computer_index_icon]
        player_icon = self.icons[player_index_icon]
        return f"😼{computer_icon} vs {player_icon}🙂"

    def get_result(self):
        if self.player_action == self.computer_action:
            return "tie"
        elif self.player_action == "rock":
            if self.computer_action == "scissors":
                return "win"
            else:
                return "lose"
        elif self.player_action == "paper":
            if self.computer_action == "rock":
                return "win"
            else:
                return "lose"
        elif self.player_action == "scissors":
            if self.computer_action == "paper":
                return "win"
            else:
                return "lose"
        pass