# scripts/hello.py
import os
from datetime import datetime

def main():
    print("Hello from GitHub Actions!")
    print("Time (UTC):", datetime.utcnow().isoformat() + "Z")
    # Example of reading a secret (safe if not set)
    api_key = os.environ.get("MY_API_KEY", "<no-secret-set>")
    print("MY_API_KEY:", api_key)

if __name__ == "__main__":
    main()
