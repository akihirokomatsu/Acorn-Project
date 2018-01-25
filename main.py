import csv
import re
import pandas as pd
import os
import datetime as dt
from dateutil import parser
import math
import io


# regular expressiona that matches the exact patterns in each bank statement
p = re.compile('^(\s+)(\d{2}/\d{2})(\s+)(\d{2}/\d{2})(\s+)(.{40})(\s+)(\d+)(\s+)(\d+)(\s+)([0-9.]+)$')
q = re.compile('^(\d{2}/\d{2})(\s+)(\d{2}/\d{2})(\s+)(.{40})(\s+)(\d+)(\s+)(\d+)(\s+)([0-9.]+)$')


my_Files = ['eStmt_2017-01-22.txt', 'eStmt_2017-02-22.txt','eStmt_2017-03-22.txt', 'eStmt_2017-04-22.txt',
            'eStmt_2017-05-22.txt', 'eStmt_2017-06-22.txt', 'eStmt_2017-07-22.txt', 'eStmt_2017-08-22.txt', 
            'eStmt_2017-09-22.txt', 'eStmt_2017-10-22.txt', 'eStmt_2017-11-22.txt', 'eStmt_2017-12-22.txt' ]

# Change working directory
os.chdir("/Users/akihirokomatsu/Documents/BoA_Statements")
# initialize list
results = []

for file in my_Files:
    with io.open(file, 'r', encoding='latin-1') as f:
        for line in f:
            m1 = p.match(line)
            m2 = q.match(line)
            if m1:
                # group(2)= transaction date; group(6)= transaction description; group(12)= transaction amount 
                new_line1 = [m1.group(2), m1.group(6), m1.group(12)]
                results.append(new_line1)
            elif m2:
                # group(1)= transaction date; group(5)= transaction description; group(11)= transaction amount
                new_line2 = [m2.group(1), m2.group(5), m2.group(11)]
                results.append(new_line2)
            
            
# set up dataframe
headers = ['Trans_Dt', 'Descr', 'Amt']
df = pd.DataFrame(results)
df.columns = headers

df.Amt = df.Amt.astype(float)
# create new column, which is 'Amount' rounded up
df['Amt_Rounded'] = df.Amt+0.49
df.Amt_Rounded = round(df.Amt_Rounded)
# create new column, the difference between Amount and Amount_Rounded 
df['Amt_Invested'] = df.Amt_Rounded - df.Amt


#df['Trans_Dt'] = parser.parse(df['Trans_Dt'])
df.Amt = df.Amt.astype(float)
