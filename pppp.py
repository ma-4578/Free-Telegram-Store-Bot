from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# မင်း သတ်မှတ်ချင်တဲ့ Welcome ပုံ Link
WELCOME_PHOTO = "https://files.catbox.moe/jebxwm.jpg"

@Client.on_message(filters.new_chat_members)
async def welcome_bot(client: Client, message: Message):
    for user in message.new_chat_members:
        if user.is_self:
            continue
            
        welcome_text = (
            f"🎊 **မင်္ဂလာပါ၊ Group မှ ကြိုဆိုပါတယ်!**\n\n"
            f"👤 **အမည်:** {user.mention}\n"
            f"✨ **{message.chat.title}** မှာ ပျော်ရွှင်ပါစေဗျာ။"
        )
        
        # ခလုတ် ၂ ခုကို list တစ်ခုတည်းထဲ ထည့်ရင် ဘေးချင်းယှဉ် ပေါ်ပါတယ်
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Add Me ➕", url=f"https://t.me/{client.me.username}?startgroup=true"),
                InlineKeyboardButton("Support 💬", url="https://t.me/myanmarbot_music")
            ]
        ])
        
        try:
            await message.reply_photo(
                photo=WELCOME_PHOTO, 
                caption=welcome_text,
                reply_markup=buttons
            )
        except:
            await message.reply_text(welcome_text, reply_markup=buttons)

@Client.on_message(filters.left_chat_member)
async def goodbye_bot(client: Client, message: Message):
    user = message.left_chat_member
    if user.is_self:
        return
        
    await message.reply_text(f"👋 **Bye Bye {user.first_name}!**\nနောက်မှ ပြန်ဆုံကြမယ်ဗျာ။")
