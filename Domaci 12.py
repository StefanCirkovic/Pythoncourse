
import psutil


memory_info = psutil.virtual_memory()

memory_bytes = memory_info.total
memory_gigabytes = memory_bytes / (1024**3)

print(f"{memory_gigabytes: .2f}GB")


cpu_usage = psutil.cpu_percent(interval=1)
cores = psutil.cpu_count(logical=False)
logical_cores = psutil.cpu_count(logical=True)

current_process = psutil.Process()
num_threads = current_process.num_threads()


print(f"Total CPU Usage: {cpu_usage}%")
print(f"Total physical cores: {cores}")
print(f"Total logical cores: {logical_cores}")
print(f"Currently used logical cores: {num_threads}")

