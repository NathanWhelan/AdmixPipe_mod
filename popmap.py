from __future__ import print_function

from collections import defaultdict
from collections import OrderedDict

class Popmap():
	'Class for parsing a popmap'

	def __init__(self, infile):
		#member variables
		self.popmap = OrderedDict()
		self.popnums = defaultdict(int)
	
		try:
			with open(infile, 'r') as f:
				for line in f:
					(key, val) = line.split()
					self.popmap[key] = val #make map of individual->population
		except ValueError:
			print("Too many columns detected in your popmap file.")
			print(infile, "may have spaces in either sample or population names.")
			print("Verify your popmap file is in the correct format and try rerunning.")
			raise SystemExit

	def get_pop(self,ind):
		return self.popmap.get(ind)

	def get_list(self):
		return list(self.popmap.keys())
