import numpy as np

from .abstract_class import FeatureScalingAbstractClass


class StandardScore(FeatureScalingAbstractClass):

    __slots__ = ["_mean", "_std"]

    def __init__(self):
        self._mean = None
        self._std = None

    def __str__(self):
        return "Standard Score Method"

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def _set_scaling_attributes(self, feature) -> None:
        feature = np.array(feature)
        self._mean = feature.mean()
        self._std = feature.std()

    def _scaling_function(self, xi):
        return (xi - self._mean) / self._std

    def _unscaling_function(self, xi):
        return (self._std * xi) + self._mean
