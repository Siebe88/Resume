#!/usr/bin/env python3
"""
Generate LaTeX files from JSON data for the resume project.
This script separates data from structure, making it easier to maintain.
"""

from .generator import generate_all


def main():
    """Main function to generate all LaTeX files from JSON data."""
    generate_all()


if __name__ == "__main__":
    main() 