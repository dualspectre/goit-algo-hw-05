import log_reader
from sys import argv


def main():
    
    # log_file = argv[1]
    try:
        log_file = 'logs.txt'
        logs = log_reader.load_logs(log_file)
        log_counts = log_reader.count_logs_by_level(logs)
        # print(logs)
        # print(log_counts)
        # fil_logs = log_reader.filter_logs_by_level(logs, 'ERROR')
        # print(list(fil_logs))
    except Exception as e:
        print(f"Error: {e}")
        return
    log_reader.display_log_counts(log_counts)


if __name__ == "__main__":
    main()