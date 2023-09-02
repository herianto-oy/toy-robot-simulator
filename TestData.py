# Test data 1: Basic movement
test_data_1 = [
    "PLACE 0,0,NORTH",
    "MOVE",
    "REPORT",  # Expected output: "Output: 0,1,NORTH"
    "LEFT",
    "MOVE",
    "REPORT",  # Expected output: "Output: 0,0,WEST"
    "RIGHT",
    "MOVE",
    "REPORT",  # Expected output: "Output: 1,0,NORTH"
]

# Test data 2: Turning and reporting
test_data_2 = [
    "PLACE 2,2,EAST",
    "RIGHT",
    "REPORT",  # Expected output: "Output: 2,2,SOUTH"
    "RIGHT",
    "REPORT",  # Expected output: "Output: 2,2,WEST"
    "LEFT",
    "REPORT",  # Expected output: "Output: 2,2,SOUTH"
]

# Test data 3: Prevent falling off the table
test_data_3 = [
    "PLACE 0,0,SOUTH",
    "MOVE",
    "MOVE",
    "MOVE",
    "REPORT",  # Expected output: "Output: 0,0,SOUTH"
    "LEFT",
    "MOVE",
    "MOVE",
    "MOVE",
    "REPORT",  # Expected output: "Output: 0,0,EAST"
]

# Test data 4: Random commands
test_data_4 = [
    "PLACE 1,1,NORTH",
    "MOVE",
    "LEFT",
    "MOVE",
    "LEFT",
    "MOVE",
    "LEFT",
    "REPORT",  # Expected output: "Output: 0,0,SOUTH"
    "RIGHT",
    "MOVE",
    "RIGHT",
    "MOVE",
    "REPORT",  # Expected output: "Output: 1,1,WEST"
]

# Test data 5: Robot never placed
test_data_5 = [
    "MOVE",
    "RIGHT",
    "LEFT",
    "REPORT",  # Expected output: "Output: Robot is not placed on the table."
]

# Test data 6: Moving to the edge
test_data_6 = [
    "PLACE 4,4,WEST",
    "MOVE",
    "MOVE",
    "RIGHT",
    "MOVE",
    "MOVE",
    "REPORT",  # Expected output: "Output: 4,0,NORTH"
]

# Test data 7: Complex sequence
test_data_7 = [
    "PLACE 0,0,NORTH",
    "MOVE",
    "RIGHT",
    "MOVE",
    "PLACE 3,1,WEST",
    "MOVE",
    "LEFT",
    "MOVE",
    "MOVE",
    "LEFT",
    "MOVE",
    "REPORT",  # Expected output: "Output: 3,2,NORTH"
]
