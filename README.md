# newlywed-game
I wanted to randomly select questions so that a player could compete against another person to see who got the most questions correct.

To generate these questions, I imported lines of text from a text file into an array. Then I randomly shuffled that array.

To keep track of the index, I used a counter that incremented each time I pressed a key as to avoid any index out of bounds exceptions.

To keep track of score, I press down the 'a' key for player 1 and the 'j' key for player 2. The count of correct answers is shown in the top corners. If neither player answered correctly, we can select any key besides a, j, or ESCAPE to move on to the next question.

It is worth mentioning that I had 2 hours to code this and make it work, so there certainly are flaws.
