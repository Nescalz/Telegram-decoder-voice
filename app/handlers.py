from aiogram import F, Router, Bot
from aiogram.types import Message, ContentType, File
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
import speech_recognition as sr
import os 
from pathlib import Path
router = Router()

root_path = Path(__file__).resolve().parents[1]

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(f"Отправте голосовое сообщение, а я его расшифрую!")

@router.message(Command("help"))
async def apels(message: Message):
    await message.answer(f"Отправте голосовое сообщение, а я его расшифрую!")

@router.message(F.content_type == ContentType.VOICE)
async def cmd_start(message: Message, state: FSMContext, bot: Bot):
    msg = await message.answer(f"Скачиваю...")

    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"{message.message_id}.ogg")

    await msg.edit_text(f"Переделываю в нужный формат...")

    os.system(f"C:\\FFmpeg\\bin\\ffmpeg.exe -i {root_path}\\{message.message_id}.ogg {root_path}\\{message.message_id}.wav")
    
    await msg.edit_text(f"Начинаю расшифровывать...")
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(f"{root_path}\\{message.message_id}.wav")
    with audio_file as source:
        audio_data =  recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="ru-RU")

    os.system(f"del {root_path}\\{message.message_id}.ogg")
    os.system(f"del {root_path}\\{message.message_id}.wav")

    await message.answer(f"Расшифровка:\n{text}")
