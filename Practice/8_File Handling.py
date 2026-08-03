# What is file handling in Python?
# File handling in Python allows you to create, read, update, and delete files.
# Python provides built-in functions and methods to work with files, making it easy
# to perform file operations.

from pathlib import Path
import os
import shutil


def main():
    base_dir = Path(__file__).resolve().parent
    demo_file = base_dir / "demo.txt"
    copied_file = base_dir / "demo_copy.txt"
    renamed_file = base_dir / "demo_renamed.txt"

    # Create a file and write content.
    with open(demo_file, "w", encoding="utf-8") as file:
        file.write("Hello, Python!\n")
        file.write("This is a file handling demo.\n")
        file.write("We can create, read, update, and delete files.\n")

    # Read a file.
    with open(demo_file, "r", encoding="utf-8") as file:
        content = file.read()
        print("File content:")
        print(content)

    # Append data.
    with open(demo_file, "a", encoding="utf-8") as file:
        file.write("Appended line.\n")

    # Count words, lines, and characters.
    with open(demo_file, "r", encoding="utf-8") as file:
        text = file.read()

    word_count = len(text.split())
    line_count = len(text.splitlines())
    character_count = len(text)

    print(f"Words: {word_count}")
    print(f"Lines: {line_count}")
    print(f"Characters: {character_count}")

    # Copy a file.
    shutil.copy2(demo_file, copied_file)

    # Rename a file.
    os.rename(copied_file, renamed_file)

    # Delete a file.
    os.remove(demo_file)
    os.remove(renamed_file)


if __name__ == "__main__":
    main()