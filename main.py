from telegram import Update, ChatPermissions
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8417423139:AAHc6ECFwjg6fr938CMn8-jbzYkD9x1iUiw"

# Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot Active hai!")

# Help
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
/ban - reply karke ban
/kick - reply karke kick
/mute - reply karke mute
/unmute - unmute
""")

# Ban
async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        await update.effective_chat.ban_member(user_id)
        await update.message.reply_text("✅ User banned")
    else:
        await update.message.reply_text("Reply karke use karo")

# Kick
async def kick(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        await update.effective_chat.ban_member(user_id)
        await update.effective_chat.unban_member(user_id)
        await update.message.reply_text("✅ User kicked")
    else:
        await update.message.reply_text("Reply karke use karo")

# Mute
async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        permissions = ChatPermissions(can_send_messages=False)
        await update.effective_chat.restrict_member(user_id, permissions)
        await update.message.reply_text("🔇 Muted")
    else:
        await update.message.reply_text("Reply karke use karo")

# Unmute
async def unmute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        permissions = ChatPermissions(can_send_messages=True)
        await update.effective_chat.restrict_member(user_id, permissions)
        await update.message.reply_text("🔊 Unmuted")
    else:
        await update.message.reply_text("Reply karke use karo")

# App start
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("ban", ban))
app.add_handler(CommandHandler("kick", kick))
app.add_handler(CommandHandler("mute", mute))
app.add_handler(CommandHandler("unmute", unmute))

print("Bot chal raha hai...")
app.run_polling()
