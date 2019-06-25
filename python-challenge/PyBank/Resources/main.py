#Import modules os and csv
 
import os 
import csv

budget_data= os.path.join("budget_data.csv")
analysis = os.path.join("analysis.txt")
print(budget_data)

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the csv file 
with open(budget_data, newline = "") as csvfile:
  csvreader = csv.reader(csvfile, delimiter = ",")
  print(csvreader)

#Reading the header row
  csv_header = next(csvreader)
  print(csv_header)

#Reading the first row (so that we track the changes properly)
  first_row = next(csvreader)
  print(first_row)
  total_months +=1
  total_pl += int(first_row[1])
  value = int(first_row[1])  

 
#Process through each row of data after the header/first row
  for row in csvreader:
        #Going to keep track of the dates
    dates.append(row[0])

    #I will calculate the change, then add it to list of changes
    change = int(row[1])-value
    profits.append(change)
    value = int(row[1])

    #The total numbers of months
    total_months += 1

    #Have the total net amount of profit/losses over the entire period.
    total_pl = total_pl + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

#Average change in profit/losses between months over entire peroid
avg_change = sum(profits)/len(profits)

#Displaying information
print("Financial Analysis")
print("-----------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change, 2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits:{worst_date} (${str(greatest_decrease)})")

output = (
  f"\nFinancial Analysis\n"
  f"---------\n"
  # f"\str(f"Total Months: {str(total_months)}"
  # f"\str(f"Total: ${str(total_pl)}"
)
print(output)

with open(analysis,"w") as txt_file:
  txt_file.write(output)




# line5 = str(f"Average Change: ${str(round(avg_change,2))}")
# line6 = str(f"Greastest Increase in Profits:{greatest_date} (${str(greatest_increase)})")
# line7 = str(f"Greastest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
# output.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(line1,line2,line3,line4,line5,line6,line7))

#Exporing to .txt file 
# output = open("C:/TempDataDir.txt")
# line1 = "Financial Analysis"
# line2 = "---------"
# line3 = str(f"Total Months: {str(total_months)}")
# line4 = str(f"Total: ${str(total_pl)}")
# line5 = str(f"Average Change: ${str(round(avg_change,2))}")
# line6 = str(f"Greastest Increase in Profits:{greatest_date} (${str(greatest_increase)})")
# line7 = str(f"Greastest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
# output.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(line1,line2,line3,line4,line5,line6,line7))




   







