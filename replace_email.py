import sys, re, csv

#function to convert to string
def data_to_string(filename):
  data_list = []
  data_string = ''
#open file and populate the empty list with rows
  with open(filename) as csvfile:
    data_list = list(csv.reader(csvfile))
#convert the list into string
  for row in data_list:
     data_string += ','.join(row) + '\n'
  return data_string

#function to convert to list and create new file with changed email
def change_email():
  old_data_string = data_to_string(filename)
#change required domains with regex & convert string to list
  data_string = re.sub(r'' + old_domain + '', r'' + new_domain + '', old_data_string)
  data_list = data_string.split('\n')
#create new file and write csv rows
  with open('updated_emails.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for item in data_list:
      if item != '':
        csvwriter.writerow(item.split(','))

#handle argument error
if __name__ == '__main__': 
 #set argument parameters & run
  try:
    filename = sys.argv[1]
    old_domain = sys.argv[2]
    new_domain = sys.argv[3]
    change_email()
  except IndexError:
    print("Missing parameters")
