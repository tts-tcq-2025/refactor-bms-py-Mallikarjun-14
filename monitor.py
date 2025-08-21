
import sys
from time import sleep
from typing import List, Tuple, Callable

# --- Pure functions for vital checks --- #
def is_temperature_ok(temp: float) -> bool:
    return 95 <= temp <= 102

def is_pulse_ok(pulse: int) -> bool:
    return 60 <= pulse <= 100

def is_spo2_ok(spo2: int) -> bool:
    return spo2 >= 90

# --- Early warning thresholds --- #
def is_temperature_warning(temp: float) -> str:
    if 95 <= temp < 95 + 1.53:
        return "Warning: Approaching hypothermia"
    if 102 - 1.53 < temp <= 102:
        return "Warning: Approaching hyperthermia"
    return ""

def is_pulse_warning(pulse: int) -> str:
    if 60 <= pulse < 65:
        return "Warning: Low pulse approaching limit"
    if 95 < pulse <= 100:
        return "Warning: High pulse approaching limit"
    return ""

def is_spo2_warning(spo2: int) -> str:
    if 90 <= spo2 < 92:
        return "Warning: Approaching hypoxemia (low oxygen)"
    return ""

# --- Alert functions (side effects separated) --- #
def blink_alert(duration: int = 6):
    for _ in range(duration):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def print_alert(message: str):
    print(message)
    blink_alert()

def print_warning(message: str):
    print(message)

# --- Mapping vital checkers to messages --- #
VitalCheck = Tuple[Callable[[], bool], str]

def vitals_ok(temperature: float, pulse_rate: int, spo2: int) -> bool:
    # --- Early Warnings --- #
    warnings: List[str] = [
        is_temperature_warning(temperature),
        is_pulse_warning(pulse_rate),
        is_spo2_warning(spo2),
    ]
    for w in warnings:
        if w:
            print_warning(w)

    # --- Critical Checks --- #
    checks: List[VitalCheck] = [
        (lambda: is_temperature_ok(temperature), "Temperature critical!"),
        (lambda: is_pulse_ok(pulse_rate), "Pulse Rate is out of range!"),
        (lambda: is_spo2_ok(spo2), "Oxygen Saturation out of range!"),
    ]

    for check_func, error_msg in checks:
        if not check_func():
            print_alert(error_msg)
            return False
    return True


# Example test
if __name__ == "__main__":
    vitals_ok(95.2, 97, 91)   # Will show warnings
    vitals_ok(94.5, 55, 88)   # Will trigger critical alerts

