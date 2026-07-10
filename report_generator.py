from datetime import datetime

def generate_report(total, unknown, blacklisted):

    report_file = "reports/final_report.txt"

    with open(report_file, "w") as file:

        file.write("=" * 60 + "\n")
        file.write("WINDOWS SERVICE & PROCESS MONITOR REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Scan Date : {datetime.now()}\n\n")

        file.write(f"Total Processes Scanned : {total}\n")
        file.write(f"Unknown Processes       : {unknown}\n")
        file.write(f"Blacklisted Processes   : {blacklisted}\n\n")

        if blacklisted > 0:
            status = "THREAT DETECTED"
        elif unknown > 0:
            status = "REVIEW RECOMMENDED"
        else:
            status = "SYSTEM HEALTHY"

        file.write(f"Overall Status : {status}\n\n")

        file.write("=" * 60 + "\n")

    print(f"\n📄 Report saved successfully at: {report_file}")