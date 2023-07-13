from discord import *
from discord.ext import commands
from ngrok import Client
from paramiko import SSHClient, AutoAddPolicy
from time import sleep
from os import system
from uuid import uuid4
import disnake


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
pre = lambda x, y: str(x)[:9:].lower() == "квадратик"
client = Client("Ъ")

intents = Intents.all()

bot = commands.Bot(command_prefix=["Виталя ", "Виталий  ", "Владимир ",  "Хуйло ", "Чмо ", "Ъ ", "Квадратик ", "квадратик ", "КВАДРАТИК "],  description=description, intents=intents)

#["Квадратик ", "квадратик "]

def vniz(el):
    return el.lower()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def айпи(ctx):
    for i in client.tunnels.list():
        if i.forwards_to == "localhost:25565":
            await ctx.send(f"Айпи для подключения к серверу: {str(i.public_url)[6::]}")
            return
    asd = SSHClient()
    asd.set_missing_host_key_policy(AutoAddPolicy())
    # Подключение
    asd.connect(hostname="192.168.1.105", username="ubuntu", password="ubuntupi", port=22)
    
    # Выполнение команды
    stdin, stdout, stderr = asd.exec_command('ngrok start --all')
    asd.close()
    sleep(2)
    for i in client.tunnels.list():
        if i.forwards_to == "localhost:25565":
            await ctx.send(f"Айпи для подключения к серверу: {str(i.public_url)[6::]}")
            return

@bot.command()
async def Я_адМин_а_нЕ_геЙ(ctx):
    for i in client.tunnels.list():
        if i.forwards_to == "localhost:22":
            await ctx.send(f"Команда для подключения к серверу по ssh: ssh ubuntu@{str(i.public_url)[6:23:]} -p{str(i.public_url)[24::]}")
            return
    asd = SSHClient()
    asd.set_missing_host_key_policy(AutoAddPolicy())
    # Подключение
    asd.connect(hostname="192.168.1.105", username="ubuntu", password="хуй тебе а не пароль", port=22)
    
    # Выполнение команды
    stdin, stdout, stderr = asd.exec_command('ngrok start --all')
    asd.close()
    sleep(2)
    for i in client.tunnels.list():
        if i.forwards_to == "localhost:22":
            await ctx.send(f"Айпи для подключения к серверу: ssh ubuntu@{str(i.public_url)[6:str(i.public_url).find(':'):]} -p{str(i.public_url)[str(i.public_url).find(':')::]}")
            return


@bot.command()
async def joined(ctx, member: Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    return


@bot.command()
async def умри(ctx):
    if str(ctx.author) == "velikii_bog_gnomovidnyi_kvadrat#0":
        await ctx.send("@everyone я умираю https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")
        await bot.close()
        return
    else: 
        await ctx.send("Нетъ.")
        return
    return

@bot.command()
async def йцу(ctx):
    channel = bot.get_channel(980943660818505828)
    await channel.send('Да https://tenor.com/view/mujikcboro-seriymujik-gif-24361533')
    return

@bot.command()
async def скажи(ctx, *args):
    dat = list(args)
    with open("swears.txt") as f1:
        swears = f1.readlines()
    if any([i in list(map(vniz, dat)) for i in swears]) and any([i in list(map(vniz, dat)) for i in ['Я','я','Квадрат', '<@761891958208987156>']]):
        ans = list(filter(lambda x: x in ['Я','я','Квадрат', '<@761891958208987156>'],list(map(vniz, dat))))
        dat[dat.index(ans[0])] = "Ты"
        await ctx.send(" ".join(dat))
        return
    await ctx.send(" ".join(dat))
    return

class Role_list(disnake.ui.View):
    def __init__ (self):
        super().__init__(timeout=None)
        self.value: Optional[bool] = None

    @disnake.ui.button(label='Вывод текса',style=disnake.ButtonStyle.gray)
    async def vivod_texta(self,button:disnake.Button,interaction:disnake.Interaction):
        await interaction.response.send_message('Проверка')

@bot.command(name='verify')
async def verify(self,ctx):
    view=Role_list()
    verify_embed = disnake.Embed(
        title='Верификация',
        description='Пройдите верификацию чтобы продолжить общение!'
    )
    await self.send(embed=verify_embed,view=view)

@bot.command() # Create a command
async def геноцид(ctx):
    for _ in range(1000):
        await ctx.send("https://media.discordapp.net/attachments/1085583894285393941/1128814103188750336/unknown.png") 
        sleep(1)


'''@bot.event
async def on_command_error(ctx, error):
    await ctx.send('卐')'''


bot.run('token not found')