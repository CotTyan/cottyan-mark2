import discord
import os
import asyncio
import requests
client = discord.Client()

@client.event
async def on_message(message):
if massage.author.bot
    return
if message.content == "*gpg"
    await message.channel.send('GitHubに登録されているユーザーのGPG公開鍵を取得します ユーザー名を続けて入力して下さい')
    def check(command):
        return command.author == message.author
    c = await client.wailt_for('message', check=check)

    search = c.content
    count = 0
    baseurl = "https://github.com/"
    res = requests.get(url+c)
    await message.channel.send(res)