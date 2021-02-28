#Read RDS file data
NEI <- readRDS("summarySCC_PM25.rds")
SCC <- readRDS("Source_Classification_Code.rds")

#process data
coal_sources <- grep(unique(SCC$EI.Sector), pattern = "*[Cc]oal", value = TRUE)
coal_SCC <- subset(SCC, EI.Sector %in% coal_sources, SCC)
coal_Dataset <- subset(NEI, SCC %in% coal_SCC[,1])
plot4 <- with(coal_Dataset,tapply(Emissions, year, mean))

#create plot
png("Plot4.png")
plot(plot4, type = "b", main = "Mean emissions over time for US Coal", xlab = "Year", ylab = "Mean emissions", xaxt ='n')
axis(1, at = c(1,2,3,4), labels = c("1999", "2002", "2005", "2008"))
dev.off()
windows()