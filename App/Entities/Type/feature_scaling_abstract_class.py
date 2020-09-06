import abc
import numpy as np

from .feature_scaling_interface import FeatureScalingInterface


class FeatureScalingAbstractClass(FeatureScalingInterface, metaclass=abc.ABCMeta):

    def do(self, feature):
        feature = np.array(feature)
        self._set_scaling_attributes(feature)

        return np.vectorize(self._scaling_function)(feature)

    def undo(self, original_feature, scaled_feature):
        original_feature = np.array(original_feature)
        scaled_feature = np.array(scaled_feature)

        self._set_scaling_attributes(original_feature)

        return np.vectorize(self._unscaling_function)(scaled_feature)
