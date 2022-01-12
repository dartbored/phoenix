init python:

    class ProgressTracker(object):
        'Class for tracking progres in the game, including clues'

        def __init__(self, landmark, newgameplus=False):
            self.landmark = landmark
            self.location = 'police'
            self.plus = newgameplus
            self.chars = []
            self.clues = []

        def addclue(self, clue):
            self.clues.append(clue)
            renpy.notify("New clue found!")
            if clue.suspects:
                for suspect in clue.suspects:
                    suspect.sus += clue.weight

        def hasclueid(self, topic):
            for clue in self.clues:
                if clue.id == topic:
                    return True

    class Chara(object):
        'Class for tracking character information and stats'

        def __init__(self, name, bio):
            self.name = name
            self.bio = bio
            self.aff = 0
            self.sus = 0

    class Clue(object):
        'Class for showing clues'

        def __init__(self, topic, info, suspects=[], weight=5):
            self.id = topic
            self.info = info
            ## suspects: put the character variable so we know who to add sus to
            self.suspects = suspects
            self.weight = weight
            #notif
            ## to make the final conclusion, player needs clues of a certain number of topics
            ## some topics are necessary, but some can be replaced with others

        def edit(self, newinfo):
            self.info = newinfo
            renpy.notify("Clue updated!")
            # notif
