#!/usr/bin/python3
import matplotlib
import matplotlib.pyplot as plt

import numpy as np


def import_results(filename):
	with open(filename) as f:
		lines = f.read().split('\n')

	cores = [[],[],[],[]]

	for line in lines:
		line_arr = line.split(',')
		for i in range(4):
			cores[i].append(int(line_arr[i]))

	return cores

def plot_cores(method, results):
	time = [ i/60 for i in range(len(results[0]))]

	fig, ax = plt.subplots()

	colors = ['r', 'g', 'b', 'orange']
	i = 0	
	for core in results:
		ax.plot(time, core, color=colors[i], linewidth=0.25, label='Core '+ str(i))
		i += 1

	y_min, y_max = ax.get_ylim()
	plt.yticks(np.arange(int(y_min), int(y_max)+5, 5))
	plt.xlim(0, len(results[0])/60)
	ax.set(xlabel='Time (min)', ylabel='CPU Core Temp (C)',
       title=str('Core Temps for CPU Over Time ('+method+')'))
	ax.grid()
	ax.legend()

	fig.savefig(method + '-results.png')

def return_average(results):
	average_core_temp = []

	for i in range(len(results[0])):
		average_core_temp.append(np.mean([results[0][i],results[1][i],results[2][i],results[3][i]]))

	return average_core_temp

def plot_averages(results):

	averaged_results = []

	for result in results:
		averaged_results.append(return_average(results[result]))

	fig, ax = plt.subplots()

	colors = ['r', 'g', 'b', 'orange']
	methods = [ 'Stock Heatsink', 'Stock Heatsink & Case Fan', 'AIO 120mm']
	i = 0

	for method in averaged_results:
		ax.plot([ i/60 for i in range(len(averaged_results[i]))], method, color=colors[i], linewidth=0.25, label=methods[i])
		i += 1

	y_min, y_max = ax.get_ylim()
	plt.yticks(np.arange(int(y_min), int(y_max)+5, 5))
	plt.xlim(0, len(averaged_results[0])/60)
	ax.set(xlabel='Time (min)', ylabel='CPU Core Temp (C)',
       title=str('Core Temps for CPU Over Time by Method of Cooling'))
	ax.grid()
	ax.legend()

	fig.savefig('method-results.png')

if __name__ == '__main__':

	results = {'stock_heatsink' : import_results('stock-heatsink-results.csv'), 'stock_plus_case_fan': import_results('stock-plus-case-fan.csv'), 'aio_120mm': import_results('aio-120mm-results.csv')}

	for result in results:
		plot_cores(result, results[result])

	plot_averages(results)