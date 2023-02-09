# ITP
## Kevin
### Think Python Questions
#### Pigeon Taco Game

**Think Python**

Chapter 1: This chapter introduced me to the basics of value types, such as floats, integers, strings, etc. and how they are used. It was very informative as I have done some basic python courses in high school but I didn't know what the formal classification was.

Chapter 2: This chapter explained the difference between a variable and a keyword. I've used Unity before and there woudl always be something along the lines of "class Program" and I didn't really know what it meant. Apparently the interpreter uses these keywords to recognize the structure of the program, which is very important

**Scratch**

**What I Did***

I tried to make a game where the player controls this dove and tries to eat the taco that has been left on the ground. It involves the use of the WASD keys to steer the dove into the taco that is diagonally across from it. The basic controls include:

1. WASD for movement
2. Space for flapping

**How I Did It**

I first created the movement script for the dove, where I used the event "When "x" is clicked, then...", which allowed me to input the condition of having either the W, A, S, or D key be the trigger for some function. I added the variable "change x by" or "change y by", which allowed me to input a value that in which the axis of the dove will change based on the key they pressed. For example, if the player presses "W", the dove will move 20 units up the y axis. I then added "when *space* is pressed, **LOOP**, wait 0.5 seconds, change costume", which allowed me to create a simple flapping animation

I then programmed "When *flag* is clicked" and chained a bunch of codes, such as having the bird speak out its intial thoughts (it wanting the taco) to give the player some clues as to what they are suppose to do.


I then worked on the taco itself, which was a hassle to figure out what to do. First, I wanted the taco to shrink when the dove is eating it (touching it), so I added the condition of "if the dove is touching the taco, change size by -10 and play sound "pop"" to indicate the taco is being eaten

Once the taco reached a certain size, it would "disappear" as if it was eaten completely. All sounds would also be stopped as it wouldn't make sense to have the taco eating sound continue to play even when it has been fully consumed. The game would be completed by then.

**Difficulties and Debugging**

1. When I intially coded the bird flapping its wings, I didn't insert "wait 0.5 seconds", which made the wings beat like crazy. Thought about it logically and added a slight delay to make it more realistic

2. When coding the taco sound, it just wouldn't play even when the dove was touching it. This was very irritating as I set the condition to "if touching dove? - *Loop forever*, start sound "pop". change size by -10, change volume by -10". However, I had forgotten to add an intialization event such as "when *flag* is clicked", which meant the code wounldn't be executed at all since there is no prompt for it to trigger.

3. Even when taco was not touching dove, it would still play the sound no matter what I tried. Apparently, it was because by putting the "if not touching dove, then stop all sounds" into the *forever loop* of the taco code, it would stop the sounds, then start the sounds again because the front of the loop is "start sound, pop". I ended up needing to execute the code "stop this script" so it would pause the forever loop.

4. Minor fix. Taco wouldn't return to original size and volume after it was eaten by the dove. I had to put "set size fo 100%, set volume fo 100%" for when the flag was clicked to resolve this. 

**I did not use code from elsewhere**


