import abc
from App.CustomTyping.feature import Feature


class FeatureScalingInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def _set_scaling_attributes(self, feature: Feature) -> None:
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
