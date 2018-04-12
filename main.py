from player import *
from experiment_random_search import *


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


if __name__ == '__main__':
    random_search_for_better_policy(100, 1000)
    # main()
