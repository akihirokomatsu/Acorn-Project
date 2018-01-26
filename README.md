# Acorn-Project

Trying to find how much money Acorn would have made me last year -- 

Source: my Bank of America monthly credit card statements

Tools: python, Excel

Steps:

1) downloaded monthly Bank of America credit card statements of 2017
2) copied records of credit card transactions into .txt file called 'cc_transactions.txt'

--python portion

3) used python script (main.py) to parse records and grab only the Date and Amount
4) exported parsed records to a new .txt file called 'cc_transactions_parsed.txt'

-- Excel portion

5) opened 'cc_transactions_parsed.txt' in Excel, space delimited
6) created new columns - Purchase_Amt_Rounded, Amt_Invested, No_days_until_EOY, Compounded_Amt
    Purchase_Amt_Rounded: round each credit card transaction up
    Amt_Invested: the difference between Purchase_Amt_Rounded and the transaction amount
    No_days_until_EOY: number of days until the end of the year
    Compounded_Amt: value of Amt_Invested compounded based on SPY daily returns
7) calculated compounding returns with Acorn costs

How much Acorn invested $145.53

Value of investment EOY (without Acorn fees) $160.73

Compounding Acorn Fees $13.26

Actual Value of Investment	$147.47

Annual Return	1.33% (YUCK!)

Conclusion: Acorn's $1 monthly fee ate into my annual return. I was better off setting aside money initially and putting it in an index fund, which is less costly than Acorn's fees.

# Readme edit

After my initial findings, I wanted to improve my code to make it more usable and flexible. I also wanted use pandas Dataframe rather than Excel

Changes:
- access files via computer directory
- regular expression to detect records of date, description, and amount from files
- create pandas dataframe with columns: date, description, amount, amount rounded, etc. 
- find the avg daily return of SPY, principal investment, acorn fees, final value, annual return
- graphical visualizations of $SPY vs return from acorn
