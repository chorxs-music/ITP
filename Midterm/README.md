# ITP
## Kevin
### Midterm

**Midterm - Cannon Cart**

### Phase 1
This was definitely one of the most fun projects yet.

For the midterm, I decided to create a cannon cart inspired by the game "Ball Blast" by Voodoo Studios. Phase 1 was relatively simple; I drew out a rough outline of the cart on a sheet of grid paper.

### Phase 2
This was one of the most time-consuming parts of the project. I wasn't adept at translating shapes around, and especially with the (x1, y1, x2, y2) configuration of Processing, it took my many attempts to scale and position the circles and rectangles to closely resemble my sketch. One other problem I had in this phase was that I could not get the final rectangle to "stack" upon the vertical rectangle because it refused to center itself. This was slightly annoying and I ended up extending the vertical one slightly (I refrained form using decimal points). The total dimensions of the sketch was 100 pixels wide and roughly 40 pixels tall.

### Phase 3
This is where the fun began. Using the template code you provided on Github, I duplicated a copy of my sketch 200 pixels down. However, the grid was way too small and I forgot to resize my sketch, but that was a quick fix. I decided to go for the classic 500x500 pixel grid and soon saw the duplicated sketch around halfway down the grid. Up until here, everything was smooth sailing...

### Phase 4
The grid phase was relatively simple. I had coincidentally sized my sketch to example 100 pixels wide, which was the limiting factor as the widest point of the sketch would take up the most space and be the first point to overlap. I wanted more volume than size, so I decided to scale my sketch to *25% of the original size* (i.e. 25 pixels), which would perfectly tile 20 sets of my drawings over 500 pixels. I gave "s" a value of 0.25 and everything was ready for tiling.

However, this was where things started getting hairy. I ran into the first problem as I couldn't get the *for* loop working. I first created a "for" loop under "def draw()" with a range function that stated "for i in range of 500 pixels, draw the sketch at (0, i*20, 40[found the "s" coordinate to not really impact much]), where it ended up duplicating an entire column of cannon carts perfectly. I knew I was on the right track, however, this was only one single column and I needed 19 more of them.

I tried inserting a counter, where counter == 0 and the "x" coordinate would get multiplied by "counter" every cycle similar to how I multiplied the "y" coordinate by "i" using the "for" loop. However, what happened was that the program ran through the "x" and the "y" functions at the same intervals, meaning as the "y" coordinate went down, "x" also continuously went "right". It created this diagonal line of carts where each column now only had one cart.

Eventually, I found out that using the nesting method, you can nest another *for loop* and get it to track something independently. I created a *for loop* that dictates "for k in range 500, drawObject (k*25, i*20, 40)" where the function would execute "k" up until the value of 500, which would draw a horizontal line, then proceed to the next "y" coordinate.

This solved my problem and the layering was completed. There were 20 columns of 25 pixel width cannon carts. The only external code I used was from the chapter where we discussed nested *for* loops, which I mainly used to draw **inspiration**.