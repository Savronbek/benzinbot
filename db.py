import sqlite3

from aiogram import Bot

TOKEN = "2130598875:AAFO9ZLU8_crI5caGkfDX5xjH9VSXX1rCTo"

bot = Bot(token=TOKEN, parse_mode="HTML")


class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Достаем id юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    async def all_users(self, message):
        for ret in self.cursor.execute("SELECT * FROM 'users'").fetchall():
            await bot.send_message(message.from_user.id, f"Количество пользователей: {ret}")
        return self.conn.commit()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()

