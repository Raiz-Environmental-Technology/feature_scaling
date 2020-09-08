import sys
from feature_scaling.use_cases.facede import FeatureScalingFacede

message = "Sorry, only Python versions greater than 3.6 are accepted."

if sys.version_info.major < 3:
    sys.exit(message)
if sys.version_info.minor < 6:
    sys.exit(message)
