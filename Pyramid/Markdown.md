# ITP
## Kevin
## Pyramid and FizzBuzz Homework

**Pyramid**

This homework was the hardest one yet, mainly because I couldn't wrap my head around how for loops worked alongside nesting and the *range()* function.

I first created an input, where the variable "stacks" is determined by the user input that prompts a value between 1-8. I had to convert this into an integer so the inputted value wouldn't be a string.

I then created the *#* function that is *nested* inside the "i" function. The "i" function dictates that for "i" within the range of the **stacks** variable we created (1-8), it would start at 0, stop at "stacks", and increment by "1" every iteration. The nested "j" loop will fire all its values for every increment. The basic function was that for "j" within the range of our **stacks** variable, it is to check whether its "stacks" variable is less than or equal to the "stacks" variable within "i" and if it is, it would print out "#". It ends its function after it has reached the "stacks" value as it signals to *stop*. For example, at stacks = 2, the possible values are {0, 1}. When "i" = 0, "j" would execute at a value of 0 as well. "j" would be <= "i", therefore it would print a "#" symbol. It ends the loop as "0" would signal "stop". The next iteration, "i" = 1, and "j" would run its entire iteration. Starting at "0", "j" would print out a "#" and end it. Once "i" = 1, "j" would fire again, starting from "0", printing a "#" and firing again at "1", printing another "#". This creates two "#" side-by-side.

I ran into a problem trying to create the spaces. I first tried to manipulate the "print" command by adding a space before it, which didn't work as it ended up following the "j" function and spacing before every "#". I then realized that I can also add another nested range function "k", where for "k" is > "i", it would print a space. I wrote this BEFORE the "j" loop so the space places before the "#". If "stacks" = 3, "k" at "i" = 0 would run values from 0, 1, and 2. Realizing that "k" at 1 and 2 is > than "i" value of 0, it prints two spaces, then "j" would execute and print one hashtag. This was enlightening for me as I didn't actually have hopes that it would work, but it did.

I did not use any external code to help me. However, I had ChatGPT explain to me how the nested loops worked for me to write the "k" loop 

**FizzBuzz**

This assignment was fairly straightforward and asks us to use the **if, elif, and else** statements to create conditions in which if the number is divisible by 3, 5, or "both 3 *and* 5", it would print out specific values.

First, I started by defining the index. It should start at 1, end at 100, and increment its value by 1. To create the conditions, the code must write "Fizz" when the index number has a *remainder of **0*** when it divided by 3. Similarly for 5, but you write "buzz". Lastly, if it is divisible by both 3 and 5, the program needs to print "FizzBuzz".

I approached this by creating if statements that equates to "if index % 3 == 0", which satisfies the condition of being fully divisible by 3. The after statement was that the program needed to print out "Fizz". I did the same thing for "Buzz". However, when I started with the "3 *and* 5", I tried writing it as "if index % 3 and 5 == 0, print("FizzBuzz")". Apparently, the program interpreted as "(index % 3) AND 5 == 0", which means it would always be false. I had to apparently switch it around and manually type both conditions out, with (index % 3 == 0) AND (index % 5 == 0). I then created an "else" statement where if none of the above conditions were true, print out the "index" value.n It was a very fun assignment overall. No external codes were used.