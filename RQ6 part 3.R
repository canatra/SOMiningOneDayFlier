match1 <- semi_join(onedayflies_user_ids, x)
x <- combined_6_[1]

match4 <- full_join(onedayfliesWdate , combined_6_ , by = c("OwnerUserID"))

notnull<- na.omit(match4)
write.csv(notnull, file = "notnull.csv")
