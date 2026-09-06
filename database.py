import sqlite3


DB_NAME = "ellie.db"


# --------------------
# Database
# --------------------

def create_database():

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY,

        telegram_id INTEGER UNIQUE,

        name TEXT,

        reminder_enabled TEXT,

        reminder_time TEXT,

        calendar_type TEXT

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (

        id INTEGER PRIMARY KEY,

        user_id INTEGER,

        title TEXT,

        status TEXT,

        created_at TEXT,

        FOREIGN KEY(user_id)
        REFERENCES users(id)

    )
    """)


    connection.commit()
    connection.close()



# --------------------
# Users
# --------------------

def add_user(telegram_id, name):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO users (

            telegram_id,

            name

        )

        VALUES (?, ?)
        """,
        (
            telegram_id,
            name
        )
    )


    connection.commit()
    connection.close()



def get_user(telegram_id):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *

        FROM users

        WHERE telegram_id = ?

        """,
        (
            telegram_id,
        )
    )


    user = cursor.fetchone()


    connection.close()

    return user



def update_user_settings(
        telegram_id,
        reminder_enabled,
        reminder_time,
        calendar_type
):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE users

        SET

        reminder_enabled = ?,

        reminder_time = ?,

        calendar_type = ?

        WHERE telegram_id = ?

        """,
        (
            reminder_enabled,
            reminder_time,
            calendar_type,
            telegram_id
        )
    )


    connection.commit()
    connection.close()



# --------------------
# Tasks
# --------------------


def add_task(user_id, title, created_at):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO tasks (

            user_id,

            title,

            status,

            created_at

        )

        VALUES (?, ?, ?, ?)

        """,
        (
            user_id,

            title,

            "pending",

            created_at
        )
    )


    connection.commit()
    connection.close()



def get_tasks(user_id):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *

        FROM tasks

        WHERE user_id = ?

        ORDER BY id DESC

        """,
        (
            user_id,
        )
    )


    tasks = cursor.fetchall()


    connection.close()

    return tasks



def get_task(task_id):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *

        FROM tasks

        WHERE id = ?

        """,
        (
            task_id,
        )
    )


    task = cursor.fetchone()


    connection.close()

    return task



def update_task(task_id, new_title):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE tasks

        SET title = ?

        WHERE id = ?

        """,
        (
            new_title,

            task_id
        )
    )


    connection.commit()
    connection.close()



def complete_task(task_id):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE tasks

        SET status = ?

        WHERE id = ?

        """,
        (
            "done",

            task_id
        )
    )


    connection.commit()
    connection.close()



def reopen_task(task_id):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE tasks

        SET status = ?

        WHERE id = ?

        """,
        (
            "pending",

            task_id
        )
    )


    connection.commit()
    connection.close()



def delete_task(task_id):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute(
        """
        DELETE FROM tasks

        WHERE id = ?

        """,
        (
            task_id,
        )
    )


    connection.commit()
    connection.close()