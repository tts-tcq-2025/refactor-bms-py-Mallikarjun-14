import sys
from time import sleep
from typing import Callable, List, Tuple
from datetime import datetime
import os

LOG_FILE = os.path.join(os.getcwd(), "vitals_log.txt")

# --- Configurable ranges and warning thresholds --- #
VITAL_RANGES = {
    "temperature": {"ok": (95, 102), "warn": (1.53, "Temperature")},
    "pulse": {"ok": (60, 100), "warn": (5, "Pulse Rate")},
    "spo2": {"ok": (90, float("inf")), "warn": (2, "Oxygen Saturation")},
}

# --- Logging helper (safe) --- #
def log_message(message: str):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}\n")
    except Exception as e:
        print(f"(Logging failed: {e})")

# --- Alert functions (safe in CI) --- #
def blink_alert(duration: int = 6):
    try:
        for _ in range(duration):
            print('\r* ', end='')
            sys.stdout.flush()
            sleep(1)
            print('\r *', end='')
            sys.stdout.flush()
            sleep(1)
    except Exception:
        print("*ALERT BLINKING* (skipped)")

def print_alert(message: str):
    print(message)
    log_message("ALERT: " + message)
    blink_alert()

def print_warning(message: str):
    print(message)
    log_message("WARNING: " + message)

# --- Generic check functions --- #
def in_range(value: float, min_val: float, max_val: float) -> bool:
    return min_val <= value <= max_val

def check_vital(name: str, value: float) -> bool:
    ok_min, ok_max = VITAL_RANGES[name]["ok"]
    warn_range, label = VITAL_RANGES[name]["warn"]

    # Warning check
    if name == "temperature":
        if ok_min <= value < ok_min + warn_range:
            print_warning(f"Warning: Approaching hypothermia")
        elif ok_max - warn_range < value <= ok_max:
            print_warning(f"Warning: Approaching hyperthermia")
    elif name == "pulse":
        if ok_min <= value < ok_min + warn_range:
            print_warning(f"Warning: Low pulse approaching limit")
        elif ok_max - warn_range < value <= ok_max:
            print_warning(f"Warning: High pulse approaching limit")
    elif name == "spo2":
        if ok_min <= value < ok_min + warn_range:
            print_warning(f"Warning: Approaching hypoxemia (low oxygen)")

    # Critical check
    if not in_range(value, ok_min, ok_max):
        print_alert(f"{label} critical!")
        return False
    return True

# --- Main vital check --- #
def vitals_ok(temperature: float, pulse_rate: int, spo2: int) -> bool:
    return all([
        check_vital("temperature", temperature),
        check_vital("pulse", pulse_rate),
        check_vital("spo2", spo2),
    ])

# --- Example test --- #
if __name__ == "__main__":
    vitals_ok(95.2, 97, 91)   # Will show warnings
    vitals_ok(94.5, 55, 88)   # Will trigger critical alerts

