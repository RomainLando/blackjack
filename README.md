## Blackjack Game and Tests

This is a simple game of blackjack between a player (user) and dealer (programmatic). 

To run the game, run the blackjack.py file. 
To run the tests, run the run_tests.py file.

This project was written using Python, TDD, and OOP.


### Starting assumptions

There are many assumptions I have made for this project:
- There is only one player (the user) going up against the dealer (pc)
- The goal of the player is to score a hand higher than that of the dealer, without going over a hand value of 21.
- The player loses if their hand goes over 21, or if the dealer scores a higher hand. 
- The player ties with the dealer if they score a hand of equal value.
- At the start of the game, the player and dealer are both dealt 2 cards each. 
- Number cards are worth their face value (2-10).
- Jacks, Queens, and Kings are worth 10.
- Aces are worth either 1 or 11 (player chooses).
- I have also assumed that the player only chooses the value of aces if they can be worth 11 without making the user go "bust".
- The can be given more cards by choosing to "hit", they will then be given one more card. 
- Once the player is satisfied they can choose to "stand" and their score will be evaluated.
- If the player "hits" until their score goes over 21, they go "bust" and the game ends with them losing.
- Once the player has chosen to "stand" the dealer will add cards until their hand is over the value of 16.
- The player's hand is displayed fully from the onset, however the dealer's hand has one card hidden at the start and their the value of their hand isn't displayed.
- A game is only played with one deck of 52 cards.
- the deck is shuffled in a random order at the start of each game.