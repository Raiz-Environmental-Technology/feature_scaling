import numpy as np
from feature_scaling.custom_typing.feature import Feature


class FeatureModel:
    """
    The FeatureModel object is used to validate input features

    Parameters
    ----------
    feature : Feature (feature_scaling.custom_typing)

    Attributes
    ----------
    _feature : Feature (feature_scaling.custom_typing)

    """

    __slots__ = ["_feature"]

    def __init__(self, feature: Feature):
        self._feature = None
        self.feature = feature

    def __str__(self):
        return f"feature: {self.feature}"

    def __repr__(self):
        return f"{self.__class__.__name__}(feature={self.feature})"

    @property
    def feature(self) -> Feature:
        return self._feature

    @feature.setter
    def feature(self, feature: Feature) -> None:
        """
        Only numeric vectors will be accepted.
        If nested vectors are present, they must be the same size.
        All values in feature ​​cannot be the same.

        Parameters
        ----------
        feature : Feature (feature_scaling.custom_typing)

        Raises
        ------
        ValueError
            Bad feature input.

        Returns
        -------
        None
        """
        try:
            feature = np.array(feature, dtype=np.float32)
        except ValueError as error:
            raise ValueError(f"Bad feature input. {error}")

        if np.all(feature == feature.flatten()[0]):
            raise ValueError(
                "Bad feature input. All values cannot be the same")

        self._feature = feature
