import unittest

from feature_scaling.models.feature import FeatureModel


class TestFeatureModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n")
        print("---------- Starting Feature Model Tests ----------")
        print("\n")
        feature0 = [1.9, 2, 3.2, 4, 5]
        feature1 = [[1, -2, 3], [-4, 5, -6], [-7, 8, 9]]
        feature2 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
        feature3 = [[1, "2", 3], [4, "5.7", 6], [7, 8, 9]]

        feature4 = [1, "a", 2.2, 1]
        feature5 = [[1, "a"], [2, "b"]]
        feature6 = [[1], [1, 2], [1]]
        feature7 = [[1, 2], [1], [1, 2, "a", 4]]

        cls.right_features = [feature0, feature1, feature2, feature3]
        cls.wrong_features = [feature4, feature5, feature6, feature7]

    @classmethod
    def tearDownClass(cls):
        print("\n")
        print("---------- Feature Model Tests Finished ----------")

    def test_wrong_features(self):
        print("Running Wrong Features Test")
        for feature in self.wrong_features:
            with self.assertRaises(ValueError):
                FeatureModel(feature)

    def test_right_features(self):
        print("Running Right Features Test")
        for feature in self.right_features:
            try:
                FeatureModel(feature)
            except ValueError:
                self.fail("ValueError raised")

    def test_class_representations(self):
        print("Running Feature Model Class Representations Test")
        feature = FeatureModel([1, 2, 3])
        self.assertTrue(isinstance(feature.__str__(), str))
        self.assertTrue(isinstance(feature.__repr__(), str))
