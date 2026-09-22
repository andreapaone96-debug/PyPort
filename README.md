# PyPort
A lightweight TCP port scanner built with Python.

# PyPort — Basic TCP Port Scanner

A lightweight TCP port scanner developed in Python as a personal cybersecurity learning project.

## Overview

PyPort performs TCP connection attempts across a predefined port range and reports which ports accept connections.

The project was developed to strengthen my understanding of TCP/IP networking, Python socket programming and exception handling.

## Features

* TCP port scanning using Python's `socket` library.
* Connection timeout and basic error handling.
* Detection of ports accepting TCP connections.
* Lookup of conventional service names.

## Usage

Requires Python 3. No third-party libraries are needed.

Configure the target and port range in `main.py`, then run:

`python main.py`

By default, the target is `127.0.0.1` (your own computer).

## Limitations

This is an educational TCP connect scanner, not a replacement for Nmap.

Service names are conventional port associations, not verified identification of running software.

Results may be incomplete due to timeouts, firewalls or network conditions.

## Security

Use this tool only on systems you own or have explicit authorization to test.
