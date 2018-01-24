import csv
# from django.template.defaultfilters import slugify

# copied raw data from statements and created a .txt file
rawfilename = 'cc_transactions.txt'

# created blank .txt file to be written in with code below
processedfilename = 'cc_transactions_parsed.txt'

# open blank .txt file
with open(processedfilename, 'w') as myfile:
  # open file with raw data
  with open(rawfilename) as f:
    #iterate over every line in the file
    for line in f:
      # grab the date column which is found between the first character to the first space
      # transaction  column is in last space to the end of line
      date_split = line.split(' ', 1)[0]
      r_split_lines = line.rsplit(' ', 1)[1]
      
      # create a new record line with splits
      new_line = date_split + ' ' + r_split_lines
    
      #mid_split = line.split() --try to 'slugify' the middle portion 
      #line = date_split + slugify(line[1:-1]) + r_split_lines
      #print (slugify(line[12:-7]))
      
      # write new line into the blank .txt file
      myfile.write(new_line)
