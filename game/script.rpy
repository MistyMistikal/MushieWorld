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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg desk_prosecutor
    show Rex
    Rex "Would you kindly state your name and occupation to this courtroom?"
    scene bg desk_defendant
    show Anom
    anom "…sure. i suppose i don’t mind."
    show Verus
    Verus "My name is Verus Lumiere. i suppose i was a college student until about 8:10pm last night, when I was apprehended by Detective Bruntforce and taken to the detention center. I guess my profession now would be best described as… ‘defendant'."
    scene bg desk_judge
    show Judge
    Judge "Lumiere? Where have I heard Lumiere before…"

    Judge "Oh… OH"
    scene bg desk_defendant
    Show DetectiveLumiere
    DetectiveLumiere "…" 

    DetectiveLumiere "Are you sure you are comfortable talking about what happened to Myra?"
    show Verus
    Verus "...i have to, Mom. MaiMai wanted...needed to show me this.
    Verus "i have to see this through, even if I risk my own life."
    show DectectiveLumiere
    Lumiere "...okay. If this is what you want..."
    scene bg desk_prosecutor
    show Rex 
    Rex "Please testify to the events that lead you to discover the body."
    scene bg desk_defendant
    show Verus
    Verus "...yeah, sure."

    # Cross-Examination Intro section
    # Animation and Music cues in

    show Verus
    
    # Could our Anom 'character' be used to say the following text:
    # "- how i found the body -"
    # the music would play after this text

    play music one

    Verus "i received a text from Myra at around 6:30pm. we haven’t spoken for some years, so i was caught off guard by her message."
    Verus "she said to meet her at her new place at 8:30pm, but i couldn't wait to see her."
    Verus "she didn't answer when i arrived around 7:45pm, but as i turned to leave, i heard a loud crash from inside."
    Verus "i frantically funmbled with the doorknob until it unlocked, and ran inside."
    Verus "i discovered her body in her study. frozen in place, i remained by her side until Bruntforce arrived."

    fade out music one

    # Quick reflection on the testimony

    scene bg desk_judge
    show Judge
    Judge "I can’t imagine what that must have been like, seeing such a horrific sight of someone you once deeply cared about."
    scene bg desk_defendant
    show Verus
    Verus "i can still see the shock in her eyes. she didn't even see her attacker coming..."
    scene bg desk_prosecutor
    show Rex
    Rex "...she was most definitely taken by surprise."
    scene bg desk_defendant
    show Lumiere
    Lumiere "Verus..." # internal monologue

    # Cross-Examination gameplay section
    # Animation and Music cues in

    show Verus
    
    # Could our Anom 'character' be used to say the following text:
    # "- how i found the body -"
    # the music would play after this text

    play music one

    # Pressing Statement 1
    Verus "i received a text from Myra at around 6:30pm. we haven’t spoken for some years, so i was caught off guard by her message."
    # Halt! - animation and expands on the statement
    show DetectiveLumiere
    DetectiveLumiere "She reached out to you? After keeping you in the dark for so long, why did she choose to speak with you now?"
    show Verus
    Verus "i don’t know, and it seems like i will never know."
    Verus "She really wanted to fix our friendship that night, and she never got the chance..."
    scene bg desk_judge
    show Judge
    Judge "..."
    scene bg desk_prosecutor
    show Rex
    Rex "..."
    scene bg desk_defendant
    show DetectiveLumiere
    DetectiveLumiere "Seems like everyone is feeling the impact of this travesty." # internal monologue
    show Verus
    Verus "...to think I even tried to see her earlier..."
    
    # Pressing Statement 2
    Verus "she said to meet her at her new place at 8:30pm, but i couldn't wait to see her."
    # Halt! - animation and expands on the statement
    show DetectiveLumiere
    DetectiveLumiere "Why couldn’t you wait until 8:30pm to see her?"
    show Verus
    Verus "would you be able to sit with something that heavy for that long?"
    Verus "to have someone close to you abandon you, ghost you for years, and suddenly reach out as if nothing happened?"
    show DetectiveLumiere
    DetectiveLumiere "...I suppose not."
    show Verus
    Verus "I had a lot to I wanted to say to her...but I suppose it will remain unsaid."
    scene bg desk_prosecutor
    show Rex
    Rex "What happened when you arrived at her estate?"
    
    #Pressing Statement 3
    scene bg desk_defendant
    show Verus
    Verus "she didn't answer when i arrived around 7:45pm, but as i turned to leave, i heard a loud crash from inside."
    # Halt! - animation and expands on the statement
    show DetectiveLumiere
    DetectiveLumiere "A loud crash? Please, tell us more!"
    show Verus
    Verus "i guess it was more like two sounds."
    Verus "they happened in quick succession, the second louder than the first." 
    Verus "it was almost as if glass was shattering."
    Lumiere "!!" #play realization sfx
    Verus "i called out for Myra, trying to save her from the danger approaching her."
    Verus "...but it would seem that I wasn’t fast enough to protect her."

    #Pressing Statement 4
    Verus "i frantically funmbled with the doorknob until it unlocked, and ran inside."
    # Halt! - animation and expands on the statement
    show DetectiveLumiere
    DetectiveLumiere "The door was unlocked?" # Mysterious sfx over 'unlocked'
    show Verus
    Verus "i didn’t question it at the time."
    Verus "i was more focused on finding Myra."
    Verus "...unfortunately, i did."

    # Pressing Statement 5
    Verus "i discovered her body in her study. frozen in place, i remained by her side until Bruntforce arrived."
    # Halt! - animation and expands on the statement
    show DetectiveLumiere
    DetectiveLumiere "So you stood there and did nothing?"
    show Verus
    Verus "Yes, I- I was frozen in place." 
    scene bg desk_judge
    show Judge
    Judge "That is understandable. I can’t imagine what you must have been going through your mind." 
    Judge "I am sorry that you had to suffer such a terrible experience."
    scene bg desk_defendant
    Verus "ah...thank you..."
    scene bg desk_prosecutor
    show Rex 
    Rex "...yes, most people would be frozen in place, wouldn't they?"
    scene bg desk_defendant
    show DetectiveLumiere
    DetectiveLumiere "..."

    # Internal Monologue
    DetectiveLumiere "I don’t know why, but I know Verus is not telling the whole truth." 
    DetectiveLumiere "He’s holding back, and if I am to save him, I have to bring out the ugly truth he harbors."

