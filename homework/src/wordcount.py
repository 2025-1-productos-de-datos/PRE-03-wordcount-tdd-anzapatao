import argparse
import os

from _internals.parse_args import parse_args


def read_all_lines(input_folder):

    lines = []
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines


def main():
    """
    Main function to count words in a file.
    """
    # Parse command line arguments
    input_folder, output_folder = parse_args()

    # Aquí puedes agregar el resto de tu lógica para contar palabras
    # ...

    print(f"Processing files from {input_folder} to {output_folder}")


if __name__ == "__main__":
    main()
