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
async def on_ready():
    print(client.user.id)
    print('It is ready')
    channel = client.get_channel(hello_id)
    embed = discord.Embed(title="ただ今起動しました",description="動作していない場合は管理者に問い合わせてください")
    embed = embed.set_author(name="CotTyanからのお知らせ",icon_url="https://www.repo.approvers.dev/g2058.png")
    await channel.send(embed=embed)
    
@client.event
async def on_member_join(member):
    lrn = []
    for role in member.roles:
        lrn.append(role.name)
        if len(lrn) == 2:
            break
    m = "Hi!<@"+str(member.id)+">,\nPlease read <#736628061289578496> and type [ok]. \nIf you are going to to be able to do it, please introduse yourself in <#736627134604378143>\n"
    channel = client.get_channel(737576896476348447)
    await channel.send(m)
    

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '*cot.help!':
        embed = discord.Embed(title="CotTyanへるぷ", description="このヘルプを表示 `*cot.help!`\nボットについての情報を見る`*cot.about!`\n現在時刻を表示[Ruby]`*cot.daemon.time!`\n 機能追加はまだまだこれからですので気を長くしてお待ちください", color=0x00ccff)
        embed = embed.set_author(name="COTTYAN MARK II by laminne", url="https://github.com/laminne", icon_url="https://www.repo.approvers.dev/g2058.png")
        embed.set_footer(text="ふぇぇ、恥ずかしいよぅ(*ﾉωﾉ)")
        await channel.send(embed=embed)
    if message.content == '*cot.about!':
        embed = discord.Embed(title="CotTyanについて", description="Laminne33569がコマンド部分をPython、コマンド実行部分をRubyで書いたボットです\n仕組みとしてはコマンドを取得し\nRubyのコードを実行、出力の成形を行い、\nそれをPythonで受け取り送信しています\nデプロイ先はVPSですのでいろいろできます", color=0x00ccff)
        embed = embed.set_author(name="COTTYAN MARK II by laminne", url="https://github.com/laminne", icon_url="https://www.repo.approvers.dev/g2058.png")
        embed.set_footer(text="ちゃんと自己紹介できるもん！")
        await channel.send(embed=embed)
    if message.content == '*cot.daemon.time!':
        ruby = subprocess.check_output(['/root/.rbenv/shims/ruby', '/root/cottyan-mark2/main.rb'])
        m = ruby.decode()
        ruby = m.replace('"','')
        await message.channel.send(ruby.replace('"',''))
    if message.guild.id == server_id:
        if message.content == "ok":
            lrn = []
            for role in message.author.roles:
                lrn.append(role.name)
                if len(lrn) == 2:
                    return
            role = discord.utils.get(message.guild.roles, name="自己紹介してね")
            return await message.author.add_roles(role)

if __name__ == "__main__":
    client.run(TOKEN)
