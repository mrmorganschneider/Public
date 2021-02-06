#NOTE: All data loading and processing is completed
#in the load_data.R file.

#read previously formatted data into system
library(tidyverse, help, pos = 2, lib.loc = NULL)
data <- as_tibble(readRDS("formattedData.rds"))

#Set display to PNG plot 3
png("Plot3.png")

datetime = c(1,1440,2880)

#plot line graph and set axis values
plot(data$Sub_metering_1, type ="l", 
    xaxt = 'n', xlab = "", ylab = "Energy sub metering")
axis(1, at = datetime, labels = c("Thu", "Fri", "Sat"))

#add additional required line graphs to plot
lines(data$Sub_metering_2, type ="l", col = "red")
lines(data$Sub_metering_3, type ="l", col = "blue")

#add legend
legend("topright", legend = c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"),
    col = c("black", "red", "blue"), lwd = 1)

#turn off pdf
dev.off()