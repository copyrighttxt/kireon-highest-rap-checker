import requests
import time

API_BASE = 'https://www.kireon.xyz/public-api/v1/users/'

# Your Discord webhook URL
DISCORD_WEBHOOK = 'webhook_here'

# Your Discord ID
DISCORD_MENTION = '<@your_discord_id_here>'

user_id = 1
highest_rap = 0
top_user_data = {}

def send_to_discord(username, rap, user_id):
    content = (
        f"{DISCORD_MENTION} New top RAP found.\n"
        f"Username: {username}\n"
        f"RAP: {rap}\n"
        f"User ID: {user_id}\n"
        f"https://www.kireon.xyz/user/{user_id}"
    )
    payload = {"content": content}
    try:
        response = requests.post(DISCORD_WEBHOOK, json=payload)
        if response.status_code == 204:
            print(f"Sent to Discord: {username} ({rap})")
        else:
            print(f"Discord webhook error: {response.status_code} {response.text}")
    except Exception as e:
        print(f"Error sending to Discord: {e}")

try:
    while True:
        url = f"{API_BASE}{user_id}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except Exception as e:
            print(f"Error fetching user {user_id}: {e}")
            user_id += 1
            continue

        try:
            data = response.json()
        except Exception as e:
            print(f"Invalid JSON for user {user_id}: {e}")
            user_id += 1
            continue

        if isinstance(data, dict) and "data" in data and data["data"]:
            user_data = data["data"]
            rap = user_data.get("inventory_rap")
            username = user_data.get("username", "Unknown")

            if isinstance(rap, (int, float)):
                print(f"User {user_id} | {username} | RAP: {rap}")

                if rap > highest_rap:
                    highest_rap = rap
                    top_user_data = user_data
                    print(f"New top RAP: {rap} (Username: {username}, ID: {user_id})")
                    send_to_discord(username, rap, user_id)
            else:
                print(f"User {user_id} has no valid RAP.")
        else:
            print(f"No valid data for user {user_id}")

        user_id += 1
        time.sleep(1.0)

except KeyboardInterrupt:
    print("\nStopped.")
    print(f"Top RAP: {highest_rap}")
    print("Top user data:")
    print(top_user_data)
