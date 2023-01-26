import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        # brains = 0
        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']

        #     if brains < 2:
        #         diceRollResults = zombiedice.roll() # roll again
        #     else:
        #         break
       
        # brains = 0
        # ram = 1
        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']
        #     if ram != 0:
        #         ram = random.randint(0,1)
        #         diceRollResults = zombiedice.roll() # roll again
        #     else:
        #         break

        # brains = 0
        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']
        #     if diceRollResults['brains'] == 2:
        #         break
        #     else:
        #         diceRollResults = zombiedice.roll() # roll again
        # brains = 0

        # while diceRollResults is not None:
        #     brains += diceRollResults['brains']
        #     if diceRollResults['shotgun'] == 2:
        #         break;
        #     else:
        #         diceRollResults = zombiedice.roll() # roll again

        # brains = 0
        # while diceRollResults is not None:
        #     ram = random.randint(1,4)
        #     temp = 0
        #     brains += diceRollResults['brains']
        #     if ram > temp:
        #         temp += 1
        #         diceRollResults = zombiedice.roll() # roll again
        #     elif diceRollResults['shotgun'] == 2:
        #         break;
        #     else:
        #         diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if diceRollResults['shotgun'] > diceRollResults['brains']:
                break;
            else:
                diceRollResults = zombiedice.roll() # roll again


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
