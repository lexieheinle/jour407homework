#JOUR 407 Homework

This repository contains my homework for JOUR 407 Data Journalism class taught by Matt Waite at the University of Nebraska-Lincoln. The majority of the files involve data analysis by agate and documentation via Jupyter.

##Contents:
###[DataNormalizationHomework](DataNormalizationHomework)
This folder contains a dirty data set of [leaking underground storage tanks] (http://www.deq.state.ne.us/lustsurf.nsf/pages/sssi "NDEQ lust database") from the Nebraska Department of Environmental Quality. I used [OpenRefine] [http://openrefine.org] to normalize the data before finding the top 20 owners using Agate.

###[DataSmellsHomework](DataSmellsHomework)
This folder looked at data from the University of Nebraska-Lincoln Police Department. By using Agate's group_by and count functions, inconsistent locations and buildings were revealed. Additionally, outliers in stolen and damaged amounts were found using agate-stats.

###[JoinHomework](JoinHomework)
From Nebraska school data, I calculated the percent change in free &amp; reduced lunch and enrollment from 2013 to 2015. This assignment required joining agate tables and creating custom functions to round decimals.

###[ChartHomework](ChartHomework)
Using [seaborn] (https://stanford.edu/~mwaskom/software/seaborn/) a Python data visualization based on [matploblib](http://matplotlib.org), I constructed three different chart styles of the top 10 Nebraska counties for mountain lion sightings.

###[IndependentStory](IndependentStory)
Using [general election data](http://www.sos.ne.gov/elec/prev_elec/index.html) from the Nebraska Secretary of State, I analyzed the changes in the state's political party distribution from 2000 to 2014. From my analysis, I found that if the current growth trend of the independent party continues, it would overtake the Democratic party by 2020.

To find the party's distributions, I had to write custom functions to calculate the correct percents. The percent change was calculated using agate functions. Estimating the future growth was based on the instructions in [Numbers in the Newsroom](http://store.ire.org/products/numbers-in-the-newsroom-using-math-and-statistics-in-news-second-edition-e-version) and required defining new functions.

###[CellPhoneStory](CellPhoneStory)