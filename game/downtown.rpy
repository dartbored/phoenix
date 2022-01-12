label downtown:
    scene brownstone
    if len(progress.clues) == 1:
        jump downtown1
    else:
        jump downtownnothing


label downtown1:
    "At last, the scene of the crime."
    jump map
