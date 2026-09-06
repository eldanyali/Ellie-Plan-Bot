\# Ellie 🌱



\## Plan. Learn. Grow.



Ellie is a Telegram personal assistant bot designed to help users with

planning, learning, progress tracking, task management, goal setting,

and habit building.



Ellie is designed to feel like a reliable companion for growth and

learning, not just a reminder bot.



\------------------------------------------------------------------------



\# Current Features



\## User Onboarding



New users go through:



1\.  Choosing a name

2\.  Reminder preference

3\.  Reminder time selection

4\.  Calendar selection

5\.  Entering the main menu



\------------------------------------------------------------------------



\## Task Management



Current task features:



\-   Add tasks

\-   View today's tasks

\-   Complete tasks

\-   Return completed tasks to active state

\-   Edit tasks

\-   Delete tasks



Task states:



&#x20;   pending

&#x20;   done



\------------------------------------------------------------------------



\## Main Menu



&#x20;   📋 برنامه امروز

&#x20;   ➕ افزودن کار

&#x20;   🎯 هدف های من

&#x20;   📊 گزارش من

&#x20;   ⚙️ تنظیمات



\------------------------------------------------------------------------



\# Technology



Built with:



\-   Python 3.12

\-   python-telegram-bot

\-   SQLite

\-   python-dotenv



\------------------------------------------------------------------------



\# Project Structure



&#x20;   ElliePlanBot



&#x20;   ├── main.py

&#x20;   ├── database.py

&#x20;   ├── requirements.txt

&#x20;   └── README.md



\------------------------------------------------------------------------



\# Setup



Install dependencies:



``` bash

pip install -r requirements.txt

```



Create `.env`:



&#x20;   BOT\_TOKEN=YOUR\_TELEGRAM\_BOT\_TOKEN



Run:



``` bash

python main.py

```



\------------------------------------------------------------------------



\# Security



Do not upload:



&#x20;   .env

&#x20;   ellie.db

&#x20;   venv/

&#x20;   \_\_pycache\_\_/



Reason:



\-   Environment files contain private tokens

\-   Database files may contain user data

\-   Virtual environments are system specific



\------------------------------------------------------------------------



\# Future Roadmap



\## Reminder System



Smart reminders that respect users and avoid becoming annoying.



\## Reports



Daily, weekly, and monthly progress reports.



\## Goals



Goal tracking with progress visualization.



\## Habit Tracker



Tracking habits such as:



\-   Learning

\-   Reading

\-   Exercise

\-   Coding



\## Streak System



Tracking consistent progress based on real completed activities.



\------------------------------------------------------------------------



\# Development Philosophy



Ellie is intentionally built with a simple architecture.



Goals:



\-   Clean code

\-   Easy maintenance

\-   Beginner friendly development

\-   Gradual feature growth



The project avoids unnecessary complexity during early stages.



\------------------------------------------------------------------------



\# Status



Ellie is currently under active development.

