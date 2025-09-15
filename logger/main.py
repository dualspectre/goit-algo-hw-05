import log_reader
from sys import argv
import re

def main():
    
    # log_file = argv[1]
    with open('logs.txt', 'r') as file:
        lines = [el.strip() for el in file.readlines()]
    


if __name__ == "__main__":
    main()