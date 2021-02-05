#NOTE: All data loading and processing is completed
#in the load_data.R file.

#read previously formatted data into system
library(tidyverse, help, pos = 2, lib.loc = NULL)
data <- as_tibble(readRDS("formattedData.rds"))

#Set display to PNG
png("Plot1.png")

#Create Plot 1
hist(data$Global_active_power, col="red", 
    main = "Global Active Power",
    xlab = "Global Active Power (Kilowatts)")

#Return display to windows
dev.off()
windows()