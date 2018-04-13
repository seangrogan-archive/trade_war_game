# Trade War Game
A python script to test (in batches) different policies of the "Trade War Game" from FiveThirtyEight's recent aricle about Trade Wars

The game can be found [here](https://fivethirtyeight.com/features/how-to-win-a-trade-war/).

## Results

Well, after executing a small sample of random trials using random policies for both player 1 and player 2, typically speaking, higher values of friendliness lead to a better overall value, high values of imitation lead to more ties, and high values of vindictiveness seem to lead to the most wins (of course at the cost of value.  Presently I am executing a 10,000 tests by 10,000 opponents.  we'll see what the results will yield.

### Results from 10k by 10k

| Criteria           | Friendliness  | Imitation | Vindictiveness | Wins | Ties | Losses | Average Value |
| :----------------- |:-------------:|:---------:|:--------------:| ---: | ---: | -----: | --------: |
| Most Wins          |  0%           | 1%        | 27%            | 6460 | 3540 | 0      | 1028.3915 |
| Most Ties          |  3%           | 100%      | 4%             | 2999 | 6943 | 58     | 1024.7500 |
| Best Average Value | 100%          | 2%        | 1%             | 0    | 481  | 9519   | 1182.9615 |

What does this mean?

Well, being unfriendly (i.e. defecting all the time) will keep you from loosing to your opponent; however, you will end up with a lower value versus being cooperative.  If you mimc your opponent most of the time, you will tie them most of the time.  Finally, even though you may never come out on top, being friendly most of the time will give the player the highest value (on average).

Note, the best possible value one can get is if they defect 100% of the time and their opponent cooperates 100% of the time.  That value is 2500 (using the base case from the article and 100 turns).  If both players cooperate 100% of the time, they both can expect $1500.

### Multiprocessing Results