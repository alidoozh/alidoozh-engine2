from mlp_model import predict_mlp
from drl_model import predict_drl
from risk_reward import get_risk_reward

def get_signals():
    return {
        "mlp": predict_mlp(),
        "drl": predict_drl(),
        "risk_reward": get_risk_reward()
    }
