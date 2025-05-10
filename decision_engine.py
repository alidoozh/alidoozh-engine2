from signal_engine import get_signals

def get_final_signal():
    s = get_signals()
    score = (s['mlp']['confidence'] + s['drl']['confidence']) / 2
    rr = s['risk_reward']['ratio']
    if score >= 0.7 and rr > 2:
        if s['mlp']['signal'] == s['drl']['signal']:
            return s['mlp']['signal']
        return "hold"
    return "no_trade"
