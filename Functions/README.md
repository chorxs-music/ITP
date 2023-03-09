# ITP
## Kevin
### Think Python Chapter 10, Functions Homework

**Think Python Chapter 10**

One thing that I knew about lists in programming was the ability to *delete, slice, and concatenate* various lists together. For example, you can append [1, 3, 6] with [3, 6, 7] using "list".append("newlist"). However, I did not know about the extent in which you can customize these lists to your liking, include aliasing, splitting, etc. It blows my mind away that you can do so much with just a list of numbers/values.


**Lists and Arrays**

Based on the template you provided, the first step was to define the function that prints out "*" "n" number of times. This was simple; a *for* loop that prints out "*" when they are within the range of "n". Next, I had to define a function that takes an inputted value and **square** it because we are trying to emulate the graph y = x^2. This was also fairly straightforward; you just need to return "return x ** n", where "n" = 2. To combine them together, I used a *for* loop with ranges of -8 ~ 8, where for every incrementing value, I need to square it, then print out the corresponding number of "*" . This was the hardest part and I ran into some difficulties trying to come up with the code. At first, I approached it using another *for* loop, wanting to place a counter that tracks how many times the increment has occurred, which didn't really work out since the graph is a parabola and values were mirrored. I toyed around and found out that by inputting the function that squares the number with the corresponding value on the *for* loop, I can effectively square whatever value the *for* function dictated, then ferry that value into the *print* function to print out the asterisks. No external code was used.
