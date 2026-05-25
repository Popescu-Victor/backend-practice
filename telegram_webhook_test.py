from typing import Final
import dotenv
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
from fastapi import FastAPI
import sqlalchemy as sa
import json
import requests
import worldnewsapi


TELEGRAM_TOKEN = dotenv.get_key(".env", "TELEGRAM_TOKEN")
WN_TOKEN = dotenv.get_key(".env", "WNAPI")