# Ellie 🌱

## Plan, Learn, Grow.

Ellie is a Telegram personal assistant bot designed to help users with:

- Planning
- Learning
- Progress tracking
- Task management
- Goal setting
- Habit building

Ellie is designed to feel like a reliable companion for growth and learning, not just a reminder bot.

---

# Current Features

## User Onboarding

New users go through:

1. Choosing a name
2. Reminder preference
3. Reminder time selection
4. Calendar selection
5. Entering the main menu

---

## Task Management

Current task features:

- Add tasks
- View today's tasks
- Complete tasks
- Return completed tasks to active state
- Edit tasks
- Delete tasks

Task states:

```text
pending
done
```

---

## Main Menu

```text
📋 برنامه امروز
➕ افزودن کار
🎯 هدف های من
📊 گزارش من
⚙️ تنظیمات
```

---

# Technology

Built with:

- Python 3.12
- python-telegram-bot
- SQLite
- python-dotenv

---

# Project Structure

```text
ElliePlanBot

├── main.py
├── database.py
├── requirements.txt
└── README.md
```

---

# Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```text
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

Run:

```bash
python main.py
```

---

# Security

Do not upload:

```text
.env
ellie.db
venv/
__pycache__/
```

Reason:

- Environment files contain private tokens
- Database files may contain user data
- Virtual environments are system specific

---

# Future Roadmap

## Reminder System

Smart reminders that respect users and avoid becoming annoying.

## Reports

Daily, weekly, and monthly progress reports.

## Goals

Goal tracking with progress visualization.

## Habit Tracker

Tracking habits such as:

- Learning
- Reading
- Exercise
- Coding

## Streak System

Tracking consistent progress based on real completed activities.

---

# Development Philosophy

Ellie is intentionally built with a simple architecture.

Goals:

- Clean code
- Easy maintenance
- Beginner friendly development
- Gradual feature growth

The project avoids unnecessary complexity during early development.

---

# Status

Ellie is currently under active development.
