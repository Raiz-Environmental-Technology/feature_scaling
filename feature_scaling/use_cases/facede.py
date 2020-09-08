from feature_scaling.custom_typing.feature import Feature
from feature_scaling.models.feature import FeatureModel
from feature_scaling.entities.factory import FeatureScalingFactory
from feature_scaling.entities.type.mean_normalization import MeanNormalization
from feature_scaling.entities.type.min_max_normalization import MinMaxNormalization
from feature_scaling.entities.type.standard_score import StandardScore


class FeatureScalingFacede:
    """"""

    __slots__ = ["_feature", "_scaling_method",
                 "_feature_scaling_factory"]

    implemented_methods = {
        "mean_normalization": MeanNormalization,
        "min_max_normalization": MinMaxNormalization,
        "standard_score": StandardScore
    }

    def __init__(self, feature: Feature, scaling_method: str):
        self._feature = None
        self.feature = feature
        self._scaling_method = None
        self.scaling_method = scaling_method
        self._feature_scaling_factory = FeatureScalingFactory(
            self.scaling_method())

    def __str__(self):
        return f"feature: {self.feature}, scaling_method: {self.scaling_method().__str__()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(feature={self.feature}, scaling_method={self.scaling_method().__repr__()})"

    @property
    def feature(self) -> Feature:
        return self._feature

    @feature.setter
    def feature(self, feature) -> None:
        self._feature = feature

    @property
    def scaling_method(self) -> "implemented_methods":
        return self._scaling_method

    @scaling_method.setter
    def scaling_method(self, scaling_method: str) -> None:
        if isinstance(scaling_method, str):
            scaling_method = scaling_method.strip().lower()
        else:
            raise ValueError("Bad scaling method input. It must be a string.")
        if scaling_method not in self.implemented_methods:
            msg = "Bad scaling method input. The implemented methods are as follows: "
            msg += ", ".join(self.implemented_methods)
            raise ValueError(msg)
        else:
            self._scaling_method = self.implemented_methods[scaling_method]

    def scale_feature(self):
        return self._feature_scaling_factory.do(self.feature)

    def unscale_feature(self, feature_to_unscale: Feature):
        return self._feature_scaling_factory.undo(self.feature, feature_to_unscale)
