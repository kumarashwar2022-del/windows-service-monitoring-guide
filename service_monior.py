import wmi

c = wmi.WMI()

print("=" * 110)
print("WINDOWS STARTUP SERVICE AUDIT")
print("=" * 110)

for service in c.Win32_Service():

    path = service.PathName if service.PathName else "Unknown"

    print(f"Service Name : {service.Name}")
    print(f"Display Name : {service.DisplayName}")
    print(f"Status       : {service.State}")
    print(f"Startup Type : {service.StartMode}")
    print(f"Executable   : {path}")

    # -------- Suspicious Path Detection --------

    suspicious = False

    lower_path = path.lower()

    if "temp" in lower_path:
        suspicious = True

    elif "appdata" in lower_path:
        suspicious = True

    elif "\\users\\" in lower_path:
        suspicious = True

    if suspicious:

        print("🚨 ALERT : Suspicious Service Path Detected")

    else:

        print("✅ Path Looks Safe")

    print("-" * 110)