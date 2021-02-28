library(tidyverse)
library(reshape)
library(RColorBrewer)
library(cowplot)

#Read RDS file data
NEI <- subset(readRDS("summarySCC_PM25.rds"), fips == c("24510","06037"))
SCC <- readRDS("Source_Classification_Code.rds")

#process data
vehicle_sources <- grep(unique(SCC$EI.Sector), pattern = "^Mobile *", value = TRUE)
vehicle_SCC <- subset(SCC, EI.Sector %in% vehicle_sources, c(SCC, EI.Sector))
vehicle_data <- subset(NEI, SCC %in% vehicle_SCC[,1])

#find and replace SCC codes with their description
for( i in vehicle_SCC$SCC){
    vehicle_data[vehicle_data == i] <- as.vector(subset(vehicle_SCC, SCC == i, EI.Sector)[1,])
}

#sort baltimore and la data
vehicle_data_B <- subset(vehicle_data, fips == "24510")
vehicle_data_L <- subset(vehicle_data, fips == "06037")

plot6B <- data.frame(tapply(vehicle_data_B$Emissions, list(vehicle_data_B$year, vehicle_data_B$SCC), mean))
plot6B$Year <- rownames(plot6B)
plot6B <- melt(plot6B, id.vars = 'Year', variable.name = 'Type')
names(plot6B) <- c("Year", "Type", "Emissions")


plot6L <- data.frame(tapply(vehicle_data_L$Emissions, list(vehicle_data_L$year, vehicle_data_L$SCC), mean))
plot6L$Year <- rownames(plot6L)
plot6L <- melt(plot6L, id.vars = 'Year', variable.name = 'Type')
names(plot6L) <- c("Year", "Type", "Emissions")

#create plot
png("plot6.png", width = 1080, height = 960)
p <- ggplot(plot6B, aes(x=Year, y=Emissions)) + coord_cartesian(ylim = c(0,100))
p <- p + geom_line(aes(color=Type, group=Type)) 
p <- p + labs(title="Particulate output for Baltimore")

q <- ggplot(plot6L, aes(x=Year, y=Emissions)) + coord_cartesian(ylim = c(0,100))
q <- q + geom_line(aes(color=Type, group=Type)) 
q <- q + labs(title="Particulate output for Los Angeles")

plot_grid(p,q, cols=2)
dev.off()
windows()