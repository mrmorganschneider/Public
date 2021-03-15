library(tidyverse)
#download.file("https://d396qusza40orc.cloudfront.net/repdata%2Fdata%2FStormData.csv.bz2", "StormData.csv.bz2")
raw_Data <- read.csv("StormData.csv.bz2")
raw_Data <- raw_Data[,c("EVTYPE","FATALITIES","INJURIES","PROPDMG","PROPDMGEXP")]

#replace names with generic ones as required
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "HEAT WAVE", "EXCESSIVE HEAT")
raw_Data$EVTYPE <- gsub( ".*THUNDERSTORM.*", "TSTM WIND", raw_Data$EVTYPE, perl = TRUE)
raw_Data$EVTYPE <- gsub( ".*HEAT.*", "EXCESSIVE HEAT", raw_Data$EVTYPE, perl = TRUE)
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "RIP CURRENTS", "RIP CURRENT")
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "HEAVY SNOW", "WINTER STORM")
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "STRONG WIND", "HIGH WIND")
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "EXTREME COLD/WIND CHILL", "WINTER STORM")
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "BLIZZARD", "WINTER STORM")
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "EXTREME HEAT", "EXCESSIVE HEAT")
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "COLD/WIND CHILL", "WINTER STORM")
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "ICE STORM", "WINTER STORM")
raw_Data$EVTYPE <- str_replace_all(raw_Data$EVTYPE, "TSTM WINDS", "TSTM WIND")
raw_Data$EVTYPE <- gsub(".*HURRICANE.*", "HURRICANE", raw_Data$EVTYPE, perl = TRUE)
raw_Data$EVTYPE <- gsub( ".*HIGH SURF.*", "HIGH SURF", raw_Data$EVTYPE, perl = TRUE)

#create fatality data
sum_health_Data <- aggregate(cbind(raw_Data$FATALITIES, raw_Data$INJURIES), 
    by=list(raw_Data$EVTYPE), FUN=sum) %>%
    subset(V1 != 0 & V2 != 0)
names(sum_health_Data) <- c("Event", "Fatalities", "Injuries")   
sum_health_Data <- sum_health_Data[order(-sum_health_Data$Fatalities),]
event_types <- sum_health_Data$Event[1:6]

top_6_data <- subset(raw_Data, EVTYPE %in% event_types)
boxplot(top_6_data$FATALITIES ~ top_6_data$EVTYPE, xlab = "Event",
    ylab = "Fatalities", main = "Event fatalities boxplot")

#create injury data
sum_health_Data <- aggregate(cbind(raw_Data$FATALITIES, raw_Data$INJURIES), 
    by=list(raw_Data$EVTYPE), FUN=sum) %>%
    subset(V1 != 0 & V2 != 0)
names(sum_health_Data) <- c("Event", "Fatalities", "Injuries")   
sum_health_Data <- sum_health_Data[order(-sum_health_Data$Injuries),]
event_types <- sum_health_Data$Event[1:6]

top_6_data <- subset(raw_Data, EVTYPE %in% event_types)
boxplot(top_6_data$INJURIES ~ top_6_data$EVTYPE, xlab = "Event",
    ylab = "Injuries", main = "Event injuries boxplot")

#create cost data
sum_cost_data <- aggregate(cbind(raw_Data$PROPDMG, raw_Data$PROPDMGEXP), 
    by=list(raw_Data$EVTYPE), FUN=sum) %>%
    subset(V1 != 0 & V2 != 0)