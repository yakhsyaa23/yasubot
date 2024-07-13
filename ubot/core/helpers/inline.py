import re

from pykeyboard import InlineKeyboard
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from ubot import *


class Button:
    def alive(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="Close",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ]
        ]
        return button

    def button_add_expired(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} Month",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton("Account Link", callback_data=f"profil {user_id}")
        )
        buttons.row(
            InlineKeyboardButton("Reject Payment", callback_data=f"failed {user_id}")
        )
        return buttons

    def deak(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "Return ",
                    callback_data=f"prev_ub {int(count)}",
                ),
                InlineKeyboardButton(
                    "Approve", callback_data=f"deak_akun {int(count)}"
                ),
            ],
        ]
        return button

    def expired_button_bot():
        button = [
            [
                InlineKeyboardButton(
                    text=f"{bot.me.first_name}",
                    url=f"https://t.me/{bot.me.username}",
                )
            ]
        ]
        return button

    def start(message):
        if message.from_user.id not in USER_ID:
            button = [
                [InlineKeyboardButton("Create a Userbot", callback_data="bahan")],
                [
                    InlineKeyboardButton("Tutorial", callback_data="cb_tutor"),
                    InlineKeyboardButton(
                        "Account Status", callback_data="start_profile"
                    ),
                ],
            ]
        else:
            button = [
                [InlineKeyboardButton("Create a Userbot", callback_data="bahan")],
                [
                    InlineKeyboardButton("Updates", callback_data="gitpull"),
                    InlineKeyboardButton("Restart", callback_data="restart"),
                ],
                [
                    InlineKeyboardButton("User Check", callback_data="cek_ubot"),
                    InlineKeyboardButton("Hosting", callback_data="host"),
                ],
            ]
        return button

    def plus_minus(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-1",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+1",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("Confirmation", callback_data="confirm")],
            [InlineKeyboardButton("Cancel", callback_data=f"home {user_id}")],
        ]
        return button

    def userbot(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "Delete From Database",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check Number",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check Expiry",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check OTP",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check 2L Verification",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [InlineKeyboardButton("Destroyed", callback_data=f"ub_deak {int(count)}")],
            [
                InlineKeyboardButton("❮", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("❯", callback_data=f"next_ub {int(count)}"),
            ],
            [
                InlineKeyboardButton("Tutup", callback_data=f"0_cls"),
            ],
        ]
        return button

    def ambil_akun(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "Delete From Database",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check Number",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check Expiry",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check OTP",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Check 2L Verification",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [InlineKeyboardButton("Destroyed", callback_data=f"ub_deak {int(count)}")],
            [
                InlineKeyboardButton("❮", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("❯", callback_data=f"next_ub {int(count)}"),
            ],
        ]
        return button


class INLINE:
    def QUERY(func):
        async def wrapper(client, inline_query):
            users = ubot._get_my_id
            if inline_query.from_user.id not in users:
                await client.answer_inline_query(
                    inline_query.id,
                    cache_time=0,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title=f"Anda Belum Melakukan Pembelian @{bot.me.username}",
                                input_message_content=InputTextMessageContent(
                                    f"Kamu Bisa Melakukan Pembelian @{bot.me.username} Agar Bisa Menggunakan"
                                ),
                            )
                        )
                    ],
                )
            else:
                await func(client, inline_query)

        return wrapper

    def DATA(func):
        async def wrapper(client, callback_query):
            users = ubot._get_my_id
            if callback_query.from_user.id not in users:
                await callback_query.answer(
                    f"Silakan Order Bot @{bot.me.username} Agar Bisa Menggunakan Bot Ini",
                    True,
                )
            else:
                try:
                    await func(client, callback_query)
                except MessageNotModified:
                    await callback_query.answer("❌ ERROR")

        return wrapper


async def create_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    msg = []
    if "~" not in m.text.split(None, 1)[1]:
        for X in m.text.split(None, 1)[1].split():
            X_parts = X.split("|", 1)
            keyboard.append(
                InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1])
            )
            msg.append(X_parts[0])
        buttons.add(*keyboard)
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            text = " ".join(msg)
    else:
        for X in m.text.split("~", 1)[1].split():
            X_parts = X.split("|", 1)
            keyboard.append(
                InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1])
            )
        buttons.add(*keyboard)
        text = m.text.split("~", 1)[0].split(None, 1)[1]

    return buttons, text


async def gcast_create_button(m):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = m.text.split("~", 1)
    for X in split_text[1].split():
        button_data = X.split("|", 1)
        button_label = button_data[0].replace("_", " ")
        button_url = button_data[1]
        keyboard.append(InlineKeyboardButton(button_label, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0].split(None, 1)[1]
    return buttons, text_button


async def notes_create_button(text):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    for button_text in re.findall(r"\[(.*?)\]", text):
        button_label, button_url = button_text.split("|")
        keyboard.append(InlineKeyboardButton(button_label, url=button_url))
    buttons.add(*keyboard)
    text_button = re.sub(r"\[(.*?)\]", "", text)
    return buttons, text_button
