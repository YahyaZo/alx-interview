#!/usr/bin/python3
"""
Module for log parsing script.
Reads from stdin and computes metrics.
"""


import sys
import signal
import re



# Initialize counters and accumulators
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


# Regular expression to match the log line format
log_pattern = re.compile(
    r'^\d+\.\d+\.\d+\.\d+ - \[.+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')




def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")



def signal_handler(sig, frame):
    """Handles the keyboard interruption signal."""
    print_stats()
    sys.exit(0)



# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0
except Exception as e:
    sys.stderr.write(f"Error: {str(e)}\n")


# Print remaining statistics at the end
print_stats()
