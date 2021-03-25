import unittest
from task import conv_num, conv_endian, my_datetime


class Function_1_Tests(unittest.TestCase):

    def test1(self):
        # test 12345
        result_expected = 12345
        self.assertEqual(conv_num("12345"), result_expected)

    def test2(self):
        # test -12345
        result_expected = -12345
        self.assertEqual(conv_num("-12345"), result_expected)

    def test3(self):
        # test .45
        result_expected = .45
        self.assertEqual(conv_num(".45"), result_expected)

    def test4(self):
        # test -.45
        result_expected = -.45
        self.assertEqual(conv_num("-.45"), result_expected)

    def test5(self):
        # test 0.45
        result_expected = 0.45
        self.assertEqual(conv_num("0.45"), result_expected)

    def test6(self):
        # test -0.45
        result_expected = -0.45
        self.assertEqual(conv_num("-0.45"), result_expected)

    def test7(self):
        # test 123.
        result_expected = 123.0
        self.assertEqual(conv_num("123."), result_expected)

    def test8(self):
        # test -123.
        result_expected = -123.0
        self.assertEqual(conv_num("-123."), result_expected)

    def test9(self):
        # test 123.0
        result_expected = 123.0
        self.assertEqual(conv_num("123.0"), result_expected)

    def test10(self):
        # test -123.0
        result_expected = -123.0
        self.assertEqual(conv_num("-123.0"), result_expected)


class Function_2_Tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test2(self):
        self.assertEqual(my_datetime(2703600), "02-01-1970")

    def test3(self):
        self.assertEqual(my_datetime(68169700), "02-29-1972")

    def test4(self):
        self.assertEqual(my_datetime(1582946657), "02-29-2020")

    def test5(self):
        self.assertEqual(my_datetime(617945057), "08-01-1989")

    def test6(self):
        self.assertEqual(my_datetime(975666845), "12-01-2000")

    # example from assignment
    def test7(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    # example from assignment
    def test8(self):
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    def test9(self):
        self.assertEqual(my_datetime(31343858657), "04-01-2963")

    def test10(self):
        self.assertEqual(my_datetime(21637445645), "08-31-2655")

    def test11(self):
        self.assertEqual(my_datetime(8362607645), "01-01-2235")

    def test12(self):
        self.assertEqual(my_datetime(9814188257), "12-31-2280")

    def test13(self):
        self.assertEqual(my_datetime(16756799645), "01-01-2501")

    def test14(self):
        self.assertEqual(my_datetime(446932799), "02-29-1984")


class Function_3_Tests(unittest.TestCase):

    def test1(self):
        # test invalid endian parameter
        num = 1
        endian = 'error'
        expected = None
        self.assertEqual(conv_endian(num, endian), expected, "Incorrect endian type should return None")

    def test2(self):
        # test 954786
        num = 954786
        endian = 'big'
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num, endian), expected, "{0} should be {1} when {2} endian".format(num, expected,
                                                                                                        endian))

    def test3(self):
        # test -954786
        num = -954786
        endian = 'big'
        expected = '-0E 91 A2'
        self.assertEqual(conv_endian(num, endian), expected, "{0} should be {1} when {2} endian".format(num, expected,
                                                                                                        endian))

    def test4(self):
        # test 16; edge case
        num = 16
        endian = 'big'
        expected = '10'
        self.assertEqual(conv_endian(num, endian), expected, "{0} should be {1} when {2} endian".format(num, expected,
                                                                                                        endian))

    def test5(self):
        # test 15; edge case
        num = 15
        endian = 'big'
        expected = '0F'
        self.assertEqual(conv_endian(num, endian), expected, "{0} should be {1} when {2} endian".format(num, expected,
                                                                                                        endian))

    def test6(self):
        # test 0; edge case
        num = 0
        endian = 'big'
        expected = '00'
        self.assertEqual(conv_endian(num, endian), expected, "{0} should be {1} when {2} endian".format(num, expected,
                                                                                                        endian))

    def test7(self):
        # test 954786 without specifying endian
        num = 954786
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num), expected, "{0} should be {1} without specifying Endian".format(num, expected)
                         )

    def test8(self):
        # test 954786 little endian
        num = 954786
        endian = 'little'
        expected = 'A2 91 0E'
        self.assertEqual(conv_endian(num, endian), expected, "{0} should be {1} when {2} endian".format(num, expected,
                                                                                                        endian))

    def test9(self):
        # test -954786 little endian
        num = -954786
        endian = 'little'
        expected = '-A2 91 0E'
        self.assertEqual(conv_endian(num, endian), expected, "{0} should be {1} when {2} endian".format(num, expected,
                                                                                                        endian))

    def text10(self):
        # test passing parameter names
        num_param = -954786
        endian_param = 'little'
        expected = '-A2 91 0E'
        self.assertEqual(conv_endian(num=num_param, endian=endian_param), expected, "{0} should be {1} when {2} endian".
                         format(num_param, expected, endian_param))


if __name__ == '__main__':
    unittest.main()
