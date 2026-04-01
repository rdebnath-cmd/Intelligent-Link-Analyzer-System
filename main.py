from linkpkg.validator import is_valid_url
from linkpkg.analyzer import check_status
from linkpkg.security import check_security, is_suspicious
from linkpkg.storage import save_result, view_records


def main():
    while True:
        print("\n=== Intelligent Link Analyzer ===")
        print("1. Analyze URL")
        print("2. View Past Records")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter URL: ")

            try:
                # Validation
                if not is_valid_url(url):
                    print("Invalid URL format!")
                    continue

                # Analysis
                status = check_status(url)
                security = check_security(url)
                suspicious = is_suspicious(url)

                print("\n--- Analysis Result ---")
                print(f"URL: {url}")
                print(f"Status: {status}")
                print(f"Security: {security}")
                print(f"Suspicious: {suspicious}")

                # Save result
                save_result(url, status, security, suspicious)

            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            view_records()

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
