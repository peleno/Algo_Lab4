import unittest

from ijones import ijones


class MyTestCase(unittest.TestCase):
    def test1(self):
        corridor = ['aaa',
                    'cab',
                    'def']
        self.assertEqual(ijones(corridor), 5)

    def test2(self):
        corridor = ['aaaaaaa',
                    'aaaaaaa',
                    'aaaaaaa',
                    'aaaaaaa',
                    'aaaaaaa',
                    'aaaaaaa']
        self.assertEqual(ijones(corridor), 201684)

    def test3(self):
        corridor = ['abcdefaghi']
        self.assertEqual(ijones(corridor), 2)
        
    def test_one_column(self):
        corridor = ['a', 'b', 'c', 'a']
        self.assertEqual(ijones(corridor), 2)

    def test_one_tile(self):
        corridor = ['a']
        self.assertEqual(ijones(corridor), 1)

    def test_one_row_with_unique_tiles(self):
        corridor = ['abcdefgh']
        self.assertEqual(ijones(corridor), 1)


if __name__ == '__main__':
    unittest.main()
