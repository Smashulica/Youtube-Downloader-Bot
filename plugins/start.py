from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channels", url="https://t.me/OTRportal")],
        [InlineKeyboardButton(
            "Developer", url="https://t.me/iarbadevanzare")]
    ])
    welcomed = f"👋🏻Hey <b>{message.from_user.first_name}</b>,\n\n<b>Pot descarca video/audio de pe YouTube.</b>\n<b>Trimite un link de youtube !</b>\n<b>Tasteaza /help ca sa afli mai multe despre mine !!</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
