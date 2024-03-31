# This is a money analysis app. Purpose is to simplify what is done per month to track my expenses 
# Input: Will be a csv file from ASB and this is done manually
# Output as of 31st Mar 2024:
#  - Pie chart of spending

# Future additions:
# - Be able to save each month so we can review it in the future 
# - Check whether it is the correct file format 

#SETUP
import os
import csv

ALLOWED_EXTENSTIONS = {".csv"}
while True:
    filename = input("Enter csv file for money analysis: ")
    extension = os.path.splitext(filename)[1]
    if extension in ALLOWED_EXTENSTIONS:
        break

# with open(filename) as f:
#     print("File is open")

#     #\Downloads\Export20240331164304.csv