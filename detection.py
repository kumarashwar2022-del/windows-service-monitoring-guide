from report_generator import generate_report
from logger import write_log
import psutil

# Read whitelist
with open("whitelist.txt", "r") as file:
    whitelist = [line.strip().lower() for line in file]

# Read blacklist
with open("blacklist.txt", "r") as file:
    blacklist = [line.strip().lower() for line in file]

print("=" * 90)
print("UNAUTHORIZED PROCESS DETECTION")
print("=" * 90)

total_processes = 0
unknown_processes = 0
blacklisted_processes = 0

for process in psutil.process_iter(['pid', 'name']):
    total_processes += 1
    try:
        name = process.info['name']

        if not name:
            continue

        name = name.lower()

        if name in blacklist:
            blacklisted_processes += 1
            print(f"🚨 HIGH ALERT : {name} (Blacklisted Process)")
            print(f"PID : {process.info['pid']}")
            print("-" * 90)

            write_log("HIGH", name, process.info['pid'], "Blacklisted Process")

        elif name not in whitelist:
            unknown_processes += 1
            print(f"⚠️ UNKNOWN PROCESS : {name}")
            print(f"PID : {process.info['pid']}")
            print("-" * 90)

            write_log("HIGH", name, process.info['pid'], "Blacklisted Process")

    except (psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess):
        pass

    print("\n" + "=" * 60)
print("WINDOWS MONITORING SUMMARY")
print("=" * 60)

print(f"Total Processes Scanned : {total_processes}")
print(f"Unknown Processes       : {unknown_processes}")
print(f"Blacklisted Processes   : {blacklisted_processes}")

if blacklisted_processes > 0:
    print("\n🚨 Overall Status : THREAT DETECTED")
elif unknown_processes > 0:
    print("\n⚠️ Overall Status : REVIEW RECOMMENDED")
else:
    print("\n✅ Overall Status : SYSTEM HEALTHY")

print("=" * 60)

generate_report(
    total_processes,
    unknown_processes,
    blacklisted_processes
)