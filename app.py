import discord
from discord.ext import commands
import inspect
import datetime

app = commands.Bot(command_prefix = 'r!')



@app.event
async def on_ready():
    print('Login!')

@app.event
async def on_message(message):
    if message.author.bot: return
    if message.content.startswith('py!compile'):
        if message.author.id == 480240821623455746:
            msg=message.content
            arg=msg.split(" ")
            args=arg[1:]
            msg = ''.join(args)
            try:
                python = '```py\n{}\n```'
                res = eval(msg)
                if inspect.isawaitable(res):
                    result = await res
                else:
                    result = res
            except Exception as e:
                embed = discord.Embed(colour=0xef6767, timestamp=datetime.datetime.utcnow())
                embed.add_field(name='Error', value=python.format(str(e)))
                return await message.channel.send(embed=embed)

            embed = discord.Embed(colour=0x6bffc8, timestamp=datetime.datetime.utcnow())
            embed.add_field(name='Success', value=python.format(result))
            await message.channel.send(embed=embed)

app.run(TOKEN)