<h1> Python Project 12: Number Guessing Game </h1>
<p><em>Updated 30 October 2024: Reattempted project and committed new changes to practice what I've learned. New learnings added under "Learnings" section. This is a project that I want to revisit and practice again in the future, as my first run-through of today's reattempt was vastly different and I got stuck in a different while loop when asking for a guess input and showing the number of attempts remaining. The second run-through of today's reattempt was better but I needed more guidance in the order of steps for writing the code, as I knew the parts I wanted but was confusing myself by writing them out of order. After a break and quick review of the steps needed, I was able to create the game. </em></p>
<h2>Summary</h2>
<p>This project is for day 12 of the 100 Days of Code challenge that I'm completing as part of the Complete Python Pro Bootcamp with Dr. Angela Yu from the London App Brewery. Each project in this challenge will be using Python so that I can grow my skills in software development.</p>
<p>This project is a simple number guessing game that allows the user to guess a number between 1 and 100. There are two levels to this game: easy and hard. The user has 10 guess attempts in the easy level and 5 guess attempts in the hard level.</p>
<p>
  The games uses global constants (to set the attempts per difficulty level), functions, if/elif/else statements, while loops, random(), and local scope access. When the user makes a guess, they will be advised whether their guess is too high or too low (losing a life if they did not guess correctly) or whether their guess was correct. If the user guesses correctly or runs out of attempts, it's game over and the program will ask if they want to play again.
</p>
<h3>Learnings</h3>
<ul>
  <li>
    As global constants are still a fairly new term for me, I made sure to use best practice when setting them by using ALL CAPS. Previously, I was more focused on making the game run properly that I set them as I would normally in lowercase. This was an important aspect as it further reiterated that those variables do not change/update as the values are used in other functions.
  </li>
  <li>
    Coding this game also reiterated how overwhelming learning multiple coding elements can be and that I won't also remember everything. I really had to set out a checklist and take the time to look up specific elements to ensure I was on the right track. For example, I used random.rantint(0, 100) this time, whereas I used random.choice(range(0, 101)) last time. The randint() function is much newer to me and therefore I wanted to clarify its use with ranges and whether the second parameter was inclusive or exclusive.
  </li>
  <li>
    As I'm also getting used to using the return element, I found that I had to continually check that the program was running as it was meant to. Often, I would use print rather than return because it's been a habit thus far to display the result for my learning. After running through my solution with the training program's, I found that I used break to end the game when turns = 0 instead of return. In this case, they had the same intended result; however, using return on its own wasn't something I immediately thought of because I've only been using it with a specific thing needing to be returned. For example, "return" vs "return turns - 1".
  </li>
  <li>
    I also added the feature of running the game again if the user wishes. This was a while loop that I learned in the previous project (Day 11: Blackjack Game) and I wanted to practice again.
  </li>
</ul>
<h2>Tech stack</h2>
<ul>
  <li>Python</li>
  <li>VS Code</li>
  <li>PyCharm</li>
  <li>ASCII</li>
