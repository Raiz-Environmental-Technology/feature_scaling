from typing import List, Union

Number = Union[int, float]

Feature_1D = List[Number]
Feature_2D = List[Feature_1D]
Feature_3D = List[Feature_2D]
Feature = Union[Feature_1D, Feature_2D, Feature_3D]
