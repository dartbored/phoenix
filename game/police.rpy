label police:
    $ progress.location = 'police'
    scene precint
    if len(progress.clues) == 0:
        scene precint
        show elliot
        pc "Didn't I tell you to go down to Station 4 and find some clues?"
        jump map
    elif len(progress.clues) > 0 and progress.landmark == 'exposition':
        jump police1
    elif progress.landmark == 'rising' and len(progress.clues) > 1:
        jump police2
    else:
        jump policenothing

label police1:
    "The precinct is just as busy as ever."
    "Before you can even reach your desk, Elliot is in front of you."
    show elliot

    po "Did you talk to the fire captain?"

    "You nod and begin to explain what Maleko told you."

    if progress.hasclueid("phoenix name"):
        po "Huh, that's interesting."
        po "I guess whoever is doing this is really meticulous."
        po "It wouldn't be a bad idea to go visit the scene of the crime and try to collect more clues."
    else:
        po "So I guess that rules out random civilians."
        po "I'm not surprised no one drops by the fire station, to be honest."
        po "Even if you wanted to circumvent their internal protocols, you wouldn't learn much when they're just hanging around the firehouse."
        po "When you get a chance, maybe you should talk more with the other firefighters."

    $ progress.landmark = 'rising'
    po "Do you have any quesions for me?"
    menu howto:
        "How do I find more clues?":
            po "Just go out and talk to people. Maybe they saw something or heard something suspicious."
            jump howto
        "How do I know someone is telling the truth?":
            po "You don't."
            po "You just have to compare clues from different people and try to infer who is telling the truth."
            po "In your files, there should be graphics representing each suspect's suspicion level."
            po "The more suspicious they are, the more likely they are to be the culprit."
            jump howto
        "I don't have any questions.":
            po "Alright, go find clues then."
            jump map

label policenothing:
    show nathaniel
    pc "You find any good clues recently?"
    jump map
