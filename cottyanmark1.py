# -*- coding: utf-8 -*-
import asyncio
import discord
import subprocess
import os
TOKEN = ""
entry_id = 736628061289578496
server_id = 736622331178254426
hello_id = 737068025253200069

server_id = int(server_id)
entry_id = int(entry_id)
hello_id = int(hello_id)
client = discord.Client()

async def send(channel,*args, **kwargs): return await channel.send(*args, **kwargs)
 

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '*cot.help!':
        embed = discord.Embed(title="CotTyanへるぷ", description="このヘルプを表示 `*cot.help!`\nボットについての情報を見る`*cot.about!`\n現在時刻を表示[Ruby]`*cot.daemon.time!`\n 機能追加はまだまだこれからですので気を長くしてお待ちください", color=0x00ccff)
        embed = embed.set_author(name="COTTYAN MARK II by laminne", url="https://github.com/laminne", icon_url="https://www.repo.approvers.dev/g2058.png")
        embed = embed.set_thumbnail(url="https://www.repo.approvers.dev/g2058.png")
        embed = embed.set_footer(text="ふぇぇ、恥ずかしいよぅ(*ﾉωﾉ)")
        await channel.send(embed=embed)
    if message.content == '*cot.about!':
        embed = discord.Embed(title="CotTyanについて", description="Laminne33569がコマンド部分をPython、コマンド実行部分をRubyで書いたボットです\n仕組みとしてはコマンドを取得し\nRubyのコードを実行、出力の成形を行い、\nそれをPythonで受け取り送信しています\nデプロイ先はVPSですのでいろいろできます", color=0x00ccff)
        embed = embed.set_author(name="COTTYAN MARK II by laminne", url="https://github.com/laminne", icon_url="https://www.repo.approvers.dev/g2058.png")
        embed = embed.set_thumbnail(url="https://www.repo.approvers.dev/g2058.png")
        embed = embed.set_footer(text="ちゃんと自己紹介できるもん！")
        await channel.send(embed=embed)
    if message.content == '*cot.daemon.time!':
        ruby = subprocess.check_output(['/root/.rbenv/shims/ruby', '/root/cottyan-mark2/main.rb'])
        m = ruby.decode()
        ruby = m.replace('"','')
        await message.channel.send(ruby.replace('"',''))

if __name__ == "__main__":
    client.run(TOKEN)
