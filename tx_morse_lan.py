import socket
import time
import sys

TARGET_IP = "192.168.1.200"
TARGET_PORT = 9999

DOT_DURATION = 0.15
DASH_DURATION = 0.45
SYMBOL_GAP = 0.15
PACKET_SIZE = 1400

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = b"A" * PACKET_SIZE

def send_burst(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        sock.sendto(payload, (TARGET_IP, TARGET_PORT))

def send_symbol(symbol):
    if symbol == ".":
        send_burst(DOT_DURATION)
    elif symbol == "_":
        send_burst(DASH_DURATION)
    time.sleep(SYMBOL_GAP)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python tx_morse_lan.py ._._")
        sys.exit(1)

    message = sys.argv[1]
    print("Enviando Morse:", message)

    for symbol in message:
        if symbol in [".", "_"]:
            send_symbol(symbol)
        else:
            time.sleep(DASH_DURATION)  # pausa larga si hay otro caracter
