# Create a class for a user / skater
class Player:
    def __init__(self, name, score, total):
        self.name = name
        self.score = score
        self.total = total

    def update_score(self, add):
        self.score += add

    def update_total(self, total):
        self.total += total

    def get_percentage(self):
        return round(float(int(self.score) / int(self.total)) * 100)


if __name__ == "__main__":
    main()
