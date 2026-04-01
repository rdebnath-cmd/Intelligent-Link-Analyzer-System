import json

FILE_NAME = "records.json"

def save_result(url, status, security, suspicious):
    """Save results to JSON file"""
    record = {
        "url": url,
        "status": status,
        "security": security,
        "suspicious": suspicious
    }

    try:
        try:
            with open(FILE_NAME, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(record)

        with open(FILE_NAME, 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print("Error saving file:", e)


def view_records():
    """Display saved records"""
    try:
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
            print("\n--- Past Records ---")
            for record in data:
                print(f"URL: {record['url']} | Status: {record['status']} | Security: {record['security']} | Suspicious: {record['suspicious']}")
    except FileNotFoundError:
        print("No records found!")
