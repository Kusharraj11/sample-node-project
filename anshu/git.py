import argparse
import psutil
import sys

def get_vm_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    return cpu_usage, memory_usage, disk_usage

def analyze_health(cpu, memory, disk):
    # VM is healthy if ALL metrics are less than 60% utilized
    if cpu < 60 and memory < 60 and disk < 60:
        return "Healthy", None
    else:
        reasons = []
        if cpu >= 60:
            reasons.append(f"CPU usage is high: {cpu:.1f}%")
        if memory >= 60:
            reasons.append(f"Memory usage is high: {memory:.1f}%")
        if disk >= 60:
            reasons.append(f"Disk usage is high: {disk:.1f}%")
        return "Not Healthy", reasons

def main():
    parser = argparse.ArgumentParser(description="Analyze VM health based on CPU, memory, and disk usage.")
    parser.add_argument("--explain", action="store_true", help="Explain reason for health status")
    args = parser.parse_args()

    cpu, memory, disk = get_vm_metrics()
    status, reasons = analyze_health(cpu, memory, disk)

    print(f"VM Health Status: {status}")
    if args.explain:
        if status == "Healthy":
            print("All metrics are below 60% utilization. VM is healthy.")
        else:
            print("Reasons:")
            for reason in reasons:
                print(f"- {reason}")

if __name__ == "__main__":
    main()