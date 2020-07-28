# -*- coding: utf-8 -*-
import asyncio
import discord
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
    m = 'Hi!\nPlease read <#736628061289578496> and type "ok". \nIf you are going to to be able to do it, please introduse yourself in <#736627134604378143>'
    channel = client.get_channel(737576896476348447)
    await channel.send(m)

     #channel = client.get_channel(payload.channel_id)
     #   if channel.id != ID_CHANNEL_README:
     #       return    

@client.event
async def on_message(message):
    if message.guild.id == server_id:
        if message.content == "ok":
            role = discord.utils.get(message.guild.roles, name="自己紹介してね")
            return await message.author.add_roles(role)

if __name__ == "__main__":
    client.run(TOKEN)
