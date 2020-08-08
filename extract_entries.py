with open('kaka_BC OUT (1).txt', mode='r') as file:
	with open('final_entries.txt', mode='w') as data:

		for line in file.readlines():

			a = line.split()
			b = ''
			
			if (len(a) > 0):

				for i in a[-1]:
					if (i == ','):
						pass
					else:
						b = b + i

				if (float(b) > 999):
					data.write(' '.join(a))
					data.write('\r\n')

