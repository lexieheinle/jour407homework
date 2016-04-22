#JOUR 407 Homework

This repository contains my homework for JOUR 407 Data Journalism class taught by Matt Waite at the University of Nebraska-Lincoln. The majority of the files involve data analysis by agate and documentation via Jupyter.

##Contents
###[DataNormalizationHomework](DataNormalizationHomework)
This folder contains a dirty data set of [leaking underground storage tanks] (http://www.deq.state.ne.us/lustsurf.nsf/pages/sssi "NDEQ lust database") from the Nebraska Department of Environmental Quality. I used [OpenRefine] (http://openrefine.org) to normalize the data before finding the top 20 owners using Agate.

###[DataSmellsHomework](DataSmellsHomework)
This folder looked at data from the University of Nebraska-Lincoln Police Department. By using Agate's group_by and count functions, inconsistent locations and buildings were revealed. Additionally, outliers in stolen and damaged amounts were found using agate-stats.

###[JoinHomework](JoinHomework)
From Nebraska school data, I calculated the percent change in free &amp; reduced lunch and enrollment from 2013 to 2015. This assignment required joining agate tables and creating custom functions to round decimals.

###[ChartHomework](ChartHomework)
Using [seaborn](https://stanford.edu/~mwaskom/software/seaborn/) a Python data visualization based on [matploblib](http://matplotlib.org), I constructed three different chart styles of the top 10 Nebraska counties for mountain lion sightings.

###[ChartSecondHomework](ChartSecondHomework)
From the political ads database, I attempted to split the events by subjects to see which ads/candidates are most likely to use certain ones. However, this quest wasn't successful due to program limitations.

###[IndependentStory](IndependentStory)
Using [general election data](http://www.sos.ne.gov/elec/prev_elec/index.html) from the Nebraska Secretary of State, I analyzed the changes in the state's political party distribution from 2000 to 2014. From my analysis, I found that if the current growth trend of the independent party continues, it would overtake the Democratic party by 2020.

To find the party's distributions, I had to write custom functions to calculate the correct percents. The percent change was calculated using agate functions. Estimating the future growth was based on the instructions in [Numbers in the Newsroom](http://store.ire.org/products/numbers-in-the-newsroom-using-math-and-statistics-in-news-second-edition-e-version) and required defining new functions.

###[CellPhoneStory](CellPhoneStory)
To gather the data for this story, I had to request records from the E911 departments in both [Nebraska](http://www.psc.nebraska.gov/ntips/ntips_e911.html) and [Iowa](http://homelandsecurity.iowa.gov/programs/e_911.html). I looked at each state's E911 fund, which is funded by surcharges on cellphones. In the article, I explored how emergency services adapted to cover cellphones and the future plans.

###[WellDatabases](WellDatabases)
Using irrigated acres data from the [National Agriculture Statistics Service](http://quickstats.nass.usda.gov) in United States Department of Agriculture and registered groundwater well data from [Nebraska Department of Natural Resources](http://quickstats.nass.usda.gov), I built an Agate custom computation to find whether a well was active during a given year. Next, I found the number of active wells for each county and also listed the number of irrigated acres. Currently, the complied information is saved in the [wells_acres_total.csv](WellDatabases/wells_acres_total.csv).

###[ClimateData](ClimateData)
I grabbed different climate-related statistics from the [High Plains Regional Climate Center](http://climod.unl.edu/) for use in an in-depth story on Nebraska climate. Those statistics include the frost season lengths, mean temperatures, and snowfall sums. I also had to build a [scrapper](ClimateData/snrScrapper.py) to grab the monthly Lincoln temperatures from the [UNL climate and data website](http://snr.unl.edu/lincolnweather/data/monthly-observed-vs-normals.asp) and how they compare to 30-year normals.

###[SpouseBusinessStory](SpouseBusinessStory)
Using the US Census' [Survey of Business Owners](http://www.census.gov/econ/sbo/getdata.html) from 2012 and 2007, I looked at how the distribution of businesses that are equally owned and operated by both spouses has changed. Several industries including utilities have significantly dropped perhaps due to the Great Recession effects.

###[StormData](StormData)
From the [National Centers for Environmental Information](https://www.ncdc.noaa.gov/stormevents/), I grabbed all events from January 1950 to 2016. To grab only Nebraska events from the plethora of files, I wrote a quick Python [program](StormData/findNebraska.py) and looked into how each storm event has increased/decreased over the years.

###[USstatesNaturalBeauty](USstatesNaturalBeauty)
From a [lovely cleaned csv](https://www.dropbox.com/s/qfv8xn4cffwqtvg/naturalamenities.csv?dl=0) that used the [USDA's Natural Amenities Index](http://www.ers.usda.gov/data-products/natural-amenities-scale.aspx), I used QGIS to join those scores to a United States map. The [final map](USstatesNaturalBeauty/natural-amenities-map.png) shows the lower scoring counties in dark brown or lighter yellow, and the higher ranking in either dark teal or a lighter one.
