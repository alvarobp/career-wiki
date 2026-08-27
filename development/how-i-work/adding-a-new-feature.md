# Adding a new feature

This reflects how I approach adding a new feature, what I usually call "extracting tasks from User Stories". My own process is as simple as:

1. Gather a list of assumptions (about the feature, about existing implementation, about conditions/requirements of the new implementation, etc)
2. Based on the assumptions think of, in a broad sense, how the new change can be implemented.
3. Create a list of tasks that will implement the change. Tasks that are independent, that can be tackled in parallel, which scope is well undrestood and somehow estimable, that when all done the feature will be releaseable.

I'd like to borrow this more thorough approach from James Shore [https://www.jamesshore.com/Blog/Lunch-and-Learn/How-to-Add-a-Feature-Cleanly.html](https://www.jamesshore.com/Blog/Lunch-and-Learn/How-to-Add-a-Feature-Cleanly.html) since it pretty much matches my own approach but in more detail and more focused at code level:

1. Understand the feature
    1. How is this different than what the code does today?
    2. What parts are important?
    3. What can we safely ignore?
2. Skim the existing design
    1. Look at folder and file names, not details.
    2. Based on their names, make an educated guess: what are their one-sentence responsibilities?
    3. Look at function/method names inside files, if it helps, but don't look at every file. Just the big ones.
    
    **"The trick with modifying existing code cleanly is to rather than focus on the stuff that you hate find the beauty. Everybody who creates code has some sort of design in mind, if they're really junior it may have not been a great design but they still have some design in mind. Your job as someone that is coming and modifying this code is to find the beautiful design they had in mind and make it better."**
    
3. Find the current implementation
    1. Start with review of file responsibilities.
    2. Make an educated guess, then read code/tests.
    3. To confirm, change code and see if behavior changes.
4. Find the file whose responsibilities best align with the new behaviour
    1. This isn't necessarily the code that implements the current behavior.
    2. Start with review of file responsibilities.
    3. Think about information flows. Where is the data?
    4. Read code to confirm. It may be in dependencies.
5. Decide how step 3 and 5 will connect
    1. Does current implementation connect to responsibility?
    2. If not, is this a design flaw?
    3. If it is a design flaw, should you fix it? 
6. Decide what to change
    1. How will you change current implementation?
    2. How will you add new behavior to code which should have responsibility for it?
    3. Programming by intention can help.
7. Implement the change
    1.  Think of your code as a graph of dependencies.
    2. Your changes are least disruptive if you start depth-first. Change the leaf dependencies first, in isolation.
    3. Then work your way up, wiring each higher node to the nodes underneath.
    4. The root node will be the old implementation.