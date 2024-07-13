from ubot import *

__MODULE__ = "Copy"
__HELP__ = """
 Bantuan Untuk Copy

• Perintah : <code>{0}copy</code> [link]
• Penjelasan : Untuk mengambil pesan melalui link telegram.
  """


@PY.BOT("copy")
async def _(client, message):
    await copy_bot_msg(client, message)


@PY.UBOT("copy", sudo=True)
async def _(client, message):
    await copy_ubot_msg(client, message)


@PY.UBOT("ccopy")
async def _(client, message):
    await cancel_nyolong(client, message)


@PY.INLINE("^get_msg")
@INLINE.QUERY
async def _(client, inline_query):
    await copy_inline_msg(client, inline_query)


@PY.CALLBACK("^copymsg")
@INLINE.DATA
async def _(client, callback_query):
    await copy_callback_msg(client, callback_query)
