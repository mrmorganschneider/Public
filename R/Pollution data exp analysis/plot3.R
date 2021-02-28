library(reshape)
library(tidyverse)

#Read RDS file data
NEI <- subset(readRDS("summarySCC_PM25.rds"), fips == "24510")
SCC <- readRDS("Source_Classification_Code.rds")

#process data
plot3 <- data.frame(tapply(NEI$Emissions, list(NEI$year, NEI$type), mean))
plot3$Year <- rownames(plot3)
plot3 <- melt(plot3, id.vars = 'Year', variable.name = 'Type')
names(plot3) <- c("Year", "Type", "Emissions")


#create plot
png("Plot3.png")
qplot(data = plot3, Year, Emissions, color = Type, size = 4, main = "Type emissions for Baltimore")
dev.off()
windows()