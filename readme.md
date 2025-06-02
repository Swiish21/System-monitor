# System Monitor

A simple terminal-based system monitor built with Python, [psutil](https://pypi.org/project/psutil/), and [rich](https://pypi.org/project/rich/).  
It displays real-time CPU, memory, disk, and network usage in a live-updating table.

## Features

- **CPU Usage**: Shows current CPU utilization percentage.
- **Memory Usage**: Displays used and total memory in GB, with percentage.
- **Disk Usage**: Shows used and total disk space in GB, with percentage.
- **Network Usage**: Displays total MB sent and received.

## Requirements

- Python 3.6+
- [psutil](https://pypi.org/project/psutil/)
- [rich](https://pypi.org/project/rich/)

## Installation

Install dependencies using pip:

```sh
pip install psutil rich
```

## Usage

Run the monitor with:

```sh
python system_monitor.py
```

The terminal will display a live-updating table with your system stats.

## License

MIT License