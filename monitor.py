
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

# --- Mapping vital checkers to messages --- #
VitalCheck = Tuple[Callable[[], bool], str]

def vitals_ok(temperature: float, pulse_rate: int, spo2: int) -> bool:
    checks: List[VitalCheck] = [
        (lambda: is_temperature_ok(temperature), "Temperature critical!"),
        (lambda: is_pulse_ok(pulse_rate), "Pulse Rate is out of range!"),
        (lambda: is_spo2_ok(spo2), "Oxygen Saturation out of range!")
    ]
    
    for check_func, error_msg in checks:
        if not check_func():
            print_alert(error_msg)
            return False
    return True
