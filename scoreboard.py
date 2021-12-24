

class Scoreboard():

    def __init__(self):
        self.current_score = 0

    def increase_score(self):
        self.current_score += 1

    def highscores(self):
        with open("highscores.txt", "r") as file:
            score = int(file.read())

            if self.current_score > score:
                with open("highscores.txt", "w") as another_file:
                    another_file.write(str(self.current_score))
