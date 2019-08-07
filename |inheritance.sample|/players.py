# It was adopted from yazbel/python-istihza


# Firstly we defined general Player class.

class Player():
    def __init__(self, name, duty):
        self.name = name
        self.duty = duty
        self.health = 0

    def make_move(self):
        print("Moved.")

    def make_point(self):
        print("Points have been earned.")

    def lose_point(self):
        print("Points have been lost.")

# Three diffrence class defined in Player class as subclass
# If we call any class below here it will bring main classes features. But we want unique values for some features
# In here we changed health values for all subclass help with super() method

class Soldier(Player):
    def __init__(self, name, duty):
        super().__init__(name, duty)
        self.health = 100

# We can make short code with using --*args-- method. Below codes has same process wiht above code. 

class Worker(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.health = 75

class Monk(Player):
    def __init__(self, *args):
        super().__init__(*args)
        self.health = 50
