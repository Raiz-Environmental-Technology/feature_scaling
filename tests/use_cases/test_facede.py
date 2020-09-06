import unittest

from feature_scaling.use_cases.facede import FeatureScalingFacede


class TestFeatureScalingFacede(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n")
        print("---------- Starting Feature Scaling Facede Tests ----------")
        print("\n")
        cls.input_feature = [2, 4, 6]

        cls.valid_methods = ["mean_normalization",
                             "min_max_normalization",
                             "standard_score",
                             "Mean_Normalization",
                             "  mean_normalization  "]

        cls.invalid_methods = ["invalid", "minmaxnormalization",
                               "min max normalization"]

    @classmethod
    def tearDownClass(cls):
        print("\n")
        print("---------- Feature Scaling Facede Tests Finished ----------")
        print("\n")

    def test_valid_methods(self):
        print("Running Valid Methods Test")
        for method in self.valid_methods:
            try:
                FeatureScalingFacede(
                    self.input_feature, method)
            except ValueError:
                self.fail("ValueError raised")

    def test_invalid_methods(self):
        print("Running Invalid Methods Test")
        for method in self.invalid_methods:
            with self.assertRaises(ValueError):
                FeatureScalingFacede(
                    self.input_feature, method)

    def test_facede(self):
        print("Running Facede Test")
        facede = FeatureScalingFacede(
            self.input_feature, self.valid_methods[0])
        scaled_feature = facede.scale_feature()
        unscaled_feature = facede.unscale_feature(scaled_feature)

    def test_class_representations(self):
        print("Running Feature Scaling Facede Class Representations Test")
        facede = FeatureScalingFacede(
            self.input_feature, self.valid_methods[0])

        print(facede)
        print(repr(facede))
        self.assertTrue(isinstance(facede.__str__(), str))
        self.assertTrue(isinstance(facede.__repr__(), str))
