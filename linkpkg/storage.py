FILE_NAME = "records.txt"


def save_result(url, status, security, suspicious):
    """Save results to file"""
    try:
        with open(FILE_NAME, 'a') as file:
            file.write(f"{url} | {status} | {security} | {suspicious}\n")
    except Exception as e:
        print("Error saving file:", e)


def view_records():
    """Display saved records"""
    try:
        with open(FILE_NAME, 'r') as file:
            data = file.read()
            print("\n--- Past Records ---")
            print(data)
    except FileNotFoundError:
        print("No records found!")
