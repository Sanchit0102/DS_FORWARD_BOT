from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import Config

async def checkSub(client, message):
    userid = message.from_user.id
    try:
        user =await client.get_chat_member(Config.FORCE_SUB_ID, userid)
        if user.status == enums.ChatMemberStatus.BANNED:
            await message.reply_text("Sorry. You're Banned. Contact my [Support Group](https://www.google.com) to get unbanned.")
            return False
        return True
    except UserNotParticipant:
        invite_link = await client.export_chat_invite_link(Config.FORCE_SUB_ID)
        join_button = InlineKeyboardButton("Join Channel", url=invite_link)
        join = InlineKeyboardMarkup([[join_button]])
        await message.reply_text("**Sᴏʀʀy Dᴜᴅᴇ Yᴏᴜ'ʀᴇ Nᴏᴛ Jᴏɪɴᴇᴅ My Cʜᴀɴɴᴇʟ 😐. Sᴏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Oᴜʀ Uᴩᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Cᴄᴏɴᴛɪɴᴜᴇ**", reply_markup=join)
        return False
    except Exception as e:
        print(e)
        await message.reply_text("Something went wrong. Contact my [Support Group](https://www.google.com).")
        return False
