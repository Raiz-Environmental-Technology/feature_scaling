import unittest

import numpy as np

from App.Entities.Type.standard_score import StandardScore


class TestStandardScore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n")
        print("---------- Starting Standard Score Tests ----------")
        print("\n")
        cls.feature0 = [2, 4, 6]
        cls.feature1 = [1.9, 2, 3.2, 4, 5]
        cls.feature2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    @classmethod
    def tearDownClass(cls):
        print("\n")
        print("---------- Standard Score Tests Finished ----------")

    def test_standard_score_do(self):
        print("Running Standard Score Do Method Test")
        standard_score = StandardScore()

        feature = standard_score.do(self.feature0)
        feature = np.around(feature, decimals=3)

        expected_result = np.array([-1.225, 0.0, 1.225])

        self.assertTrue(
            np.equal(feature, expected_result).all()
        )

    def test_standard_score_undo(self):
        print("Running Standard Score Undo Method Test")
        standard_score = StandardScore()

        for feature in [self.feature0, self.feature1, self.feature2]:
            scaled_feature = standard_score.do(feature)
            unscaled_feature = standard_score.undo(feature, scaled_feature)
            self.assertTrue(np.equal(feature, unscaled_feature).all())
