import csv
import re
import pandas as pd
import os
import datetime as dt

# regular expression that will scan each credit card statement and find exactly what I want in the statements
p = re.compile('^(\s+)(\d{2}/\d{2})(\s+)(\d{2}/\d{2})(\s+)(.{40})(\s+)(\d+)(\s+)(\d+)(\s+)([0-9.]+)$')

my_Files = ['eStmt_2017-01-22.txt', 'eStmt_2017-02-22.txt','eStmt_2017-03-22.txt', 'eStmt_2017-04-22.txt',
            'eStmt_2017-05-22.txt', 'eStmt_2017-06-22.txt', 'eStmt_2017-07-22.txt', 'eStmt_2017-08-22.txt', 
            'eStmt_2017-09-22.txt', 'eStmt_2017-10-22.txt', 'eStmt_2017-11-22.txt', 'eStmt_2017-12-22.txt' ]


# Change working directory
os.chdir("/Users/akihirokomatsu/Documents/BoA_Statements")
#initialize list
results = []

for file in my_Files:
    with open(file, 'r') as f:
        for line in f:
            m = p.match(line)
            if m:
                new_line = [m.group(2), m.group(6), m.group(12)]
                results.append(new_line)
                print (results)

#set up dataframe
#list_of_labels = ['Transaction_Date', 'Description', 'Amount']
#df = pd.DataFrame(data= results,columns= list_of_labels)

#print (df)
            
            
