class ToyRobot:
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None

    def place(self, x, y, facing):
        if self.is_valid_position(x, y) and self.is_valid_direction(facing):
            self.x = x
            self.y = y
            self.facing = facing

    def move(self):
        if self.facing == 'NORTH':
            if self.is_valid_position(self.x, self.y + 1):
                self.y += 1
        elif self.facing == 'SOUTH':
            if self.is_valid_position(self.x, self.y - 1):
                self.y -= 1
        elif self.facing == 'EAST':
            if self.is_valid_position(self.x + 1, self.y):
                self.x += 1
        elif self.facing == 'WEST':
            if self.is_valid_position(self.x - 1, self.y):
                self.x -= 1

    def left(self):
        if self.facing == 'NORTH':
            self.facing = 'WEST'
        elif self.facing == 'SOUTH':
            self.facing = 'EAST'
        elif self.facing == 'EAST':
            self.facing = 'NORTH'
        elif self.facing == 'WEST':
            self.facing = 'SOUTH'

    def right(self):
        if self.facing == 'NORTH':
            self.facing = 'EAST'
        elif self.facing == 'SOUTH':
            self.facing = 'WEST'
        elif self.facing == 'EAST':
            self.facing = 'SOUTH'
        elif self.facing == 'WEST':
            self.facing = 'NORTH'

    def report(self):
        if self.x is not None and self.y is not None and self.facing is not None:
            print(f"Output: {self.x},{self.y},{self.facing}")
        else:
            print("Output: Robot is not placed on the table.")

    def is_valid_position(self, x, y):
        return 0 <= x <= 4 and 0 <= y <= 4

    def is_valid_direction(self, direction):
        return direction in ['NORTH', 'SOUTH', 'EAST', 'WEST']

def main():
    robot = ToyRobot()

    while True:
        command = input("Enter a command (e.g., PLACE X,Y,F or MOVE, LEFT, RIGHT, REPORT): ").strip().upper()
        
        if command == 'EXIT':
            break
        
        if command.startswith('PLACE'):
            _, args = command.split(' ', 1)
            x, y, facing = args.split(',')
            robot.place(int(x), int(y), facing)
        elif command == 'MOVE':
            robot.move()
        elif command == 'LEFT':
            robot.left()
        elif command == 'RIGHT':
            robot.right()
        elif command == 'REPORT':
            robot.report()
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    main()
