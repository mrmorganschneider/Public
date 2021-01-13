acs <- read.csv("acs.csv")

#commands will select only the data for the probability weights pwgtp1 with ages less than 50
sqldf("select pwgtp1 from acs where AGEP 50")

#what is the equivalent function to unique(acs$AGEP)
sqldf("select distinct AGEP from acs")