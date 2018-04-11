import csv


with open('onedayTags.csv') as onedayTags:
	with open('allotherTags.csv') as allotherTags:

		oneDayreader = csv.reader(onedayTags)
		#allreader = csv.reader(allotherTags)
		oneDayDict ={}
		count = 0

		for row in oneDayreader:
			if len(row) > 0:
				
				rowBreak = row[0].split('>')

				for tag in rowBreak:
					if len(tag) > 0:
						tag = tag.split('<')
						if len(tag) == 2:
							if tag[1] in oneDayDict:
								oneDayDict[tag[1]] += 1
								count +=1
							else:
								oneDayDict[tag[1]] = 1
								count +=1
		#code reused from project 4 part 3 number 7
		with open('tags.csv', 'w') as csvWritefile:						
			writer = csv.writer(csvWritefile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			writer.writerow(['Total Number of Tags','One day flies Tags'])
						

			sortedList =[]
			sortedTag = {}
			for key in oneDayDict:
				sortedTag[oneDayDict[key]] = key
				sortedList.append(oneDayDict[key])
			sortedList = sorted(sortedList, reverse = True)	
			
			count = 0
			for key in sortedList:
				writer.writerow([key, sortedTag[key]])
				count += 1
				if count == 50:
					break
