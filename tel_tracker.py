import os
from telethon import TelegramClient
from dotenv import load_dotenv, dotenv_values

load_dotenv()

# To get these values: GOTO me.telegram.com

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient("anon.session", api_id, api_hash)

client.start()


async def get_messages():
    print("-" * 50)
    userId = int(input("Enter your friend id: "))
    print("-" * 50)
    me = await client.get_me()
    your_user_id = me.id
    try:
        print("-" * 50)
        # Prompt the user to choose the order of messages
        print("1. From Oldest To Newest Messages")
        print("2. From Newest To Oldest Messages.")
        choice = input("Enter your choice: ")
        print("-" * 50)

        # Reverse the message order based on the user's choice
        print("-" * 50)
        reverse_order = True if choice == "1" else False
        (
            print("Arranging from Oldest to Newest Messages")
            if choice == "1"
            else print("Arranging from Newest to Oldest Messages")
        )
        print("-" * 50)
        # Fetch and print messages from the specified user ID
        async for message in client.iter_messages(userId, reverse=reverse_order):
            if message.sender_id == your_user_id:  # Messages sent by you
                if message.photo:
                    print("-" * 50)
                    print(f"You ({userId}), Photo with ID {message.photo.id} detected")
                    print("-" * 50)
                else:
                    print("-" * 50)
                    print(f"You ({userId}):", message.text)
                    print("-" * 50)
            else:  # Messages sent by other users
                if message.photo:
                    print("-" * 50)
                    print(
                        f"Other user ({message.sender_id}), Photo with ID {message.photo.id} detected"
                    )
                    print("-" * 50)
                else:
                    print("-" * 50)
                    print(f"Other user ({message.sender_id}):", message.text)
                    print("-" * 50)

    except ValueError:
        print("-" * 50)
        print("Invalid user ID. Please try again.")
        print("-" * 50)

    except Exception as e:
        print("-" * 50)
        print("An error occurred:", e)
        print("-" * 50)


async def get_all_messages():
    try:
        while True:
            print("-" * 50)
            print(
                "To get all the messages from your friend, you need to enter his/her id."
            )
            print("1. I know ID")
            print("2. I don't know my friend ID")
            print("3. Exit")
            print("-" * 50)
            choice = input("Enter your choice: ")

            if choice == "1":
                await get_messages()
            elif choice == "2":
                print("-" * 50)
                print("Choose Id from your contact list.")
                await get_all_users()
                print("-" * 50)
            elif choice == "3":
                break
            else:
                print("-" * 50)
                print("Invalid choice. Please try again")
                print("-" * 50)
    except KeyboardInterrupt:
        print("")
        print("-" * 50)
        print("Quitting")


async def get_all_users():
    async for dialog in client.iter_dialogs():
        # phone = dialog.entity.id
        # print(phone)
        print("-" * 50)
        print(dialog.name, "has ID", dialog.id)
        print("-" * 50)


async def main():
    try:
        while True:
            me = await client.get_me()
            print("-" * 50)
            print("Welcome To Telegram Message Extractor")
            print(f"Good to see you, {me.first_name} {me.last_name}!")
            print("-" * 50)
            print("1. Get all messages from your friend")
            print("2. Get All Users who Messaged you.")
            print("3. Exit the application")
            print("-" * 50)
            choice = input("Enter your choice: ")
            if choice == "1":
                await get_all_messages()  # Await the asynchronous function call

            elif choice == "2":
                await get_all_users()  # Await the asynchronous function call
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again")
    except KeyboardInterrupt:
        print("")
        print("Quiting")


with client:
    client.loop.run_until_complete(main())
