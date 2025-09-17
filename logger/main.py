import log_reader
from sys import argv


def main():
    
    args_counts = len(argv)
    if args_counts != 1:
        # Input file name logs
        log_file = argv[1]

        try:
            logs = log_reader.load_logs(log_file)
            log_counts = log_reader.count_logs_by_level(logs)
            log_reader.display_log_counts(log_counts)
        except FileNotFoundError:
            print(f"Error: File '{log_file}' not found.")
            return
        except Exception as e:
            print(f"Error: {e}")
            return
    else:
        print("Usage: python main.py <log_file_path> [log_level]")
        return
    
    if args_counts > 2:
        log_level = argv[2].upper()
        filtered_logs = log_reader.filter_logs_by_level(logs, log_level)
        if filtered_logs:
            print(f"\nDetails logs with level '{log_level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nNo logs found with level '{log_level}'.")


if __name__ == "__main__":
    main()