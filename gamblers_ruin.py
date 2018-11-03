import random
import matplotlib.pyplot as plt

def gamblers_ruin(bankroll=1000, house=100000):
    house_record = []
    bankroll_record = []

    while bankroll > 0 and house > 0:
        coin_flip = random.randint(0, 1)
        if coin_flip:
            bankroll += 1
            house -= 1
        else:
            bankroll -= 1
            house += 1
        house_record.append(house)
        bankroll_record.append(bankroll)
    fig, ax = plt.subplots()
    ax.plot(range(len(bankroll_record)), bankroll_record)
    plt.show()
    fig, ax = plt.subplots()
    ax.plot(range(len(house_record)), house_record)
    plt.show()

    return bankroll_record, house_record