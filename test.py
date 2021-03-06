import unittest
import sys
from main import *


class TestCaseTurn(unittest.TestCase):

    def test_turning_left(self):
        assert turnLeft('N') == 'W'
        assert turnLeft('E') == 'N'
        assert turnLeft('S') == 'E'
        assert turnLeft('W') == 'S'

    def test_turning_right(self):
        assert turnRight('N') == 'E'
        assert turnRight('E') == 'S'
        assert turnRight('S') == 'W'
        assert turnRight('W') == 'N'


class TestCaseMove(unittest.TestCase):

    def setUp(self):
        self.moveEast = move([2, ' ', 4, ' ', 'E'], 7, 7)
        self.moveWest = move([5, ' ', 3, ' ', 'W'], 7, 7)
        self.moveNorth = move([3, ' ', 5, ' ', 'N'], 7, 7)
        self.moveSouth = move([5, ' ', 4, ' ', 'S'], 7, 7)

    def test_move(self):
        self.assertIn(self.moveEast, range(1, 8))
        self.assertIn(self.moveNorth, range(1, 8))
        self.assertIn(self.moveWest, range(1, 8))
        self.assertIn(self.moveSouth, range(1, 8))

    def test_move_off_edge(self):
        with self.assertRaises(ValueError):
            move([4, ' ', 6, ' ', 'N'], 5, 5)
        with self.assertRaises(ValueError):
            move([4, ' ', 6, ' ', 'E'], 3, 5)
        with self.assertRaises(ValueError):
            move([-1, ' ', 6, ' ', 'W'], 5, 5)
        with self.assertRaises(ValueError):
            move([4, ' ', -1, ' ', 'S'], 5, 5)


class TestRover(unittest.TestCase):

    def test_rover(self):
        assert rover([5, ' ', 4, ' ', 'N'],
                     ['L', 'M', 'L', 'M', 'M', 'R', 'R', 'M'],
                     7, 8) == '4 3 N'

    def test_rover_inst(self):
        assert rover([2, ' ', 4, ' ', 'N'],
                     ['M', 'M', 'M'], 3, 5) is None


class TestMain(unittest.TestCase):

    def setUp(self):
        self.filename1 = 'inputtt.txt'
        self.filename2 = 'inputtest.txt'

    def test_filename(self):
        main(self.filename1)
        self.assertTrue(sys.stdout, 'File not found Error.')

    def test_main_input(self):
        f = open(self.filename2, 'w')
        f.write('5 D')
        f.close()
        main(self.filename2)
        self.assertTrue(sys.stdout, 'The top line should have '
                                    'integer coordinates')
        f = open(self.filename2, 'w')
        f.write('5 4\n2 1 5\nLLMMRM')
        f.close()
        main(self.filename2)
        self.assertTrue(sys.stdout, 'The start co-ordinates '
                                    'of the rover must be '
                                    'in the format 2 3 E')

        f = open(self.filename2, 'w')
        f.write('5 4\n2 1 E\nLLMTRM')
        f.close()
        main(self.filename2)
        self.assertTrue(sys.stdout, 'The instructions must '
                                    'contain only one of these '
                                    'characters (L,R,M)')


if __name__ == '__main__':
    unittest.main()
