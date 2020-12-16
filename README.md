# Implementation of a Database of Guitar Heroes

GuitaristsDatabase is a projects that takes users' inputs from the a machine terminal, checks whether or not 
they are Guitarists or Bands inside of an internal csv database and, if needed, it can let the user add them directly 
inside the database.

## Installation

Use the command `git clone https://github.com/GiovanniFabris/GuitaristsDatabase/tree/main` in the command prompt
of your PC in order to automatically download the whole folder containing the modules.
Git should have been previously installed on the machine.
In alternative, just download manually the package from Github.

## Usage

The aim of the project is to create a database containing all of the most famous guitarists associated with their respective bands.  
Once the name of a guitarist (e.g. Brian May) has been entered as input, the program controls if the name of the guitarist or of the band is already present in the dataset. 
If it is not, the program will kindly ask you if you want to add the couple (guitarist + band).

On the other hand, if the name is already present (input ex. `"Brian May"`), the `get_band` function will return the name of the artist's respective band. (Queen in this case).
Of course, it also works the other way around(entering the band name, it will return the guitarist's name of that band). 

The functions `check_guitarist`, `check_band`and `adder` are all stored in their respective modules.
The Argparse calls them from the `main.py` module.

If wanting the execute the program, the command should be written as follows:

```bash
python main.py "name"
```
Whereas "name" should be either the name of a band or the name of a guitarist. 
For example:

```bash
python main.py "Led Zeppelin"
```
In this case, since the band is in the archive, the output will be:

```bash
The guitar hero of Led Zeppelin is Jimmy Page
```

Otherwise, if we input the name of the guitarist of this band:

```bash
Jimmy Page is the guitar hero of Led Zeppelin
```

To do so, we preferred storing the guitarists' and band's names into a csv file in order to keep it neat and tidy. 

To increase the speed of interaction, the user can access the shortcut `-a` thanks to `argparse`.
This command allows you to skip a step and add a new component or band name directly to the database by simply writing the -a keyword next to the new name to add.

```bash
python main.py "John Wick" -a
```
The program will then ask the user to specify whether the name entered concerns a band or the guitarist. 
When you reach this point, to add a guitarist the input command is `-g`, for a band `-b`.

An another useful optional argument is `-d`.
This can be used if the user wants to check directly the database and print it in the command prompt.
Since the `"name"` argument is positional, the command should be written as follows:

```bash
python main.py "Led Zeppelin" -d
```
In this case, the output will be:

```bash
Now you can see by yourself if Led Zeppelin is present in our database!
            Players                     Bands
0      Eric Clapton                     Cream
1        Jimmy Page              Led Zeppelin
2    Keith Richards            Rolling Stones
3   Eddie Van Halen                 Van Halen
4     David Gilmour                Pink Floyd
5       Angus Young                     AD/DC
6         Brian May                     Queen
7     Johnny Ramone                   Ramones
8       Tom Morello  Rage Against the Machine
9             Slash              Guns'n Roses
10         Jim Root                  Slipknot
11      Kirk Hammet                 Metallica
```
The last optional argument is `-h`, that gives the user some help about the functioning and the rules of the code.
The output in this case will be:

```bash
usage: main.py [-h] [-a | -d] name

this program will check if the name you put isinside our database of known guitarists or their bands.If the names
havemore than one space,please wrap them around quotes ("")

positional arguments:
  name            input the name of a known guitarist or band

optional arguments:
  -h, --help      show this help message and exit
  -a, --add       add a new guitarist or band
  -d, --database  add a new guitarist or band
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)












