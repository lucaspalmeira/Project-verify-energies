#! /usr/bin/python3

import math
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import glob

def main():

	file_pdbqt = glob.glob('*/*.pdbqt')
	file_log = glob.glob('*/*.txt')
	error_log = []
	error_out = []
	energies = []

	for log in file_log:
		reading_log = open(log)
		lines_log = reading_log.readlines()
		reading_log.close()
		try:
			line_27 = lines_log[25].rstrip()
			energy_affinity = line_27[12:17]
			energies.append(energy_affinity)
		except:
			error_log.append(log)

	CID = []
	path = []

	for pdbqt in file_pdbqt:
		reading_out = open(pdbqt)
		lines_out = reading_out.readlines()
		reading_out.close()
		try:
			line_3 = lines_out[2].rstrip()
			name_CID = line_3[8:]
			CID.append(name_CID)
			path.append(pdbqt)
		except:
			error_out.append(pdbqt)

	new_energies = []

	for x in energies:
		element = x
		for y in [' ']:
			element = element.replace(y, "")
		new_energies.append(float(element))

	with open('verify_energies.txt', 'w') as file:

		arithmetic_average = (math.fsum(new_energies)) / len(new_energies)
		file.write(f'Arithmetic mean of the affinity energy in Kcal/mol: {arithmetic_average}\n')

		more_frequent_energy = statistics.mode(new_energies)
		file.write(f'Most common energy value: {more_frequent_energy}\n')

		median = statistics.median(new_energies)
		file.write(f'Median of energies: {median}\n')

		variance = statistics.variance(new_energies)
		file.write(f'Variance of energies: {variance}\n')

		print('Creating dataframe...\n')

	data = {'Path': path, 'CID Molecule': CID, 'Affinity Energy (Kcal/mol)': new_energies}
	df = pd.DataFrame(data, columns=['Path','CID Molecule','Affinity Energy (Kcal/mol)'])
	df.to_csv('verify_energies.csv')

	print('The verify_energies.csv file has been saved.')

	plt.title('Verify Energies', fontsize = 20)
	plt.xlabel('Affinity Energy (Kcal/mol)', fontsize = 15)
	plt.ylabel('Number of compounds', fontsize = 15)
	plt.hist(new_energies, 20, rwidth = 0.8, edgecolor = 'black')
	plt.savefig('verify_energies.png', format='png')


if __name__ == '__main__':
	main()
