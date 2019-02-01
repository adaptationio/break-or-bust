from stable_baselines.common.policies import MlpLnLstmPolicy, FeedForwardPolicy, LstmPolicy, CnnPolicy, CnnLstmPolicy, CnnLnLstmPolicy


class CustomPolicy(FeedForwardPolicy):
    def __init__(self, *args, **kwargs):
        super(CustomPolicy, self).__init__(*args, **kwargs,
                                           layers=[256, 256, 256],
                                           layer_norm=True,
                                            feature_extraction="mlp")
                    
class CustomPolicy_2(LstmPolicy):
    def __init__(self, *args, **kwargs):
        super(CustomPolicy_2, self).__init__(*args, **kwargs,
                                           layers=[256,256],
                                           layer_norm=True,
                                            feature_extraction="mlp",
                                            n_envs=16,
                                            )

class CustomPolicy_3(FeedForwardPolicy):
    def __init__(self, *args, **kwargs):
        super(CustomPolicy_3, self).__init__(*args, **kwargs,
                                           layers=[256,256,256],
                                           layer_norm=True,
                                            feature_extraction="mlp")

                                            

class CustomPolicyCnn(CnnPolicy):
    def __init__(self, *args, **kwargs):
        super(CustomPolicyCnn, self).__init__(*args, **kwargs,
                                           layers=[256,256],
                                           layer_norm=True,
                                            feature_extraction="cnn")

class CustomPolicyCnnLstm(CnnLstmPolicy):
    def __init__(self, *args, **kwargs):
        super(CustomPolicyCnnLstm, self).__init__(*args, **kwargs,
                                           layers=[256,256],
                                           layer_norm=True,
                                            feature_extraction="cnn")

class CustomPolicyCnnLnLstm(CnnLstmPolicy):
    def __init__(self, *args, **kwargs):
        super(CustomPolicyCnnLnLstm, self).__init__(*args, **kwargs,
                                           layers=[256,256],
                                           layer_norm=True,
feature_extraction="cnn")