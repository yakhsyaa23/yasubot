from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import *

from ubot import (DEVS, get_expired_date, get_prefix, get_seles, get_time,
                  start_time, ubot)

# from .str import *


async def profile_command(client, message):
    dia = message.from_user.id
    my_id = []
    for _ubot_ in ubot._ubot:
        my_id.append(_ubot_.me.id)
    if dia in my_id:
        status2 = "aktif"
    else:
        status2 = "tidak aktif"
    if dia in DEVS:
        status = "<b>premium</b> <code>[kepala toko]</code>"
    elif dia in await get_seles():
        status = "<b>premium</b> <code>[kasir]</code>"
    else:
        status = "<b>premium</b> <code>[pembeli]</code>"

    uptime = await get_time((time() - start_time))
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    (end - start).microseconds / 1000
    exp = await get_expired_date(dia)
    prefix = await get_prefix(dia)
    habis = exp.strftime("%d.%m.%Y") if exp else "None"
    "Aktif" if habis else "Nonaktif"
    b = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="Tutup", callback_data="0_cls")]]
    )
    await message.reply_text(
        f"""
<b>HimiUbot</b>
    <b>Status Ubot:</b> <code>{status2}</code>
      <b>Status Pengguna:</b> <i>{status}</i>
      <b>Prefixes :</b> <code>{prefix[0]}</code>
      <b>Tanggal Kedaluwarsa:</b> <code>{habis}</code>
      <b>Uptime Ubot:</b> <code>{uptime}</code>
""",
        reply_markup=b,
    )


async def ewdsfgj(client, callback_query):
    user_id = callback_query.from_user.id
    my_id = []
    for _ubot_ in ubot._ubot:
        my_id.append(_ubot_.me.id)

    if user_id in my_id:
        status2 = "aktif"
    else:
        status2 = "tidak aktif"

    if user_id in DEVS:
        status = "<b>premium</b> <code>[kepala toko]</code>"
    elif user_id in await get_seles():
        status = "<b>premium</b> <code>[kasir]</code>"
    else:
        status = "<b>premium</b> <code>[pembeli]</code>"
    uptime = await get_time((time() - start_time))
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    (end - start).microseconds / 1000
    exp = await get_expired_date(user_id)
    habis = exp.strftime("%d.%m.%Y") if exp else "None"
    prefix = await get_prefix(user_id)
    ubotstatus = "Aktif" if habis else "Nonaktif"

    if ubotstatus == "Nonaktif":
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Buat Userbot", callback_data="start_pmb"
                    ),
                ],
                [
                    InlineKeyboardButton(text="Kembali", callback_data="start0"),
                    InlineKeyboardButton(text="Tutup", callback_data="0_cls"),
                ],
            ]
        )
    else:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Kembali", callback_data="start0"),
                    InlineKeyboardButton(text="Tutup", callback_data="0_cls"),
                ],
            ]
        )

    await callback_query.edit_message_text(
        f"""
<b>HimiUbot</b>
    <b>Status Ubot:</b> <code>{status2}</code>
      <b>Status Pengguna:</b> <i>{status}</i>
      <b>Prefixes :</b> <code>{prefix[0]}</code>
      <b>Tanggal Kedaluwarsa:</b> <code>{habis}</code>
      <b>Uptime Ubot:</b> <code>{uptime}</code>
""",
        reply_markup=keyboard,
    )
