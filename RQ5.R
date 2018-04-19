#RQ5

#import file
notOneDayAnsCount <- read_csv("Downloads/notOneDayAnsCount.csv")
onedayAnswerCount <- read_csv("Downloads/onedayAnswerCount.csv")

#find the avg of Null values for both files
#sum
a1=sum(is.na(notOneDayAnsCount$answer_count))
#avg
a11=sum(is.na(notOneDayAnsCount$answer_count))/128260*100
#sum
a2=sum(is.na(onedayAnswerCount$answer_count))
#avg
a22=sum(is.na(onedayAnswerCount$answer_count))/128260*100

# one day fly was 19%
# all users was 7%
#plot


