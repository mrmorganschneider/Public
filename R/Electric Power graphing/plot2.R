#NOTE: All data loading and processing is completed
#in the load_data.R file.

#read previously formatted data into system
library(tidyverse, help, pos = 2, lib.loc = NULL)
data <- as_tibble(readRDS("formattedData.rds"))

#Set display to PNG plot 2
png("Plot2.png")

datetime = c(1,1440,2880)

#plot line graph
plot(data$Global_active_power, type ="l", 
    xaxt = 'n', xlab = "", ylab = "Global active power (kilowatts)")
axis(1, at = datetime, labels = c("Thu", "Fri", "Sat"))

#Return display to windows
dev.off()
windows()