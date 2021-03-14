#library(tidyverse)
#download.file("https://d396qusza40orc.cloudfront.net/repdata%2Fdata%2FStormData.csv.bz2", "StormData.csv.bz2")
#raw_Data <- read.csv("StormData.csv.bz2")
#raw_Data <- raw_Data[,c("EVTYPE","FATALITIES","INJURIES","PROPDMG","PROPDMGEXP")]

raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "HEAT WAVE", "EXCESSIVE HEAT")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "THUNDERSTORM WIND", "TSTM WIND")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "RIP CURRENTS", "RIP CURRENT")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "HEAVY SNOW", "WINTER STORM")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "STRONG WIND", "HIGH WIND")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "EXTREME COLD/WIND CHILL", "WINTER STORM")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "BLIZZARD", "WINTER STORM")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "EXTREME HEAT", "EXCESSIVE HEAT")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "COLD/WIND CHILL", "WINTER STORM")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "ICE STORM", "WINTER STORM")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "TSTM WINDS", "TSTM WIND")
raw_Data$EVTYPE <- str_replace(raw_Data$EVTYPE, "HURRICANE/TYPHOON", "HURRICANE")

health_Data <- aggregate(cbind(raw_Data$FATALITIES, raw_Data$INJURIES), 
    by=list(raw_Data$EVTYPE), FUN=sum) %>%
    subset(V1 != 0 & V2 != 0)

names(health_Data) <- c("Event", "Fatalities", "Injuries")   
health_Data <- health_Data[order(-health_Data$Fatalities),]