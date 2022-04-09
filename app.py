#from aiogram import executor
from aiogram.utils.executor import start_webhook

from loader import dp, bot
from data import config
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await bot.set_webhook(config.WEBHOOK_URL)
    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)


async def on_shutdown(dp):
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    start_webhook(
            dispatcher=dp,
            webhook_path=config.WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=False,
            host=config.WEBAPP_HOST,
            port=config.WEBAPP_PORT
    )