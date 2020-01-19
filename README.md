# Game Simulations
Game simulations and statistical analyziers

## Spoons
Simulates a series of rounds of spoons, with the following assumptions:
1. The first player to get four of a kind wins the round
2. All players act logically, constantly attempting to reach four of a kind in their hand
3. Players are too focused on the speed of the game to remember which cards have already passed them, and thus past cards have no effect on current decision making

Reports statistical percentage of games won by each player with respect to the player drawing from the deck


#### Todo
* Add multi-threading to speed up processing large
* Add progress meter for large simulations
* Add additional statistics (average number of rounds before win, etc.)
