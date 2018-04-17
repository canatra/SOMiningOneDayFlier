#RQ6

#import files
allUsersPostedQuestions <- read_csv("Downloads/allUsersPostedQuestions.csv")
onedayflies_user_ids <- read_csv("Downloads/onedayflies_user_ids.csv")

#use the match funcation called semi_join
 match1 <- semi_join(onedayflies_user_ids, allUsersPostedQuestions)
 
 # total number of onedayflies that are not onedayflies anymore is 436 out of the 128260
 
 #working with dates
 
 #match between match 1 and one dayflyWdate
 match2 <- semi_join(onedayfliesWdate, match1)
 
 #match between match 1 and one ownerUserIDWdate
 match3 <- semi_join(OwnerUserIDsWDate, match1)
 
 