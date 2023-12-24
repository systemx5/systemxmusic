import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from BrandrdXMusic import app  

photo = [
    "https://te.legra.ph/file/aab8ee34e7455ed347c3f.jpg",
    "https://te.legra.ph/file/aab8ee34e7455ed347c3f.jpg",
    "https://te.legra.ph/file/aab8ee34e7455ed347c3f.jpg",
    "https://te.legra.ph/file/aab8ee34e7455ed347c3f.jpg",
    "https://te.legra.ph/file/aab8ee34e7455ed347c3f.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"───────────────────────────\n\n"
                f"ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                
                f"ᴄʜᴀᴛ ɪ'ᴅ: {message.chat.id}\n"
                
                f"ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                
                f"ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                
                f"ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                
                f"ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"★ sᴇᴇ ɢʀᴏᴜᴘ ★", url=f"{link}")]
         ]))


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ "
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#ʟᴇғᴛ ɢʀᴏᴜᴘ</u></b> ✫\n\ᴄʜᴀᴛ ᴛɪᴛʟᴇ : {title}\n\ᴄʜᴀᴛ ɪᴅ  : {chat_id}\n\nʀᴇᴍᴏᴠᴇᴅ ʙʏ : {remove_by}\n\nʙᴏᴛ: @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"{member.id}ᴡᴇʟᴄᴏᴍᴇ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                
                f"ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                
                f"ᴄʜᴀᴛ ᴜ.ɴ: @{message.chat.username}\n"
                
                f"ᴜʀ ɪ'ᴅ: {member.id}\n"
                
                f"ᴜʀ ᴜ.ɴᴀᴍᴇ: @{member.username}\n"
            
                f"ᴄᴏᴍᴘʟᴇᴛᴇᴅ {count} ᴍᴇᴍʙᴇʀs"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"★ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ★", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))

#tagall
