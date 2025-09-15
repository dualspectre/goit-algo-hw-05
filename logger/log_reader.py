from datetime import datetime
import re


def parse_log_line(line: str)->dict:
    log_data = {}
    log_pattern = r"^(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>INFO|DEBUG|ERROR|WARNING)\s(?P<message>.*)$"
    match = re.match(log_pattern, line)
    if match:
        log_data = match.groupdict()
    return log_data

def load_logs(file_path: str) ->list:
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            log_data = parse_log_line(line.strip())
            if log_data:
                logs.append(log_data)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    pass

def count_logs_by_level(logs: list)->dict:
    pass

def display_log_counts(counts: dict):
    pass