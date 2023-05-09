#LMSC-261: The Blessed Slime

#Character colour
define Zoey = Character('Zoey', color="06F7FF")
define Ronan = Character('Ronan', color="FF06E1")
define Josh = Character('Josh', color="FF8306")
define Slime = Character('Slime', color="33FF06")

#images label
image zoey smile 1 = "Zoey smile 1.png"
image zoey smile 2 = "Zoey smile 2.png"
image zoey annoyed = "Zoey Annoyed 1.png"
image zoey neutral 2 = "Zoey Neutral 2.png"
image zoey angry 2 = "Zoey Angry 2.png"
image josh smile = "Josh_smile.png"
image josh happy = "Josh_happy.png"
image josh neutral = "Josh_neutral.png"
image josh bored = "Josh_bored.png"
image josh angry = "Josh_serious.png"
image josh serious = "Josh_serious.png"
image ronan happy = "Boy_Happy.png"
image ronan confused = "Boy_Confused.png"
image ronan scared = "Boy_Scared.png"
image ronan surprised = "Boy_Surprised.png"
image ronan blush = "Boy_Blush.png"
image slime mad = "slime mad.png"
image slime sad = "slime sad.png"
image slime neutral = "slime neutral.png"

#background label
image path 1 = "bg path 1.png"
image clearing 1 = "Clearing 1.png"
image path 5 = "bg path 5.png"
image dark = "Dark 1.png"
image dark 2 = "Dark 7.png"
image darkness = "Black background.png"
image castle light = "Castle 2.png"
image castle dark = "Castle 4.png"
image castle ballroom = "Castle Ballroom.png"
image castle basement = "Village Tavern 1.png"
image blessed lands = "Purple 1.png"

# The game starts here.

label start:
    scene path 1
    play music "audio/Fresh Winter Breeze.ogg" fadeout 2.0 volume 0.5
    "In a calming jungle..."
    show zoey smile 1 
    Zoey "I cannot BELIEVE how beautiful this place is!"
    Zoey "I wish I could live here forever..."

    show zoey smile 1 at left
    show josh neutral at right
    Josh "You've been saying that all day long."
    hide josh neutral
    show josh angry at right
    Josh "Seriously, I hope you know that we passed two leopards and three snakes on the way here."
    hide zoey smile 1
    hide josh angry

    show ronan happy 
    Ronan "Alright stop arguing! I heard that we will enter The Blessed Lands very soon."
    hide ronan happy with dissolve

    show zoey smile 2
    Zoey "I can't WAIT to taste the special pineapples and oranges there!"

    scene clearing 1

    show josh serious at left
    Josh "It's been two hours already. According to the map we got from the trader, we should have arrived by now."
    show ronan confused at right
    Ronan "Maybe we miscalculated the distance? I mean there is only one path here."
    hide josh serious
    show zoey annoyed at left
    Zoey "Not anymore..."
    Zoey "Guys...the path splits into two here. This wasn't on the map..."
    Zoey "The right path seems like a continuation of this lush forest, while the left path seems like it leads to some gloomy forest..."
    hide zoey annoyed
    hide ronan confused
    show josh serious
    Josh "Which path do y'all want to choose?"
    default dark_path = False

menu:
    "Continue walking through lush forest":
        jump lush_forest

    "Enter the dark forest":
        jump dark_forest

label lush_forest:
    scene path 5
    show josh happy
    Josh "Phew. I'm glad we didn't go into that gloomy forest. That looked like a scene out of a horror movie."
    Josh "Anyways...let's get going."
    hide josh happy
    show zoey neutral 2 at left
    Zoey "But I wanted to explore the other road! This place is beautiful, but we've been walking for four hours already!"
    show ronan surprised at right
    Ronan "Zoey are you crazy? Just look at those lifeless trees! Before we step three feet into the woods, we would probably become skeletons!"
    "two hours later..."
    hide path 5
    jump castle

