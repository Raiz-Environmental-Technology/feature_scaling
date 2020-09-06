import numpy as np

from .abstract_class import FeatureScalingAbstractClass


class MeanNormalization(FeatureScalingAbstractClass):

    __slots__ = ["_min", "_max", "_mean"]

    def __init__(self):
        self._min = None
        self._max = None
        self._mean = None

    def _set_scaling_attributes(self, feature) -> None:
        feature = np.array(feature)
        self._min = feature.min()
        self._max = feature.max()
        self._mean = feature.mean()

    def _scaling_function(self, xi):
        return (xi - self._mean) / (self._max - self._min)

    def _unscaling_function(self, xi):
        return (xi*(self._max - self._min)) + self._mean
