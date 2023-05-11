#!/usr/bin/python3
import sys
import random
import datetime
import time

# Variables to track statistics
total_size = 0
status_counts = {}

# Function to print statistics
def print_statistics():
    print(f"File size: {total_size}")

    # Sort status codes in ascending order
    sorted_status_codes = sorted(status_counts.keys())

    # Print number of lines for each status code
    for status_code in sorted_status_codes:
        count = status_counts.get(status_code, 0)
        if count > 0:
            print(f"{status_code}: {count}")

# Read input from stdin
try:
    line_count = 0
    for i in range(10000):
        time.sleep(random.random())

        ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
        file_size = random.randint(1, 1024)

        line = f"{ip_address} - [{current_time}] \"GET /projects/260 HTTP/1.1\" {status_code} {file_size}"

        # Update statistics
        total_size += file_size
        status_counts[status_code] = status_counts.get(status_code, 0) + 1

        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

        # Write the line to stdout
        sys.stdout.write(line + '\n')
        sys.stdout.flush()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL+C)
    print_statistics()