label dark_forest:
    play music "audio/Heavens Blight.ogg" fadeout 2.0 volume 0.5
    $ dark_path = True
    scene dark 
    show ronan scared at left
    Ronan "Zoey, Josh? I don't think we should be here..."
    Ronan "I feel like i'm going to pee myself."
    show zoey angry 2 at right
    Zoey "Ronan, seriously? It's just a little dark and barren. It's not like there are ghosts or anything here."
    Zoey "Don't you dare wet yourself this time. Last time during our trip to the ambient cave, you smelled so bad after that we had to cover our mouths with a wet towel!"
    show ronan blush at left
    Ronan "You didn't have to bring that up..."
    hide ronan blush
    hide zoey angry 2
    show josh angry
    Josh "Be quiet. I think I see something up ahead."
    jump castle

label castle:
    if dark_path:
        scene castle dark
        show ronan scared at left
        Ronan "Guys...Wha..what is that?..."
        show josh serious at right
        Josh "This can't be the blessed lands...right?"
        Josh "Why is everything so dark??? Is that suppose to be a molehill? Wait no..."
        Josh "It's a CASTLE!"
        Josh "In the fabled legends, The Blessed Castle is the most prominent landmarks of The Blessed Lands."
        hide ronan scared
        hide josh serious
        show zoey angry 2
        Zoey "But seriously. This is messed up. Why is there a castle in the middle of the woods? And why does it look like there hasn't been a single soul living in that place for hundreds of years???"
        hide zoey angry 2
        show zoey angry 2 at left
        show ronan confused at right
        Ronan "Should we...turn around?"
        show josh serious
        show dark 2
        Josh "It's too late. Look behind us. Which way is back?"
        Zoey "..."
        Ronan "*Gulp* I guess we have to move forward. I mean, maybe it's just the lighting that makes it look so gloomy?"
        Josh "I hope so..."
        jump castle_room
    else:
        scene castle light
        show ronan surprised at left
        Ronan "WOW LOOK AT THAT!"
        show zoey smile 2 at right
        Zoey "Is that a castle? Why does it look so run down?"
        Zoey "Maybe it's the entrance to The Blessed Lands?"
        hide ronan surprised
        hide zoey smile 2
        show josh neutral
        Josh "This is what i'm talking about. There are definitely some lost treasures and secrets in this castle."
        show josh smile
        Josh "Let's go check it out!"
        jump castle_room

