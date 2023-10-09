# Define the Batsman class
class Batsman:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is batting.")

# Define the Bowler class
class Bowler:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is bowling.")

# Create objects of the Batsman and Bowler classes
batsman1 = Batsman("Sachin")
bowler1 = Bowler("Warne")

# Call the play() method for each object
batsman1.play()  # Sachin is batting.
bowler1.play()   # Warne is bowling.