
class SubmarineCommands:
    def __init__(self, submarine):
        self.commands = []
        self.args = []
        self.get_commands()
        self.sub = submarine

    def get_commands(self):
        with open('input.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            command, arg = line.split(' ')
            self.commands.append(command)
            self.args.append(arg)

    def execute(self):
        for command, arg in zip(self.commands, self.args):
            function_string = f'self.sub.{command}({arg})'
            eval(function_string)