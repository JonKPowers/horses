import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def gamblers_ruin(bankroll=1000, house=100000, return_data=False):
    house_record = []
    bankroll_record = []
    rounds = 0

    while bankroll > 0 and house > 0:
        rounds += 1
        coin_flip = random.randint(0, 1)
        if coin_flip:
            bankroll += 1
            house -= 1
        else:
            bankroll -= 1
            house += 1
        house_record.append(house)
        bankroll_record.append(bankroll)

    # Set up plots
    fig, ax = plt.subplots()

    # Scale the number of rounds by a thousand
    ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/1000))
    ax.xaxis.set_major_formatter(ticks_x)

    ax.set_xlabel('Number of Rounds (thousands)')
    ax.set_ylabel('Bankroll ($)')
    ax.set_title(f'Gambler\'s Ruin ({rounds} rounds)')
    ax.plot(range(len(bankroll_record)), bankroll_record)
    plt.show()
    # fig, ax = plt.subplots()
    # ax.plot(range(len(house_record)), house_record)
    # plt.show()

    return None
