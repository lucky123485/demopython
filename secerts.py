# secrets.py

secrets = {
    "AWS Keys": [
        "AKIA[0-9A-Z]{16}",
        "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    ],
    "Database Passwords": [
        "password",
        "pass123",
        "123456",
        # Add more common passwords here
    ],
    # Add more secret types and patterns here
}

def find_secrets(file_contents):
    found_secrets = {}
    for secret_type, patterns in secrets.items():
        found_secrets[secret_type] = []
        for pattern in patterns:
            found = re.findall(pattern, file_contents)
            found_secrets[secret_type].extend(found)
    return found_secrets

if __name__ == "__main__":
    import re

    file_path = "path/to/your/file.txt"  # Replace with your file path
    with open(file_path, 'r') as file:
        file_contents = file.read()

    secrets_found = find_secrets(file_contents)

    if secrets_found:
        print("Secrets found:")
        for secret_type, secrets in secrets_found.items():
            if secrets:
                print(f"{secret_type}:")
                for secret in secrets:
                    print(f"  - {secret}")
    else:
        print("No secrets found in the file.")
