# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define pc = Character("Sgt. Nathaniel")
define yo = Character("You")
define po = Character("Elliot")
define ff = Character("Firefighter")
define fc = Character("Cpt. Maleko")
define nf = Character("Vincent")
define vf = Character("Hyde") ## Hyde
define fi = Character("Fiore")

image splash = "splash.png"

label splashscreen:
    scene white
    with Pause(1)

    show text "SENUE Presents" with dissolve
    with Pause(2)

    # play sound "ping.ogg"

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return
# The game starts here.
default persistent.finished_game = False
default newgameplus = False

label start:
    $ progress = ProgressTracker('exposition', newgameplus)
    if newgameplus:
        jump game_plus
    else:
        pass

    python:
        elliot = Chara('Elliot', 'One of the best detectives at the station. She has a greivance with how the fire department is spending their budget.')
        nathan = Chara('Nathaniel', "Your new sergeant. He's awkward but not unfriendly, and seems to want to have nothing to do with the arson case.")
        vincent = Chara('Vincent', "One of the newer firefighters at Station 4. Currently out of active duty due to a medical concern. Introverted and quick to anger.") ## he just inspects buildings now, until he is fully healed, didnt want to join military, he is actually funny and writes poetry. he was a poetry slam on the night of two of the fires, doesnt want to tell that, active fire marshall
        maleko = Chara('Maleko', "Fire Captain of Station 4. Certified in hazmat tech and wildfire supression. He is admired and respected by all members of his team.") ## pacific islander, really loves his job, was a chemical engineering major in college. loves the team, especially vincent. very welcoming and wants to help detective, is friends with nathaniel.
        fiore = Chara('Ms. Fiore', "A young entepreneur looking to get a foothold in the downtown real estate scene. She has had multiple feuds with the city fire inspectors.") ## recently broke up with bf who has a better business than her, wanted to prove him wrong
        hyde = Chara('Hyde', "A volunteer firefighter at Station 4. Early retiree, has a lot of time on his hands. Doesn't appear to enjoy firefighting.") # kicked out of dads company for being too immature and reckless, he is lonely, has connection to fiore

        ## CLUES
        visitfirehouse = Clue("firehouse gets no visitors", "{b}Maleko{/b} claims that no one suspicious has been visiting the fire station. Only police and firefighters have entered the station.")
        phoenixname = Clue("phoenix name", "The person lighting the fires has been nicknamed {b}Phoenix{/b} because of how similar the arson incidents are. Same location, same ignition method, same target.")

        oldbuildings = Clue("fiore wants renovation", "The targeted buildings were all old brick apartments owned by {b}Ms. Fiore{/b}. However, she was not the one who called 9-1-1.", [fiore], 10)
        fiorebuildings = Clue("fiore wants renovation", "{b}Ms. Fiore{/b} owns the apartments that were targeted by the arsonist. She has been cited several times by the fire marshall for not following fire code.", [fiore], 15)

        vincentinspect = Clue("buildings up to code", "{b}Vincent{/b} has recently taken up the role of fire marshall. He claims that all the buildings were up to code when they burned down.", [vincent], 5)
        inspecttogether = Clue("buildings up to code", "From {b}Vincent's{/b} inspection and the fire code manual, it appears that all Fiore's buildings are up to code.")

        insurancestatements = Clue("big insurance", "According to statements found on her desk, {b}Ms. Fiore{/b} bought a large insurance policy for her apartment complexes.", [fiore], 15)

        hydejob = Clue("hyde hates job", "Despite being a wealthy early retiree, {b}Hyde{/b} volunteers as a firefighter. He does not appear to enjoy the work.", [hyde], 10)
        malekohyde = Clue("hyde hates job", "{b}Maleko{/b} claims that {b}Hyde{/b} hasn't adjusted well to firefighting, and doesn't appear to enjoy his shifts.", [hyde], 5)

        hydefiore = Clue("hyde knows fiore", "{b}Hyde{/b} and {b}Fiore{/b} were together near one of Fiore's buildings. They appeared to be arguing.", [hyde, fiore], 5)


    ## show newspaper of neighborhood fire incidents
    ## short exposition of player character

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene precint

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    "The police station is bustling with activity. Detectives run from desk to desk, exchanging notes, signing documents, and digging up files."

    "And on occasion, they whisper and cast a glance in your direction."

    "As the newest addition to the forensics team, you've barely had a chance to unpack your uniform, much less meet-and-greet with the rest of the officers."

    "To make things worse, the desk they gave you looks like it hasn't been used in years."

    "Dust and grime covers the top, and when you pull out one of the drawers, there's nothing but cobwebs."

    "Just as you were beginning to regret leaving your old precinct, you spy someone walking toward your desk."

    show nathaniel

    "It's Sergeant Nathaniel Flament. He gives you a strained smile as he comes up to where you're standing."

    $ progress.chars.append(nathan)

    pc "Good morning, Detective."

    "From how tired he looks, you can tell it's been a long one too."

    pc "Hope you've had time to settle in and all."
    pc "Also, I, uh, didn't catch your name earlier. Could you remind me?"

    python:
        name = renpy.input("Enter your name.")
        name = name.strip() or "Rouge"

    pc "Alright Detective [name], welcome to the team."

    "He gives your hand a firm shake, and a genuine smile lights up his face."

    pc "Gotta admit, exchanging pleasantries isn't my forté. You're probably tired of my talking, so let's cut to the chase."
    pc "Did you see the case I put on your desk?"
    $ looked_at_files = False

    show screen openfiles
    pc "I need you to take a look at what's going on with the fire department."
    pc "We'll need all hands on deck if we want to prevent downtown from going up in flames."

    yo "Yes, chief. I'll be right on it."

    pc "Good. Once you give it a look-over, head over to Elliot. She's just over there at her desk. I want y'all working together on this case."

    "He looks about ready to leave, but just before he does, he turns back to you."

    pc "Hey, I know you were a real hot shot wherever you came from, but Elliot will help you get adjusted to how we do things here."
    pc "This isn't a sprawling metropolis where you can just accuse anyone of anything."
    pc "We are a community, and people don't take nicely to being seen as suspects."

    "He nods to you, then ambles back to his office."
    hide nathaniel

    show screen elliotdesk(progress)

    "Go to Elliot" (advance=False)

    label meetelliot:
        scene precint
        show elliot
        hide screen elliotdesk
        $ progress.chars.append(elliot)
        po "So you're the new detective. You look pretty green."
        po "I'm Elliot, and it looks like we've been thrown together in this mess."
        "She slaps her hands down on the stacks of files and printouts on her desk."
        po "You've read the debrief, right?"

        menu:
            "Did you read the debrief?"
            "Yes" if looked_at_files:
                po "Okay, great. That means you know the nonsense that we are dealing with."
                po "The fire department is having trouble doing its one job: stopping fires."
                po "There have been at least 3 incidents of what the chief suspects is arson over the past few weeks."
                $ elliot.aff += 5
            "Yes" if not looked_at_files:
                po "Oh really?"
                "She doesn't look impressed."
                po "I can tell you're lying. I went through detective school too, you know."
                po "If we're going to work together, you're going to need to keep up with protocol."
                po "That means no slacking, especially not on paperwork."
                po "Now let's get you up to speed..."
                po "The fire department is having trouble doing its one job: stopping fires."
                po "There have been at least 3 incidents of what the chief suspects is arson over the past few weeks."
                $ elliot.aff += -5
            "No":
                "She gives you a dirty look."
                po "I don't know what kind of operations they ran at your old precinct, but here we actually get things done."
                po "That means no slacking, especially not on paperwork."
                po "Now let's get you up to speed..."
                po "The fire department is having trouble doing its one job: stopping fires."
                po "There have been at least 3 incidents of what the chief suspects is arson over the past few weeks."
                $ elliot.aff += -3

        po "The first time it happened, the fire department ran in and did their thing, and now they seem to be handling these newer fires {i}worse{/i} than they did initially."

        po "I can't believe it! They have a bigger budget than us and they're never understaffed and yet—"

        "She cuts herself off and takes a deep breath to reel in her temper. It's obvious she has some serious greivance with the fire station."

        po "Let's just cut to the point. You need to go down to the firehouse and collect some statements. Maybe they'll give us a clue to how incompetent they are, though I don't need one."

        po "I know the chief thinks it's someone setting fire to buildings, but I just think it's fire inspectors getting paid to look the other way."

        po "This whole investigation is probably moot, but until the chief decides the same, we're on the case."

        po "Now go out there and try to get some clues out of those firefighters."

        jump map

        label map:
            scene
            call screen map(progress)
            $ renpy.choice_for_skipping()
            $ renpy.jump(_return)




    # This ends the game.

    return
