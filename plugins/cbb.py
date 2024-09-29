from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Language : <code>Pʏᴛʜᴏɴ𝟹</code></b> 🐍\n<b>○ Vᴇʀsɪᴏɴ : v1 🫏</b>\n<b>○ Dᴇᴠᴇʟᴏᴘᴇʀ : <code>@PKlinkzz_admin_bot</code> 😼</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "buy_prem":
        await query.message.edit_text(
            text=f"👋 {query.from_user.username}\n\n🎖️ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs :\n\n● {PRICE1} ʀs ғᴏʀ 𝟽 ᴅᴀʏs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE2} ʀs ғᴏʀ 𝟷 ᴍᴏɴᴛʜ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE3} ʀs ғᴏʀ 3 ᴍᴏɴᴛʜ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE4} ʀs ғᴏʀ 6 ᴍᴏɴᴛʜ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE5} ʀs ғᴏʀ 𝟷 ʏᴇᴀʀ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n\n💵 UPI ID -  <code>{UPI_ID}</code>\n\n\n📸 QR - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ ({UPI_IMAGE_URL})\n\n♻️ ɪғ ᴘᴀʏᴍᴇɴᴛ ɪs ɴᴏᴛ ɢᴇᴛᴛɪɴɢ sᴇɴᴛ ᴏɴ ᴀʙᴏᴠᴇ ɢɪᴠᴇɴ ǫʀ ᴄᴏᴅᴇ ᴛʜᴇɴ ɪɴғᴏʀᴍ ᴀᴅᴍɪɴ, ʜᴇ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ɴᴇᴡ ǫʀ ᴄᴏᴅᴇ\n\n\n ✔ Nᴏᴛᴇ:  ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("Sᴇɴᴅ Pᴀʏᴍᴇɴᴛ Sʀᴇᴇɴsʜᴏᴛ(ADMIN) 📸", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("🔒 ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
            )
