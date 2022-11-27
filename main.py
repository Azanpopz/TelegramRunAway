from pyrogram import Client
from pyrogram.enums import ChatType

api_id = YOUR_APP_ID
api_hash = "YOUR_APP_HASH)"
app = Client("AnyString")


async def main():
    async with app:
        async for dialog in app.get_dialogs():
            if dialog.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
                print("Cleaning Messages in Group:{}...".format(dialog.chat.title))
                async for msg in app.search_messages(chat_id=dialog.chat.id, from_user="me"):
                    if msg.text:
                        print("Deleting Message Contents:{}...".format(msg.text))
                    await app.delete_messages(chat_id=dialog.chat.id, message_ids=msg.id)


app.run(main())
