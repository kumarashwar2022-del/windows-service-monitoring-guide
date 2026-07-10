from datetime import datetime


def write_log(severity, process, pid, reason):

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/detection_log.txt", "a") as file:

        file.write("=" * 60 + "\n")
        file.write(f"Date     : {time}\n")
        file.write(f"Severity : {severity}\n")
        file.write(f"Process  : {process}\n")
        file.write(f"PID      : {pid}\n")
        file.write(f"Reason   : {reason}\n")
        file.write("=" * 60 + "\n\n")