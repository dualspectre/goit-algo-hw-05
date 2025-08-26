from typing import Callable, Generator
import re

# generator function to extract numbers from text
def generator_number(text:str) -> Generator[float, float, float]:
    pattern = r' \d+(|.|.\d+) '
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text:str, generator:Callable[[str], float]) -> float:
    """
    Calculate the total profit from the given text using the provided generator text number function.

    Input: text (str): The input text containing profit numbers.
    generator: Callable[[str], float]: A generator function that extracts numbers from the text.

    return: float: The total profit calculated from the text.
    """
    next_number = generator(text)
    total_profit = 0.0
    try:
        while True:
            total_profit += next(next_number)
    except StopIteration:
        pass
    except Exception:
        print(f"Input data in <text> parameter is not a string. Please provide a valid string.")

    return total_profit


# Example usage
"""
text = "Загальний дохід працівника складається з декількох частин:\
      1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

profit = sum_profit(text, generator_number)
print(f"Total profit: {profit}")
"""