import unittest

import numpy as np

from feature_scaling.entities.type.min_max_normalization import MinMaxNormalization


class TestMinMaxNormalization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n")
        print("---------- Starting Min Max Normalization Tests ----------")
        print("\n")
        cls.feature0 = [2, 4, 6]
        cls.feature1 = [1.9, 2, 3.2, 4, 5]
        cls.feature2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    @classmethod
    def tearDownClass(cls):
        print("\n")
        print("---------- Min Max Normalization Tests Finished ----------")

    def test_min_max_normalization_do(self):
        print("Running Min Max Normalization Do Method Test")
        min_max_normalization = MinMaxNormalization()

        feature = min_max_normalization.do(self.feature0)
        feature = np.around(feature, decimals=3)

        expected_result = np.array([0., 0.5, 1.])

        self.assertTrue(
            np.equal(feature, expected_result).all()
        )

    def test_min_max_normalization_undo(self):
        print("Running Min Max Normalization Undo Method Test")
        min_max_normalization = MinMaxNormalization()

        for feature in [self.feature0, self.feature1, self.feature2]:
            scaled_feature = min_max_normalization.do(feature)
            unscaled_feature = min_max_normalization.undo(
                feature, scaled_feature)
            self.assertTrue(np.equal(feature, unscaled_feature).all())

    def test_class_representations(self):
        print("Running Min Max Normalization Class Representations Test")
        min_max_normalization = MinMaxNormalization()
        self.assertTrue(isinstance(min_max_normalization.__str__(), str))
        self.assertTrue(isinstance(min_max_normalization.__repr__(), str))
