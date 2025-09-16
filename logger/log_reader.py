import re

# Function to parse a log line
def parse_log_line(line: str)->dict:
    log_data = {}
    log_pattern = r"^(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>INFO|DEBUG|ERROR|WARNING)\s(?P<message>.*)$"
    match = re.match(log_pattern, line)
    if match:
        log_data = match.groupdict()
    return log_data

# Function to load logs from file
def load_logs(file_path: str) ->list:
    """
    Load logs from a specified file and return a list of log entries.
    Input: file_path (str) - Path to the log file.
    
    Return: List of log entries (list of dicts).
    """
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            log_data = parse_log_line(line.strip())
            if log_data:
                logs.append(log_data)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = filter(lambda log: log.get('level') == level, logs)
    return filtered_logs

def count_logs_by_level(logs: list)->dict:
    logs_counts = {}
    for log in logs:
        level = log.get('level')
        if level:
            logs_counts[level] = logs_counts.get(level, 0) + 1
    return logs_counts

def display_log_counts(counts: dict):
    print(f"{'Log level':<10} | {'Counts':<6}")
    print("-" * 11,"|","-" * 7, sep="")
    for level, count in counts.items():
        print(f"{level:<10} | {count:<6}")