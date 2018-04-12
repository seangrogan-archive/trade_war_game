import random


class Player:
    def __init__(self, friendliness, imitation, vindictiveness, horizon=100):
        """
        Initializer function for the Player class.
        :param friendliness: As a baseline, how often (as a percentage of all rounds) will you cooperate, allowing free
                                trade between your country and your opponent’s?
        :param imitation: Once trade begins, your opponent’s policy could be unpredictable. How often (as a percentage
                                of all rounds) will you abandon your baseline strategy to mimic their actions,
                                responding to them in kind?
        :param vindictiveness: If you’re crossed by an unkind, defecting opponent who imposes tariffs on your goods,
                                how long (as a percentage of the remaining rounds) do you hold a grudge, putting your
                                other strategies aside to punish the other country by defecting yourself?
        """
        self._friendliness = friendliness
        self._imitation = imitation
        self._vindictiveness = vindictiveness
        self._my_actions = list()  # memory of actions taken
        self._their_actions = list()  # memory of opponent's actions
        self._my_value = 0  # running tally of my value
        self._horizon = horizon  # the number of rounds remaining
        self._vindictive_horizon = 0  # the number of turns the player will defect
        self._current_turn = 0  # counter for the current turn
        self._imitate = list()  # a list of the number of

        # Calculating the number of rounds
        k = int(imitation * horizon)
        for i in range(horizon):
            if i < k:
                self._imitate.append(True)
            else:
                self._imitate.append(False)
        random.shuffle(self._imitate)

    def make_choice(self):
        """
        Uses the parameters of the player to decide if the player will cooperate oer defect
        :return: True if cooperate, false if defect
        """
        if self._current_turn == 0:
            # If its the first turn, it will choose based on the friendliness parameter
            c = random.random() <= self._friendliness
            self._my_actions.append(c)
            return c
        if self._vindictive_horizon > 0:
            # If the player chooses to be vindictive, will return false until the counter expires
            self._vindictive_horizon -= 1
            self._my_actions.append(False)
            return False
        if self._imitate[self._current_turn]:
            # Check to see if this is an imitation turn
            self._my_actions.append(self._their_actions[self._current_turn-1])
            return self._their_actions[self._current_turn-1]
        # when all else fails, return according to the friendliness parameter.
        c = random.random() <= self._friendliness
        self._my_actions.append(c)
        return c

    def their_choice(self, their_choice):
        """
        Imports their choice into the player class
        :param their_choice: True if cooperates, false if not
        :return: nothing
        """
        self._current_turn += 1
        self._their_actions.append(their_choice)
        if not their_choice:
            remain_turns = self._horizon - self._current_turn
            self._vindictive_horizon = int(remain_turns * self._vindictiveness)

    def adjust_value(self, val):
        """
        Adds the value of the result to the
        :param val: amount to add
        :return: nothing
        """
        self._my_value += val

    def get_my_value(self):
        """
        Returns the value of the player
        :return: self._my_value
        """
        return self._my_value
