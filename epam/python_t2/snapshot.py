import psutil
import json
import time
import os
import argparse


class SystemMonitor:
    def __init__(self, interval, filename, count):
        self.interval = interval
        self.filename = filename
        self.count = count

    def get_snapshot(self):
        # Tasks / processes
        statuses = {"total": 0, "running": 0, "sleeping": 0, "stopped": 0, "zombie": 0}
        for proc in psutil.process_iter(["status"]):
            try:
                status = proc.info["status"]
                statuses["total"] += 1
                if status == psutil.STATUS_RUNNING:
                    statuses["running"] += 1
                elif status == psutil.STATUS_SLEEPING or status == psutil.STATUS_IDLE:
                    statuses["sleeping"] += 1
                elif status == psutil.STATUS_STOPPED:
                    statuses["stopped"] += 1
                elif status == psutil.STATUS_ZOMBIE:
                    statuses["zombie"] += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        # CPU
        cpu = psutil.cpu_times_percent(interval=None)

        # Memory (bytes → KiB)
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()

        snapshot = {
            "Tasks": statuses,
            "%CPU": {
                "user": cpu.user,
                "system": cpu.system,
                "idle": cpu.idle,
            },
            "KiB Mem": {
                "total": mem.total // 1024,
                "free": mem.available // 1024,
                "used": mem.used // 1024,
            },
            "KiB Swap": {
                "total": swap.total // 1024,
                "free": swap.free // 1024,
                "used": swap.used // 1024,
            },
            "Timestamp": int(time.time()),
        }
        return snapshot

    def clear_file(self):
        with open(self.filename, "w") as f:
            f.write("")  # opens in write mode → clears the file

    def write_snapshot(self, snapshot):
        with open(self.filename, "a") as f:
            f.write(json.dumps(snapshot, indent=2))
            f.write("\n")

    def run(self):
        self.clear_file()
        for i in range(self.count):
            snapshot = self.get_snapshot()

            # Print to console
            os.system("clear")
            print(json.dumps(snapshot, indent=2), end="\r")

            # Write to file
            self.write_snapshot(snapshot)

            # Wait (skip sleep after the last snapshot)
            if i < self.count - 1:
                time.sleep(self.interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System monitor")
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshots to output", type=int, default=20)
    args = parser.parse_args()

    monitor = SystemMonitor(interval=args.i, filename=args.f, count=args.n)
    monitor.run()