# -*- coding: utf-8 -*-
import asyncio
import discord
import subprocess
import os

server_id = 665189315877535753

server_id = int(server_id)

client = discord.Client()

async def send(channel,*args, **kwargs): return await channel.send(*args, **kwargs)
 
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '*cot.help!':
        help = random.choice('ふぇぇ、恥ずかしいよぅ(*ﾉωﾉ)', 'ちゃんと動作してる、よね？', 'おしごとおしごと！', 'ねぇねぇ、きいてきいて？', 'あのねあのね？')
        embed = discord.Embed(title="CotTyanへるぷ", description="このヘルプを表示 `*cot.help!`\nボットについての情報を見る`*cot.about!`\n現在時刻を表示[Ruby]`*cot.daemon.time!`\nメンテナンス通知を出す`*cot.develop!`\n※<@487393376078004225>にしか使えません\n機能追加はまだまだこれからですので気を長くしてお待ちください", color=0x00ccff)
        embed = embed.set_author(name="COTTYAN MARK II by laminne", url="https://github.com/laminne", icon_url="https://www.repo.approvers.dev/g2058.png")
        embed = embed.set_thumbnail(url="https://www.repo.approvers.dev/g2058.png")
        embed = embed.set_footer(text=help)
        await message.channel.send(embed=embed)
    if message.content == '*cot.about!':
        about = random.choice('ふぇぇ、恥ずかしいよぅ(*ﾉωﾉ)', 'ちゃんと動作してる、よね？', 'おしごとおしごと！', 'ねぇねぇ、きいてきいて？', 'あのねあのね？')
        embed = discord.Embed(title="CotTyanについて", description="Laminne33569がコマンド部分をPython、実行部分(ほんの一部)をRubyで書いたボットです\n仕組みとしてはコマンドを取得し\nRubyのコードを実行、出力の成形を行い、\nそれをPythonで受け取り送信しています\nデプロイ先はVPSですのでいろいろできます", color=0x00ccff)
        embed = embed.set_author(name="COTTYAN MARK II by laminne", url="https://github.com/laminne", icon_url="https://www.repo.approvers.dev/g2058.png")
        embed = embed.set_thumbnail(url="https://www.repo.approvers.dev/g2058.png")
        embed = embed.set_footer(text=about)
        await message.channel.send(embed=embed)
    if message.content == '*cot.daemon.time!':
        ruby = subprocess.check_output(['/root/.rbenv/shims/ruby', '/root/cottyan-mark2/main.rb'])
        m = ruby.decode()
        ruby = m.replace('"','')
        await message.channel.send(ruby.replace('"',''))
    if message.author.id == 487393376078004225:
        if message.content == "*cot.develop!":
            #a = message.author
            #print(a)
            text = random.choice('ふぇぇ、恥ずかしいよぅ(*ﾉωﾉ)', 'ちゃんと動作してる、よね？', 'おしごとおしごと！', 'ねぇねぇ、きいてきいて？', 'あのねあのね？')
            embed = discord.Embed(title="ボットが止まります",description="ボットが再起動、またはメンテナンス等に入るためオフラインになります", color=0x00ccff)
            embed = embed.set_author(name="CotTyanからのお知らせ",icon_url="https://www.repo.approvers.dev/g2058.png")
            embed = embed.set_thumbnail(url="https://www.repo.approvers.dev/g2058.png")
            embed = embed.set_footer(text=text)
            await message.channnel.send(embed=embed)
    else:
        #print(message.content)
        print(message.author.id)
        print("fail")

if __name__ == "__main__":
    client.run(os.environ['MARK1_TOKEN'])