import unittest
from unittest.mock import patch
from io import StringIO

import ToyRobot

class ToyRobotTest(unittest.TestCase):
    # Test method place
    def test_place(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'NORTH')
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.facing, 'NORTH')
    
    def test_invalid_place(self):
        robot = ToyRobot.ToyRobot()
        robot.place(6, 7, 'NORTH')
        self.assertIsNone(robot.x)
        self.assertIsNone(robot.y)
        self.assertIsNone(robot.facing)
    
    def test_invalid_direction(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'INVALID')
        self.assertIsNone(robot.facing)

    # Test method move
    def test_move_north(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'NORTH')
        robot.move()
        self.assertEqual(robot.y, 3)

    def test_move_south(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'SOUTH')
        robot.move()
        self.assertEqual(robot.y, 1)

    def test_move_east(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'EAST')
        robot.move()
        self.assertEqual(robot.x, 2)

    def test_move_west(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'WEST')
        robot.move()
        self.assertEqual(robot.x, 0)
    
    #Test method move falling 5x5 max 4 (0, 1, 2, 3, 4)
    def test_prevent_falling_north(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 4, 'NORTH')
        robot.move()
        self.assertEqual(robot.y, 4)

    def test_prevent_falling_south(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 0, 'SOUTH')
        robot.move()
        self.assertEqual(robot.y, 0)

    def test_prevent_falling_east(self):
        robot = ToyRobot.ToyRobot()
        robot.place(4, 2, 'EAST')
        robot.move()
        self.assertEqual(robot.x, 4)

    def test_prevent_falling_west(self):
        robot = ToyRobot.ToyRobot()
        robot.place(0, 2, 'WEST')
        robot.move()
        self.assertEqual(robot.x, 0)

    # Test method left
    def test_left_from_north(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'NORTH')
        robot.left()
        self.assertEqual(robot.facing, 'WEST')

    def test_left_from_south(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'SOUTH')
        robot.left()
        self.assertEqual(robot.facing, 'EAST')

    def test_left_from_east(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'EAST')
        robot.left()
        self.assertEqual(robot.facing, 'NORTH')

    def test_left_from_west(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'WEST')
        robot.left()
        self.assertEqual(robot.facing, 'SOUTH')
    
    # Test method right
    def test_right_from_north(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'NORTH')
        robot.right()
        self.assertEqual(robot.facing, 'EAST')

    def test_right_from_south(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'SOUTH')
        robot.right()
        self.assertEqual(robot.facing, 'WEST')

    def test_right_from_east(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'EAST')
        robot.right()
        self.assertEqual(robot.facing, 'SOUTH')

    def test_right_from_west(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'WEST')
        robot.right()
        self.assertEqual(robot.facing, 'NORTH')

    # Test method report
    def test_report(self):
        robot = ToyRobot.ToyRobot()
        robot.place(1, 2, 'NORTH')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            robot.report()
            self.assertEqual(mock_stdout.getvalue().strip(), "Output: 1,2,NORTH")
