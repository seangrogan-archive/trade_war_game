from trade_war_game import *
import multiprocessing as mp


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

    #for i in range(n_test):
        #test(i, n_opp, most_wins, most_ties, best_vals)

    pool = mp.Pool(processes=mp.cpu_count())
    result = [pool.apply(test, args=(i, n_opp, most_wins, most_ties, best_vals)) for i in range(n_test)]
    output = [p.get() for p in result]
    print(output)



    print()
    print("Most Wins  ", most_wins["policy"], most_wins["win"], most_wins["tie"], most_wins["avg"])
    print("Most Ties  ", most_ties["policy"], most_ties["win"], most_ties["tie"], most_ties["avg"])
    print("Best Value ", best_vals["policy"], best_vals["win"], best_vals["tie"], best_vals["avg"])


def test(i, n_opp, most_wins, most_ties, best_vals):
    print(" Executing Test", i)
    win = 0
    tie = 0
    val = list()
    f1 = random.randint(0, 100) / 100.0
    i1 = random.randint(0, 100) / 100.0
    v1 = random.randint(0, 100) / 100.0
    p1_pol = [f1, i1, v1]
    for i in range(n_opp):
        p1v, p2v = game(val, p1_pol)
        if p1v > p2v:
            win += 1
        if p1v == p2v:
            tie += 1
    avg = sum(val) / n_opp
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


def game(val, p1_pol):
    f2 = random.randint(0, 100) / 100.0
    i2 = random.randint(0, 100) / 100.0
    v2 = random.randint(0, 100) / 100.0
    p2_pol = [f2, i2, v2]
    p1v, p2v = experiment(p1_pol, p2_pol)
    val.append(p1v)
    return p1v, p2v
