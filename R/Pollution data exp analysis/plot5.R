library(tidyverse)
library(reshape)
library(RColorBrewer)

#Read RDS file data
NEI <- subset(readRDS("summarySCC_PM25.rds"), fips == "24510")
SCC <- readRDS("Source_Classification_Code.rds")

#process data
vehicle_sources <- grep(unique(SCC$EI.Sector), pattern = "^Mobile *", value = TRUE)
vehicle_SCC <- subset(SCC, EI.Sector %in% vehicle_sources, c(SCC, EI.Sector))
vehicle_data <- subset(NEI, SCC %in% vehicle_SCC[,1])

for( i in vehicle_SCC$SCC){
    vehicle_data[vehicle_data == i] <- as.vector(subset(vehicle_SCC, SCC == i, EI.Sector)[1,])
}

plot5 <- data.frame(tapply(vehicle_data$Emissions, list(vehicle_data$year, vehicle_data$SCC), mean))
plot5$Year <- rownames(plot5)
plot5 <- melt(plot5, id.vars = 'Year', variable.name = 'Type')
names(plot5) <- c("Year", "Type", "Emissions")

#create plot
png("Plot5.png", width = 600, height = 600)
p <- ggplot(plot5, aes(x=Year, y=Emissions)) + coord_cartesian(ylim = c(0,10))
p <- p + geom_line(aes(color=Type, group=Type)) 
p <- p + labs(title="Particulate output for Baltimore")
print(p)
dev.off()
windows()