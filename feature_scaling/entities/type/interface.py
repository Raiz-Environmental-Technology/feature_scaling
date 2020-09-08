import abc
from feature_scaling.custom_typing.feature import Feature


class FeatureScalingInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def _set_scaling_attributes(self, feature: Feature) -> None:
        """
        Use this method to set the atributes to be used on the scaling operation.
        The attributes that was set, should be used to unscaling the feature.        
        """
        raise NotImplementedError

    @abc.abstractmethod
    def _scaling_function(self, xi: float) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def _unscaling_function(self, xi: float) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def do(self, feature: Feature) -> Feature:
        raise NotImplementedError

    @abc.abstractmethod
    def undo(self, original_feature: Feature, scaled_feature: Feature) -> Feature:
        raise NotImplementedError
