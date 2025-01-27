# Scope

This library can be used for feature scaling and unscaling.

## Installation

```bash
pip install git+ssh://git@github.com/Raiz-Environmental-Technology/feature_scaling.git
```

## Usage

```python
from feature_scaling import FeatureScalingFacede

input_feature = [2, 4, 6]
facede = FeatureScalingFacede(feature=input_feature, scaling_method="mean_normalization")
scaled_feature = facede.scale_feature()
unscaled_feature = facede.unscale_feature(scaled_feature)

```

## Implemented Scaling Methods
```python
for method in FeatureScalingFacede.implemented_methods:
    print(method)
```

## Simplified Class Diagram
![Alt text](ClassDiagram.png?raw=true "Simplified Class Diagram")


## License
This is private python package from Raiz Environmental Technology
[MIT](https://github.com/Raiz-Environmental-Technology/feature_scaling/blob/master/LICENSE)