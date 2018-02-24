# Acorn-Project

Simulating how much money Acorns would have made for me in 2017 --

Source: my Bank of America monthly credit card statements

Tool: python

Steps:

1) downloaded monthly Bank of America credit card statements of 2017
2) copied records of credit card transactions into .txt file called 'cc_transactions.txt'
3) used python script (main.py) to parse records and grab data
4) created new columns - Purchase_Amt_Rounded, Amt_Invested, No_days_until_EOY, Compounded_Amt
    Purchase_Amt_Rounded: round each credit card transaction up
    Amt_Invested: the difference between Purchase_Amt_Rounded and the transaction amount
    No_days_until_EOY: number of days until the end of the year
    Compounded_Amt: value of Amt_Invested compounded based on SPY daily returns
5) calculated compounding returns with Acorn costs

How much Acorn invested $150.58

Value of investment EOY (without Acorn fees) $167.98307654

Compounding Acorn Fees $13.1563874787

Actual Value of Investment	$154.826689062

Annual Return	2.8202211858% (YUCK!)

Conclusion: Acorn's $1 monthly fee ate into my annual return. I was better off setting aside money initially and putting it in an index fund, which is less costly than Acorn's fees.
