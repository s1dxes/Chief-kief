#!/usr/bin/env python3
"""
Chief-kief: A simple CLI tool inspired by Chief Keef
"""

import random
import sys


QUOTES = [
    "Bang Bang! 🔫",
    "That's that... Chief Kief!",
    "Love no Thotties",
    "I Don't Like",
    "These... foolish... tricks",
    "300!",
    "Sosa Baby!",
    "Glory Boyz Entertainment",
]


def get_random_quote():
    """Get a random Chief Keef inspired quote"""
    return random.choice(QUOTES)


def main():
    """Main entry point for the Chief-kief CLI"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "quote":
            print(get_random_quote())
        elif command == "help" or command == "-h" or command == "--help":
            print("Chief-kief: A Chief Keef inspired CLI tool")
            print("\nUsage:")
            print("  python chief_kief.py quote    - Get a random quote")
            print("  python chief_kief.py help     - Show this help message")
        else:
            print(f"Unknown command: {command}")
            print("Use 'help' to see available commands")
    else:
        # Default behavior - show a random quote
        print(get_random_quote())


if __name__ == "__main__":
    main()
