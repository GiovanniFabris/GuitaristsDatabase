"""
This is the main file where we created
the interaction between the user and the
database of guitarists and bands.
We used the argparse module to configure
all the positional and optional arguments.

Depending on the arguments given,
the program leads the user to a series of steps
to either check the presence of a band or guitarist
inside the database and/or add them to it.

There is also the possibility to check out
the database on the terminal itself.
"""
from adder import add_element
from checker import Check
import argparse
import pandas as pd

db = pd.DataFrame(pd.read_csv('players_bands.csv'))
parser = argparse.ArgumentParser(description='this program will' +
                                             ' check if the name you put is' +
                                             'inside our database of ' +
                                             'known guitarists or ' +
                                             'their bands.' +
                                             'If the names have' +
                                             'more than one space,' +
                                             'please wrap them ' +
                                             'around quotes ("")')
group = parser.add_mutually_exclusive_group()
parser.add_argument("name", help="input the name of a known guitarist or band")
group.add_argument("-a", "--add", action="store_true",
                   help="add a new guitarist or band")
group.add_argument("-d", "--database", action="store_true",
                   help="add a new guitarist or band")
args = parser.parse_args()
answer = args.name

check = Check()

if args.database:
    print("Now you can see by yourself if " +
          answer + " is present in our database!")
    db.drop("Unnamed: 0", axis=1, inplace=True)
    print(db)
else:
    if args.add:
        add_element(answer)
    elif check.check_band(answer):
        print("The guitar hero of", db["Bands"]
              .loc[db["Bands"].str.lower() == answer.lower()].values[0],
              "is", db["Players"].loc[db["Bands"].str.lower() ==
              answer.lower()].values[0])
    elif check.check_guitarist(answer):
        print(db["Players"].loc[db["Players"].str.lower() == answer.lower()]
              .values[0], "is the guitar hero of",
              db["Bands"].loc[db["Players"].str.lower() ==
              answer.lower()].values[0])
    else:
        response = input(answer + " is not present in our database." +
                         "Would you like to add him? (y or n) -> ")
        if response == "y":
            print(answer)
            add_element(answer)
        else:
            print("Thank you anyway")
