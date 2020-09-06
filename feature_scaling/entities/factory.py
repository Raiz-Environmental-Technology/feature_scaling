from feature_scaling.custom_typing.feature import Feature
from feature_scaling.models.feature import FeatureModel
from .type.interface import FeatureScalingInterface


class FeatureScalingFactory:
    __slots__ = ["_feature_scaling_method"]

    def __init__(self, feature_scaling_method: FeatureScalingInterface):
        self._feature_scaling_method = None
        self.feature_scaling_method = feature_scaling_method

    def __str__(self):
        return f"Feature Scaling Factory using {self.feature_scaling_method.__str__()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(feature_scaling_method={self.feature_scaling_method.__repr__()})"

    @property
    def feature_scaling_method(self) -> FeatureScalingInterface:
        return self._feature_scaling_method

    @feature_scaling_method.setter
    def feature_scaling_method(self, feature_scaling_method: FeatureScalingInterface) -> None:
        assert isinstance(feature_scaling_method,
                          FeatureScalingInterface)
        self._feature_scaling_method = feature_scaling_method

    @feature_scaling_method.deleter
    def feature_scaling_method(self) -> None:
        del self._feature_scaling_method

    def do(self, feature: Feature) -> Feature:
        feature = FeatureModel(feature).feature
        return self._feature_scaling_method.do(feature)

    def undo(self, original_feature: Feature, scaled_feature: Feature) -> Feature:
        original_feature = FeatureModel(original_feature).feature
        scaled_feature = FeatureModel(scaled_feature).feature
        return self._feature_scaling_method.undo(original_feature, scaled_feature)
