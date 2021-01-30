#Nike run analysis program for peer-graded assigment for 
#Getting and cleaning data course project

#Created by Morgan Schneider Jan 27, 2021

library(tidyverse, help, pos = 2, lib.loc = NULL)

#Function to check for data sets and download if not
#present in the current working directory
data_download <- function(URL) {
    download.file(URL, destfile = "nike_data.zip", method = "curl" )
    unzip("nike_data.zip")
}

#check if data has been downloaded and unzipped
if(!file.exists("nike_data.zip")){
    data_download("https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip")
}

if(!file.exists("UCI HAR Dataset") & file.exists("nike_data.zip")){
    unzip("nike_data.zip")
}

#load data into R
if(file.exists("UCI HAR Dataset")){

    #load measurement names
    measurement_names <- (read.table(".\\UCI HAR Dataset\\features.txt", header = FALSE))[,"V2"]

    subject_test <- as_tibble(read.table(".\\UCI HAR Dataset\\test\\subject_test.txt", header = FALSE, sep = " "))
    subject_train <- as_tibble(read.table(".\\UCI HAR Dataset\\train\\subject_train.txt", header = FALSE, sep = " "))

    X_test <- read_fwf(".\\UCI HAR Dataset\\test\\X_test.txt", 
        fwf_empty(".\\UCI HAR Dataset\\test\\X_test.txt", col_names = measurement_names))
    X_train <- read_fwf(".\\UCI HAR Dataset\\train\\X_train.txt", 
        fwf_empty(".\\UCI HAR Dataset\\train\\X_train.txt", col_names = measurement_names))

    Y_test <- as_tibble(read.table(".\\UCI HAR Dataset\\test\\Y_test.txt", header = FALSE, sep = " "))
    Y_train <- as_tibble(read.table(".\\UCI HAR Dataset\\train\\Y_train.txt", header = FALSE, sep = " "))

    names(subject_test) = "Subject"
    names(subject_train) = "Subject"
    names(Y_test) = "Activity"
    names(Y_train) = "Activity"

}else{
    print("ERROR: UCI HAR Dataset doesn't exist")
    quit(save="no")
}

#Merge datasets

full_dataset <- bind_rows(add_column(subject_test, Y_test, X_test),
                add_column(subject_train, Y_train, X_train))

#Select mean and standard deviation dataset

mean_and_std_dataset <- select(full_dataset, matches("*-mean()-*"), matches("*-std()-*"))

#Replace activity labels

full_dataset$Activity[full_dataset$Activity == "1"] <- "Walking"
full_dataset$Activity[full_dataset$Activity == "2"] <- "Walking_upstairs"
full_dataset$Activity[full_dataset$Activity == "3"] <- "Walking_downstairs"
full_dataset$Activity[full_dataset$Activity == "4"] <- "Stitting"
full_dataset$Activity[full_dataset$Activity == "5"] <- "Standing"
full_dataset$Activity[full_dataset$Activity == "6"] <- "Laying"

#Replace measurement names

renamed_measurement_names <- str_replace(measurement_names, "^t", "") %>% #Remove leading t's
    str_replace("^f", "Fourier ") %>% #replace f with Fourier
    str_replace("-","") %>% #remove first dashes
    str_replace("Mag", "Magnitute ") %>%
    str_replace("Jerk", " Jerk ") %>%
    str_replace("BodyAcc", "Body Acceleration ") %>%
    str_replace("GravityAcc", "Gravity Acceleration ") %>%
    str_replace("BodyGyro", "Body Gyro ") %>%
    str_replace("std()","Standard deviation") %>%
    str_replace("mad()","Median absolute deviation") %>%
    str_replace("sma()","Signal magnitude area") %>%
    str_replace("iqr()","Interquartile range") %>%
    str_replace("arCoeff()","Autorregresion coefficient") %>%
    str_replace("maxInds()","Max index") %>%
    str_replace("MeanFreq()","Average frequency") %>%
    str_replace("BodyBody","Body") %>% 
    str_replace("tBody","Body") %>%
    str_replace("  "," ")

renamed_measurement_names <- c("Subject", "Activity", renamed_measurement_names)

names(full_dataset) <- renamed_measurement_names

#Replace measurement names

tidy_dataset <- full_dataset[!duplicated(as.list(full_dataset))] #Removes duplicate columns
tidy_dataset <- tidy_dataset[, !duplicated(names(tidy_dataset))]

tidy_dataset <- summarize_at(group_by(tidy_dataset, Subject, Activity), #summarize data by subject and activity
                    vars(names(tidy_dataset)[3:458]), funs(mean(.,na.rm=TRUE)))

write.csv(tidy_dataset, file = "tidy_dataset.csv")