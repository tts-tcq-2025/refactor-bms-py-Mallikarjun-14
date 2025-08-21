# --- Notification --- #
def notify(msg, critical=False):
    print(f"{'ALERT' if critical else 'Warning'}: {msg}")

# --- Temperature checks --- #
def check_temp1(v): 
    if 95 <= v < 96.5: notify("Approaching hypothermia")
def check_temp2(v): 
    if 100.5 < v <= 102: notify("Approaching hyperthermia")
def check_temp_critical(v): 
    if v < 95 or v > 102: notify("Temperature critical!", critical=True)

# --- Pulse checks --- #
def check_pulse1(v): 
    if 60 <= v < 65: notify("Low pulse approaching limit")
def check_pulse2(v): 
    if 95 < v <= 100: notify("High pulse approaching limit")
def check_pulse_critical(v): 
    if v < 60 or v > 100: notify("Pulse rate critical!", critical=True)

# --- SpO2 checks --- #
def check_spo21(v): 
    if 90 <= v < 92: notify("Approaching hypoxemia (low oxygen)")
def check_spo2_critical(v): 
    if v < 90: notify("Oxygen saturation critical!", critical=True)

# --- Run checks --- #
if __name__ == "__main__":
    # Patient 1
    t, p, s = 95.2, 97, 91
    check_temp1(t)
    check_temp2(t)
    check_temp_critical(t)
    check_pulse1(p)
    check_pulse2(p)
    check_pulse_critical(p)
    check_spo21(s)
    check_spo2_critical(s)

    # Patient 2
    t, p, s = 94.5, 55, 88
    check_temp1(t)
    check_temp2(t)
    check_temp_critical(t)
    check_pulse1(p)
    check_pulse2(p)
    check_pulse_critical(p)
    check_spo21(s)
    check_spo2_critical(s)
(spo2_val)
