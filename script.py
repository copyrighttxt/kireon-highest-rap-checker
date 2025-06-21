import requests

API_BASE = 'https://www.kireon.xyz/public-api/v1/users/'

def check_user(user_id):
    try:
        res = requests.get(f"{API_BASE}{user_id}", timeout=5)
        if res.status_code != 200:
            print(f"User ID {user_id} not found (HTTP {res.status_code})")
            return

        data = res.json().get("data", {})
        if not data:
            print(f"No user data found for ID {user_id}")
            return

        username = data.get("username", "Unknown")
        rap = data.get("inventory_rap", "N/A")
        value = data.get("value", "N/A")

        print(f"\nUsername: {username}")
        print(f"User ID: {user_id}")
        print(f"Inventory RAP: {rap}")
        print(f"Value: {value}")

    except Exception as e:
        print(f"Error fetching user: {e}")

# Prompt for input
try:
    while True:
        user_input = input("\nEnter a User ID (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        if user_input.isdigit():
            check_user(int(user_input))
        else:
            print("Please enter a valid numeric user ID.")
except KeyboardInterrupt:
    print("\nExiting.")
