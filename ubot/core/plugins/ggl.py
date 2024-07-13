import re
import urllib
import urllib.request

from search_engine_parser import GoogleSearch

from ubot import *

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


async def gsearch(client, message):
    webevent = await message.reply("`Searching Google...`")
    match = get_arg(message)
    if not match:
        await webevent.edit("`Give me some to search..`")
        return
    page = re.findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"- [{title}]({link})\n**{desc}**\n\n"
        except IndexError:
            break
    await webevent.edit("**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg)
