import time #to check system time and date
import psutil #utility to scan specified systems stats

from rich.console import Console
from rich.table import Table
from rich.live import Live


console = Console()

def get_system_info():
    
    #cpu stats
    cpu_usage = psutil.cpu_percent(interval=0.5)
    
    #memory stats
    memory = psutil.virtual_memory()
    mem_total = memory.total / (1024 ** 3) # Convert to GB
    mem_used = memory.used / (1024 ** 3) 
    mem_free = memory.free / (1024 ** 3)
    
    mem_percentage = memory.percent
    
    #disk stats
    disk = psutil.disk_usage('/')
    disk_total = disk.total / (1024 ** 3) # Convert to GB
    disk_used = disk.used / (1024 ** 3)
    disk_free = disk.free / (1024 ** 3)
    
    disk_percentage = disk.percent
    
    #network stats
    net = psutil.net_io_counters()
    bytes_sent = net.bytes_sent / (1024 ** 2)  # Convert to MB
    bytes_recv = net.bytes_recv / (1024 ** 2)  # Convert to MB
    
    return {
        "CPU Usage": f"{cpu_usage}%",
        "Memory": f"{mem_used:.2f} / {mem_total:.2f} GB ({mem_percentage}%)",
        "Disk": f"{disk_used:.2f} / {disk_total:.2f} GB ({disk_percentage}%)",
        "Network": f"{bytes_sent:.2f} MB sent, {bytes_recv:.2f} MB received"
    }
    
def generate_table():
    stats = get_system_info()
    table = Table(title="System Monitor", show_header=True, header_style="cyan")
    
    table.add_column("Component", style="bold")
    table.add_column("Usage", style="green")
    
    for key, value in stats.items():
        table.add_row(key, value)
        
    return table

if __name__ == "__main__":
    with Live(generate_table(), refresh_per_second=1) as live:
        while True:
            live.update(generate_table())
            time.sleep(1)
