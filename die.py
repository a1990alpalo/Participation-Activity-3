from random import randint

class Die:
    """Represent a die that can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die with a default number of sides."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides."""
        print(randint(1, self.sides))


six_sided_die = Die()

print("Rolling a 6-sided die 10 times:")
for number in range(10):
    six_sided_die.roll_die()


ten_sided_die = Die(10)

print("\nRolling a 10-sided die 10 times:")
for number in range(10):
    ten_sided_die.roll_die()


twenty_sided_die = Die(20)

print("\nRolling a 20-sided die 10 times:")
for number in range(10):
    twenty_sided_die.roll_die()