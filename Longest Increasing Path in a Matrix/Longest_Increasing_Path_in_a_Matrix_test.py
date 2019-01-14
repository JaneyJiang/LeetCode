import unittest

from Longest_Increasing_Path_in_a_Matrix import Solution

#//TODO:Test cases are incomplete and need to be supplemented
class LongestIncreasingPathTest(unittest.TestCase):
    def test_normal_matrix1(self):
        matrix =  [
            [9,9,4],
            [6,6,8],
            [2,1,1]
            ] 
        excepted = 4
        self.assertEqual(Solution().longestIncreasingPath(matrix),excepted)
    def test_normal_matrix2(self):
        matrix =  [
            [3,4,5],
            [3,2,6],
            [2,2,1]
            ] 
        excepted = 4
        self.assertEqual(Solution().longestIncreasingPath(matrix),excepted)
    def test_Empty_matrix(self):
        matrix =  [] 
        excepted = 0
        self.assertEqual(Solution().longestIncreasingPath(matrix),excepted)
    def test_Same_matrix1(self):
        matrix =  [1,1,1] 
        excepted = 1
        self.assertEqual(Solution().longestIncreasingPath(matrix),excepted)
    def test_Same_matrix1(self):
        matrix =  [[1,1],[1,1],[1,1]] 
        excepted = 1
        self.assertEqual(Solution().longestIncreasingPath(matrix),excepted)

if __name__ == "__main__":
    unittest.main()