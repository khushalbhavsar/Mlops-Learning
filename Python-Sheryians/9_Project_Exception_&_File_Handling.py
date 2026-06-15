from pathlib import Path

BASE_PATH = Path("D:/MLops/MLops_Learning-/Python/Python-Sheryians/")

def read_file_folder():
    print("\n Files & Folders:")
    items = list(BASE_PATH.rglob("*"))
    if not items:
        print("No files found.")
    for i, item in enumerate(items, start=1):
        print(f"{i}: {item}")

def create_file():
    try:
        read_file_folder()
        filename = input("\nEnter file name with extension: ")
        file_path = BASE_PATH / filename

        if file_path.exists():
            print("File already exists.")
            return

        data = input("Enter data to write into the file:\n")
        with open(file_path, "w") as f:
            f.write(data)

        print(f"File '{filename}' created successfully.")

    except Exception as e:
        print("Error:", e)

def read_file():
    try:
        filename = input("Enter file name to read: ")
        file_path = BASE_PATH / filename

        if not file_path.exists():
            print(" File not found.")
            return

        with open(file_path, "r") as f:
            print("\n File Content:\n")
            print(f.read())

    except Exception as e:
        print("Error:", e)

def update_file():
    try:
        filename = input("Enter file name to update: ")
        file_path = BASE_PATH / filename

        if not file_path.exists():
            print("File not found.")
            return

        data = input("Enter new data to append:\n")
        with open(file_path, "a") as f:
            f.write("\n" + data)

        print("File updated successfully.")

    except Exception as e:
        print("Error:", e)

def delete_file():
    try:
        filename = input("Enter file name to delete: ")
        file_path = BASE_PATH / filename

        if not file_path.exists():
            print("File not found.")
            return

        file_path.unlink()
        print("File deleted successfully.")

    except Exception as e:
        print("Error:", e)


# ===== MENU =====
print("\n===== FILE MANAGEMENT SYSTEM =====")
print("1. Create File")
print("2. Read File")
print("3. Update File")
print("4. Delete File")

choice = int(input("Enter your choice: "))

if choice == 1:
    create_file()
elif choice == 2:
    read_file()
elif choice == 3:
    update_file()
elif choice == 4:
    delete_file()
else:
    print("Invalid choice")
