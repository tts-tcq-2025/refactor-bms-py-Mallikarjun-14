import sys
from time import sleep
from typing import Dict, Tuple
from datetime import datetime
import os

LOG_FILE = os.path.join(os.getcwd(), "vitals_log.txt")

# --- Vital ranges and warning bands (data-driven) --- #
VITALS: Dict[str, Dict] = {
    "temperature": {
        "range": (95, 102),
        "warnings": [
            ("Approaching hypothermia", lambda v, r: r[0] <= v < r[0] + 1.53),
            ("Approaching hyperthermia", lambda v, r: r[1] - 1.53 < v <= r[1]),
        ],
    },
    "pulse": {
        "range": (60, 100),
        "warnings": [
            ("Low pulse approaching limit", lambda v, r: r[0] <= v < r[0] + 5),
            ("High pulse approaching limit", lambda v, r: r[1] - 5 < v <= r[1]),
        ],
    },
    "spo2": {
        "range": (90, float("inf")),
        "warnings": [
            ("Approaching hypoxemia (low oxygen)", lambda v, r: r[0] <= v < r[0] + 2),
        ],
    },
}

# --- Helpers --- #
def log_message(message: str):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}\n")
    except Exception:
        print("(Logging skipped)")

def blink_alert():
    try:
        for _ in range(2):  # shorter for CI
            print("*", end=" ", flush=True)
            sleep(0.2)
    except Exception:
        print("*ALERT*")

def notify(message: str, critical: bool = False):
    print(message)
    log_message(("ALERT: " if critical else "WARNING: ") + message)
    if critical:
        blink_alert()

# --- Vital checking --- #
def check_vital(name: str, value: float) -> bool:
    vrange = VITALS[name]["range"]

    # warnings
    for msg, cond in VITALS[name]["warnings"]:
        if cond(value, vrange):
            notify(f"Warning: {msg}")

    # critical
    if not (vrange[0] <= value <= vrange[1]):
        notify(f"{name.capitalize()} critical!", critical=True)
        return False
    return True

def vitals_ok(temperature: float, pulse: int, spo2: int) -> bool:
    return all([
        check_vital("temperature", temperature),
        check_vital("pulse", pulse),
        check_vital("spo2", spo2),
    ])

# --- Example test --- #
if __name__ == "__main__":
    vitals_ok(95.2, 97, 91)   # warnings only
    vitals_ok(94.5, 55, 88)   # critical alerts

