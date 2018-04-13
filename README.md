# Trade War Game
A python script to test (in batches) different policies of the "Trade War Game" from FiveThirtyEight's recent aricle about Trade Wars

The game can be found [here](https://fivethirtyeight.com/features/how-to-win-a-trade-war/).

## Results

Well, after executing a small sample of random trials using random policies for both player 1 and player 2, typically speaking, higher values of friendliness lead to a better overall value, high values of imitation lead to more ties, and high values of vindictiveness seem to lead to the most wins (of course at the cost of value.  Presently I am executing a 10,000 tests by 10,000 opponents.  we'll see what the results will yield.

### Results from 10k by 10k

Most Wins   [0.00, 0.01, 0.27] 6460  3540   1028.3915
Most Ties   [0.03, 1.00, 0.04] 2999  6943   1024.75
Best Value  [1.00, 0.02, 0.01] 0     481    1182.9615