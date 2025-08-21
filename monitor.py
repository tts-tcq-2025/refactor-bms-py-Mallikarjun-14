# --- Warning condition functions --- #
def temp_low_warning(v): return 95 <= v < 96.5
def temp_high_warning(v): return 100.5 < v <= 102

def pulse_low_warning(v): return 60 <= v < 65
def pulse_high_warning(v): return 95 < v <= 100

def spo2_low_warning(v): return 90 <= v < 92

# --- Notification --- #
def notify(msg, critical=False):
    print(f"{'ALERT' if critical else 'Warning'}: {msg}")

# --- Flat vital check --- #
def check_all_vitals(temp, pulse, spo2):
    ok = True

    # Temperature
    if temp_low_warning(temp):
        notify("Approaching hypothermia")
    if temp_high_warning(temp):
        notify("Approaching hyperthermia")
    if not (95 <= temp <= 102):
        notify("Temperature critical!", critical=True)
        ok = False

    # Pulse
    if pulse_low_warning(pulse):
        notify("Low pulse approaching limit")
    if pulse_high_warning(pulse):
        notify("High pulse approaching limit")
    if not (60 <= pulse <= 100):
        notify("Pulse rate critical!", critical=True)
        ok = False

    # SpO2
    if spo2_low_warning(spo2):
        notify("Approaching hypoxemia (low oxygen)")
    if spo2 < 90:
        notify("Oxygen saturation critical!", critical=True)
        ok = False

    return ok

# --- Example usage --- #
if __name__ == "__main__":
    check_all_vitals(95.2, 97, 91)   # warnings
    check_all_vitals(94.5, 55, 88)   # alerts
ts
