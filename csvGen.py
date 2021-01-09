import csv, random, time
import numpy as np

day = 0
infected = 10
healthy = 1000 - infected
removed = 0
infected_list = [1.0] * infected

interaction_rate = .01
transission_rate = .25
removal_rate = .005

fieldnames = ['day', 'healthy', 'infected', 'removed']

with open('data.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
	csv_writer.writeheader()

while True:
	with open('data.csv', 'a') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

		info = {
		"day" : day,
		"healthy" : healthy,
		"infected" : infected,	
		"removed" : removed
		}

		csv_writer.writerow(info)
		print(day, healthy, infected, removed)

		iters = (infected * healthy) * 0.1
		for i in range(int(iters)):
			chance_interaction = np.random.random()
			if chance_interaction < interaction_rate:
				chance_transmission = np.random.random()
				if chance_transmission < transission_rate:
					infected += 1
					healthy -= 1
					infected_list.append(1)
			chance_removal = np.random.uniform(0.0001,0.3)
		for x in infected_list:
			if x < chance_removal: 
				removed += 1
				infected -= 1
				infected_list.pop(0)
		day += 1
		if day > 100: break

	infected_array = np.asarray(infected_list)
	updated = np.subtract(infected_array, 0.1)
	#print(updated)

	infected_list = list(updated)
	time.sleep(0.1)

# Add queue with each item in the queue on a countd
#own timer (7 days till removal)
# Ideally removal rate would increase with each day past 3 days into infection
# Print out summary using the CSV file
