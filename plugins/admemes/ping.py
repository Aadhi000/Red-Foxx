"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "വെറുതെ Alive അടിച്ചു വെറുപ്പിക്കാതട ഞൻ ഇവട ജീവനോടെ ഒക്കെ തന്നെയുണ്ട് ചത്തൊന്നും പോയിട്ടില്ല 🥲\n\n╔════❰ ᗩᒍᗩ᙭ ❱═❍☣
║╭━━━━━━━━━━━━━━━⏤͟͟͞͞★ 
║┣⪼ 𝙼𝚈 𝙽𝙰𝙼𝙴 - <a href="https://t.me/Devil0Bot_Bot"> ᗩᒍᗩ᙭ </a>
║┣⪼ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 𝙰 - <a href="https://t.me/Aadhi010"> 𝙰𝙰𝙳𝙷𝙸 </a>
║┣⪼ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 𝙱 - <a href="https://t.me/albintko"> 𝙰𝙻𝙱𝙸𝙽 </a>
║┣⪼ 𝙶𝚁𝙾𝚄𝙿 𝙰 - <a href="https://t.me/+EqhXLhL3T1w4Zjc1"> 𝙼𝙾𝚅𝙸𝙴𝚂 𝚆𝙾𝚁𝙻𝙳 </a>
║┣⪼ 𝙶𝚁𝙾𝚄𝙿 𝙱 - <a href="https://t.me/moviebus2"> 𝙵𝙸𝙻𝙼 𝙲𝙻𝚄𝙱 </a>
║┣⪼ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙰 - <a href="https://t.me/+ShU9T97lYysxZjFl"> 𝙵𝙲 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 </a>
║┣⪼ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙱 -  <a href="https://t.me/+veUIdIW2CQ5mOGU5"> 𝙼𝚆 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 </a>
║╰━━━━━━━━━━━━━━━⏤͟͟͞͞★ ╚══════════════════❍☣"
HELP = "Help ഒന്നും ഇല്ല ഓടിക്കോ...."
REPO = "https://github.com/Aadhi000/Adv-Ajax"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
