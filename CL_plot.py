import matplotlib
import matplotlib.pyplot as plt
import aggregation_functions as ag

db = ag.QueryDB('horses_data')

data = ag.query_table(db, 'race_general_results', ['time_final', 'race_temp'], where='distance = "1870"')

filtered_data = [item for item in data[0] if item[1] != 0 and item[0] != 0 and item[1] is not None
                 and item[0] is not None and item[1] < 120 and item[0] > 60]

times = [item[0] for item in filtered_data]
temps = [item[1] for item in filtered_data]

vmin = min(temps)
vmax = max(temps)

cmap = matplotlib.cm.get_cmap('jet')
norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)

fig, ax = plt.subplots(dpi=350)
scatter = ax.scatter(times, temps, s=0.2, c=cmap(norm(temps)))

print(len(times))
plt.show()


