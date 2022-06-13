import discord
from discord.ext import commands

client = commands.Bot(command_prefix= ">" , case_insensitive = True)

@client.event
async def on_ready():
    print('Bot on')

@client.command()
async def play (ctx, url : str, channel):
	voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	if not voice.is_connected():	
		await voiceChannel.connect()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith('>leo'):
        user_id = "221731639883988993"
        await message.channel.send(f"Coe <@{user_id}> voce é um otario")

@client.command()
async def comandos(ctx):
	await ctx.send('Meus comandos são:\n\n>comandos - Para listar os comandos\n>leo - Mandar leo sucumbir\n')

client.run('NzEwOTI3NDM1NjgzNzI1Mzky.Xr7kxQ.9b0y2gik8XbC2cNF13s2UuKsjKc')
