import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("13740761"))
API_HASH = os.getenv("4ce319a92c01fab2b02551af8d7f73a4")
SESSION = os.getenv("AgCXmLZz65Iap7uZHESrE_B5fzLdiZv5R2TOYAN-CL8EhmamM7YJcCNuh7Jd6mgSUYf1KbQbH60MwSUOb_WKIxPnux3RnMaFxx7NWij74zTYq9xWdYzFHOnZ4EUXbm_ZoYwGAY4UzbP50HztECOMhEIUEQptarGTCo4O88WIy3GTYFltviEazJElvPTK6871kPmjCrIuJYNuW7WTjbUAI2K8IKLXhRNcpFp1myipaK9TeL8VtZybfpXB7TTjmWh_pQToHDRTP_kBv-hx-q00P4C7wylDIq89zhxHpVxEpPDpcAYNKJBlZIJ4W3YqB5sltguEOFEzH3WZz3cwwGop_pq_AAAAAUf6DjgA")
HNDLR = os.getenv("HNDLR", "$")
SUDO_USERS = list(map(int, os.getenv("5502537272").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
