
import os
from datetime import datetime

from database import (
    create_database,
    add_user,
    get_user,
    update_user_settings,
    add_task,
    get_tasks,
    get_task,
    update_task,
    complete_task,
    reopen_task,
    delete_task
)

from dotenv import load_dotenv

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


def main_menu():
    keyboard = [
        ["📋 برنامه امروز"],
        ["➕ افزودن کار"],
        ["🎯 هدف های من", "📊 گزارش من"],
        ["⚙️ تنظیمات"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


def create_time_keyboard(page):

    buttons = []

    start = 0 if page == 1 else 12
    end = 12 if page == 1 else 24

    row = []

    for hour in range(start, end):

        row.append(
            InlineKeyboardButton(
                f"{hour:02d}:00",
                callback_data=f"time_{hour:02d}:00"
            )
        )

        if len(row) == 3:
            buttons.append(row)
            row = []

    if row:
        buttons.append(row)

    if page == 1:
        buttons.append(
            [
                InlineKeyboardButton(
                    "ساعت های بعدی ➡️",
                    callback_data="time_page_2"
                )
            ]
        )
    else:
        buttons.append(
            [
                InlineKeyboardButton(
                    "⬅️ ساعت های قبلی",
                    callback_data="time_page_1"
                )
            ]
        )

    return InlineKeyboardMarkup(buttons)

def task_keyboard(tasks):

    buttons = []

    for task in tasks:

        icon = "✅" if task[3] == "done" else "▫️"

        buttons.append(
            [
                InlineKeyboardButton(
                    f"{icon} {task[2]}",
                    callback_data=f"task_{task[0]}"
                )
            ]
        )

    return InlineKeyboardMarkup(buttons)



def task_action_keyboard(task):

    buttons = []


    if task[3] == "done":

        buttons.append(
            [
                InlineKeyboardButton(
                    "↩️ برگشت به انجام نشده",
                    callback_data="reopen_task"
                )
            ]
        )

    else:

        buttons.append(
            [
                InlineKeyboardButton(
                    "✅ انجام شد",
                    callback_data="complete_task"
                )
            ]
        )


    buttons.append(
        [
            InlineKeyboardButton(
                "✏️ ویرایش",
                callback_data="edit_task"
            )
        ]
    )


    buttons.append(
        [
            InlineKeyboardButton(
                "🗑 حذف",
                callback_data="delete_task"
            )
        ]
    )


    return InlineKeyboardMarkup(buttons)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    saved_user = get_user(user.id)

    if saved_user:
        await update.message.reply_text(
            f"خوش برگشتی {saved_user[2]} 🌱",
            reply_markup=main_menu()
        )
        return

    context.user_data["step"] = "name"

    await update.message.reply_text(
        "سلام، من Ellie هستم ✨\n\n"
        "برای شروع چی صدات کنم؟"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
راهنمایی ✨

📋 برنامه امروز:

دیدن و مدیریت کارهای امروزت

➕ افزودن کار:

اضافه کردن یک کار جدید

🎯 هدف های من:

هدف هایی که برای خودت انتخاب کردی

📊 گزارش من:

دیدن پیشرفت ات

⚙️ تنظیمات:

تغییر تنظیمات و اطلاعاتت
"""

    await update.message.reply_text(
        text,
        reply_markup=main_menu()
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user = update.effective_user
    step = context.user_data.get("step")
    saved_user = get_user(user.id)

    main_buttons = [
        "📋 برنامه امروز",
        "➕ افزودن کار",
        "🎯 هدف های من",
        "📊 گزارش من",
        "⚙️ تنظیمات"
    ]


    if text in main_buttons and not saved_user:

        await update.message.reply_text(
            "هنوز ثبت نام نکردی 🌱\n"
            "ابتدا /start را بزن تا بشناسمت"
        )

        return

    if text == "➕ افزودن کار":

        context.user_data["step"] = "add_task"

        await update.message.reply_text(
            "چه کاری می خوای اضافه کنی؟"
        )
        return


    if text == "📋 برنامه امروز":

        user_data = get_user(user.id)

        tasks = get_tasks(user_data[0])

        if not tasks:
            await update.message.reply_text(
                "هنوز کاری ثبت نکردی 🌱",
                reply_markup=main_menu()
            )
            return

        await update.message.reply_text(
            "برنامه امروز:",
            reply_markup=task_keyboard(tasks)
        )
        return


    if text == "🎯 هدف های من":
        await update.message.reply_text(
            "این بخش در حال آماده سازی است."
        )
        return


    if text == "📊 گزارش من":
        await update.message.reply_text(
            "این بخش در حال آماده سازی است."
        )
        return


    if text == "⚙️ تنظیمات":
        await update.message.reply_text(
            "این بخش در حال آماده سازی است."
        )
        return


    if step == "name":

        add_user(user.id, text)

        context.user_data["step"] = "reminder"

        keyboard = [
            ["بله", "نه"]
        ]

        await update.message.reply_text(
            f"خوشحالم از آشناییت {text} 🤝🏻\n"
            "دوست داری کارهات را هر روز بهت یادآوری کنم؟",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )


    elif step == "reminder":

        if text == "بله":

            context.user_data["reminder_enabled"] = "yes"
            context.user_data["step"] = "time"

            await update.message.reply_text(
                "چه ساعتی هر روز بهت یادآوری بشه؟",
                reply_markup=ReplyKeyboardRemove()
            )

            await update.message.reply_text(
                "ساعت را انتخاب کن:",
                reply_markup=create_time_keyboard(1)
            )

        else:

            context.user_data["reminder_enabled"] = "no"
            context.user_data["reminder_time"] = None
            context.user_data["step"] = "calendar"

            keyboard = [
                ["شمسی", "میلادی"]
            ]

            await update.message.reply_text(
                "تقویم مورد علاقه ات را انتخاب کن:\n\n"
                "شمسی یا میلادی؟",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard,
                    resize_keyboard=True
                )
            )


    elif step == "calendar":

        context.user_data["calendar_type"] = text

        update_user_settings(
            user.id,
            context.user_data.get("reminder_enabled"),
            context.user_data.get("reminder_time"),
            context.user_data.get("calendar_type")
        )

        context.user_data.clear()

        await update.message.reply_text(
            "عالیه، از اینجا به بعد می توانیم برنامه ها و هدف هایت را دنبال کنیم",
            reply_markup=main_menu()
        )

    elif step == "edit_task":

        task_id = context.user_data.get(
            "selected_task"
        )

        update_task(
            task_id,
            text
        )

        context.user_data.clear()

        await update.message.reply_text(
            "کار ویرایش شد ✨",
            reply_markup=main_menu()
        )

        return

    elif step == "add_task":

        user_data = get_user(user.id)

        add_task(
            user_data[0],
            text,
            datetime.now().strftime("%Y-%m-%d")
        )

        context.user_data.clear()

        await update.message.reply_text(
            "کار اضافه شد 🌱",
            reply_markup=main_menu()
        )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data.startswith("task_"):

        task_id = int(
            data.replace("task_", "")
        )

        task = get_task(task_id)

        if not task:
            await query.message.reply_text(
                "این کار پیدا نشد."
            )
            return

        context.user_data["selected_task"] = task_id

        await query.message.reply_text(
            task[2],
            reply_markup=task_action_keyboard(task)
        )

        return

    
    if data == "time_page_2":
        await query.edit_message_reply_markup(
            reply_markup=create_time_keyboard(2)
        )
        return

    if data == "time_page_1":
        await query.edit_message_reply_markup(
            reply_markup=create_time_keyboard(1)
        )
        return

    if data.startswith("time_"):

        selected_time = data.replace("time_", "")

        context.user_data["reminder_time"] = selected_time
        context.user_data["step"] = "calendar"

        keyboard = [
            ["شمسی", "میلادی"]
        ]

        await query.message.reply_text(
            "تقویم مورد علاقه ات را انتخاب کن:\n\n"
            "شمسی یا میلادی؟",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    task_id = context.user_data.get("selected_task")

    if not task_id:
        return


    if data == "complete_task":

        complete_task(task_id)

        await query.message.reply_text(
            "کار انجام شد ✅",
            reply_markup=main_menu()
        )


    elif data == "reopen_task":

        reopen_task(task_id)

        await query.message.reply_text(
            "کار دوباره به لیست فعال برگشت 🌱",
            reply_markup=main_menu()
        )


    elif data == "delete_task":

        delete_task(task_id)

        await query.message.reply_text(
            "کار حذف شد 🗑",
            reply_markup=main_menu()
        )


    elif data == "edit_task":

        context.user_data["step"] = "edit_task"

        await query.message.reply_text(
            "متن جدید کار را وارد کن:"
        )

        return


def main():

    create_database()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
    CommandHandler("help", help_command)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print("Ellie is running...")

    app.run_polling()


if __name__ == "__main__":
    main()