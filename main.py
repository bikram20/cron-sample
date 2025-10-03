# cron_job.py
import subprocess
import datetime

def run_job():
    # Example: fetch current UTC time from worldtimeapi.org
    url = "http://worldtimeapi.org/api/timezone/Etc/UTC"

    try:
        # Run curl command
        result = subprocess.run(
            ["curl", "-s", url],
            capture_output=True,
            text=True,
            check=True
        )
        response = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        response = f"Error fetching data: {e}"

    # Print log output
    print("=== Cron Job Triggered ===")
    print("Timestamp:", datetime.datetime.utcnow().isoformat())
    print("API Response:", response)
    print("==========================")

if __name__ == "__main__":
    run_job()