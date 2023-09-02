# Toy Robot Simulator
This is a simple Toy Robot Simulator that allows you to control a toy robot on a 5x5 grid tabletop. The robot can be placed on the grid and instructed to move, turn left, turn right, and report its position. The robot is prevented from falling off the grid.

## Getting Started
1. **Run the Simulator**: Run the simulator by executing the Python script.

    ```bash
    python3.8 ToyRobot.py
    ```

2. **Enter Commands**: You can enter commands to control the robot. The available commands are:

   - `PLACE X,Y,F`: Place the robot on the grid at position (X, Y) facing direction F (NORTH, SOUTH, EAST, or WEST).
   - `MOVE`: Move the robot one step in the current direction.
   - `LEFT`: Turn the robot 90 degrees to the left.
   - `RIGHT`: Turn the robot 90 degrees to the right.
   - `REPORT`: Display the current position and direction of the robot.

3. **Example Commands**: Try entering commands like:

    ```
    PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT
    ```

    The robot will execute the commands and report its final position.

4. **Enjoy**: Have fun experimenting with different commands and scenarios to see how the robot behaves!

## Tests

Unit tests are provided to ensure that the simulator functions correctly. You can run the tests using the following command:

```bash
python3.8 -m unittest ToyRobotTest.py
```