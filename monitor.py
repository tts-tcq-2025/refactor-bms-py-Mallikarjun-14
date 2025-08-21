# --- Notification --- #
def notify(msg, critical=False):
    print(f"{'ALERT' if critical else 'Warning'}: {msg}")

# --- Temperature checks --- #
def check_temp_low(temp):
    if 95 <= temp < 96.5:
        notify("Approaching hypothermia")

def check_temp_high(temp):
    if 100.5 < temp <= 102:
        notify("Approaching hyperthermia")

def check_temp_critical(temp):
    if temp < 95 or temp > 102:
        notify("Temperature critical!", critical=True)

# --- Pulse checks --- #
def check_pulse_low(pulse):
    if 60 <= pulse < 65:
        notify("Low pulse approaching limit")

def check_pulse_high(pulse):
    if 95 < pulse <= 100:
        notify("High pulse approaching limit")

def check_pulse_critical(pulse):
    if pulse < 60 or pulse > 100:
        notify("Pulse rate critical!", critical=True)

# --- SpO2 checks --- #
def check_spo2_low(spo2):
    if 90 <= spo2 < 92:
        notify("Approaching hypoxemia (low oxygen)")

def check_spo2_critical(spo2):
    if spo2 < 90:
        notify("Oxygen saturation critical!", critical=True)

# --- Example usage --- #
if __name__ == "__main__":
    # First patient
    temp, pulse, spo2 = 95.2, 97, 91
    check_temp_low(temp)
    check_temp_high(temp)
    check_temp_critical(temp)
    check_pulse_low(pulse)
    check_pulse_high(pulse)
    check_pulse_critical(pulse)
    check_spo2_low(spo2)
    check_spo2_critical(spo2)

    # Second patient
    temp, pulse, spo2 = 94.5, 55, 88
    check_temp_low(temp)
    check_temp_high(temp)
    check_temp_critical(temp)
    check_pulse_low(pulse)
    check_pulse_high(pulse)
    check_pulse_critical(pulse)
    check_spo2_low(spo2)
    check_spo2_critical(spo2)

