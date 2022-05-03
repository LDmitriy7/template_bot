import asyncio

from aiogram import Bot
from aiogram.utils.exceptions import TelegramAPIError
from aiogram_utils.errors import suppress

import config
from loader import tm, bot, bot2, bot3, log


async def safe_edit(_bot: Bot, text: str):
    with suppress(TelegramAPIError, logger=log):
        await bot.edit_message_text(
            chat_id=config.Secret.channel_id,
            message_id=config.Secret.post_id,
            text=text,
        )


@tm.forever(sleep_time=0)
async def _():
    sleep_time = config.Secret.sleep_time
    texts = config.Secret.texts

    await safe_edit(bot, texts[0])
    await asyncio.sleep(sleep_time)
    await safe_edit(bot2, texts[1])
    await asyncio.sleep(sleep_time)
    await safe_edit(bot3, texts[2])
    await asyncio.sleep(sleep_time)
