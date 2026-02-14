# PoC_paLANTENNA

**Proof of Concept -- Ethernet Cable Electromagnetic Emission
Transmission**\
Inspired by LANtenna research\ https://arxiv.org/pdf/2110.00104 (Mordechai Guri,Ben-Gurion - University of the Negev, Israel)
Author: Jeremías Palazzesi

------------------------------------------------------------------------

## Overview

**PoC_paLANTENNA** is an experimental proof of concept demonstrating how
an Ethernet cable can unintentionally act as an electromagnetic
radiator, enabling low-bitrate data transmission through controlled
network activity.

This project recreates, in a simplified and educational manner, the
concept of transmitting information by deliberately modulating Ethernet
traffic and detecting the resulting RF emissions using an RTL-SDR
receiver.

This project is intended strictly for educational and laboratory
research purposes in controlled environments.

------------------------------------------------------------------------

## Concept

The system works by:

-   Generating controlled UDP traffic bursts\
-   Using Ethernet cable electrical activity to produce measurable EM
    emissions\
-   Capturing those emissions with an RTL-SDR\
-   Detecting signal presence via power thresholding\
-   Encoding and decoding Morse code (`.` and `_`) using OOK (On-Off
    Keying)

This is not a practical exfiltration method, but a side-channel research
experiment.

------------------------------------------------------------------------

## Architecture

    [ Transmitter PC ]
            |
            |  UDP burst modulation
            v
      Ethernet Cable (UTP)
            |
            |  Electromagnetic emission
            v
    [ RTL-SDR + Linux Receiver ]
            |
            |  Power detection
            v
     Morse decoding (real-time)

------------------------------------------------------------------------

## Components

### 1. Transmitter

File: `tx_morse_lan.py`

-   Sends Morse symbols using UDP traffic bursts\
-   `.` → short burst\
-   `_` → long burst\
-   Silence → symbol separation

Usage:

    python tx_morse_lan.py ...___...

Works on:

-   Windows\
-   Linux\
-   Any OS with Python 3

------------------------------------------------------------------------

### 2. Receiver

File: `rx_morse_lan.py`

-   Uses RTL-SDR to monitor a fixed frequency\
-   Measures average RF power\
-   Detects signal presence\
-   Classifies dot or dash based on duration\
-   Decodes Morse to ASCII in real time

------------------------------------------------------------------------

## Requirements

### Hardware

-   2 computers (TX + RX)\
-   Ethernet UTP cable (preferably unshielded)\
-   RTL-SDR (e.g., RTL-SDR Blog V4)\
-   Basic VHF antenna

### Software (Receiver -- Ubuntu)

    sudo apt install rtl-sdr python3-numpy
    pip install pyrtlsdr

Verify RTL-SDR:

    rtl_test

------------------------------------------------------------------------

## Initial Setup

### 1. Find a Suitable Frequency

1.  Open GQRX (or similar spectrum viewer)\
2.  Sweep between 50--300 MHz\
3.  Run the transmitter\
4.  Look for a signal spike that appears only during transmission\
5.  Adjust `CENTER_FREQ` in the receiver script

------------------------------------------------------------------------

### 2. Tune Critical Parameters

Receiver:

-   `CENTER_FREQ`\
-   `GAIN`\
-   `THRESHOLD`\
-   `DOT_THRESHOLD`\
-   `LETTER_GAP`

Transmitter:

-   `DOT_DURATION`\
-   `DASH_DURATION`\
-   `SYMBOL_GAP`

Fine tuning is required for each environment.

------------------------------------------------------------------------

## Lab Recommendations

-   Use unshielded UTP cable (avoid STP)\
-   Longer cables radiate more effectively\
-   Try forcing NIC speed to 100 Mbps\
-   Place RTL-SDR 20--50 cm from cable initially\
-   Minimize nearby RF interference

------------------------------------------------------------------------

## Limitations

-   Extremely low bitrate\
-   Highly sensitive to noise\
-   Requires manual calibration\
-   Proof-of-concept only\
-   Not suitable for real-world data transfer

------------------------------------------------------------------------

## Ethical Notice

This repository is intended for:

-   Academic study\
-   RF side-channel experimentation\
-   Controlled laboratory environments

Do not use this technique against systems without explicit
authorization.

The author assumes no responsibility for misuse.

------------------------------------------------------------------------

## Research Background

This project is inspired by academic research on Ethernet
electromagnetic side channels and air-gapped data exfiltration
techniques.

It recreates the concept in a simplified and educational form.

------------------------------------------------------------------------

## License

MIT License
