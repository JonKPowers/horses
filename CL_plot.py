import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as si
import re

import aggregation_functions as ag



def generate_individual_plots():
    for distance, title, min_time, max_time, min_temp, max_temp in zip(races_to_review.keys(), titles, min_times,
                                                                       max_times, min_temps, max_temps):
        fig, ax  = plt.subplots()
        temps, times, average_temps, average_times = pull_final_times(distance, min_time, max_time, min_temp, max_temp)

        # Smoothing with interp1d:
        t_ipl = np.linspace(min(average_temps), max(average_temps), 200)
        interpl_func = si.interp1d(average_temps, average_times, kind='cubic')
        times_interpl = interpl_func(t_ipl)

        # Set up the colormap to use min and max values for color spectrum
        vmin = min(temps)
        vmax = max(temps)
        cmap = matplotlib.cm.get_cmap('jet')
        norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)

        ax.scatter(temps, times, s=0.2, c=cmap(norm(temps)))
        ax.plot(t_ipl, times_interpl, label='mean race time')
        ax.set_title(title)
        ax.set_xlabel('Temperature (degrees F)')
        ax.set_ylabel('Final time (seconds)')
        ax.legend(loc='best')
        plt.tight_layout()
        plt.savefig(re.sub(r'/', '', title)+'.png')


def pull_final_times(db, race_distance, min_time, max_time, min_temp, max_temp):
    # Get the race times and temperature from the database
    data = ag.query_table(db,
                          'race_general_results',
                          ['time_final', 'race_temp'],
                          where=f'distance = "{race_distance}"')

    # Pull out items with missing final times or temps that are wildly out of range
    filtered_data = [item for item in data if item[1] != 0 and item[0] != 0 and item[1] is not None
                     and item[0] is not None and item[0] < max_time and item[0] > min_time
                     and item[1] < max_temp and item[1] > min_temp]
    
    # Sort data by temps
    filtered_data = sorted(filtered_data, key=lambda x: x[1])

    # Split up the data into x- and y-values (temp and time, respectively)
    times = [item[0] for item in filtered_data]
    temps = [item[1] for item in filtered_data]

    # Get average race time for each temperature
    # Group final times by temp in a dict
    average_dict = dict.fromkeys(temps)
    for key in average_dict:
        average_dict[key] = []
    for item in filtered_data:
        average_dict[item[1]].append(item[0])
    # Get the average for each dict entry/temperature and set that as the dict value for that temp
    for temp in average_dict:
        average_dict[temp] = sum(average_dict[temp]) / len(average_dict[temp])

    # Put the averages in order and split them into lists of temps and times
    averages = sorted([(temp, time) for temp, time in average_dict.items()])
    average_temps = [item[0] for item in averages]
    average_times = [item[1] for item in averages]

    return temps, times, average_temps, average_times

def make_plot(db):
    db = ag.QueryDB(db)
    races_to_review = {
        '1100': ['5 Furlongs', 40, 120, -20, 105],
        '1210': ['5.5 Furlongs', 40, 120, -20, 105],
        '1320': ['6 Furlongs', 60, 120, -20, 150],
        '1430': ['6.5 Furlongs', 0, 100, -20, 110],
        '1540': ['7 Furlongs', 0, 120, -20, 150],
        '1760': ['1 Mile', 0, 120, -20, 150],
        '1830': ['1 Mile + 70 Yards', 0, 120, -20, 150],
        '1870': ['1 1/16 Mile', 0, 120, -5, 150],
    }

    titles = [races_to_review[key][0] for key in races_to_review.keys()]
    min_times = [races_to_review[key][1] for key in races_to_review.keys()]
    max_times = [races_to_review[key][2] for key in races_to_review.keys()]
    min_temps = [races_to_review[key][3] for key in races_to_review.keys()]
    max_temps = [races_to_review[key][4] for key in races_to_review.keys()]

    fig, ax = plt.subplots(8, figsize=(8, 45), dpi=200)
    axes = [ax_item for _, ax_item in np.ndenumerate(ax)]


    for distance, ax, title, min_time, max_time, min_temp, max_temp in zip(races_to_review.keys(), axes, titles,
                                                                           min_times, max_times, min_temps, max_temps):
        temps, times, average_temps, average_times = pull_final_times(db, distance,
                                                                      min_time, max_time,
                                                                      min_temp, max_temp)

        # Smooth out the averages for visualization purposes
        # Smoothing with b-spline for parameterized x- and y-values
        t = average_temps
        t_ipl = np.linspace(min(average_temps), max(average_temps), 200)

        temps_tup = si.splrep(t, average_temps)
        times_tup = si.splrep(t, average_times)
        temps_ipl = si.splev(t_ipl, temps_tup)
        times_ipl = si.splev(t_ipl, times_tup)

        # Smoothing with interp1d:
        interpl_func = si.interp1d(average_temps, average_times, kind='cubic')
        times_interpl = interpl_func(t_ipl)


        # Set up the colormap to use min and max values for color spectrum
        vmin = min(temps)
        vmax = max(temps)
        cmap = matplotlib.cm.get_cmap('jet')
        norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)

        ax.scatter(temps, times, s=0.2, c=cmap(norm(temps)))
        ax.plot(t_ipl, times_interpl, label='mean race time')
        ax.set_title(title)
        ax.set_xlabel('Temperature (degrees F)')
        ax.set_ylabel('Final time (seconds)')
        ax.legend(loc='best')


    fig.tight_layout()
    fig.savefig('race_times_vs_temperature.png')
    # plt.show()


