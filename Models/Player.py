import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../"
class Player:
    def __init__(self):
        self.score = 0
        pass

    def add_score(self, extra_score):
        self.score += extra_score

    def minu_score(self, minu_score):
        self.score -= minu_score

    def save_score(self):
        print(self.score)
        fileTXT = open(f"{ROOT_DIR}best_score.txt", "w")
        fileTXT.write(str(self.score))
        fileTXT.close()

    def get_message_score(self):
        return f"Điểm của bạn là: {self.score}"