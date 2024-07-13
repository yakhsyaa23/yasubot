from ubot import *

__MODULE__ = "Global"
__HELP__ = """
 Bantuan Untuk Global

• Perintah : <code>{0}gban</ᴄᴏᴅᴇ> [user_id/username/bales pesan]
• Penjelasan : Untuk melakukan global banned.

• Perintah : <code>{0}ungban</code> [user_id/username/bales pesan]
• Penjelasan : Untuk melakukan global banned.

• Perintah : <code>{0}listgban</code> [user_id/username/bales pesan]
• Penjelasan : Untuk melihat daftar pengguna gban.
"""


@PY.UBOT("gban", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("cgban", "") & ~filters.me)
async def _(client, message):
    await global_banned(client, message)


@PY.UBOT("ungban", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("cungban", "") & ~filters.me)
async def _(client, message):
    await cung_ban(client, message)


@PY.UBOT("listgban", sudo=True)
async def _(client, message):
    await gbanlist(client, message)
