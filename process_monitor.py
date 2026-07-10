import psutil

print("=" * 90)
print("WINDOWS PARENT-CHILD PROCESS MONITOR")
print("=" * 90)

for process in psutil.process_iter(['pid', 'ppid', 'name']):
    try:
        pid = process.info['pid']
        ppid = process.info['ppid']
        name = process.info['name']

        parent_name = "Unknown"

        if ppid != 0:
            try:
                parent = psutil.Process(ppid)
                parent_name = parent.name()
            except:
                parent_name = "Not Found"

        print(f"Parent : {parent_name}")
        print(f"Child  : {name}")
        print(f"PID    : {pid}")
        print(f"PPID   : {ppid}")
        print("-" * 90)

    except (psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess):
        pass