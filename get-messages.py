from telethon import TelegramClient
from datetime import datetime, timedelta, timezone

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = ""
api_hash = ""

client = TelegramClient(
    "anon.session", api_id, api_hash
)  # You need run twice because this part create session in first run.
client.start()

user_name = ""  # Write here username you want to get last 1 hour of chat.

for message in client.iter_messages(
    user_name,
    reverse=True,
):
    print(message.sender_id, ":", message.text)
