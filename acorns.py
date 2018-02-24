import csv
import re
import pandas as pd
import os
import datetime as dt
import io
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# regular expressions that parses data in credit card statement
p = re.compile('^(\s*)(\d{2}/\d{2})(\s+)(\d{2}/\d{2})(\s+)(.{40})(\s+)(\d+)(\s+)(\d+)(\s+)([0-9.]+)$')

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
            if m1:
                # group(2)= transaction date; group(6)= transaction description; group(12)= transaction amount 
                new_line1 = [m1.group(2), m1.group(6), m1.group(12)]
                results.append(new_line1)
        
# set up dataframe
headers = ['Trans_Dt', 'Description', 'Amt']
df = pd.DataFrame(results)
df.columns = headers

df['Trans_Dt'] = df['Trans_Dt'].astype(str) + '/2017'
df['Trans_Dt'] = pd.to_datetime(df['Trans_Dt'], format='%m/%d/%Y')

# drop records that are payments of credit card bills, drop records that are actually 2016 transactions
df = df[df.Description != 'PAYMENT - THANK YOU                     ']
df = df[df.Trans_Dt != '12/22/2017']
df = df[df.Trans_Dt != '12/31/2017']
df = df.reset_index(drop=True)
df = df.sort_values(by='Trans_Dt')
df.Amt = df.Amt.astype(float)

# create new column, which is 'Amount' rounded up
df['Amt_Rounded'] = df.Amt+0.49

#diff between amt and amount rounded is what Acorns is investing
df.Amt_Rounded = round(df.Amt_Rounded)
df['Amt_Invested'] = df.Amt_Rounded - df.Amt

# add column with number of compounding days
last_day = pd.to_datetime('12/31/2017', format='%m/%d/%Y')
df['Compounding_Days'] = (last_day-df['Trans_Dt']).dt.days

# calc avg daily returns of SPY
SPY_2017 = 1.2169
daily = (SPY_2017**(1/365))-1
principal_investment = sum(df['Amt_Invested'])

# create column called Compounded_Amt
df['Compounded_Amt'] = df['Amt_Invested']*(1+daily)**df['Compounding_Days']
sum_CompoundedAmt = sum(df['Compounded_Amt'])
df['cumSumCompoundedAmt'] = df['Compounded_Amt'].cumsum()

# compute future value of acorns fees
acorn_dates = pd.to_datetime(['01/31/2017', '02/28/2017', '03/31/2017', '04/30/2017','05/31/2017','06/30/2017',
               '07/31/2017','08/31/2017','09/30/2017','10/31/2017', '11/30/2017', '12/31/2017'], format='%m/%d/%Y')
monthlycharge = [1.00]*12
acorn_df = pd.DataFrame(data=acorn_dates, columns=['ChargeDate'])
acorn_df['Fees'] = monthlycharge
acorn_df['CompoundingDays'] = (last_day-acorn_df['ChargeDate']).dt.days
acorn_df['FVFees'] = acorn_df['Fees']*(1+daily)**acorn_df['CompoundingDays']

AcornTotalCost = sum(acorn_df['FVFees'])

# Calculate and print key measures of Acorns investment
print ('average daily return of SPY = ' + str(daily*100) + '%')
print ('principal investment in 2017 = $' + str(principal_investment))
print ('value of my investment before fees = $' + str(sum_CompoundedAmt))
print ('fees charged = $' + str(AcornTotalCost))
FinalValue = sum_CompoundedAmt - AcornTotalCost
print ('final value of investment in 2017 = $' + str(FinalValue))
ValueAdded = FinalValue-principal_investment
print ('value added in 2017 = $' + str(ValueAdded))
AnnualRet = 100*ValueAdded/principal_investment
print ('annnual return = ' + str(AnnualRet) + '%')


""" practice plotting data """
plt.plot(365 - df['Compounding_Days'], df['cumSumCompoundedAmt'])
plt.xlabel('Day #')
plt.ylabel('Dollar Value of Investment')
plt.show()

_ = sns.swarmplot(x='Trans_Dt', y='Amt_Invested', data=df)
_ = plt.xlabel('Transaction Date')
_ = plt.ylabel('$ Amount Invested')
plt.show()
