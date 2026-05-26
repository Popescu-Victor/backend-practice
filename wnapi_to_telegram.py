from typing import Final
import dotenv
import asyncio
from telegram import Bot


TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "TOKEN")
CHAT_ID: Final = dotenv.get_key(dotenv.find_dotenv(), "CHAT_ID")

async def send_news(message: str) -> None:
    bot = Bot(token=TOKEN)
    print("Type a message to send. Type 'quit' to stop.")

    while True:
    
        if message.lower() == "quit":
            break

        if message.strip():
            await bot.send_message(chat_id=CHAT_ID, text=message)
