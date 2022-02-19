import asyncio
import os
import time
from os import listdir
from os import mkdir
import heroku3
from git import Repo
from rich.table import Table
from rich.console import Console
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as Bot
from git.exc import GitCommandError, InvalidGitRepositoryError

loop = asyncio.get_event_loop()
vps = Console()

UPDATE_BRANCH = "main"
UPDATE_REPO = "https://github.com/TG-TeamIndia/IndianMusicBot"
