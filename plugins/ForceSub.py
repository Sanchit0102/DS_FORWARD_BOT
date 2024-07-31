# from pyrogram import Client, filters, enums 
# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from pyrogram.errors import UserNotParticipant
# from config import Config
# from database import db

# async def not_subscribed(_, client, message):
#     await db.add_user(client, message)
#     if not Config.AUTH_CHANNEL:
#         return False
#     try:             
#         user = await client.get_chat_member(Config.AUTH_CHANNEL, message.from_user.id) 
#         if user.status == enums.ChatMemberStatus.BANNED:
#             return True 
#         else:
#             return False                
#     except UserNotParticipant:
#         pass
#     return True


# @Client.on_message((filters.private | filters.group) & filters.create(not_subscribed))
# async def forces_sub(client, message):
#     invite_link = await client.create_chat_invite_link(int(Config.AUTH_CHANNEL))
#     buttons = [[InlineKeyboardButton(text="📢 Join Update Channel 📢", url=invite_link.invite_link) ]]
#     text = "**Sᴏʀʀy Yᴏᴜ'ʀᴇ Nᴏᴛ Jᴏɪɴᴇᴅ My Cʜᴀɴɴᴇʟ 😐. Sᴏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Oᴜʀ Uᴩᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Cᴄᴏɴᴛɪɴᴜᴇ**"

#     return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from config import Config


@Client.on_message(~filters.edited & filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"You must join [this channel]({link}) to use me. After joining try again !",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ Join Channel ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