#(Loops dialogue)

#Present the Standing Lamp on this dialogue

#"i discovered her body in her study. Unable to move, I hovered in front of her corpse until bruntforce appeared to on the scene."

#DESIST! Scene change
fade out music one

show DetectiveLumiere
DetectiveLumiere "..."
DetectiveLumiere  "Verus, if you want me to get you out of this situation, you’re going to have to start telling the truth."
show Verus
Verus "!!" #play realization sfx
show DetectiveLumiere
DetectiveLumiere "You said that you were 'frozen in place' until Bruntforce arrived. 
DetectiveLumiere "Is this true?"
show Verus
Verus "...yes it is."
show DetectiveLumiere
# slam effect?
DetectiveLumiere "Then why were your fingerprints found on this lamp!" # play desist theme at the end of this line
show Verus
Verus "!!" # play mysterious sfx
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
Judge "Verus, why did you lie about being frozen in place?"
scene bg desk_defendant
show Verus
Verus  "...because of how i found the body." # fade out the desist theme
show DetectiveLumiere
DetectiveLumiere "!!" # play mysterious sfx
scene bg desk_prosecutor
show Rex
Rex "Maybe you should also testify to the state of the crime scene, including the reason why you tampered with the evidence."
scene bg desk_defendant
show Verus
Verus "…okay. I can do it."

return