label castle_room:
    scene castle ballroom
    show zoey smile 1 at left
    Zoey "Wow look at this! I did not expect the interior to look so nice! What happened to the castle walls outside? It looked so run down."
    show josh happy at right
    Josh "I guess it wasn't that bad after all."
    hide zoey smile 1
    hide josh happy
    show ronan scared
    Ronan "Guys...why are the candles still lit?"
    hide ronan scared
    "..."
    show josh serious
    Josh "Yeah this isn't right. The candles seem to be fresh despite the desolate exterior of the castle. It seems like someone lives here."
    hide josh serious
    show josh serious at left
    show zoey annoyed at right
    Zoey "Are y'all trying to scare me? Maybe the candles are some sort of new technology that lights on their own?"
    Josh "Zoey...have you seen what this castle looks like on the outside? You think they got electricity?"
    show zoey neutral 2 at right
    Zoey "Oh right...wait what?"
    hide josh serious
    show ronan scared at left
    Ronan "I don't like the look of this..."
    play sound "audio/Floor break.mp3" volume 0.5
    "*crack*"
    Zoey "What was that?!?"
    Ronan "AHHHHHHH"
    hide castle ballroom

    scene darkness
    play music "audio/Melancholy.ogg" fadeout 2.0 volume 0.5
    "..."
    Josh "Ronan? Zoey? Where are you guys?"
    Zoey "Ow..."
    Ronan "I'm fine. That sure was a heck of a fall."
    Ronan "Can someone light up a candle or something? It's pitch black in here."
    Josh "Yeah, I'll activate my emergency flashlight."
    scene castle basement
    show josh smile at left
    Josh "I'm so glad I brought this baby with me"
    show ronan surprised at right
    Ronan "KSJIDHAOISHJDILASJILDJIOAJDIO...AHHHHHHHh...AISJDIAJIOD"
    hide josh smile
    show zoey angry 2 at left
    Zoey "What are you yelling abo-"
    show zoey neutral 2 at left
    Zoey "Holy moly...what in THE WORLD IS THAT THING!"
    play sound "audio/Monster 1.mp3" volume 0.5
    hide zoey neutral 2
    hide ronan surprised
    show slime mad with fade
    Slime "𐌌ዐꝊነ𐋅 𐌀ነ𐌃ፓ𐌅ክ𐌉ረ ል𐌔ዐ𐌵ቹ𐋅ቻꝊሠ𐌍ረ𐌀ር"
    Slime "Ꮤ፱𐌁 ꝊፓᏔ 𐌃ረ𐌔 Ꝋል𐌔ክ𐌃ዐ𐌒፪ ል𐌔ጋ𐌂"
    hide slime mad
    show zoey angry 2 at left
    Zoey "Wha...what is it saying?!??"
    hide zoey angry 2
    show josh serious at left
    Josh "It looks like a pile of melted gummy bears. I think it's some sort of slime creature."
    show slime mad at right
    play sound "audio/Monster 2.mp3" volume 0.5
    Slime "𐌒ሠ𐌉ቹᏖቻ ልᏔቹꝋጎ𐌅. ል ጎᏔር𐋄"
    show slime sad at right
    Slime "𐌋ር𐌍ል ,Ꮤነ𐌀ዐ𐌃ክ𐌅.𐌀ጎ የ𐌉ዓ"
    hide josh serious
    show ronan scared at left
    Ronan "Please Mr. Slime. We don't mean to trespass upon your territory. We will leave immediately..."
    hide slime sad
    show josh serious at right
    Josh "Wait no. I've seen these creatures before in the lost chapter. They are suppose to be the janitors of the Blessed Castle."
    show josh bored at right
    Josh "It don't seem hostile with us. It almost sounds like...he's pleading us."
    hide josh bored
    hide josh serious
    hide ronan scared
    show slime sad
    play sound "audio/Monster 3.mp3" volume 0.5
    Slime "𐌓ረ𐌄ል𐌔ቹ ⶴ𐌄ረ𐌓 𐌵ነ..."
    Slime "𐌓ረ𐌄ል𐌔ቹ..."
    hide slime sad with fade
    show zoey neutral 2 at left
    Zoey "It seems to be asking us to help...?"
    show ronan confused at right
    Ronan "It does seem like it's pleading to us. I don't speak Slimenglish, but just look at it's face! It's crying!"
    show slime sad
    Slime "*sniff sniff*"
    hide slime sad
    hide ronan confused
    hide zoey neutral 2
    show josh serious at left
    Josh "Do you know how to speak any other languages? We really don't understand. We'll do anything we can to help you."
    show slime sad at right
    Slime "..."
    Slime "01001010 11010111 01100 10100 100 100 0101001 0100101 01010111010110 0111 01001010 10010 0101010 10101010010100101010101"
    hide josh serious
    show zoey annoyed at left
    Zoey "What? It's speaking in numbers now?"
    hide slime sad
    show ronan confused at right
    Ronan "No. What it's saying is oddly familiar. A string of numbers that only uses 0 and 1s, what language was it again?"

label menu_language:
menu:
    "Slimenglish":
        jump language_incorrect
    "Binary":
        jump language_correct
    "Hexadecimal":
        jump language_incorrect
    "Gibberish":
        jump language_incorrect

label language_incorrect:
    Zoey "I don't think that's the right language. It seems that the slime only talks in TWO digits, 0s and 1s. Have another guess?"
    jump menu_language

