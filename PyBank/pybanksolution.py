#!/usr/bin/env python
# coding: utf-8

# In[47]:


# step 1 importing budget_data.csv file and determine output file
import csv 
import os




upload_file = os.path.join(".", "Resources", "budget_data.csv")
upload_output = os.path.join(".","Financial_analysis.txt")

#define start values
total_months = 0
total_profits = 0
net_change_list = []
month_changes = []
greatest =["",0]
least = ["",10000000000000000]


# open file
with open (upload_file) as financial_data:
    reader = csv.reader(financial_data)
      
    #define start values
    total_months = 0
    total_profits = 0
    
    # read and skip Header 
    title_field =next(reader)
    #print(f"header: {title_field}")
    
    #profit calc work 
    first_row = next(reader)
    total_profits += int(first_row[1])
    previous_profit =int(first_row[1])
     
    
    #total answers 
    for row in reader:
        total_months += 1
        total_profits += int(row[1])
        
        
        #net changes
        net_change = int(row[1]) - previous_profit
        previous_profit = int(row[1])
        net_change_list.append(net_change)
        
        #greatest increase
        if(net_change > greatest[1]):
            greatest[0] = row [0]
            greatest[1] = net_change
        #greatest decrease
        if(net_change < least[1]):
            least[0] = row [0]
            least[1] = net_change
            
         
       
    #averaging net changes
    net_avg = sum(net_change_list) / len(net_change_list)

#print(net_change_list)
#print(net_avg) 
#print(greatest)
#print(least)
    
#Answers print out using output 

output = (
    f" Financial Status\n"
    f" Months: {total_months}\n"
    f" Total: {total_profits}\n"
    f" Average Change: {net_avg:.2f}\n"
    f" Greatest Increase in Profits: {greatest[0]} (${greatest[1]}) \n"
    f" Greatest Decrease in Profits: {least[0]} (${least[1]})\n"
)

print(output)

#output to txt file
with open(upload_output,"w") as txt_file:
    txt_file.write(output)


# In[ ]:




