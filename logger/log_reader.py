import re

# Function to parse a log line
def parse_log_line(line: str)->dict:
    """
    Parse a single log line and return a dictionary with log details.
    Input: line (str) - A single line from the log file.
    Return: Dictionary with log details (dict).
    """
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

# Function to filter logs by level
def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filter logs by a specified log level.
    Input: logs (list) - List of log entries (list of dicts).
           level (str) - Log level to filter by (e.g., 'INFO', 'ERROR').
    Return: Filtered list of log entries (list of dicts).
    """
    filtered_logs = filter(lambda log: log.get('level') == level, logs)
    return list(filtered_logs)

# Function to count logs by level
def count_logs_by_level(logs: list)->dict:
    """
    Count the number of logs for each log level.
    Input: logs (list) - List of log entries (list of dicts).
    Return: Dictionary with log levels as keys and their counts as values (dict).
    """
    logs_counts = {}
    for log in logs:
        level = log.get('level')
        if level:
            logs_counts[level] = logs_counts.get(level, 0) + 1
    return logs_counts

# Function to display log counts
def display_log_counts(counts: dict):
    """
    Display the counts of logs by level in a formatted manner.
    Input: counts (dict) - Dictionary with log levels as keys and their counts as values (dict).
    Return: None
    """
    print(f"{'Log level':<10} | {'Counts':<6}")
    print("-" * 11,"|","-" * 7, sep="")
    for level, count in counts.items():
        print(f"{level:<10} | {count:<6}")