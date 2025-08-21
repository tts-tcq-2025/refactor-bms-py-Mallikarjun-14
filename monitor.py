from typing import Dict, Callable, List, Tuple

# --- Vital rules in one config (no duplication) --- #
VITALS: Dict[str, Dict] = {
    "temperature": {
        "range": (95, 102),
        "warnings": [
            ("Approaching hypothermia", lambda v, r: r[0] <= v < r[0] + 1.5),
            ("Approaching hyperthermia", lambda v, r: r[1] - 1.5 < v <= r[1]),
        ],
        "critical": "Temperature critical!",
    },
    "pulse": {
        "range": (60, 100),
        "warnings": [
            ("Low pulse approaching limit", lambda v, r: r[0] <= v < r[0] + 5),
            ("High pulse approaching limit", lambda v, r: r[1] - 5 < v <= r[1]),
        ],
        "critical": "Pulse rate critical!",
    },
    "spo2": {
        "range": (90, float("inf")),
        "warnings": [
            ("Approaching hypoxemia (low oxygen)", lambda v, r: r[0] <= v < r[0] + 2),
        ],
        "critical": "Oxygen saturation critical!",
    },
}

# --- Core functions (short + flat) --- #
def notify(msg: str, critical: bool = False):
    level = "ALERT" if critical else "Warning"
    print(f"{level}: {msg}")

def check_vital(name: str, value: float) -> bool:
    r = VITALS[name]["range"]
    for msg, cond in VITALS[name]["warnings"]:
        if cond(value, r):
            notify(msg)
    if not (r[0] <= value <= r[1]):
        notify(VITALS[name]["critical"], critical=True)
        return False
    return True

def vitals_ok(temp: float, pulse: int, spo2: int) -> bool:
    return all([
        check_vital("temperature", temp),
        check_vital("pulse", pulse),
        check_vital("spo2", spo2),
    ])

# --- Example --- #
if __name__ == "__main__":
    vitals_ok(95.2, 97, 91)   # warnings
    vitals_ok(94.5, 55, 88)   # alerts
