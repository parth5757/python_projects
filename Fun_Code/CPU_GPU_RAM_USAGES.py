#!/usr/bin/env python3
import os
import subprocess
from shutil import which
import psutil

# -------- CPU + RAM --------
def get_cpu_ram():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    return cpu, ram

# -------- CPU temperature (Windows WMI best-effort) --------
def get_cpu_temp_c():
    # Many Windows systems don’t expose CPU temp via standard WMI; return None if unavailable.
    if os.name != "nt":
        return None
    try:
        import wmi  # pip install wmi
    except Exception:
        return None
    # Try ACPI thermal zone (Kelvin*10). Often maps to motherboard/zone, not per-core.
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temps = w.MSAcpi_ThermalZoneTemperature()
        vals = []
        for t in temps:
            # CurrentTemperature is tenths of Kelvin
            c = (t.CurrentTemperature / 10.0) - 273.15
            # Filter unreasonable readings
            if 0.0 < c < 120.0:
                vals.append(c)
        if vals:
            # Use median-ish: average of valid zones
            return sum(vals) / len(vals)
    except Exception:
        pass
    # If nothing exposed, return None
    return None

# -------- NVIDIA GPU via NVML --------
def get_nvidia_gpus_nvml():
    gpus = []
    try:
        import pynvml  # pip install pynvml
        # Try explicit dll path on Windows if needed
        if os.name == "nt":
            dll = r"C:\Windows\System32\nvml.dll"
            try:
                if os.path.exists(dll):
                    pynvml.nvmlInitFromDriver(dll)
                else:
                    pynvml.nvmlInit()
            except Exception:
                pynvml.nvmlInit()
        else:
            pynvml.nvmlInit()

        try:
            count = pynvml.nvmlDeviceGetCount()
            for i in range(count):
                h = pynvml.nvmlDeviceGetHandleByIndex(i)
                util = float(pynvml.nvmlDeviceGetUtilizationRates(h).gpu)
                mem = pynvml.nvmlDeviceGetMemoryInfo(h)
                mem_pct = (mem.used / mem.total) * 100.0 if mem.total else 0.0
                temp = float(pynvml.nvmlDeviceGetTemperature(
                    h, pynvml.NVML_TEMPERATURE_GPU
                ))
                gpus.append((i, util, mem_pct, temp))
        finally:
            try:
                pynvml.nvmlShutdown()
            except Exception:
                pass
        return gpus
    except Exception:
        return None

# -------- NVIDIA GPU via nvidia-smi fallback --------
def get_nvidia_gpus_smi():
    exe = "nvidia-smi"
    if which(exe) is None:
        if os.name == "nt":
            win_path = r"C:\Windows\System32\nvidia-smi.exe"
            if os.path.exists(win_path):
                exe = win_path
            else:
                return None
        else:
            return None
    fmt = "--format=csv,noheader,nounits"
    query = "--query-gpu=index,utilization.gpu,memory.used,memory.total,temperature.gpu"
    try:
        out = subprocess.check_output([exe, query, fmt], stderr=subprocess.STDOUT, text=True)
        gpus = []
        for line in out.strip().splitlines():
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 5:
                continue
            idx = int(parts[0])
            util = float(parts[1])
            mem_used = float(parts[2])
            mem_total = float(parts[3])
            mem_pct = (mem_used / mem_total) * 100.0 if mem_total else 0.0
            temp = float(parts[4])
            gpus.append((idx, util, mem_pct, temp))
        return gpus if gpus else None
    except Exception:
        return None
    
def get_cpu_temp_librehw():
    if os.name != "nt":
        return None
    try:
        import wmi  # pip install wmi
        w = wmi.WMI(namespace=r"root\LibreHardwareMonitor")
        # Prefer CPU Package; fallback to average of cores
        pk = w.query('SELECT Value FROM Sensor WHERE SensorType="Temperature" AND Name LIKE "%CPU Package%"')
        if pk and pk[0].Value is not None:
            return float(pk[0].Value)
        cores = w.query('SELECT Value FROM Sensor WHERE SensorType="Temperature" AND Name LIKE "%CPU Core%"')
        vals = [float(x.Value) for x in cores if x.Value is not None]
        return sum(vals)/len(vals) if vals else None
    except Exception:
        return None


def main():
    cpu, ram = get_cpu_ram()
    # Try LibreHardwareMonitor WMI first, then ACPI as fallback
    cpu_temp = get_cpu_temp_librehw()
    if cpu_temp is None:
        cpu_temp = get_cpu_temp_c()

    if cpu_temp is not None:
        print(f"CPU: {cpu:.1f}% | RAM: {ram:.1f}% | CPU Temp: {cpu_temp:.1f}°C")
    else:
        print(f"CPU: {cpu:.1f}% | RAM: {ram:.1f}% | CPU Temp: N/A")

    gpus = get_nvidia_gpus_nvml()
    if gpus is None:
        gpus = get_nvidia_gpus_smi()

    if gpus:
        for gid, util, mem_pct, temp in gpus:
            print(f"GPU{gid}: {util:.1f}% | GPU{gid} MEM: {mem_pct:.1f}% | GPU{gid} Temp: {temp:.0f}°C")
    else:
        print("GPU: N/A (no access via NVML/nvidia-smi)")

if __name__ == "__main__":
    main()
