#Created By Solomonex#6969 on discord
#Please Dont Skid all the code 
#If Your Going to improve the code please credit me
#If your lazy just paste this at the top:
#----------------------------------------------------#
#Originally created By Solomonex#6969 on discord!
#All Credits Go To Him!
#----------------------------------------------------#

import datetime
import hikari
import lightbulb
import webbrowser
import os
import time
from win10toast import ToastNotifier
toast = ToastNotifier()

bot = lightbulb.BotApp(token='BOT TOKEN HERE', prefix=">",
default_enabled_guilds=1010882702372782161)

@bot.command
@lightbulb.command("allcmds", "Shows All Commands")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond("""**```Commands!```**
**```rickroll | Opens Never Gonna Give You Up In Their Browser!```**
**```troll | Plays You have Been Trolled On Youtube!```**
**```closeapps | Shows All Programs That Can Be Closed```**
**```killopera | Kills Opera GX (My Web Browser)```**
**```killdiscord | Forcefully quits my discord! (This will also Stop the Bot)```**
**```notify | Plays A Notification ```**
**```credits | Thanks Alot To Everyone on this list!```**""")

@bot.command
@lightbulb.command("cmds", "Shows All Commands")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond("""**```Commands!```**
**```youtube| Displays all youtube commands.```**
**```annoy | Please Dont make me want to remove this.```**
**```closeapps | Why Do i have to explain this just read the name.```**
**```credits | Thanks Alot To Everyone on this list!```**""")

@bot.command
@lightbulb.command("youtube", "Shows All Commands")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond("""**```SECTION: Youtube```**
    **```rickroll | Opens Never Gonna Give You Up In Their Browser!```**
    **```troll | Plays You have Been Trolled On Youtube!```**
    """)

@bot.command
@lightbulb.command("annoy", "Shows All Commands")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond("""**```SECTION: Troll :)```**
    **```notify | Plays A Notification ```**
    """)

@bot.command
@lightbulb.command("credits", "Shows All Beta Testers")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond("""**```Credits!```**
**```AmmonRO1#0919 (Beta Tester)```**
**```Dustin.#6270 (Beta Tester)```**
**```theoverracheiver#0820 (Beta Tester)```**
**```Solomonex#6969 (Creator)
**```DM Solomonex#6969 if you would like to test the bot!```**
""")

@bot.command
@lightbulb.command("closeapps", "Shows All commmands")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond("""**```Close Programs!```**
**```killopera | Kills Opera GX (My Web Browser)```**
**```killdiscord | Forcefully quits my discord! (This will also Stop the Bot)```**
""")

#--------------------------------------------------------#
#--------------------------------------------------------#
#Bot Commands

@bot.command
@lightbulb.command("rickroll", "Get Rickrolled")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=xvFZjo5PgG0')
    await ctx.respond("**```Opened https://www.youtube.com/watch?v=xvFZjo5PgG0 (Never Gonna Give You Up) On Youtube!```**")

@bot.command
@lightbulb.command("troll", "Get Trolled")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=BsIa_LKojJI&t=0s')
    await ctx.respond("**```Opened https://www.youtube.com/watch?v=BsIa_LKojJI&t=0s (You've been Trolled ) On Youtube!```**")

@bot.command
@lightbulb.command("error", "Shows An Error")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond("**```An Error Has Appeared On Their PC!```**")
    messagebox.showerror('Windows', 'An Error has occured!')
    await ctx.respond("**```The Error Has Been Closed!```**")

@bot.command
@lightbulb.command("killopera", "Closes Opera GX")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    os.system('taskkill /f /im opera.exe')
    await ctx.respond("**```Successfully Killed Opera GX!```**")

@bot.command
@lightbulb.command("killdiscord", "Makes The Python Bot Go Offline")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond("**```Booting Solomonex#6969 Offline...```**")
    time.sleep(2)
    await ctx.respond("**```Solomonex#6969 Has Been Booted Off Discord!```**")
    os.system('taskkill /f /im Discord.exe')
    os.system('discord.exe')

@bot.command
@lightbulb.command("notify", "Sends A Notification")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def foo(ctx: lightbulb.Context) -> None:
    await ctx.respond("**```Notification Has Been Played```**")
    toast.show_toast(
    "DISCORD Notification",
    "Never Gonna Give You Up Never Gonna Let You Down", 
    duration = 3,
    icon_path = "discord.ico",
    threaded = True)

#-----------------------------------------------------------------------#
#DEV COMMANDS

@bot.command
@lightbulb.command("update", "Powers The Bot Off")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def update(ctx: lightbulb.Context) -> None:
    await ctx.respond("**```Bot Is Updating...```**")
    await ctx.respond("**```Restarting Script...```**")
    time.sleep(1)
    os.system('Bot.py')

@bot.command
@lightbulb.command("status", "Powers The Bot Off")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("**```The Bot Is Online And Working!```**")

@bot.command
@lightbulb.command("stop", "Powers The Bot Off")
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def stopbot(ctx: lightbulb.Context) -> None:
    await ctx.respond("**```Powering Off...```**")
    time.sleep(.500)
    os.system('taskkill /f /im python.exe')

bot.run()
