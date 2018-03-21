import matplotlib
import matplotlib.pyplot as plt
import aggregation_functions as ag

db = ag.QueryDB('horses_data')

# Get the race times and temperature from the database
data = ag.query_table(db, 'race_general_results', ['time_final', 'race_temp'], where='distance = "1870"')

# Pull out items with missing final times or temps that are wildly out of range
filtered_data = [item for item in data[0] if item[1] != 0 and item[0] != 0 and item[1] is not None
                 and item[0] is not None and item[1] < 120 and item[0] > 60]

# Split up the data into x- and y-values (time and temp, respectively)
times = [item[0] for item in filtered_data]
temps = [item[1] for item in filtered_data]

# Get average race time for each temperature
# Group final times by temp in a dict
average_dict = dict.fromkeys(temps, list())
for item in filtered_data:
    average_dict[item[1]].append(item[0])
# Get the average for each dict entry/temperature and set that as the dict value for that temp
for temp in average_dict:
    average_dict[temp] = sum(average_dict[temp] / len(average_dict.temp))

# Set up the colormap to use min and max values for color spectrum
vmin = min(temps)
vmax = max(temps)
cmap = matplotlib.cm.get_cmap('jet')
norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)



fig, ax = plt.subplots(dpi=350)
scatter = ax.scatter(times, temps, s=0.2, c=cmap(norm(temps)))

print(len(times))
plt.show()


