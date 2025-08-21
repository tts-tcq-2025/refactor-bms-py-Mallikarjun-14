import sys
import os
from time import sleep
from datetime import datetime
from typing import Dict, Callable, Tuple

LOG_FILE = os.path.join(os.getcwd(), "vitals_log.txt")

# --- Vital rules (data-driven, no duplication) --- #
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
        pass

def notify(msg: str, critical: bool = False):
    print(msg)
    log_message(("ALERT: " if critical else "WARNING: ") + msg)
    if critical:
        try:
            for _ in range(2):  # minimal blink for CI
                print("*", end="", flush=True)
                sleep(0.1)
        except Exception:
            print("*ALERT*")

# --- Generic vital checker --- #
def check_vital(name: str, valu_
