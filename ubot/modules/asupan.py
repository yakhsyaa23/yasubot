from ubot import *

__MODULE__ = "Asupan"
__HELP__ = """
 Bantuan Untuk Asupan

• Perintah :  <code>{0}asupan</code>
• Penjelasan :  Untuk mengirim video asupan random.

• Perintah : <code>{0}bokep</code>
• Penjelasan : Untuk mengirim video bokep random.

• Perintah :  <code>{0}cewe</code>
• Penjelasan :  Untuk mengirim photo cewek random.

• Perintah : <code>{0}cowo</code>
• Penjelasan : Untuk mengirim photo cowok random.

• Perintah :  <code>{0}anime</code>
• Penjelasan :  Untuk mengirim photo anime random.
"""


@PY.UBOT("asupan", sudo=True)
async def _(client, message):
    await video_asupan(client, message)


@PY.UBOT("cewek", sudo=True)
async def _(client, message):
    await photo_cewek(client, message)


@PY.UBOT("cowok", sudo=True)
async def _(client, message):
    await photo_cowok(client, message)


@PY.UBOT("anime", sudo=True)
async def _(client, message):
    await photo_anime(client, message)


@PY.UBOT("bokep", sudo=True)
async def _(client, message):
    await video_bokep(client, message)
