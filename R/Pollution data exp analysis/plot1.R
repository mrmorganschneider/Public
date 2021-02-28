#Read RDS file data
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

plot1 <- tapply(NEI$Emissions, NEI$year, mean)

#create plot
png("Plot1.png")
plot(plot1, type = "b", main = "Mean emissions over time for US", xlab = "Year", ylab = "Mean emissions", xaxt ='n')
axis(1, at = c(1,2,3,4), labels = c("1999", "2002", "2005", "2008"))
dev.off()
windows()