label language_correct:
    Ronan "That's right! Binary is the language that uses 0s and 1s exclusively!"
    Zoey "But that doens't help! How are we suppose to translate binary into english?"
    hide ronan confused
    hide zoey annoyed
    show slime mad
    Slime "010 11101001 101010001 10 1010101 1010 1 0110 10 1001"
    play sound "audio/Creak.mp3" volume 0.5
    "*creak*"
    show slime sad
    Slime "11001 101 10101..."
    show josh serious at left
    Josh "What was that? It sounded like some sort of metal creaking noise"
    Josh "Wait..."
    show ronan surprised at right
    Ronan "The doors seems to be barred up by chains! How do we get out?"
    Slime "101101 101 01 100..."
    Slime "*sniff sniff*"
    Josh "It seems like it has been trapped here for quite a while. I don't think we will be able to leave either unless we break those chains."
    hide ronan surprised
    show zoey neutral 2 at right
    Zoey "These chains are made of pure steel. There is no way we can brute force our way through 4 inches of solid metal."
    hide josh serious
    show ronan confused at left
    Ronan "What's that glowing thing next to the chains?"
    Zoey "It seems to be some kind of rune?"
    Ronan "I've looked through hundreds of textbooks on ancient runes none of them look like this..."
    hide ronan confused
    show josh bored at left
    Josh "It indeed does not resemble the ancient runes we have studied, but there seems to be...buttons we can press on them?"
    Zoey "It seems to be in binary! A bunch of 0s and 1s written on the buttons themselves!"
    Josh "You can't be serious here. Is this some sort of test?"
    hide zoey neutral 2
    hide josh bored
    show slime mad
    play sound "audio/Monster 1.mp3" volume 0.5
    Slime "ል ጎᏔር𐋄 𐌀ዐ𐌃ክ𐌅 ር𐌅ዐ𐋄!"
    show slime sad
    Slime "01011 10 110 11101!"
    Slime "101010 ር𐋄 𐌀 110 10 10 𐌃ክ𐌅!"
    hide slime sad
    show slime sad at right
    show josh bored at left
    Josh "Mr. Slime, we can't understand a word that you say..."
    Josh "Are you asking us to solve the problems on the chains?"
    Slime "*spazzes out*"
    play sound "audio/Monster 4.mp3" volume 0.5
    Slime "1! 1! 1!"
    hide josh bored
    show ronan surprised at left
    Ronan "I think that means yes..."
    Ronan "Alright let's see what this is all about."
    hide ronan surprised
    hide slime sad
    "\"01 + 110 =\""
    show zoey angry 2 at left
    Zoey "ARE YOU SERIOUS? IT'S ASKING US TO TO...MATH???"
    show ronan blush at right
    Ronan "Dang it. I didn't think I would ever need to do math ever since I went to music school."
    hide zoey angry 2
    show josh serious at left
    Josh "Stop bickering. I think it wants us to complete the math operation."
    Josh "In binary, \"00\" means the value of zero and \"01\" equates to the value of one. Whenever we try to exceed the number 1 of the binary language, we are suppose to add a new digit and put a \"1\" there, while switching old values to a zero."
    Ronan "What? I didn't catch that."
    Josh "What I mean is, to represent the number \"2\", it would be \"10\" because you cannot have \"02\" in binary. Since the number \"one\" ie represented by \"01\", you would add a \"1\" as a new digit and reset the previous digit to a \"0\""
    Josh "So the number \"2\" equates to \"10\" in binary. Do you understand?"
    Ronan "Uhh..."
    Ronan "Not really."
    show slime mad
    play sound "audio/Monster 3.mp3" volume 0.5
    Slime "ሠ𐌉ቹᏖ! ሠ𐌉ቹᏖ! ሠ𐌉ቹᏖ!"
    hide ronan blush
    show ronan surprised at right
    Ronan "Whoa whoa! I mean I totally understand!"
    hide slime mad
    hide ronan blush
    show zoey annoyed at right
    Zoey "So according to your rules, what does \"01 + 110\" equal to?"

label question_one:
menu:
    "8":
        jump one_correct
    "5":
        jump one_incorrect
    "12":
        jump one_incorrect
    "102":
        jump one_incorrect

label one_incorrect:
    Zoey "That doesn't seem right. Try again"
    jump question_one

label one_correct:
    play sound "audio/Chain 1.mp3" volume 0.5
    hide zoey annoyed
    show josh happy at left
    "Creak..."
    Josh "Yes it worked! The first chain fell off!"
    Josh "Let's see what the second chain is."
    "1001 + 101 ="

