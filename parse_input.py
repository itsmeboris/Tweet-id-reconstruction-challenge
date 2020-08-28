from config import(
	input_files,
	machine_ids
)

from helper import(
	tweet_components
)

import json
import collections

class ParseInput:
	def __init__(self):
		self.input = input_files
		self.machine_id = { }
		self.total = 0
		self.sequence_id = { }
		self.s = { }
		self.m = { }

	def parse_top(self, input):
		with open(input, 'r') as inputfile:
			print(f'working on file: {input}')
			line = inputfile.readline()
			self.machine_id[input] = { }
			while line:
				machine_id, sequence_id = tweet_components(line)
				if machine_id not in machine_ids:
					line = inputfile.readline()
					continue
				elif machine_id not in self.machine_id[input]:
					self.machine_id[input][machine_id] = { 'total': 0, 'seq': { }}
				else:
					self.machine_id[input][machine_id]['total'] += 1
				if sequence_id not in self.machine_id[input][machine_id]['seq']:
					self.machine_id[input][machine_id]['seq'][sequence_id] = {'total': 1, 'percent': 0}
				else:
					self.machine_id[input][machine_id]['seq'][sequence_id]['total'] += 1 	
				line = inputfile.readline()
			print(f'finished working on file: {input}')

	def go(self):
		for key in self.input.keys():
			self.parse_top(f'{key}.txt')
		for input_key in self.machine_id.keys():
			for machine_id in self.machine_id[input_key].keys():
				total = self.machine_id[input_key][machine_id]['total']
				seq = self.machine_id[input_key][machine_id]['seq']
				l = list(seq.items())
				for line in l:
					t = line[1]['total']
					seq[line[0]]['percent'] = t/total
		with open(f'output.json', 'w') as outputjson:
			json.dump(self.machine_id, outputjson)

			
	def run(self):
		self.go()
		self.__init__()
		for key in self.input:
			print(f'working on file: {key}')
			with open(f'{key}.txt', 'r') as inputfile:
				line = inputfile.readline()
				while line:
					self.total += 1
					machine_id, sequence_id = tweet_components(line)
					if machine_id in self.machine_id:
						self.machine_id[machine_id] += 1
					else:
						self.machine_id[machine_id] = 1
					if sequence_id in self.sequence_id:
						self.sequence_id[sequence_id] += 1
					else:
						self.sequence_id[sequence_id] = 1
					line = inputfile.readline()
			sort_machine_id = sorted(self.machine_id.items(), key=lambda x: x[1], reverse=True)
			sort_sequence_id = sorted(self.sequence_id.items(), key=lambda x: x[1], reverse=True)
			with open(f'machine-{key}.txt', 'w') as machine_id_out:
				t = 0
				machine_id_out.write('Machine id\t\t%\t\t\t\tTotal %\n')
				for k, v in sort_machine_id:
					t += v/self.total
					machine_id_out.write(f'{k}\t\t\t{v/self.total}\t\t{t}\n')
				machine_id_out.write(f'total machines: {len(sort_machine_id)}\n')
			with open(f'seq-{key}.txt', 'w') as seq_id_out:
				seq_id_out.write('Sequence id\t\t%\t\t\t\tTotal %\n')
				t = 0
				for k, v in sort_sequence_id:
					t += v/self.total
					seq_id_out.write(f'{k}\t\t\t{v/self.total}\t\t{t}\n')
				seq_id_out.write(f'total seq: {len(sort_sequence_id)}\n')
			print(f'finished working on file: {key}')
if __name__ == "__main__":
	ParseInput().run()

