import openai
from aiogram import types
from aiogram.utils import executor

from main import dp, bot
openai.api_key = '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'


@dp.message_handler(commands = "start")
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

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


