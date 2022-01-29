import submarine
import submarinecommands

##############################################
### ADVENT OF CODE: DAY 2
##############################################

Submarine = submarine.Submarine
SubmarineCommands = submarinecommands.SubmarineCommands

sub = Submarine()
sub_commands = SubmarineCommands(sub)
sub_commands.execute()

result = sub.depth * sub.h_position 
print(result)

##############################################
### NOTES
##############################################
"""
Global variables: variables in a scope (i.e. a function) don't refer to the outside scope. The following causes an error because h_position hasn't been initialized inside the method scope yet:

    h_position = 0
    depth = 0

    def forward(x):
        h_position += x

This is a mistaken use of an instance variable.

    class Submarine:
        depth = 0

This is a class variable that is available to ALL instances of this class. The correct way to implement instance variables is in the __init__ function:

    def __init__(self, h_position, depth):
        self.h_position = h_position
        self.depth = depth
"""