import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Bot Token ထည့်ပါ
TOKEN = "8719681164:AAGUR3zQTnvtS6wAUaqHV0gkyQ63boGuj4"

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 မင်္ဂလာပါ။ PTK Streaming Bot မှ ကြိုဆိုပါတယ်။\n\n/movies နှိပ်ပြီး ရုပ်ရှင်စာရင်းကြည့်ပါ။")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📖 အကူအညီ\n\n/movies - ရုပ်ရှင်စာရင်း\n/search [နာမည်] - ရှာဖွေရန်\n/genre - အမျိုးအစားအလိုက်\n/request - ရုပ်ရှင်တောင်းဆိုရန်\n/latest - အသစ်ထည့်သွင်းထားသော\n/popular - လူကြိုက်များသော\n/download - ဒေါင်းလုဒ်လင့်\n/stream - တိုက်ရိုက်ကြည့်ရန်")

# /movies command
async def movies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 Action", callback_data="action"),
         InlineKeyboardButton("😱 Horror", callback_data="horror")],
        [InlineKeyboardButton("😂 Comedy", callback_data="comedy"),
         InlineKeyboardButton("💕 Romance", callback_data="romance")],
        [InlineKeyboardButton("🔙 Back", callback_data="back")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📽️ ရုပ်ရှင်အမျိုးအစား ရွေးပါ။", reply_markup=reply_markup)

# /search command
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        query = " ".join(context.args)
        await update.message.reply_text(f"🔍 '{query}' ကိုရှာဖွေနေပါသည်...\n\n(ဒေတာဘေ့စ်မရှိသေးပါ။ နောက်ပိုင်းထည့်ပေးပါမည်။)")
    else:
        await update.message.reply_text("🔍 ရုပ်ရှင်နာမည်ထည့်ပေးပါ။\nဥပမာ - /search Spider Man")

# /genre command
async def genre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 Action", callback_data="action"),
         InlineKeyboardButton("😱 Horror", callback_data="horror")],
        [InlineKeyboardButton("😂 Comedy", callback_data="comedy"),
         InlineKeyboardButton("💕 Romance", callback_data="romance")],
        [InlineKeyboardButton("🎥 Drama", callback_data="drama"),
         InlineKeyboardButton("🤖 Sci-Fi", callback_data="scifi")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🎭 အမျိုးအစားတစ်ခုခုကို ရွေးပါ။", reply_markup=reply_markup)

# /request command
async def request_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        movie_name = " ".join(context.args)
        await update.message.reply_text(f"✅ '{movie_name}' ရုပ်ရှင်တောင်းဆိုမှုကို လက်ခံပါပြီ။\nမကြာမီထည့်သွင်းပေးပါမည်။")
    else:
        await update.message.reply_text("📝 ရုပ်ရှင်နာမည်ထည့်ပေးပါ။\nဥပမာ - /request Avatar 2")

# /latest command
async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🆕 ဒီနေ့ထည့်သွင်းထားသော ရုပ်ရှင်အသစ်များ:\n\n1. Deadpool 3\n2. Inside Out 2\n3. Furiosa\n4. Kingdom of the Planet of the Apes")

# /popular command
async def popular(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 လူကြိုက်အများဆုံးရုပ်ရှင်များ:\n\n1. Spider-Man: Across the Spider-Verse\n2. Oppenheimer\n3. Barbie\n4. John Wick 4")

# /download command
async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📥 ဒေါင်းလုဒ်လင့်ရယူရန် ရုပ်ရှင်နာမည်ကို /search နဲ့ ရှာဖွေပါ။\n\nသို့မဟုတ် အောက်ပါလင့်များကို သုံးနိုင်ပါသည်:\n- Example Link 1\n- Example Link 2")

# /stream command
async def stream(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎥 တိုက်ရိုက်ကြည့်ရှုရန် လင့်များ:\n\nhttps://example.com/watch/1\nhttps://example.com/watch/2\n\n(စစ်မှန်သောလင့်များ ထည့်သွင်းပေးပါမည်။)")

# Callback query handler (for buttons)
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "action":
        await query.edit_message_text("🎬 Action ရုပ်ရှင်များ:\n1. John Wick 4\n2. Mission Impossible 7\n3. The Equalizer 3")
    elif query.data == "horror":
        await query.edit_message_text("😱 Horror ရုပ်ရှင်များ:\n1. The Nun 2\n2. Insidious 5\n3. Evil Dead Rise")
    elif query.data == "comedy":
        await query.edit_message_text("😂 Comedy ရုပ်ရှင်များ:\n1. Barbie\n2. No Hard Feelings\n3. Super Mario Bros")
    elif query.data == "romance":
        await query.edit_message_text("💕 Romance ရုပ်ရှင်များ:\n1. Past Lives\n2. Anyone But You\n3. A Star is Born")
    elif query.data == "drama":
        await query.edit_message_text("🎥 Drama ရုပ်ရှင်များ:\n1. Oppenheimer\n2. Killers of the Flower Moon\n3. The Whale")
    elif query.data == "scifi":
        await query.edit_message_text("🤖 Sci-Fi ရုပ်ရှင်များ:\n1. Dune 2\n2. Avatar 2\n3. The Creator")
    elif query.data == "back":
        await query.edit_message_text("📽️ မူလမီနူးသို့ ပြန်သွားပါပြီ။ /movies နှိပ်ပါ။")

# Main function
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("movies", movies))
    app.add_handler(CommandHandler("search", search))
    app.add_handler(CommandHandler("genre", genre))
    app.add_handler(CommandHandler("request", request_movie))
    app.add_handler(CommandHandler("latest", latest))
    app.add_handler(CommandHandler("popular", popular))
    app.add_handler(CommandHandler("download", download))
    app.add_handler(CommandHandler("stream", stream))
    app.add_handler(CallbackQueryHandler(button_callback))
    
    print("🤖 Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
