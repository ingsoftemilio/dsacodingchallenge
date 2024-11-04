def min_number(arr,lowest_index,highest_index):

    # BASE CASE, there's only one element to process, trivially one element is its minimum
    if lowest_index==highest_index:
        return arr[lowest_index]
    
    """DIVIDE"""
    # SPLIT
    mid_index = (lowest_index+highest_index) // 2

    # RECURSIVE TO GET HALF VALUES
    left_half_min=min_number(arr,lowest_index,mid_index)
    right_half_max=min_number(arr,mid_index+1,highest_index)

    """CONQUER"""
    # Perform the operation, compare and get the min
    return min(left_half_min,right_half_max)

# arr = [7, 2, -5, 3, 9, 1, 6]
# res = min_number(arr,0,len(arr)-1)
# print(f"Min number: {res}")


"""UNIT TESTS"""
import unittest

class TestFindMinimum(unittest.TestCase):
    
    def test_positive_numbers(self):
        arr = [7, 2, 5, 3, 9, 1, 6]
        self.assertEqual(min_number(arr, 0, len(arr) - 1), 1)

    def test_negative_numbers(self):
        arr = [-7, -2, -5, -3, -9, -1, -6]
        self.assertEqual(min_number(arr, 0, len(arr) - 1), -9)

    def test_mixed_numbers(self):
        arr = [7, -2, 5, 3, -9, 1, 6]
        self.assertEqual(min_number(arr, 0, len(arr) - 1), -9)
    
    def test_single_element(self):
        arr = [42]
        self.assertEqual(min_number(arr, 0, 0), 42)
    
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(min_number(arr, 0, len(arr) - 1), 1)
    
    def test_duplicate_elements(self):
        arr = [5, 5, 5, 5, 5]
        self.assertEqual(min_number(arr, 0, len(arr) - 1), 5)
    
    def test_large_range(self):
        arr = list(range(1000, -1, -1))  # [1000, 999, ..., 0]
        self.assertEqual(min_number(arr, 0, len(arr) - 1), 0)

# Run the tests
if __name__ == '__main__':
    unittest.main()

