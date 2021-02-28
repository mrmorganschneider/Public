#Read RDS file data
NEI <- subset(readRDS("summarySCC_PM25.rds"), fips == "24510")
SCC <- readRDS("Source_Classification_Code.rds")

plot2 <- tapply(NEI$Emissions, NEI$year, mean)

#create plot
png("Plot2.png")
plot(plot2, type = "b", main = "Mean emissions over time for Baltimore", xlab = "Year", ylab = "Mean emissions", xaxt ='n')
axis(1, at = c(1,2,3,4), labels = c("1999", "2002", "2005", "2008"))
dev.off()
windows()