label firehouse:
    $ progress.location = 'firehouse'
    scene station4
    if len(progress.clues) == 0:
        jump firehouse1
    elif progress.landmark == 'rising' and len(progress.clues) == 1:
        jump firehouse2
    else:
        jump firehousenothing

label firehouse1:
    ## firefighter pole somewhere
    "The firehouse is relatively new, and gives off a refined air."
    "The garage doors are open, and you can see some of the crew hanging around the main engine."
    "They see you approaching and some give you a friendly wave."
    menu:
        "Wave back":
            $ maleko.aff += 2
            $ vincent.aff += -1
            "You wave at the firefighters."
        "Pretend you don't see them":
            $ maleko.aff += -1

    "Thinking back to what the report said, you know that the arsonist has to be someone with inside knowledge of the fire department."
    "It could be anyone, so you keep a keen eye as you walk up to the fire crew."
    "Before you can get a word out, one of them stands and meets you at the opening of the garage."

    show maleko

    ff "What can I do for you, officer?"

    menu:
        # "Say Statement"
        "I'll need to ask you and your crew some questions.":
            ff "No problem. I assume this is about the fires downtown?"

            "You nod and pull out your notepad."

            yo "Now can I get your name and rank, please?"

            fc "Fire Captain Malenko of Fire Station 4."
            $ progress.chars.append(maleko)
            fc "Would you mind if I get your name as well?"

            yo "Detective [name] from the main precinct. I'm new around here."

            fc "I can tell. I know most of the officers and detectives around here."
            fc "Let me guess, you're a big city cop who decided to strike out on your own in a post-industrialist micro metropolitan township?"

            "That's almost exactly why you're here. You thought there would be better vertical mobility if you moved out of the city and into a smaller district."
            "He laughs at your shocked expression."

            fc "Don't sweat it, it's more common than you think."
            fc "Anyway, you wanted to ask about the Phoenix fires?"

            "Phoenix? Like the mythical bird creature that can be reborn from its own ashes?"

            yo "Are the fires really called that?"

            fc "Well, ever since we realized it was a pattern, we joked that the person lighting the fires is like a phoenix: always coming back."
            fc "And everyone has been talking nonstop about the fires, so the name kind of stuck."

            $ progress.addclue(phoenixname)

            yo "Do you think it's the same person lighting all the fires?"

            fc "It has to be. I was there when all of them were being put out. The type of building, the speed of the fire, the fuel used... It was all nearly identical."
            fc "I hate to think that someone in our department is going out and committing arson in residential areas..."

            fc "But from what I've seen, the arsonist has to have some knowledge of our protocols."

            "Maleko goes quiet at that, obviously unsettled by that implication."

            fc "Well, if you need to—"

        "How did you know I'm with the police?":
            ff "Well, who else would be swinging by the station on a Monday morning?"
            ff "This isn't exactly the social hub of the town, unfortunately."

            ff "It's nice to meet you though, officer..."

            yo "[name]. And it's detective, actually."

            "He extends his hand for you to shake, and then leads you into the firehouse."

            ff "My apologies, Detective [name]. I didn't think they'd send the big guns over so soon."

            "He returns to his place by the fire engine, though most of the crew has wandered off to work on various things."

            fc "You can call me Maleko, but most of my crew just call me captain."

            $ progress.chars.append(maleko)

            "So this is the captain of Station 4. He's a lot more friendly than what you expected of someone whose crew is under investigation."
            "Setting that thought aside, you pull out your notepad, ready to jot down any clues."

            yo "So you don't get any civilian visitors at the station?"

            "He shakes his head."

            fc "Not that I know of. It's pretty quiet around here."

            yo "And you haven't seen any strangers or unusual people around the station recently?"

            "He laughs a little at that, surprised."

            fc "Not at all. The only people I see coming in are my teammates."

            ## new clue!!
            $ progress.addclue(visitfirehouse)

            fc "But your visit is most welcome. It's great to see a new face around here, even if it's just to ask us some questions."
            fc "Station 4 will happily cooperate with your investigation."


    "All of a sudden, alarms and bells fill the station with noise."
    "What was a relatively calm scene two seconds ago has now turned into a whirlwind of boots and belts and heavy jackets."
    "A grave expression falls over the fire captain's face, and he turns back to you for a moment."

    fc "I gotta go, but feel free to stop by later."

    "He looks around at the station, listens to his radio, shouts some orders, then turns back to you."

    fc "Probably a lot later."

    "With that, he swings up into the fire truck, and they roll out of the garage, sirens and bells filling the air with noise."

    "You have a feeling you should head back to the precinct and share your new clues with the sergeant."

    jump map

label firehouse2:
    "The bay doors are wide open, and the firefighters inside are hustling around just like before."
    "You look around for Maleko, but he's not anywhere near the engines."
    "Peeking into the lounge, you see someone with their nose buried in a thick book."
    "They seem unaware of your presence."
    menu:
        "What should you do?"
        "Ask where Maleko is":
            yo "Excuse me, is the Captain around."

            ff "Who's asking?"

            "You flash your badge at them."
            yo "Detective [name]."
        "Ask them what they know about the fires":
            yo "Excuse me, I'm Detective [name]. You mind if I ask you a few questions?"

            "They look up from their book."

            nf "Sure, though I can't say I know much about them."

            yo "You weren't on the call when any of them happened?"

            nf "I haven't been on a call in almost a month."

    jump map

label firehousenothing:
    cycle firehousenull:
        block:
            "The big garage doors are open, but the trucks and engines aren't inside."
            "They must be out on a call. Maybe they will be back later."
        block:
            "As you slip into the firehouse, you can see some of the crew lounging around."
            "Maleko is taking swings at a punching bag mounted in the back, Vincent is in the lounge with a fresh bowl of mac and cheese, and Hyde is at his locker, fiddling with his turnout gear."
            "Maybe now would be a good time to talk with one of them."
            menu:
                "Maleko":
                    jump malekonull
                "Vincent":
                    jump vincentnull
                "Hyde":
                    jump hydenull

    jump map

label malekonull:
    "Maleko sees you walking over and stops the punching bag with his arm."
    fc "Hey, Detective! Nice to see you around."
    fc "Having any luck with the case?"
    jump map

label vincentnull:
    "Hey."
    jump map

label hydenull:
    "Nice weather we're having."
    jump map
