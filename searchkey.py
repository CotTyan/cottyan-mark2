import discord
import os
import asyncio
import requests
from urllib.parse import urljoin

client = discord.Client()


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "*gpg":
        await message.channel.send("GitHubに登録されているユーザーのGPG公開鍵を取得します ユーザー名を続けて入力して下さい")

        def check(command):
            return command.author == message.author

        c = await client.wait_for("message", check=check)
    # c = await client.wait_for("message")

    search = c.content
    count = 0
    print(search)
    search = str(search)
    search = search.lower()
    baseurl = "https://github.com/"
    # username = search + ".gpg"
    url = urljoin("https://github.com/", search)
    url = url + ".gpg"
    print(url)
    res = requests.get(url)
    if res.status_code == requests.codes.ok:
        print(res.text)
        name = search + ".gpg"
        f = open(name, "w")
        f.write(res.text)
        f.close()
        await message.channel.send(file=discord.File(name))
        os.remove(name)
    else:
        await message.channel.send("ユーザーが存在しませんでした\nもう一度やり直してください")



client.run("")
