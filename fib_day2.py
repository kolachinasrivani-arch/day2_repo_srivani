"""
Fibonacci Sequence Generator

This script provides functionality to generate Fibonacci numbers up to
a given count. It follows best practices with modular code, error handling,
and logging for debugging.

Author: <Your Name>
"""

import logging
from typing import List

# ----------------------------------------------------------------------
# Logging Configuration
# ----------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------
# Fibonacci Generator
# ----------------------------------------------------------------------
def generate_fibonacci(n: int) -> List[int]:
    """Generate a Fibonacci sequence of length `n`.

    Args:
        n (int): Number of terms in the sequence. Must be >= 0.

    Returns:
        List[int]: Fibonacci sequence.

    Raises:
        ValueError: If `n` is negative.
    """
    if n < 0:
        logger.error("Negative input received: %d", n)
        raise ValueError("Number of terms must be non-negative")

    if n == 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    logger.debug("Generated Fibonacci sequence: %s", sequence)
    return sequence


# ----------------------------------------------------------------------
# Main Entry Point
# ----------------------------------------------------------------------
def main() -> None:
    """Main program execution."""
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        sequence = generate_fibonacci(n)
        print(f"Fibonacci sequence ({n} terms): {sequence}")
    except ValueError as exc:
        logger.error("Invalid input: %s", exc)
        print("❌ Please enter a valid non-negative integer.")


if __name__ == "__main__":
    main()
