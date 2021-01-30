# Codebook for the getting and cleaning data peer review

## Created by Morgan Schneider Jan 30th 2021

## Features

### Original
The features selected for this database come from the accelerometer and gyroscope 3-axial raw signals tAcc-XYZ and tGyro-XYZ. These time domain signals (prefix 't' to denote time) were captured at a constant rate of 50 Hz. Then they were filtered using a median filter and a 3rd order low pass Butterworth filter with a corner frequency of 20 Hz to remove noise. Similarly, the acceleration signal was then separated into body and gravity acceleration signals (tBodyAcc-XYZ and tGravityAcc-XYZ) using another low pass Butterworth filter with a corner frequency of 0.3 Hz. 

Subsequently, the body linear acceleration and angular velocity were derived in time to obtain Jerk signals (tBodyAccJerk-XYZ and tBodyGyroJerk-XYZ). Also the magnitude of these three-dimensional signals were calculated using the Euclidean norm (tBodyAccMag, tGravityAccMag, tBodyAccJerkMag, tBodyGyroMag, tBodyGyroJerkMag). 

Finally a Fast Fourier Transform (FFT) was applied to some of these signals producing fBodyAcc-XYZ, fBodyAccJerk-XYZ, fBodyGyro-XYZ, fBodyAccJerkMag, fBodyGyroMag, fBodyGyroJerkMag. (Note the 'f' to indicate frequency domain signals). 

These signals were used to estimate variables of the feature vector for each pattern:  
'-XYZ' is used to denote 3-axial signals in the X, Y and Z directions.

tBodyAcc-XYZ
tGravityAcc-XYZ
tBodyAccJerk-XYZ
tBodyGyro-XYZ
tBodyGyroJerk-XYZ
tBodyAccMag
tGravityAccMag
tBodyAccJerkMag
tBodyGyroMag
tBodyGyroJerkMag
fBodyAcc-XYZ
fBodyAccJerk-XYZ
fBodyGyro-XYZ
fBodyAccMag
fBodyAccJerkMag
fBodyGyroMag
fBodyGyroJerkMag

The set of variables that were estimated from these signals are: 

mean(): Mean value
std(): Standard deviation
mad(): Median absolute deviation 
max(): Largest value in array
min(): Smallest value in array
sma(): Signal magnitude area
energy(): Energy measure. Sum of the squares divided by the number of values. 
iqr(): Interquartile range 
entropy(): Signal entropy
arCoeff(): Autorregresion coefficients with Burg order equal to 4
correlation(): correlation coefficient between two signals
maxInds(): index of the frequency component with largest magnitude
meanFreq(): Weighted average of the frequency components to obtain a mean frequency
skewness(): skewness of the frequency domain signal 
kurtosis(): kurtosis of the frequency domain signal 
bandsEnergy(): Energy of a frequency interval within the 64 bins of the FFT of each window.
angle(): Angle between to vectors.

Additional vectors obtained by averaging the signals in a signal window sample. These are used on the angle() variable:

gravityMean
tBodyAccMean
tBodyAccJerkMean
tBodyGyroMean
tBodyGyroJerkMean

The complete list of variables of each feature vector is available in 'features.txt'

### Updates

To make the variable names more readable, the following processing was applied to the variable names:

    str_replace(measurement_names, "^t", "") %>%
    str_replace("^f", "Fourier ") %>%
    str_replace("-","") %>%
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

This code first removes the leading t's from the variable names, replaces any initial "f" values with "Fourier", and then removes the leading dashes. From here, "Mag" was replaced with "Magnitute ", "Jerk" was replaced with  " Jerk ", "BodyAcc" was replaced with "Body Acceleration ", "GravityAcc" was replaced with "Gravity Acceleration ", "BodyGyro" was replaced with "Body Gyro " to make the names more clear. After this step, calculations with unclear names were expanded. "std()" was replaced with "Standard deviation", "mad()" was replaced with "Median absolute deviation", "sma()" was replaced with "Signal magnitude area", "iqr()" was replaced with "Interquartile range", "arCoeff()" was replaced with "Autorregresion coefficient", "maxInds()" was replaced with "Max index", and "MeanFreq()" was replaced with "Max index". Lastly, some clean-up work was performed to remove some extraneous outputs from the previous replacements. A complete list of the replacements is listed in the text file variables.txt.

### Processing

The code first checks to make sure that the dataset is present and unzipped. If it is not present, it downloads the file. If the file is present but not unzipped, it then unzips the file.

Once the program confirms the dataset is present, it then reads the data into several variables as follows:

    measurement_names   =   The names of the variables from the features.txt file
    subject_test        =   The subject test variable numbers from the subject_test.txt file
    subject_train       =   The subject train variable numbers from the subject_train.txt file
    X_test              =   The dataset from the test dataset from the X_test.txt file
    X_train             =   The dataset from the train dataset from the X_train.txt file
    Y_test              =   The activity list from the test dataset from the Y_test.txt file
    Y_train             =   The activity list from the train dataset from the Y_train.txt file

Once these files are read in, the header names for the subject and activity datasets are renamed respectively and the data is merged using a bind_rows command on the combined datasets, creating the variable full_dataset tibble.

The program continues to extract the mean and standard deviation columns into the mean_and_std_dataset tibble.

Afterwards, the program continues to replace the activity names with their respective values from the activitiy_labels.txt file.

Once the above is complete, the program then goes through the names of the columns and replaces each with a more descriptive name and stores the names in the renamed_measurement_names vector. The program then renames the columns in the full_dataset tibble with the values in the renamed_measurement_names vector. 

Finally, the program removes the duplicate columns from the full data set and stores the output as the first iteration of the tidy_dataset tibble. The tidy_dataset tibble is then summarized by taking the mean of each variable first by each subject and then the activity. The results are then exported as a csv file.