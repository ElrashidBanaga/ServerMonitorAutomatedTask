
#!/usr/bin/env python3

import os
import socket
import platform
import getpass
import datetime
import psutil


# --------------------------------
# Collect Server Information
# --------------------------------

# Hostname
hostname = socket.gethostname()

# Current logged-in user
current_user = getpass.getuser()

# Date and time
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Operating System
operating_system = platform.platform()

# Kernel version
kernel_version = platform.release()

# CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)

# Memory Usage
memory = psutil.virtual_memory()

total_ram = memory.total / (1024 ** 3)
used_ram = memory.used / (1024 ** 3)
free_ram = memory.available / (1024 ** 3)
memory_usage = memory.percent

# Disk Usage
disk = psutil.disk_usage("/")

used_disk = disk.used / (1024 ** 3)
free_disk = disk.free / (1024 ** 3)
disk_usage = disk.percent

# IP Address
ip_address = socket.gethostbyname(hostname)

# System Uptime
uptime_seconds = int(datetime.datetime.now().timestamp() - psutil.boot_time())

days = uptime_seconds // 86400
hours = (uptime_seconds % 86400) // 3600
minutes = (uptime_seconds % 3600) // 60

uptime = f"{days} days, {hours} hours, {minutes} minutes"


# --------------------------------
# Display Information
# --------------------------------

print("\n" + "=" * 50)
print("SERVER HEALTH REPORT")
print("=" * 50)

print(f"Hostname       : {hostname}")
print(f"Current User   : {current_user}")
print(f"Date           : {current_datetime}")
print(f"Operating System: {operating_system}")
print(f"Kernel         : {kernel_version}")
print(f"CPU Usage      : {cpu_usage}%")

print("\nMemory Usage")
print(f"Total          : {total_ram:.2f} GB")
print(f"Used           : {used_ram:.2f} GB")
print(f"Free           : {free_ram:.2f} GB")
print(f"Usage          : {memory_usage}%")

print("\nDisk Usage")
print("Filesystem     : /")
print(f"Used           : {used_disk:.2f} GB")
print(f"Available      : {free_disk:.2f} GB")
print(f"Usage          : {disk_usage}%")

print(f"\nIP Address     : {ip_address}")
print(f"System Uptime  : {uptime}")

print("=" * 50)


# --------------------------------
# Generate Report File
# --------------------------------

report = f"""# SERVER HEALTH REPORT

Hostname: {hostname}
Current User: {current_user}
Date: {current_datetime}
Operating System: {operating_system}
Kernel: {kernel_version}
CPU Usage: {cpu_usage}%

Memory Usage:
Total: {total_ram:.2f} GB
Used: {used_ram:.2f} GB
Free: {free_ram:.2f} GB
Usage: {memory_usage}%

Disk Usage:
Filesystem: /
Used: {used_disk:.2f} GB
Available: {free_disk:.2f} GB
Usage: {disk_usage}%

IP Address: {ip_address}

System Uptime: {uptime}
"""

# Create report filename based on date
report_date = datetime.datetime.now().strftime("%Y-%m-%d")
report_file = f"reports/server-health-{report_date}.txt"

# Write report to file
with open(report_file, "w") as file:
    file.write(report)

print(f"\nReport saved to: {report_file}")


