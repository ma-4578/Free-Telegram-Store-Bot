import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

WELCOME_MEDIA = "https://files.catbox.moe/jebxwm.jpg" 

@Client.on_message(filters.new_chat_members)
async def welcome_bot(client: Client, message: Message):
    for user in message.new_chat_members:
        if user.is_self:
            continue
            
        welcome_text = (
            f"🎊 **မင်္ဂလာပါ၊ Group မှ ကြိုဆိုပါတယ်!**\n\n"
            f"👤 **အမည်:** {user.mention}\n"
            f"✨ **{message.chat.title}** မှာ ပျော်ရွှင်ပါစေဗျာ။\n\n"
            f"⚠️ *ဤမက်ဆေ့ခ်ျအား ၁ မိနစ်ကြာလျှင် အလိုအလျောက် ဖျက်ပေးပါမည်။*"
        )
        
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Add Me ➕", url=f"https://t.me/{client.me.username}?startgroup=true"),
                InlineKeyboardButton("Support 💬", url="https://t.me/myanmarbot_music")
            ],
            [
                InlineKeyboardButton("Update Channel 🌐", url="https://t.me/myanmarbot_music")
            ]
        ])
        
        try:
            # Welcome Message ကို ပို့မယ်
            msg = await message.reply_photo(
                photo=WELCOME_MEDIA, 
                caption=welcome_text,
                reply_markup=buttons
            )
            
            # --- Auto Delete စနစ် ---
            await asyncio.sleep(60) # ၆၀ စက္ကန့် (၁ မိနစ်) စောင့်မယ်
            await msg.delete()      # Message ကို ပြန်ဖျက်မယ်
            
        except Exception as e:
            print(f"Error: {e}")

@Client.on_message(filters.left_chat_member)
async def goodbye_bot(client: Client, message: Message):
    user = message.left_chat_member
    if user.is_self:
        return
        
    msg = await message.reply_text(f"👋 **Bye Bye {user.first_name}!**\nနောက်မှ ပြန်ဆုံကြမယ်ဗျာ။")
    
    # နှုတ်ဆက်စာကိုလည်း ၁ မိနစ်ဆို ဖျက်ချင်ရင် အောက်က code ထည့်ပါ
    await asyncio.sleep(60)
    await msg.delete()
