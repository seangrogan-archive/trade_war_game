from player import *
import math


def main():
    # runs the default 
    default_types()
    experiment_between_def_types()

def default_types():
    pol1 = [1, 0, 0]  # Cooperator
    pol2 = [0.5, 0, 0]  # Coin Flipper
    pol3 = [1, 1, 0]  # Copycat
    pol4 = [1, 1, 0.25]  # Retaliator
    pol5 = [1, 1, 1]  # Grudge Holder
    pol6 = [0, 0, 1]  # Defector
    print("For Policy ", pol1)
    experiments(pol1)
    print()
    print("For Policy ", pol2)
    experiments(pol2)
    print()
    print("For Policy ", pol3)
    experiments(pol3)
    print()
    print("For Policy ", pol4)
    experiments(pol4)
    print()
    print("For Policy ", pol5)
    experiments(pol5)
    print()
    print("For Policy ", pol6)
    experiments(pol6)
    print()

def experiment_between_def_types():
    pol1 = [1, 0, 0]  # Cooperator
    pol2 = [0.5, 0, 0]  # Coin Flipper
    pol3 = [1, 1, 0]  # Copycat
    pol4 = [1, 1, 0.25]  # Retaliator
    pol5 = [1, 1, 1]  # Grudge Holder
    pol6 = [0, 0, 1]  # Defector
    pol_set_1 = [pol1, pol2, pol3, pol4, pol5, pol6]
    pol_set_2 = [pol1, pol2, pol3, pol4, pol5, pol6]
    for i in pol_set_1:
        win = 0
        tie = 0
        for j in pol_set_2:
            p1v, p2v = experiment(i, j)
            if p1v > p2v:
                win += 1
            if p1v == p2v:
                tie += 1
        print(i)
        print("Wins : ", win)
        print("Ties : ", tie)
        print()

def experiments(p1, n=10000):
    """
    Runs n experiemts given a player 1 value
    :param p1: list of [f, i, v]
    :param n: number of sims
    :return:
    """
    win = 0
    tie = 0
    for i in range(n):
        f = random.randint(0, 100) / 100.0
        i = random.randint(0, 100) / 100.0
        v = random.randint(0, 100) / 100.0
        p2 = [f, i, v]
        p1v, p2v = experiment(p1, p2)
        # print(p1, " \t|\t ", p2, "  \t|\t", p1v, p2v, "(", p1v - p2v, ")")
        if p1v > p2v:
            win += 1
        if p1v == p2v:
            tie += 1
    print("Wins : ", win, "(", int(win*100/n), "%)")
    print("Ties : ", tie, "(", int(tie*100/n), "%)")


def experiment(player1=[1.0, 0.5, 0.25], player2=[1.0, 0.5, 0.25], c_c=15, d_d=10, c_d=5, d_c=25, n=100):
    """
    A single execution of the experiment, we are looking at what happens to player 1
    :param player1: Player 1's Friendliness, Imitation, and Vindictiveness
    :param player2: Player 2's Friendliness, Imitation, and Vindictiveness
    :param n: number of turns the trading will last
    :param c_c: if we both cooperate, what value do we win?
    :param d_d: if we both defect, what value do we win?
    :param c_d: if I cooperate and they defect, what value do we win?
    :param d_c: if I defect and they cooperate, what value do we win?
    :return: Tuple for results of player value
    """
    p1 = Player(player1[0], player1[1], player1[2], n)
    p2 = Player(player2[0], player2[1], player2[2], n)

    # Beginning trade war
    for i in range(n):
        # Making Choice
        p1_choice = p1.make_choice()
        p2_choice = p2.make_choice()

        # Adding choices to opponent
        p1.their_choice(p2_choice)
        p2.their_choice(p1_choice)

        # Determining value to add
        if p1_choice and p2_choice:
            # i.e. c_c
            p1.adjust_value(c_c)
            p2.adjust_value(c_c)
        elif not p1_choice and not p2_choice:
            # i.e. d_d
            p1.adjust_value(d_d)
            p2.adjust_value(d_d)
        elif p1_choice and not p2_choice:
            # i.e. c_d
            p1.adjust_value(c_d)
            p2.adjust_value(d_c)
        elif not p1_choice and p2_choice:
            # i.e. d_c
            p1.adjust_value(d_c)
            p2.adjust_value(c_d)
        else:
            print("Unknown Error!")

    return p1.get_my_value(), p2.get_my_value()


if __name__ == '__main__':
    main()
