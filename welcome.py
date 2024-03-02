import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonX import app  

photo = [
    "https://telegra.ph/file/da67fb35e281fbbef4a52.jpg",
    "https://telegra.ph/file/6a2a6296ed20d386b3b75.jpg",
    "https://telegra.ph/file/860d251cb16e3977c8d73.jpg",
    "https://telegra.ph/file/6b3bb30a42ec21ead17fc.jpg",
    "https://telegra.ph/file/22c99e7e51293137e0fa7.jpg",
    "https://telegra.ph/file/6456ef8f453825dfeaedc.jpg",
    "https://telegra.ph/file/ba6117517164a19ab5507.jpg",
    "https://telegra.ph/file/2b37ec337b267f7ccb85f.jpg",
    "https://telegra.ph/file/b41dc1b55d98ccc72239f.jpg",
    "https://telegra.ph/file/88d5dac4c0f2f583dd788.jpg",
    "https://telegra.ph/file/9caca44ca2316f3e4255c.jpg",
    "https://telegra.ph/file/5b66b2ad8db582e275c56.jpg",
    "https://telegra.ph/file/79aec16d31582b7763430.jpg",
    "https://telegra.ph/file/681a67ad7dbc81c64d7ed.jpg",
    "https://telegra.ph/file/386ad165abb664a51f4f4.jpg",
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷𝐇ᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
                f"**📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**💖𝐔ʀ 𝐈d:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**✍️𝐔ʀ 𝐔.𝐍:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🥳ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ🥳", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
