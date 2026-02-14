from rtlsdr import RtlSdr
import numpy as np
import time

CENTER_FREQ = 125e6
SAMPLE_RATE = 2.4e6
GAIN = 40
THRESHOLD = 0.01

DOT_THRESHOLD = 0.3     # debajo de esto es punto
LETTER_GAP = 0.6        # silencio que indica nueva letra

MORSE_DICT = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
    ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
}

sdr = RtlSdr()
sdr.sample_rate = SAMPLE_RATE
sdr.center_freq = CENTER_FREQ
sdr.gain = GAIN

def measure_power():
    samples = sdr.read_samples(256*1024)
    return np.mean(np.abs(samples))

print("Escuchando...")

current_symbol = ""
last_state = 0
signal_start = None
silence_start = None

while True:
    power = measure_power()
    state = 1 if power > THRESHOLD else 0

    now = time.time()

    if state == 1 and last_state == 0:
        signal_start = now

    if state == 0 and last_state == 1:
        duration = now - signal_start

        if duration < DOT_THRESHOLD:
            current_symbol += "."
            print(".", end="", flush=True)
        else:
            current_symbol += "-"
            print("_", end="", flush=True)

        silence_start = now

    if state == 0 and silence_start:
        if now - silence_start > LETTER_GAP and current_symbol:
            letter = MORSE_DICT.get(current_symbol, "?")
            print(" ->", letter)
            current_symbol = ""
            silence_start = None

    last_state = state
