import unittest


class CollectionUtils:
    def findMax(self, numbers):
        maximum = 0 # return max(numbers)
        for i in numbers:
            if i > maximum:
                maximum = i
        return maximum

    def findMin(self, numbers):
        minimum = 0
        for i in numbers:
            if i < minimum:
                minimum = i
        return minimum

    def removeDuplicates(self, numbers):
        l = []
        for i in numbers:
            if i in l:
                continue
            l.append(i)
        return l


class CollectionUtilsTest(unittest.TestCase):
    def setUp(self):
        self.CollectionUtils = CollectionUtils()

    def test_findMax(self):
        self.assertEqual(self.CollectionUtils.findMax([1, 2, -2, 5, -100, 5, -99]), 5)

    def test_findMin(self):
        self.assertEqual(self.CollectionUtils.findMin([1, 2, -2, 5, -100, 5, -99]), -100)

    def test_removeDuplicates(self):
        self.assertEqual(self.CollectionUtils.removeDuplicates(['Артем', 'Иван', 'Артем']), ['Артем', 'Иван',])


if __name__ == "__main__":
    unittest.main()