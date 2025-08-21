def notify(msg, critical=False):
    print(f"{'ALERT' if critical else 'Warning'}: {msg}")

# --- Patient 1 vitals --- #
t1, p1, s1 = 95.2, 97, 91

# Temperature checks
if 95 <= t1 < 96.5: notify("Approaching hypothermia")
if 100.5 < t1 <= 102: notify("Approaching hyperthermia")
if t1 < 95 or t1 > 102: notify("Temperature critical!", critical=True)

# Pulse checks
if 60 <= p1 < 65: notify("Low pulse approaching limit")
if 95 < p1 <= 100: notify("High pulse approaching limit")
if p1 < 60 or p1 > 100: notify("Pulse rate critical!", critical=True)

# SpO2 checks
if 90 <= s1 < 92: notify("Approaching hypoxemia (low oxygen)")
if s1 < 90: notify("Oxygen saturation critical!", critical=True)

# --- Patient 2 vitals --- #
t2, p2, s2 = 94.5, 55, 88

# Temperature checks
if 95 <= t2 < 96.5: notify("Approaching hypothermia")
if 100.5 < t2 <= 102: notify("Approaching hyperthermia")
if t2 < 95 or t2 > 102: notify("Temperature critical!", critical=True)

# Pulse checks
if 60 <= p2 < 65: notify("Low pulse approaching limit")
if 95 < p2 <= 100: notify("High pulse approaching limit")
if p2 < 60 or p2 > 100: notify("Pulse rate critical!", critical=True)

# SpO2 checks
if 90 <= s2 < 92: notify("Approaching hypoxemia (low oxygen)")
if s2 < 90: notify("Oxygen saturation critical!", critical=True)
