import numpy as np

from .feature_scaling_abstract_class import FeatureScalingAbstractClass


class MinMaxNormalization(FeatureScalingAbstractClass):

    __slots__ = ["_min", "_max"]

    def __init__(self):
        self._min = None
        self._max = None

    def _set_scaling_attributes(self, feature) -> None:
        feature = np.array(feature)
        self._min = feature.min()
        self._max = feature.max()

    def _scaling_function(self, xi):
        return (xi - self._min) / (self._max - self._min)

    def _unscaling_function(self, xi):
        return (xi*(self._max - self._min)) + self._min
