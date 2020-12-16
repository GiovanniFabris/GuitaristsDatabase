## Implementation of a Database of Guitar Heroes

This is the README file for the Pillotada Project of Software project development

Let's go! 

The aim of the project is to create a database containing all of the most famous guitarists associated with their respective bands.  
Once the name of a guitarist (e.g. Brian May) has been entered as input, the program controls if the name of the guitarist or of the band is already present in the dataset. 
if it is not, the program will kindly ask you if you wanna add the couple (guitarist + band).

On the other hand, if the name is already present (input ex. "Brian May"), the "get_band" function will return the name of the character's respective band. (Queen in this case).
Of course, it also works the other way around. (entering the band name, it will return the guitarist's name of that band) 

To increase the speed of interaction, the user can access the shortcut -a.
This command allows you to skip a step and add a new component or band name directly to the database by simply writing the -a keyword next to the new name to add.

ex. --> John -a .

The program will then ask the user to specify whether the name entered concerns a band or the guitarist. 
When you reach this point, to add a guitarist the input command is -g, for a band -b.

The functions `check_guitarist`, `check_band`and `adder` are all stored in their respective modules.
The Argparse calls them from the `main.py` module.

If wanting the execute the program, the command should be written as follows:
```bash
python main.py "name"
```
Whereas "name" should be either the name of a band or the name of a guitarist. 
For example:
`python main.py "Led Zeppelin"`
In this case, since the band is in the archive, the output will be:
`The guitar hero of Led Zeppelin is Jimmy Page`
Otherwise, if we input the name of the guitarist of this band:
`Jimmy Page is the guitar hero of Led Zeppelin`

To do so, we preferred storing the guitarists' and band's names into a csv file in order to keep it neat and tidy. 



