# --- Notification --- #
def notify(msg, critical=False):
    print(f"{'ALERT' if critical else 'Warning'}: {msg}")

# --- Temperature checks --- #
def check_temp_low(temp):
    if 95 <= temp < 96.5:
        notify("Approaching hypothermia")
        return True
    return False

def check_temp_high(temp):
    if 100.5 < temp <= 102:
        notify("Approaching hyperthermia")
        return True
    return False

def check_temp_critical(temp):
    if temp < 95 or temp > 102:
        notify("Temperature critical!", critical=True)
        return False
    return True

# --- Pulse checks --- #
def check_pulse_low(pulse):
    if 60 <= pulse < 65:
        notify("Low pulse approaching limit")
        return True
    return False

def check_pulse_high(pulse):
    if 95 < pulse <= 100:
        notify("High pulse approaching limit")
        return True
    return False

def check_pulse_critical(pulse):
    if pulse < 60 or pulse > 100:
        notify("Pulse rate critical!", critical=True)
        return False
    return True

# --- SpO2 checks --- #
def check_spo2_low(spo2):
    if 90 <= spo2 < 92:
        notify("Approaching hypoxemia (low oxygen)")
        return True
    return False

def check_spo2_critical(spo2):
    if spo2 < 90:
        notify("Oxygen saturation critical!", critical=True)
        return False
    return True

# --- Aggregate check --- #
def check_all_vitals(temp, pulse, spo2):
    ok = True
    ok &= check_temp_low(temp)
    ok &= check_temp_high(temp)
    ok &= check_temp_critical(temp)
    ok &= check_pulse_low(pulse)
    ok &= check_pulse_high(pulse)
    ok &= check_pulse_critical(pulse)
    ok &= check_spo2_low(spo2)
    ok &= check_spo2_critical(spo2)
    return ok

# --- Example usage --- #
if __name__ == "__main__":
    check_all_vitals(95.2, 97, 91)   # warnings
    check_all_vitals(94.5, 55, 88)   # alerts
