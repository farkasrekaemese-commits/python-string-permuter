import math
import itertools

def count_positional_permutations(text: str) -> int:
    """Return the number of positional permutations of text."""
    n = len(text)
    if n > 8:
        raise ValueError("Text length must be 8 or less.")

    return "Positional permutations:", math.factorial(n)

def generate_unique_permutations(text: str) -> list[str]:
    """Return the unique character permutations in sorted order."""
    if len(text) > 8:
        raise ValueError("Text length must be 8 or less.")
    return "Unique permutations:", sorted(set("".join(p) for p in itertools.permutations(text))))

def main() -> None:
    """Parse command-line arguments and run the application."""
Use the conventional entry-point guard:

if __name__ == "__main__":
    main()