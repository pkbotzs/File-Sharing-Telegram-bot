from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id
from utils import short_link

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ғɪʀsᴛ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ ⏩ (ᴡɪᴛʜ ǫᴜᴏᴛᴇs)..\n\nOʀ sᴇɴᴅ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ʟɪɴᴋ\nᴜsᴇ /sbatch ғᴏʀ sᴛᴏᴘᴘɪɴɢ.", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except Exception as e:
            print(e)
            return
        if first_message.text == "/sbatch":
            return
        f_msg_id = await get_message_id(client, first_message)
        
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Eʀʀᴏʀ\n\nᴛʜɪs ғᴏʀᴡᴀʀᴅᴇᴅ ᴘᴏsᴛ ɪs ɴᴏᴛ ғʀᴏᴍ ᴍʏ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴛʜɪs ʟɪɴᴋ ɪs ᴛᴀᴋᴇɴ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ", quote = True)
            continue
    while True:
        try:
            second_message = await client.ask(text = "ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ғɪʀsᴛ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ ⏩ (ᴡɪᴛʜ ǫᴜᴏᴛᴇs)..\nOʀ sᴇɴᴅ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ʟɪɴᴋ\nᴜsᴇ /sbatch ғᴏʀ sᴛᴏᴘᴘɪɴɢ.", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        if second_message.text == "/sbatch":
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Eʀʀᴏʀ\n\nᴛʜɪs ғᴏʀᴡᴀʀᴅᴇᴅ ᴘᴏsᴛ ɪs ɴᴏᴛ ғʀᴏᴍ ᴍʏ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴛʜɪs ʟɪɴᴋ ɪs ᴛᴀᴋᴇɴ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ", quote = True)
            continue
        
    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    shortened_link = await short_link(link)
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Sʜᴀʀᴇ ᴜʀʟ", url=f'https://telegram.me/share/url?url={shortened_link}')]])
    await second_message.reply_text(f"<b>🧑‍💻 Hᴇʀᴇ ɪs ʏᴏᴜʀ ᴄᴏᴅᴇ👍 : \n<code>{base64_string}</code></b>\n\n<b>🔗 Hᴇʀᴇ ɪs ʏᴏᴜʀ ᴄᴏᴅᴇ👍 :</b>\n{shortened_link}", quote=True, reply_markup=reply_markup)



@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ғɪʀsᴛ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ ⏩ (ᴡɪᴛʜ ǫᴜᴏᴛᴇs)..\nOʀ sᴇɴᴅ ᴛʜᴇ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ʟɪɴᴋ\nType /sgen for ғᴏʀ sᴛᴏᴘᴘɪɴɢ.", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except Exception:
            return
        if channel_message.text == "/sgen":
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nᴛʜɪs ғᴏʀᴡᴀʀᴅᴇᴅ ᴘᴏsᴛ ɪs ɴᴏᴛ ғʀᴏᴍ ᴍʏ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴛʜɪs ʟɪɴᴋ ɪs ᴛᴀᴋᴇɴ ғʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ", quote = True)
            continue
    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    shortened_link = await short_link(link)
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"🔁 Sʜᴀʀᴇ ᴜʀʟ", url=f'https://telegram.me/share/url?url={shortened_link}')]])
    await channel_message.reply_text(f"<b>🧑‍💻 Hᴇʀᴇ ɪs ʏᴏᴜʀ ᴄᴏᴅᴇ👍 : \n<code>{base64_string}</code></b>\n\n<b>🔗 Hᴇʀᴇ ɪs ʏᴏᴜʀ ᴄᴏᴅᴇ👍 : </b>\n{shortened_link}", quote=True, reply_markup=reply_markup)
