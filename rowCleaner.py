import csv

my_file_name = "/Users/emilymcgivern/Dataset/uk-accidents-10-years-history-with-many-variables copy/Accidents0514.csv"
cleaned_file_name = "/Users/emilymcgivern/Dataset/uk-accidents-10-years-history-with-many-variables copy/accident_output.csv"
ONE_COLUMN = 1
remove_words = ['INAC', 'EIM']

with open(my_file_name, 'r', newline='') as infile, \
     open(cleaned_file_name, 'w',newline='') as outfile:
    writer = csv.writer(outfile)
    for row in csv.reader(infile, delimiter='|'):
        column = row[ONE_COLUMN]
        if not any(remove_word in column for remove_word in remove_words):
            writer.writerow(row)