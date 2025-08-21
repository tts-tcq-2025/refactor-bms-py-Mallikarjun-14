from typing import Dict, List, Tuple, Callable

# --- Warning condition functions --- #
def temp_low_warning(v, r): return r[0] <= v < r[0] + 1.5
def temp_high_warning(v, r): return r[1] - 1.5 < v <= r[1]

def pulse_low_warning(v, r): return r[0] <= v < r[0] + 5
def pulse_high_warning(v, r): return r[1] - 5 < v <= r[1]

def spo2_low_warning(v, r): return r[0] <= v < r[0] + 2

# --- Vital rules configuration --- #
VITALS: Dict[str, Dict] = {
    "temperature": {
        "range": (95, 102),
        "warnings": [
            ("Approaching hypothermia", temp_low_warning),
            ("Approaching hyperthermia", temp_high_warning),
        ],
        "critical": "Temperature critical!",
    },
    "pulse": {
        "range": (60, 100),
        "warnings": [
            ("Low pulse approaching limit", pulse_low_warning),
            ("High pulse approaching limit", pulse_high_warning),
        ],
        "critical": "Pulse rate critical!",
    },
    "spo2": {
        "range": (90, float("inf")),
        "warnings": [
            ("Approaching hypoxemia (low oxygen)", spo2_low_warning),
        ],
        "critical": "Oxygen saturation critical!",
    },
}

# --- Core functions --- #
def notify(msg: str, critical: bool = False):
    print(f"{'ALERT' if critical else 'Warning'}: {msg}")

def check_all_vitals(temp: float, pulse: int, spo2: int) -> bool:
    values = {"temperature": temp, "pulse": pulse, "spo2": spo2}
    all_ok = True
    messages: List[Tuple[str, bool]] = []

    # Precompute all messages
    for name, val in values.items():
        r = VITALS[name]["range"]
        for msg, cond in VITALS[name]["warnings"]:
            if cond(val, r):
                messages.append((msg, False))
        if not (r[0] <= val <= r[1]):
            messages.append((VITALS[name]["critical"], True))
            all_ok = False

    # Notify outside loops
    for msg, critical in messages:
        notify(msg, critical)
    return all_ok

# --- Example usage --- #
if __name__ == "__main__":
    check_all_vitals(95.2, 97, 91)   # warnings
    check_all_vitals(94.5, 55, 88)   # alerts
