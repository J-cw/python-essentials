# Python Hangman Project
This project is a simple and quick hangman game created with a complex range of words. 
The game has been built with python and deployed with Heroku. 
The idea is to guess the hidden word in a certain amount of tries before the man is fully hanged.

[Link to my code via Github pages](https://github.com/J-cw/python-hangman)

[Link to my Application deployed by Heroku](https://python-hangman-jacob.herokuapp.com/)


## How To Play
To begin you must guess a random letter a-z in hopes that it is included in the chosen letter, otherwise it will begin to take a life off've you. This continues throughout until A. the player runs out of lives or B. the player guesses the full word in its entirety.

## Features
### Existing Features
* Random word function
    * A random word is picked out've the words.txt file

* A check to see if the letter is within the hidden letter
    * If it isn't it will prompt the user to guess again.

* Limited lives function
    * The user only has a limited amount of guesses before the game is over.



### Future Features
* A leaderboard of which calculates the highest scoring users based off've the complexity of the word given as well as the amount of lives they lost.

* A selection of difficulty to allow the user to change between levels of 1-5 (perhaps higher) to increase the challenge and allow for more progression

* A connected spreadsheet to use instead of a words.txt file where the program can access the spreadsheet for said leaderboard or for an easier option to add extra words.

* A login system to allow to user to login to see their progress and current overall place on the leaderboards.


## Testing
* The Code Institute add-ons tested sufficiently within the program so I adjusted those errors accordingly.

* Tested from both Gitpod terminal and Heroku site. 


## bugs
### Solved Bugs
### Remaining bugs
* I can see that any input can be placed into the input prompts in multiple areas. In the future I will need to add validation techniques to raise value errors ect to disable the possibilty of flase inputs and enabling a restart of the game once over.
## Validator Testing
* Built into Code Institute template. Add-ons allow for error checking.
* Pep8 website down for testing.
## Deployment
* Instructions for deployment
    * Fork or clone Repository which is stored on Github.
    * Create Heroku account or login
    * Create new app - enter name of app and assign region.
    * If your using a creds.json file then go to Heroku settings and click "reveal config vars". 
        * In key type CREDS and in value paste your whole creds.json file text.
        * Again if you don't need to use creds.json file then skip to next step.
    * Add Buildpack then click python, then click add Buildpack again and add node.js. 
        * Make sure Python is first then node.js second.
    * Go to Deploy section in Heroku.
    * Click Github for deployment. Then click connect to Github. Login to Github to connect Heroku to Github.
        * Then type in your repo name and hit search.
        * Click connect to connect your project repo to Heroku.
    * Scroll down to Enable Automatic deployments. This updates your Heroku everytime your Github repo is updated.
        * e.g after you push any changes in github.


## Credits
* https://www.hangmanwords.com/words 
    * For the list of words used in the program.