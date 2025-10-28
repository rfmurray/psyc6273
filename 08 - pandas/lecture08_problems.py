# lecture08_problems.py  Lecture 8 workshop problems

# 1. Use pandas and the Keeling curve dataset provided in lecture 7
# to plot the average atmospheric CO2 concentration by month, averaging
# over all years in the dataset. You can use column 2 of the dataset,
# which gives an integer 1-12 that encodes the month of each measurement.
# 
# Check the help text for pd.read_csv to find what arguments that will
# make it read the Keeling dataset correctly.

# 2. Repeat problem 1, but now suppose that column 2 is not available.
# Instead, suppose you only have column 4, which gives the date of the
# measurement as a floating point number. The integer part of the number
# is the year (e.g., 1965), and the fractional part measures progress
# through the year (e.g., 1965.5 is halfway through 1965). Assume that each
# month lasts for 1/12 of the year.
# 
# Suggestion: convert the fractional part of the year to an integer
# that encodes the month, at which point you can use your solution to
# problem 1.