label question_two:
menu:
    "1042":
        jump two_incorrect
    "16":
        jump two_incorrect
    "14":
        jump two_correct
    "9":
        jump two_incorrect

label two_incorrect:
    Zoey "Nope. Not the right answer. Gotta be another one"
    jump question_two

label two_correct:
    play sound "audio/Chain 2.mp3" volume 0.5
    hide josh happy
    show zoey smile 2 at right
    "Creak..."
    Zoey "Bravo! The second chain fell off!"
    Zoey "Let's see the question at the bottom left chain!"
    "1110 + 1000 ="

label question_three:
menu:
    "18":
        jump three_incorrect
    "25":
        jump three_incorrect
    "53":
        jump three_incorrect
    "22":
        jump three_correct

label three_incorrect:
    hide zoey smile 2
    show ronan happy at left
    Ronan "I don't think it's this one. Nothing happened."
    jump question_three

label three_correct:
    play sound "audio/Chain 3.mp3" volume 0.5
    hide zoey smile 2
    show ronan happy at right
    "Creak..."
    Ronan "Yes! You are a genius! We're down to the last one!"
    "1010 + 1100 + 10"

label question_four: 
menu:
    "12":
        jump four_incorrect
    "17":
        jump four_incorrect
    "13":
        jump four_incorrect
    "26":
        jump four_correct

label four_incorrect:
    hide ronan happy
    show josh serious at left
    show zoey neutral 2 at right
    Josh "Nice try. But it isn't the right choice."
    jump question_four

label four_correct:
    play sound "audio/Chain 4.mp3" volume 0.5
    hide ronan happy
    show josh happy at left
    show zoey smile 1 at right
    "Crackle...Boom!"
    Zoey "YES! The chains fell off! We can finally leave now!!!"
    show slime sad
    Slime "𐌓ረ𐌄ል𐌔𐌓ረ𐌄ል𐌔𐌓ረ𐌄ል𐌔𐌓ረ𐌄ል𐌔 𐌓ረ𐌄ል𐌔𐌓ረ𐌄ል𐌔!"
    Josh "Let's get out of here."

label epilogue:
    scene castle ballroom
    play music "audio/Grace of the Morning Sunshine.ogg" fadeout 2.0 volume 0.5
    show josh smile at right
    Josh "Whew. That was a close one. I sure hope Mr. Slime is okay down there"
    show josh happy
    show slime sad at left
    Slime "Ꝋቹ𐌅ጎ𐌵 Ꮦ Ꮤ 𐌊ሠ𐌄ዐ𐌅ክ𐌉ዐ𐌄ክ"
    Slime "𐌅፱𐌒ፓ𐌔ጋ ፪𐌀፱𐌔፪𐌅፱Ꝋል𐌔ⶴ𐌃ዐ𐌀ⶴ..."
    show slime neutral at left
    Slime "..."
    hide slime neutral
    show josh neutral
    Josh "Guess he left..."
    show zoey neutral 2 at left
    Zoey "Poor Mr. Slime. Must've been lonely after all these years..."
    Zoey "Anyways, I don't want to stay in this gloomy castle anymore. Let's go and see what's on the other side!"

    scene blessed lands with fade
    play music "audio/Fresh Winter Breeze.ogg" fadeout 2.0 volume 0.5
    play sound "audio/Shimmer.mp3" volume 0.5
    show ronan surprised at left
    Ronan "It's so beautiful...is this The Blessed Lands?"
    show zoey smile 1 at right
    Zoey "It should be. Where else can be more stunning? Look at the rows peach blossoms. Hehe!"
    Zoey "I really want to live here forever."
    hide ronan surprised
    show josh happy at left
    Josh "It was all worth it."
    show josh neutral at left
    Josh "All worth it..."
    Zoey "Let's go. Our journey across The Blessed Lands starts today!"
    show ronan happy
    Ronan "Yes! Today!"
    scene darkness
    "To be continued..."

return



