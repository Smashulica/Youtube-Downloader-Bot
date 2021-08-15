from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<b>💁🏻‍♂️ Cum pot fi folosit?</b>\n\n<b>Doar trimite un link de YouTube si eu voi descarca pentru tine fisierul video sau MP3 !</b>\n<b>(Playlist sau inline inca nu este suportat ☹️)</b>\n\n<b>Dar merg cu @vid 🤘🏻</b>"
    await message.reply_text(helptxt)
