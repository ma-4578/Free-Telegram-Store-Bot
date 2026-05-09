import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    help_text = (
        "✨ **Bot Help Menu (အသုံးပြုနည်း)** ✨\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        
        "👫 **General Features:**\n"
        "• `/couple` - Group ထဲက ကံထူးရှင် အတွဲလေးကို ရွေးပေးမှာပါ။\n"
        "• `/happy` - စိတ်ညစ်နေရင် ဟာသနဲ့ အားပေးစာလေးတွေ ပို့ပေးမှာပါ။\n"
        "• `/tr` [စာသား] - ဘယ်ဘာသာစကားမဆို မြန်မာလို ပြန်ပေးမှာပါ။\n"
        "• `/love` - အချစ်ရေး ကံစမ်းဟောကြားပေးမှာပါ။\n\n"
        
        "🛠 **Utility Features:**\n"
        "• `/id` - မိမိရဲ့ Telegram User ID ကို ကြည့်ရန်။\n"
        "• `/info` - မိမိရဲ့ Profile အချက်အလက်တွေကို ကြည့်ရန်။\n\n"
        
        "👮 **Admin & Safety:**\n"
        "• **Welcome** - Group ထဲ လူအသစ်ဝင်ရင် Auto ကြိုဆိုပေးမှာပါ။\n"
        "• **Anti-Spam** - Link တွေ၊ Forward တွေ အများကြီးပို့ရင် Auto Mute ပေးမှာပါ။\n"
        "• `/all` - Group Member အားလုံးကို Tag ခေါ်ပေးမှာပါ။\n\n"
        
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💡 _Command တစ်ခုချင်းစီကို စာရိုက်ကွက်တွင် ရိုက်နှက်၍ အသုံးပြုနိုင်ပါသည်_"
    )

    # Bot ကို Group ထဲထည့်ဖို့ Button လေးပါ တစ်ခါတည်း ထည့်ပေးထားပါတယ်
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("သင့် Group မှာလည်း Add လိုက်ပါ ➕", url=f"https://t.me/{client.me.username}?startgroup=true")
        ]
    ])

    await message.reply_text(help_text, reply_markup=buttons)
