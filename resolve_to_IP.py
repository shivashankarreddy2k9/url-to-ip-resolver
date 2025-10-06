import csv
import socket
import re
from urllib.parse import urlparse
from datetime import datetime
import os
import time

# ---------- Configuration ----------
csv_path = os.path.join(os.getcwd(), "urls.csv")
now = datetime.now()
output_csv = os.path.join(os.getcwd(), f"Public_IPs_results-{now.strftime('%Y%m%d')}.csv")


def clean_url(value):
    """Remove http/https, everything after first slash, and strip port for hostnames."""
    value = value.strip()
    # Remove http:// or https://
    value = re.sub(r'^https?://', '', value, flags=re.IGNORECASE)
    # Remove everything after first slash
    value = value.split('/')[0]

    # Check for port (":xxxx") in hostname
    if ':' in value:
        host_part, port_part = value.split(':', 1)
        ip_pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
        if re.match(ip_pattern, host_part):
            # IP with port, keep as-is
            return value
        else:
            # Hostname with port, remove port
            value = host_part
    return value


def resolve_to_ip(value):
    """Resolve hostname to IP or return IP if already an IP with optional port."""
    ip_with_port_pattern = r'^\d{1,3}(\.\d{1,3}){3}(:\d+)?$'
    if re.match(ip_with_port_pattern, value):
        # IP (with or without port), return as-is
        return value
    try:
        hostname = clean_url(value)
        infos = socket.getaddrinfo(hostname, None)
        ips = sorted({info[4][0] for info in infos})
        return '-'.join(ips)
    except Exception:
        return "N/A"


start_time = time.time()

# ---------- Load CSV ----------
with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

total_urls = len(rows)
print(f"Total URLs in CSV: {total_urls}\n")

# ---------- Save Output ----------
with open(output_csv, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar='\\')
    writer.writerow(["Original_Value", "Resolved_IP"])  # header row
    
    for idx, row in enumerate(rows, start=1):
        if not row or not row[0].strip():
            writer.writerow([])  # blank line
            print(f"{idx}/{total_urls}: Empty row - skipped")
            continue

        original_value = row[0].strip()
        cleaned_value = clean_url(original_value)
        resolved_ip = resolve_to_ip(cleaned_value)
        writer.writerow([cleaned_value, resolved_ip])
        print(f"{idx}/{total_urls}: {cleaned_value} -> {resolved_ip}")

# ---------- End Timer ----------
end_time = time.time()
elapsed_seconds = end_time - start_time
minutes, seconds = divmod(elapsed_seconds, 60)

print(f"\nDone. Results saved to: {output_csv}")
print(f"Total execution time: {int(minutes)} min {int(seconds)} sec")
input("Press Enter to exit...")
