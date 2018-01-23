import csv
#from django.template.defaultfilters import slugify


rawfilename = 'cc_transactions.txt'
processedfilename = 'cc_transactions_parsed.txt'

#results = []

with open(processedfilename, 'w') as myfile:
  with open(rawfilename) as f:
    for line in f:
      r_split_lines = line.rsplit(' ', 1)[1]
      date_split = line.split(' ', 1)[0]
      new_line = date_split + ' ' + r_split_lines
    
      #mid_split = line.split() --try to slugify the middle portion 
      #line = date_split + slugify(line[1:-1]) + r_split_lines
      #print (slugify(line[12:-7]))
      
      myfile.write(new_line)
