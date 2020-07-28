# coding: utf-8
import discord

client = discord.Client()
TOKEN = ""
@client.event
async def on_member_join(member):
     m = "ようこそ<@"+str(member.id)+">さん\n<#667385969716232194>を読んでから「ok」と入力してください\nそのあと<#736627134604378143>で自己紹介をしていただければ書き込み可能となります"
     return await send(client.get_channel("667385969716232194"), m)
    

@client.event
async def on_message(message):
    if message.guild.id == "665189315877535753":
        if message.content.lower() == "ok":
            role = discord.utils.get(message.guild.roles, name="自己紹介してね")
            return await message.author.add_roles(role)

if __name__ == "__main__":
    client.run(TOKEN)