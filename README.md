# Python Challnge
Northwestern University Data Science Boot Camp

[Homework 3](https://nu.bootcampcontent.com/NU-Coding-Bootcamp/nu-chi-data-pt-08-2020-u-c/tree/master/02-Homework/03-Python/Instructions)

## PyBank
This script will take a specific set of fincial records (organized by Dates and Profit/Losses) and perform a brief analysis to provide the following information:

- Total of months of data
- The net amount of profits or losses over the entire period
- The average of the monthly profits/losses
- The greatest increase over that time period
- The greatest decrease over that time period

In order to accomplish this goal, I created a script that will read the CSV file and store all the dates and corresponding profits in two lists. Then, it will iterate through the profit list to find the greatest change from one month to the next. After finding the minimum and maximum of each list, it will print the information above and write the same text to a txt. file. 

![PyBank Solution](https://github.com/alextorres12/python-challenge/blob/master/Images/PyBank.png)

## PyPoll
Give a list of election votes, this script will anlalyze all of the votes to determine the winner of the election. Additionally it will provide the following information

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes won by each candidate
- The total number of votes won by each candidate

This script works by reading in a CSV of raw vote data. It will iterate through each row of the data and add all unique candidate names as keys in a dictionary then sum votes as the values associated with each key. After calculating the above information, it will print the anlaysis and export a .txt file with the same information. 

![PyPoll Solution](https://github.com/alextorres12/python-challenge/blob/master/Images/PyPoll.png)




