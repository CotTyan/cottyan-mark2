# -*- coding: utf-8 -*-
import asyncio
import discord
TOKEN = ""
entry_id = 667385969716232194
server_id = 665189315877535753
hello_id =

server_id = int(server_id)
entry_id = int(entry_id)
hello_id = (hello_id)
client = discord.Client()

async def send(channel,*args, **kwargs): return await channel.send(*args, **kwargs)

@client.event
async def on_ready():
    print(client.user.id)
    print('It is ready')
    channel = client.get_channel(hello_id)
    embed = discord.Embed(title="ただ今起動しました",description="動作していない場合は管理者に問い合わせてください")
    embed = embed.set_author(name="CotTyanからのお知らせ",icon_url="https://www.repo.approvers.dev/g2058.png)
    await channel.send(embed=embed)
    

async def on_member_join(member):
     m = 'Hi!\n Please read<#667385969716232194>and type "ok". \n If you are going to to be able to do it, please introduse yourself in<#736627134604378143>.'
     return await member.send(m)

     #channel = client.get_channel(payload.channel_id)
     #   if channel.id != ID_CHANNEL_README:
     #       return    

@client.event
async def on_message(message):
    if message.guild.id == server_id:
        if message.content == "ok":
            role = discord.utils.get(message.guild.roles, name="user")
            return await message.author.add_roles(role)

if __name__ == "__main__":
    client.run(TOKEN)
