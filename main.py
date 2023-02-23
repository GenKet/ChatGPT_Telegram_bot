from aiogram import Dispatcher, Bot, executor, types
import asyncio
from config import BOT_TOKEN
import openai

loop = asyncio.new_event_loop()
bot  = Bot(BOT_TOKEN, parse_mode='HTML')
dp   = Dispatcher(bot, loop=loop)

openai.api_key = 'YOUR_OPEN_API_KEY'

@dp.message_handler(commands= "start")
async def start(message: types.Message):
        await message.bot.send_message(message.from_user.id,"Привет, задай свой вопрос")

@dp.message_handler()
async def generate_response(message: types.Message):
        response = await openai.Completion.acreate(
            engine="text-davinci-003",
            prompt=message.text,
            temperature=0.5,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0,
        )
        await message.answer(response['choices'][0]['text'])




if __name__ == '__main__':
    from handlers import dp

executor.start_polling(dp)
