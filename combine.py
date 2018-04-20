import csv
import os


def concatFile(filename, writeFile):

	#1
	#print('AccelerationExplorer-angry3.csv')
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
	
		for row in reader:
			#print(row[1].split(',')[0])
			if 'id' not in row:
				print(row)
				writeFile.writerow(row)
					
				




with open('combined.csv','wb') as csvfile:
	combinedWriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

	for root, dirs, filenames in os.walk('.'):
		for filename in filenames:
			if '.py' not in filename and 'combined' not in filename:
				print(filename)
				concatFile(filename, combinedWriter)
