# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define DetectiveLumiere = Character("Elowen Lumiere")
define Verus = Character("Verus Lumiere")
define anom = Character("???")
define Rex = Character("Prosecutor Arlinpagne II")
define Judge = Character("Judge")


# The game starts here.
label start:
    play music one

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg desk_judge
    show Judge
    Judge "Would you kindly state your name and occupation to this courtroom?"
    scene bg desk_defendant
    show Anom
    anom "…sure. i suppose i don’t mind."
    show Verus
    Verus "Vmy name is Verus Lumiere. i suppose i was a college student until about 8:10pm last night, when I was apprehended by detective bruntforce and taken to the detention center. I guess my profession now would be best described as… ‘defendant"
    scene bg desk_judge
    show Judge
    Judge " Lumiere? Where have I heard Lumiere before…"

    Judge "Oh… OH"
    scene bg desk_defendant
    Show DetectiveLumiere
    DetectiveLumiere "…" 

    DetectiveLumiere "Are you sure you are comfortable talking about what happened to Myra?"

    show Verus
    Verus "I received a text from Myra at around 6:30pm."
    Verus "We haven’t spoken for some years, so I was caught off guard by her message."
    Verus "She said to meet her at her new place at 8:30pm."
    show DetectiveLumiere
    DetectiveLumiere "She reached out to you? After keeping you in the dark for so long, why did she choose to speak with you now?"
    show Verus
    Verus "I don’t know, and it seems like I will never know."
    Verus "She really wanted to fix our friendship that night, and she never got the chance..."
    scene bg desk_judge
    show Judge
    Judge "..."
    scene bg desk_prosecutor
    show Rex
    Rex "..."
    scene bg desk_defendant
    show DetectiveLumiere
    DetectiveLumiere "Seems like everyone is feeling the impact of this travesty."
    show Verus
    Verus "...to think I even tried to see her earlier..."
    Verus "However, I couldn’t wait to see her."
    show DetectiveLumiere
    DetectiveLumiere "Why couldn’t you wait until 8:30pm to see her?"
    show Verus
    Verus "Would you be able to sit with something that heavy for that long?"
    Verus "To have the person closest to you completely abandon you, not responding to your attempts at closure, but suddenly reaches out to you as if nothing happened?"
    show DetectiveLumiere
    DetectiveLumiere "I suppose not."
    show Verus
    Verus "I had a lot to I wanted to say to her...but I suppose it will remain unsaid."
    scene bg desk_prosecutor
    show Rex
    Rex "What happened when you arrived at her estate?"
    scene bg desk_defendant
    show Verus
    Verus "It was about 7:45pm when I knocked on her door."
    Verus "She didn’t answer, but as I turned to leave, I heard a loud crash from inside."
    show DetectiveLumiere
    DetectiveLumiere "A loud crash? Please, tell us more!"
    show Verus
    Verus "I guess it was more like two sounds."
    Verus "I heard a loud sound as I was leaving, almost like the smashing of glass."
    Verus "I called out for Myra, becoming aware of the potential danger that might be lurking around in there."
    Verus "...but it would seem that I wasn’t fast enough to protect her."
    
    Verus "I frantically messed with the doorknob, which happened to be unlocked, and ran inside."
    show DetectiveLumiere
    DetectiveLumiere "The door was unlocked?"
    show Verus
    Verus "I didn’t question it at the time."
    
    Verus "I discovered her body in her study."
    Verus "Unable to move, I hovered there in front of her corpse until Bruntforce appeared on the scene."
    show DetectiveLumiere
    DetectiveLumiere "So you stood there and did nothing?"
    show Verus
    Verus "Yes, I- I was frozen in place."
    scene bg desk_judge
    show Judge
    Judge "That is understandable. I can’t imagine what you must have been going through your mind. I am sorry that you had to suffer such a terrible experience."
    scene bg desk_defendant
    show DetectiveLumiere
    DetectiveLumiere "..."

    DetectiveLumiere "I don’t know why, but I know Verus is not telling the whole truth."
    DetectiveLumiere "He’s holding back, and if I am to save him, I have to bring out the ugly truth he harbors."
#(Loops dialogue)

#Present the Standing Lamp on this dialogue

#"i discovered her body in her study. Unable to move, I hovered in front of her corpse until bruntforce appeared to on the scene."

#DESIST!
show DetectiveLumiere
DetectiveLumiere "..."

DetectiveLumiere  "Verus, if you want me to get you out of this situation, you’re going to have to tell the truth."
show Verus
Verus "!!"
show DetectiveLumiere
DetectiveLumiere  "You said that you 'hovered in front of her corpse until Bruntforce arrived'. Is this true?"
show Verus
Verus "...yes it is."
show DetectiveLumiere
DetectiveLumiere  "Then why were your fingerprints found on this lamp!"
show Verus
Verus "!!"
scene bg desk_judge
show Judge
Judge  "Huhhh?"
scene bg desk_prosecutor
show Rex
Rex  "…"

#(courtroom chatter)
scene bg desk_judge
show Judge
Judge  "Order please! We need to get to the bottom of this!"
Judge "Verus, why did you lie about not touching the body?"
scene bg desk_defendant
show Verus
Verus  "...because of how I found the body."
show DetectiveLumiere
DetectiveLumiere "!!"
scene bg desk_judge
show Judge
Judge "Order please! We need to get to the bottom of this!"

Judge "Verus, why did you lie about not touching the body?"
scene bg desk_defendant
show Verus
Verus "…because...of how I found the body."
show DetectiveLumiere
DetectiveLumiere "!!"
scene bg desk_prosecutor
show Rex
Rex "Maybe you should also testify to the state of the body as you discovered it, including the reason why you tampered with the evidence."
scene bg desk_defendant
show Verus
Verus "…okay. I can do it."

return
