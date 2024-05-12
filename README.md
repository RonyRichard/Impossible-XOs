# Overview

I wanted to gain some practice making an AI that can make its own decisions based on what input it recieves from the player. I learned a lot from this project.

It is a simple Tic-Tac-Toe game. You can Choose vs a player (for two player on the same device) or vs AI. When you choose vs AI you can choose to play first or second. The goal is for the AI to be unbeatable. The game will always end in a draw or a win in the AI's favor. 

The hardest part was reviewing on youtube videos on how to use pygame. It has been a long time since I last used it. 


[Software Demo Video](https://youtu.be/UnzHzI91mhU)

# Development Environment

Visual Studio Code

Pygame, Python

# Useful Websites


* [Arcade Academy](https://api.arcade.academy/en/latest/examples/index.html)
* [Real Python](https://realpython.com/arcade-python-game-framework/)
* [Tic-Tac-Toe Tutorial](https://www.youtube.com/watch?v=KBpfB1qQx8w)

# Future Work

Bug 1: When playing vs AI, sometimes the code will take until the next move to acknowledge that the AI has won. For example, if the AI has won on move 7, you will have to move before the "You lost" screen appears. 

Bug 2: If the AI wins in a way that has 3 in a row in more then one way (For Example, a Horizontal and vertical win using the top middle box) it will get stuck. This bug really stumped me because I dont have this bug in the Versus mode. 