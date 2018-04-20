import csv

with open('combined.csv') as deletedPosts:
	with open('onedayfliesId.csv') as fliesId:
		with open('notOneDayFliesId.csv') as NotId:
			fliesReader = csv.reader(fliesId)
			NotReader = csv.reader(NotId)
			deletedReader = csv.reader(deletedPosts)

			count = 0
			rowcount = 0
			deletedIds =[]
			for row in deletedReader:
				if 'Id' not in row:
					deletedIds.append(float(row[0]))

			for row in fliesReader:
				
				if 'id' not in row[0]:
					rowcount += 1
					if float(row[0]) in deletedIds:
						count += 1

			print("total number of deleted= "+str(count))	
			print("total number = "+str(rowcount))		
					
			count = 0
			rowcount2 = 0
			for row in NotReader:
				rowcount2 += 1
				if 'id' not in row[0]:
					rowcount += 1
					if float(row[0]) in deletedIds:
						count += 1

			print("total number of deleted for others= "+str(count))	
			print("total number = "+str(rowcount2))		
					