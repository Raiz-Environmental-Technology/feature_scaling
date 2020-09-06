import numpy as np
from App.CustomTyping.feature import Feature


class FeatureModel:

    __slots__ = ["_feature"]

    def __init__(self, feature: Feature):
        self._feature = None
        self.feature = feature

    @property
    def feature(self) -> Feature:
        return self._feature

    @feature.setter
    def feature(self, feature: Feature) -> None:
        try:
            feature = np.array(feature, dtype=np.float32)
        except ValueError as error:
            raise ValueError(f"Bad feature input. {error}")

        if np.all(feature == feature.flatten()[0]):
            raise ValueError(
                "Bad feature input. All numbers cannot be the same")

        self._feature = feature
