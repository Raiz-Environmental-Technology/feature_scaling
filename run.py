from feature_scaling import FeatureScalingFacede


input_feature = [2, 4, 6]
facede = FeatureScalingFacede(input_feature, "mean_normalization")
scaled_feature = facede.scale_feature()
unscaled_feature = facede.unscale_feature(scaled_feature)

print(input_feature, scaled_feature, unscaled_feature)
