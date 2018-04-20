#RQ6

#import files
allUsersPostedQuestions <- read_csv("Downloads/allUsersPostedQuestions.csv")
onedayflies_user_ids <- read_csv("Downloads/onedayflies_user_ids.csv")

#use the match funcation called semi_join
 match1 <- semi_join(onedayflies_user_ids, allUsersPostedQuestions)
 
 # total number of onedayflies that are not onedayflies anymore is 23557 out of the 128260
 
