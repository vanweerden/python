class Submarine:
    def __init__(self, h_position=0, depth=0, aim=0):
        self.h_position = h_position
        self.depth = depth
        self.aim = aim

    def forward(self, x):
        self.h_position += x

        if (self.depth + self.aim * x) >= 0:
            self.depth += self.aim * x
        else:
            self.depth = 0
            print("Submarine is at depth 0 and can't rise any farther.")

    def down(self, x):
        self.aim += x

    def up(self, x):
            self.aim -= x