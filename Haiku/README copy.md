# ITP
## Kevin
### Think Python Chapters 2, 3 + Haiku.aiff

**Think Python Chapters 2 and 3**

*Chapter 2*

1. 
    a) I've done some basic C coding before, and I found that the terms that Python uses (operators, variables, etc.) are largely the same. They mostly retain their original functions and are meant to do pretty much the same thing.

    b) One thing that I did not learn in C coding is the entire notion of *strings*. Usually in C, you will have to specify the amount of bytes you allocate to an array, which is honestly so exasperating. However, I learned that in Python, you can simply type an array of characters and store that all in a single string.

*Chapter 3*

2. 
    a) I find this to be similar to C as well, where you must "include" a particular "system" for the code to run properly. For example, you will need to do "#include math.h" if you want to utilize most math operations. This seems to be the case with Python as well, instead you gotta type "import"

    b) I learned about "dot operators", where you can access different functions stored in the module object by using "xxxx.log10(100)" for example. I think this is similiar to what I saw on Unity with C# but I've never learned C# and Python seems to emulate that


**Haiku.aiff Creation Markdown**

The first thing that I did upon entering the terminal was changing the directory to a more accessible place, such as the *documents* folder on my computer. I first did "pwd", in which it showed me I was in Users/Kevin. I ended up using the "cd" command and dragging the "coding" folder inside my documents to manually change my directory. I then ran the "say" common with my Haiku, and after it executed, I ran the "-o Haiku.aiff" command to create an .aiff file, however, I was met with the problem that "-o" was a command that was not found. 

Apparently, the terminal does not recognize that I had already typed the "say" command and I had to specify that inside the "say" command that I wanted an .aiff created. I simply added the "-o" command immediately after the "say" command (inside the same terminal command) and it successfully created an .aiff recording of the Haiku inside my "coding" folder. 

I did not use any code from outside sources.