from typing import Dict, Callable, List, Tuple

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
    level = "ALERT" if critical else "Warning"
    print(f"{level}: {msg}")

def check_vital(name: str, value: float) -> bool:
    r = VITALS[name]["range"]
    # Check warnings
    for msg, condition in VITALS[name]["warnings"]:
        if condition(value, r):
            notify(msg)
    # Check critical
    if not (r[0] <= value <= r[1]):
        notify(VITALS[name]["critical"], critical=True)
        return False
    return True

def vitals_ok(temp: float, pulse: int, spo2: int) -> bool:
    results = [
        check_vital("temperature", temp),
        check_vital("pulse", pulse),
        check_vital("spo2", spo2),
    ]
    return all(results)

# --- Example usage --- #
if __name__ == "__main__":
    vitals_ok(95.2, 97, 91)   # warnings
    vitals_ok(94.5, 55, 88)   # alerts
  # alerts
