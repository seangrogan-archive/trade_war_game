from player import *


def main():
    # runs the default
    default_types()
    experiment_between_def_types()


def random_search_for_better_policy(n_test=10000, n_opp=10000):
    """
    This function will test a random policy against another random policy
    :param n_test: Number of policies to test
    :param n_opp: Number of opposition policies to test
    :return:
    """
    most_wins = dict()
    most_wins["policy"] = [0, 0, 0]
    most_wins["win"] = 0
    most_wins["tie"] = 0
    most_wins["avg"] = 0
    most_ties = dict()
    most_ties["policy"] = [0, 0, 0]
    most_ties["win"] = 0
    most_ties["tie"] = 0
    most_ties["avg"] = 0
    best_vals = dict()
    best_vals["policy"] = [0, 0, 0]
    best_vals["win"] = 0
    best_vals["tie"] = 0
    best_vals["avg"] = 0

    for i in range(n_test):
        print(" Executing Test", i)
        win = 0
        tie = 0
        val = list()
        f1 = random.randint(0, 100) / 100.0
        i1 = random.randint(0, 100) / 100.0
        v1 = random.randint(0, 100) / 100.0
        p1_pol = [f1, i1, v1]
        for i in range(n_opp):
            f2 = random.randint(0, 100) / 100.0
            i2 = random.randint(0, 100) / 100.0
            v2 = random.randint(0, 100) / 100.0
            p2_pol = [f2, i2, v2]
            p1v, p2v = experiment(p1_pol, p2_pol)
            val.append(p1v)
            if p1v > p2v:
                win += 1
            if p1v == p2v:
                tie += 1
        avg = sum(val)/n_opp
        if win > most_wins["win"]:
            most_wins["policy"] = p1_pol.copy()
            most_wins["win"] = win
            most_wins["tie"] = tie
            most_wins["avg"] = avg
            print("  Most Wins  ", most_wins["policy"], most_wins["win"], most_wins["tie"], most_wins["avg"])
        if tie > most_ties["tie"]:
            most_ties["policy"] = p1_pol.copy()
            most_ties["win"] = win
            most_ties["tie"] = tie
            most_ties["avg"] = avg
            print("  Most Ties  ", most_ties["policy"], most_ties["win"], most_ties["tie"], most_ties["avg"])
        if avg > best_vals["avg"]:
            best_vals["policy"] = p1_pol.copy()
            best_vals["win"] = win
            best_vals["tie"] = tie
            best_vals["avg"] = avg
            print("  Best Value ", best_vals["policy"], best_vals["win"], best_vals["tie"], best_vals["avg"])

    print()
    print("Most Wins  ", most_wins["policy"], most_wins["win"], most_wins["tie"], most_wins["avg"])
    print("Most Ties  ", most_ties["policy"], most_ties["win"], most_ties["tie"], most_ties["avg"])
    print("Best Value ", best_vals["policy"], best_vals["win"], best_vals["tie"], best_vals["avg"])


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
    """
    Does the experiment with different policies, specifically the default types in the
    :return:
    """
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
    :return: tuple of number of wins and ties
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
    return win, tie


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
    random_search_for_better_policy(100, 1000)
    # main()
