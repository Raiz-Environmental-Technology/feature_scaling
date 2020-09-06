import unittest

import numpy as np

from feature_scaling.entities.type.mean_normalization import MeanNormalization


class TestMeanNormalization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n")
        print("---------- Starting Mean Normalization Tests ----------")
        print("\n")
        cls.feature0 = [2, 4, 6]
        cls.feature1 = [1.9, 2, 3.2, 4, 5]
        cls.feature2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    @classmethod
    def tearDownClass(cls):
        print("\n")
        print("---------- Min Mean Normalization Tests Finished ----------")

    def test_mean_normalization_do(self):
        print("Running Mean Normalization Do Method Test")
        mean_normalization = MeanNormalization()

        feature = mean_normalization.do(self.feature0)
        feature = np.around(feature, decimals=3)

        expected_result = np.array([-0.5, 0., 0.5])

        self.assertTrue(
            np.equal(feature, expected_result).all()
        )

    def test_mean_normalization_undo(self):
        print("Running Mean Normalization Undo Method Test")
        mean_normalization = MeanNormalization()

        for feature in [self.feature0, self.feature1, self.feature2]:
            scaled_feature = mean_normalization.do(feature)
            unscaled_feature = mean_normalization.undo(
                feature, scaled_feature)
            self.assertTrue(np.equal(feature, unscaled_feature).all())

    def test_class_representations(self):
        print("Running Mean Normalization Class Representations Test")
        mean_normalization = MeanNormalization()
        self.assertTrue(isinstance(mean_normalization.__str__(), str))
        self.assertTrue(isinstance(mean_normalization.__repr__(), str))
