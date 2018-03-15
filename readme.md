# Code Louisville Python for Data Project

##TL;DR

Running `main.py` will process files in the `data` subdirectory and store them in various tables in a mySQL database.
It will then pull information from the database about how long it took horses to complete a [________] race
and what the temperature was for each of those races. It will then generate a colorful plot of the final times against 
the temperature of the race along with a black line showing the mean race time for each of the temperatures.
A few outliers and bonkers-looking values (such as final race times of 0 seconds and temperatures about 130 degrees) are taken out of the data. 

## Setup requirements.

To run `main.py` and its related scripts, your enviroment must have the following packages installed and available (most current versions should work fine):
* PyMySQL
* numpy
* pandas
* python-dateutil

In addition, the database functions expect to find a mySQL server listening on localhost.
It will need to be configured with a user whose username is `codelou` and whose password is `ABCabc123!`
If needed, a different username and password can be used by editing both of the following:
* `DbHandler.__init__()` in `db_functions.py`: `username` and `password` arguments
* `QueryDb.__init__()` in `aggregation_functions.py`: `username` and `password` arguments

The user `codelou` will need full permissions on horse-related databases along the lines of 
`GRANT ALL PRIVILEGES ON horses%.* TO 'codelou'@'localhost'`.

## The Problem

There isn't really a problem that's being solved here--this project is really just a step along the way in preparing 
the race data for use in some machine learning applications with the hopeful hope that a model can be built to predict 
the outcomes of individual horse races. As described in more detail below, the data is pretty wide 
and needed a lot of TLC to be made suitable for use.

... but for purposes of this project, I was curious about whether there is any correlation between the temperature 
during a race and the final time of the race. My hypothesis was that races run when it is very hot would be relatively
slower than races run at more pleasant temperatures. This made intuitive sense to me that it would be harder to do
a vigorous activity like running when it's hot than when it's cool. 

[______________ STUFF ABOUT THE OUTCOME ______]


## The Data

The data used in this project are from [Brisnet](http://www.brisnet.com), an online horse-handicapping resource site.
Because the data is not made available freely, [___________________]. 

There are two main formats of data that can be processed by this scipt. The first are general race results, 
which provide information regarding races that have been run, including race conditions, distance, etc., 
the horses that ran, how quickly each horse completed the race, and other details about the race. It provides very granular
data on a number of aspects of the race. The second main format of data is known as past performance information.
This information is made available before a particular race is run and is what horse handicappers scour when trying to 
predict what horses will finish first in that race. It provides some general information about the race that is going 
to be run, but its primary purpose is to provide information about how each horse has run in previous appearances.
So for each horse that is going to be in the race, the past performances data will tell us about the last 10 races 
that horse has run and how that horse did in the race. This allows us to get a general sense of how quickly the horse
ran and how tough the competition was. The downside is that the detail provided about past races isn't as rich as what
we get from the results data.

The race results data is composed of 283 columns, which is spread over 6 files. The past performance data is composed of
1,435 columns, all of which is contained in a single file. Because each file has a different columns structure 
and presents unique challenges, processing is specific to the type of file. 

The detailed file structure for the race results can be found [here](http://www.brisnet.com/library/newchart2.txt), 
and detail for the past performance data is [here](http://www.brisnet.com/cgi-bin/static.cgi?page=drfsff). 
All the raw source files are in csv format.

## Overview of program logic

The big-picture program flow is handled by main, and specific functions and routines are contained in other files
solely for ease of reading and editing. 

### `main()
By default, `main` will process all files contained in the `data` subdirectory below `main.py`. 
It can also process individual files when used interactively.

`main()` first spins up a `TableHandler` object for each of the seven file formats (six for race results and one 
for past performances). Each handler is seeded with a dictionary containing information about the file format's 
data columns and how they should be mapped into SQL tables. It also contains methods for pushing data from the files into
the appropriate SQL tables. All interaction with the SQL database at this stage is handled by an instance of `DbHandler`
which takes care of communication between the program and the database and is responsible for generating
the SQL query strings based on information passed to it by `TableHandler`.   


  