import logging
import sys
import asyncio
from aiogram import Dispatcher,Bot,types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram import F

from inline import reply_menu, inline_menu

BOT_Token=("6537271263:AAGwM-mcv9k2mu6eY2eYydyQBpuahXBvbXs")
dp=Dispatcher()
bot=Bot(BOT_Token,parse_mode=ParseMode.HTML)


@dp.message(CommandStart())
async def start_hendl(msg:Message):
    await msg.answer(f"salom {msg.from_user.full_name}",reply_markup=reply_menu())


@dp.message(F.photo)
async def photo_hendl(msg:Message):
    await msg.answer("BU rasm",reply_markup=inline_menu())
    await msg.answer_photo(msg.photo[0].file_id)

@dp.message(F.document)
async def doc_hendl(msg:Message):
    await msg.answer(msg.document.file_id)

@dp.message(F.audio)
async def audio_hend(msg:Message):
    await msg.answer("bu audio")









@dp.message()
async def hend(msg:Message):
    await msg.answer(msg.id)

async def main():
    await dp.start_polling((bot))

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    asyncio.run(main())
