import csv
from list_of_guitarists import list_of_guitarists

def database(dictionary):
    """
    the following function takes the elements present
    in the dictionary and places them into a csv file
    named guitarists.csv that we will use as our database.
    We will be able to add new bands and guitarists then.
    """
    a_file = open("guitarists.csv","w")
    writer = csv.writer(a_file)
    for key, value in dictionary.items():
        writer.writerow([key,value])
    a_file.close()

database(list_of_guitarists)
