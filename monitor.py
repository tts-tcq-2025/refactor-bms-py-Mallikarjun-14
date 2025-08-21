# --- Notification --- #
def notify(msg, critical=False):
    print(f"{'ALERT' if critical else 'Warning'}: {msg}")

# --- Vital check class --- #
class Vital:
    def __init__(self, name, warnings, critical_low=None, critical_high=None):
        self.name = name
        self.warnings = warnings        # list of tuples: (msg, condition_func)
        self.critical_low = critical_low
        self.critical_high = critical_high

    def check(self, value):
        for msg, cond in self.warnings:
            if cond(value):
                notify(msg)
        if (self.critical_low is not None and value < self.critical_low) or \
           (self.critical_high is not None and value > self.critical_high):
            notify(f"{self.name} critical!", critical=True)

# --- Define vitals --- #
temperature = Vital(
    "Temperature",
    warnings=[
        ("Approaching hypothermia", lambda v: 95 <= v < 96.5),
        ("Approaching hyperthermia", lambda v: 100.5 < v <= 102)
    ],
    critical_low=95,
    critical_high=102
)

pulse = Vital(
    "Pulse",
    warnings=[
        ("Low pulse approaching limit", lambda v: 60 <= v < 65),
        ("High pulse approaching limit", lambda v: 95 < v <= 100)
    ],
    critical_low=60,
    critical_high=100
)

spo2 = Vital(
    "Oxygen saturation",
    warnings=[
        ("Approaching hypoxemia (low oxygen)", lambda v: 90 <= v < 92)
    ],
    critical_low=90
)

# --- Check patients --- #
if __name__ == "__main__":
    patients = [
        (95.2, 97, 91),
        (94.5, 55, 88),
    ]

    for temp_val, pulse_val, spo2_val in patients:
        temperature.check(temp_val)
        pulse.check(pulse_val)
        spo2.check(spo2_val)
