#importing the code i need
import decimal
import time, sched
import datetime
start_time = time.time()
import discord
import os
import sys
import asyncio
import json
import random
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, bot
import threading
import psutil #cpu stats, disk, ram, etc
import ducoapi
import requests
import json

amttoaffect = 10


#GET data

from decimal import *
secondint = 1
multiplyST = 5.8
startup = (time.time() - start_time)

print("Importing took %s seconds" % (time.time() - start_time))
print(f"Guessed next startup time: {startup*multiplyST}")


#Version of the code (usually updates whenever I update the github)
global botversion
botversion = "V.0.1-TestingPhase"
#v = version, a = alpha, b = beta, d = in development
#so V.A.1.1  means Version Alpha 1.1


#NEW CHANGES IN V.A.3.0
'''
- ping 
'''


############################################################################################
'''
READ THIS IF YOU ARE RECOPYING THE BETA BOT CODE TO THIS
You should do this once in a while
    1. Replace all the beta stuff, like (do opposite for main→beta, you can use CTRL+H or whatever you use to replace):
        sc → kc
        betabotkccData1.json → kccData1.json
        928762834119176272 → 925243510519636008
        {Bot token} → os.getenv('TOKEN') (OR ITS OWN BOT TOKEN)
    2. ALWAYS MAKE A COPY OF THE CURRENT CODE (just in case) AND SAVE IT
    3. Remove beta messages (in cd, update list for more...) (or add if your doing main→beta)
    4. Remove limited features (exchange to not-in-code currencies, etc) (or add if your doing main→beta)
'''
############################################################################################
'''
READ THIS WHEN YOUR ADDING A NEW COMMAND:
Here are the rules when adding a command:
1. If the command involues in currency, make the the bot also gets/loses KCC
2. Make sure there is a print command with the arguments
3. Try to make the command send messages
## (OPTIONAL) 4. Make sure to add a open account (DONT HAVE TO BECAUSE OF THE NEW client.event)
5. Make sure to test it. You can copy the code and replace TOKEN with your own bot token
6. If the bot sends a message, try to make it embed and have emojis (only for new commands)
7. Make sure to not affect other commands (except for currency changes, user changes, etc)
8. Add the command to the help list, both the 'all' value and the page
'''
############################################################################################













#{"623339767756750849": {"coin1": 13816.0, "coin2": 44, "coin3": 1402, "rank": "admin", "hasKCLock": "Yes", "robCounter": 2}, "929595294583242822": {"faucet": 99409, "coin1": 890550, "coin2": 34, "coin3": 10000, "rank": "supply/bot", "hasKCLock": "Infinite", "robCounter": 0, "memberCount": 12}, "639206421707227136": {"coin1": 10000, "coin2": 0, "coin3": 0, "rank": "admin", "hasKCLock": "No", "robCounter": 0}, "646556661615558667": {"coin1": 10023, "coin2": 1, "coin3": 0, "rank": "default", "hasKCLock": "No", "robCounter": 0}, "794389647006105602": {"coin1": 11147.5, "coin2": 11, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 1}, "695703574465740851": {"coin1": 0, "coin2": 0, "coin3": 0, "rank": "mod", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "755855419758346360": {"coin1": 20136, "coin2": 21, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": 1, "robCounter": 0}, "705073774298660874": {"coin1": 10000, "coin2": 1, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "889635268070629436": {"coin1": 11136, "coin2": 3, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "452215789307559937": {"coin1": 12205.5, "coin2": 12, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "Yes", "robCounter": 2}, "704406205191159979": {"coin1": 0, "coin2": 0, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "488507021667336194": {"coin1": 10000, "coin2": 12, "coin3": 0, "rank": "default", "cmdcd": 0}, "640742876103573514": {"coin1": 0, "coin2": 100, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}}

#COPY JUST IN CASE SOMETHING GOES WRONG

#fun fact most of the code i learned before using processing python (.pyde)
#i even made a crypto miining slimartor

mainbotprefixSpace = f"kcc "# change main bot prefix (Shows in commands, etc)


#this patches a glitch with Windows 10 when running the .py file
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#you might not need this if your running linux

#load the dotenv function
load_dotenv()

#what activity the bot will show
#default: for \"{mainbotprefixSpace}help\"                               v changes the type it displays 
activity = discord.Activity(type=discord.ActivityType.watching, name=f"for \"{mainbotprefixSpace}help\"")

intents = discord.Intents().all()


#bot prefix (can be changed for $, for example) default: "{mainbotprefixSpace}"                         v status to display
client = commands.Bot(command_prefix=[f'{mainbotprefixSpace}', 'KCC ', 'Kcc ', 'KCc', '<@929595294583242822> ', '<@!929595294583242822> '], intents=intents, case_insensitive=True, activity=activity, status=discord.Status.online)
#client.remove_command('help')

# async def sec():
#     randomEvent = random.randrange(10,30)
#     threading.Timer(randomEvent, sec).start()
#     channel = bot.get_channel(636399538650742795)
#     reNum1 = random.randrange(398,2394)
#     reNum2 = random.randrange(234,3489)
#     await channel.message.send(f"random event test\nwhat is {reNum1} x {reNum2}?")
#     global REanswer
#     REanswer = (reNum1*reNum2)
# @client.event
# async def on_message(ctx):
#     global REanswer
#     if ctx.content.startswith(REanswer):
#         await open_account(ctx.author)
#         user = ctx.author #author of the user, not finshed
#         users = await get_coin2_data() #load the kccData1.json
#         users = await get_coin3_data()
#         users[str(user.id)]["coin1"] += 100
#         await ctx.send(f"{user.id} u earned 100 {mainbotprefixSpace}nice")
#         with open("kccData1.json","w") as f:
#             json.dump(users,f)
#open .env file and get %privatelol% in TOKEN=%privatelol%
TOKEN = 'OTI5NTk1Mjk0NTgzMjQyODIy.YdpnFQ.Kqhja1tGFLiN7vZloLpy2G-kAy8'

def remove_ping_letters(input1):
    input1 = input1.replace("<","")
    input1 = input1.replace("@","")
    input1 = input1.replace(">","")
    input1 = input1.replace("!","")
    return input1




#startup script
@client.event
async def on_ready():
    print('Program is now running.\nThe bot user is: {0.user}'.format(client))
    print("Code took %s seconds" % (time.time() - start_time))
    global startup
    startup = (time.time() - start_time)
   # await sec()
    global showCommandErrorsVar
    showCommandErrorsVar = True

@client.command(aliases=['testing'])
async def test(ctx, *test1):
        embed=discord.Embed(title="Admin commands:", color=0xff00ff)
        embed.add_field(name=f"{mainbotprefixSpace}add <amount> <type of coin> [wallet id or mention]", value="Gives an amount to another user\nAliases: admin.add, admin.give, admin.addBal", inline=False)
        embed.add_field(name=f"{mainbotprefixSpace}set <amount> <type of coin> [wallet id or mention]", value="Sets an amount to another user\nAliases: admin.set", inline=False)
        embed.add_field(name=f"{mainbotprefixSpace}restart", value="Restarts the program\n(Maybe for new changes in code)\nAliases: admin.restart, admin.reload, reload", inline=False)
        await ctx.send(embed=embed, delete_after=0.0)    
#when bal cmd runs:
# @client.command(aliases=['balance', 'amount'])
# async def bal(ctx, walletid: discord.Member=None):
#     await open_account(ctx.author)
#     user = ctx.author #author of the user, not finshed
#     users = await get_coin2_data() #load the kccData1.json
#     users = await get_coin3_data()
#     global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt


#     if walletid is None:
#         walletid = ctx.author
#         coin1_amt = users[str(user.id)]["coin1"]
#         coin2_amt = users[str(user.id)]["coin2"]
#         coin3_amt = users[str(user.id)]["coin3"]

#     else:
#         print(walletid.id)
#         if walletid.id == 929595294583242822 or walletid.id == "929595294583242822":
#             embed=discord.Embed(title="Error while running command: (denied)", description=("You can't check the profile of the supply bot\nRun '{mainbotprefixSpace}supply' instead"), color=0xff0000)
#             embed.set_author(name="Kevcore Game - balance")
#             embed.set_footer(text="Removed checking the bot using profile in V.A.4.2")
#             await ctx.send(embed = embed)
#             return 0
#         else:
#             coin1_amt = users[str(walletid.id)]["coin1"]
#             coin2_amt = users[str(walletid.id)]["coin2"]
#             coin3_amt = users[str(walletid.id)]["coin3"]

#     #embed text
#     em = discord.Embed(title = f"{walletid.name}'s balance",color = discord.Color.red())
#     em.add_field(name = "KCC:",value = coin1_amt)
#     em.add_field(name = "Dexa:",value = coin2_amt)
#     em.add_field(name = "KevCoin Bank:",value = coin3_amt)
#     em.set_footer(text=f"Wallet ID: {walletid.id}")
#     await ctx.send(embed = em)
#     #print when a user runs command
#     print(f"User {ctx.author.name} ({ctx.author.id}) ran 'bal' command. {walletid}")



@client.command(aliases=['pf', 'bal', 'balance'])
async def profile(ctx, walletid: discord.Member=None):
    await open_account(ctx.author)
    user = ctx.author #author of the user, not finshed
    users = await get_coin2_data() #load the kccData1.json
    users = await get_coin3_data()
    global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt

    if walletid is None:
        walletid = ctx.author
    
        coin1_amt = users[str(user.id)]["coin1"]
        coin2_amt = users[str(user.id)]["coin2"]
        coin3_amt = users[str(user.id)]["coin3"]
        hasLock = users[str(user.id)]["hasKCLock"]
        ranklvl = users[str(user.id)]["rank"]
    else:
        if walletid.id == 929595294583242822 or walletid.id == "929595294583242822":
            embed=discord.Embed(title="Error while running command: (denied)", description=("You can't check the profile of the supply bot\nRun '{mainbotprefixSpace}supply' instead"), color=0xff0000)
            embed.set_author(name="Kevcore Game - balance")
            embed.set_footer(text="Removed checking the bot using profile in V.A.4.2")
            await ctx.send(embed = embed)
        else:
            coin1_amt = users[str(walletid.id)]["coin1"]
            coin2_amt = users[str(walletid.id)]["coin2"]
            coin3_amt = users[str(walletid.id)]["coin3"]
            ranklvl = users[str(walletid.id)]["rank"]
            hasLock = users[str(walletid.id)]["hasKCLock"]
    if secondint == 0 and ranklvl == "premin":
        users[str(walletid.id)]["ranklvl"] = "default" 
        with open("kccData1.json","w") as f:
            json.dump(users,f)
    #embed text
    em = discord.Embed(title = f"{walletid.name}'s balance",color = 0x00CCFF)
    em.add_field(name = "KCC:",value = coin1_amt)
    em.add_field(name = "Dexa:",value = coin2_amt)
    em.add_field(name = "KevCoin Bank:",value = coin3_amt)
    if walletid.id != "929595294583242822":
        em.add_field(name = "Total KCC:",value = (coin3_amt+coin1_amt))

   # em.add_field(name= "KC Lock active?", value=hasLock, inline=False)
    #em.add_field(name= "Premin active?", value=f"{secondint} seconds")

    em.set_footer(text=f"Rank: {ranklvl}\nWallet ID: {walletid.id}")
    await ctx.send(embed = em)
    #print when a user runs command
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'bal' command")



@client.event
@commands.cooldown(1, 5, commands.BucketType.user)
async def on_message(ctx):
    cd_mapping = commands.CooldownMapping.from_cooldown(1, 3, commands.BucketType.user)
    bucket = cd_mapping.get_bucket(ctx)
    retry_after = bucket.update_rate_limit()
    if retry_after:
        ratelimit = True
    else:
        # not rate limited
        await client.process_commands(ctx)
        if ctx.author.bot:
            return

        await open_account(ctx.author)
        users = await get_coin2_data()
        user = ctx.author
        earnings = 1
        earnornot = random.randrange(1,10)
        earnings = 1
        users = await get_coin3_data()
        global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
        coin1_amt = users[str(user.id)]["coin1"]
        coin2_amt = users[str(user.id)]["coin2"]
        coin3_amt = users[str(user.id)]["coin3"]
        coin1_bot = users[str(929595294583242822)]["coin1"]

        # if coin1_bot >= 10000:
        #     if earnornot == 1:
        #         embed=discord.Embed(title="Reward", description=(f"The KCGame bot gave "+ ctx.author.mention + f" {earnings} KCC!"), color=0x00FF00)
        #         embed.set_author(name="Kevcore Game - beg")
        #         embed.set_footer(text=("There's a chance (1/3) to get caught while begging\nYou can only use this command 3 times every 30 seconds"))
        #         #await ctx.channel.send(embed=embed)
        #         users[str(user.id)]["coin1"] += earnings
        #         users[str(929595294583242822)]["coin1"] -= earnings
        #         with open("kccData1.json","w") as f:
        #             json.dump(users,f)

    #
@client.command(aliases=['options', 'setting'])
@commands.cooldown(1, 3, commands.BucketType.user) 
async def settings(ctx, setType=None, value=None):
    users = await get_coin2_data()
    user = ctx.author
    coin1_amt = users[str(user.id)]["coin1"]
    coin2_amt = users[str(user.id)]["coin2"]
    coin3_amt = users[str(user.id)]["coin3"]
    coin1_bot = users[str(929595294583242822)]["coin1"]   
    DMnotifs = users[str(user.id)]["DMNotifs"]   
    userFriendly = users[str(user.id)]["userFriendly"]   

    if setType == None:
        embed=discord.Embed(title="Settings", description=("Beta test - settings"), color=0x00CCFF)
        embed.set_author(name="Kevcore Game - settings")
        embed.add_field(name=f"Direct Message Notifications [dmNotif]: {DMnotifs.upper()}",value="If yes, the bot will personally send you DM notifications for people robbing you, lock breaking, etc\nValues: YES (TRUE), NO (FALSE)", inline=False)
        embed.add_field(name=f"User friendly type [userFriendly]: {userFriendly.upper()}",value="Changes the type of user friendly\nValues: DEFAULT, COMFORTABLE", inline=False)

        embed.set_footer(text="Make sure values are capitalized\nUse kc settings <option> <value> to change values")
        await ctx.send(embed=embed)
    else:
        if setType == "dmNotif":
            if value == "YES" or value == "TRUE":
                users[str(user.id)]["DMNotifs"] = "Yes"
                with open("kccData1.json","w") as f:
                    json.dump(users,f)           
                embed=discord.Embed(title="Your DM notifications are now enabled", description=("You will receive Direct Messages from the bot"), color=0x00FF00)
                embed.set_author(name="Kevcore Game - settings")
                embed.set_footer(text="Yay lol")
                await ctx.send(embed=embed)
            elif value == "NO" or value == "FALSE":
                users[str(user.id)]["DMNotifs"] = "No"
                with open("kccData1.json","w") as f:
                    json.dump(users,f)           
                embed=discord.Embed(title="Your DM notifications are now disabled", description=("You won't receive Direct Messages from the bot anymore"), color=0x00FF00)
                embed.set_author(name="Kevcore Game - settings") 
                embed.set_footer(text="No more spams, ig")
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="Unknown value", description=("Make sure your values are capitalized!\nValues: YES, NO, FALSE, TRUE"), color=0xFF0000)
                embed.set_author(name="Kevcore Game - Error (won't run)") 
                embed.set_footer(text="Error code: settings-invaildValue")
                await ctx.send(embed=embed)
        elif setType == "userFriendly":
            if value == "YES" or value == "COMFORTABLE":
                users[str(user.id)]["userFriendly"] = "comfortable"
                with open("kccData1.json","w") as f:
                    json.dump(users,f)           
                embed=discord.Embed(title="Your user friendly mode is set to comfortable", description=("Your messages will be easier to read"), color=0x00FF00)
                embed.set_author(name="Kevcore Game - settings")
                embed.set_footer(text="This is a test, it only works on the cooldown error message for now")
                await ctx.send(embed=embed)
            elif value == "NO" or value == "DEFAULT":
                users[str(user.id)]["userFriendly"] = "default"
                with open("kccData1.json","w") as f:
                    json.dump(users,f)           
                embed=discord.Embed(title="Your user friendly mode is set to default", description=("You'll see the default messages"), color=0x00FF00)
                embed.set_author(name="Kevcore Game - settings") 
                embed.set_footer(text="like: 1h, lol, imagine, lmao, etc ")
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="Unknown value", description=("Make sure your values are capitalized!\nValues: YES, NO, COMFORTABLE, DEFAULT"), color=0xFF0000)
                embed.set_author(name="Kevcore Game - Error (won't run)") 
                embed.set_footer(text="Error code: settings-invaildValue")
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Unknown option", description=("Run `kc settings` to see your options (They are in the square brackets)"), color=0xFF0000)
            embed.set_author(name="Kevcore Game - Error (won't run)") 
            embed.set_footer(text="Error code: settings-invaildSetType")
            await ctx.send(embed=embed)
startTime = time.time()

@client.command(aliases=['totalamount'])
async def supply(ctx):
    users = await get_coin2_data() #load the kccData1.json
    users = await get_coin3_data()
    global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
    coin1_amt = users[str(929595294583242822)]["coin1"]
    coin2_amt = users[str(929595294583242822)]["coin2"]
    coin3_amt = users[str(929595294583242822)]["coin3"]
    oricoin2 = users[str(929595294583242822)]["oricoin2"]

    ranklvl = users[str(929595294583242822)]["rank"]
    faucet_amt = users[str(929595294583242822)]["faucet"]
    memberCount = users[str(929595294583242822)]["memberCount"]
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    if coin1_amt > (coin3_amt/1.5):
        KCliquidity = "HIGH"
    elif coin1_amt > (coin3_amt/3):
        KCliquidity = "MEDIUM"
    else:
        KCliquidity = "LOW"
    #embed text
    BALpercent = (coin1_amt/coin3_amt * 100)
    BALpercent = "{:.1f}".format(BALpercent)

    BALpercent = float(BALpercent)
    em = discord.Embed(title = f"Currency Supply:",color = 0x00CCFF)
    em.add_field(name = "KCC:",value = coin1_amt)
    em.add_field(name = "KevCoin Faucet:",value = faucet_amt)
    em.add_field(name = "Dexa:",value = coin2_amt)
    em.add_field(name = "KC obtainable:",value = coin3_amt)
    em.add_field(name = "Dexa obtainable:",value = oricoin2)
    em.add_field(name = "KC Liquidity:",value = f"{KCliquidity} ({BALpercent}%)")

    em.set_footer(text=f"A good amount of supply for KC is >700k\nThe supply will regenerate a bit after some time")
    await ctx.send(embed = em)

    #print when a user runs command
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'supply' command")

#{"623339767756750849": {"coin1": 26555.5, "coin2": 55, "coin3": 2773, "rank": "admin", "hasKCLock": "Yes", "robCounter": 1}, "929595294583242822": {"faucet": 95635, "coin1": 851609, "coin2": 9, "coin3": 1100500, "oricoin2": 117, "rank": "supply/bot", "hasKCLock": "Infinite", "robCounter": 0, "memberCount": 13}, "639206421707227136": {"coin1": 10000, "coin2": 0, "coin3": 0, "rank": "admin", "hasKCLock": "No", "robCounter": 0}, "646556661615558667": {"coin1": 10052, "coin2": 1, "coin3": 0, "rank": "default", "hasKCLock": "No", "robCounter": 0}, "794389647006105602": {"coin1": 19138.5, "coin2": 1, "coin3": 2126, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 3}, "695703574465740851": {"coin1": 0, "coin2": 0, "coin3": 0, "rank": "mod", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "755855419758346360": {"coin1": 19099, "coin2": 21, "coin3": 2123, "rank": "default", "cmdcd": 0, "hasKCLock": "Yes", "robCounter": 0}, "705073774298660874": {"coin1": 10000, "coin2": 1, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 3}, "889635268070629436": {"coin1": 13169.5, "coin2": 4, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 1}, "452215789307559937": {"coin1": 22440.0, "coin2": 13, "coin3": 2456, "rank": "default", "cmdcd": 0, "hasKCLock": "Yes", "robCounter": 0}, "704406205191159979": {"coin1": 0, "coin2": 0, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "488507021667336194": {"coin1": 10000, "coin2": 12, "coin3": 0, "rank": "default", "cmdcd": 0}, "640742876103573514": {"coin1": 0, "coin2": 0, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}}



@client.command(aliases=['lb'])
async def leaderboard(ctx, x=5):
    with open('kccData1.json', 'r') as f:
        users = json.load(f)
    leaderboard = {}
    total=[]
    user1 = 1

    for user1 in list(users):
        name = int(user1)
        total_amt = users[str(user1)]['coin1']
        leaderboard[total_amt] = name
        total.append(total_amt)
      

    total = sorted(total,reverse=True)


    em = discord.Embed(title = f'Top {x} members for KCC', description = 'The leaderboard for KCC', color=0xFF00FF)
    em.set_footer(text=f"Note: This is globally")


    index = 1
    for amt in total:
        id_ = leaderboard[amt]
        member = client.get_user(id_)
        print(member)
        if member != "Kevcore Game Bot#0908":
            em.add_field(name = f'{index}: {member}', value = f'{amt} KCC', inline=False)
        
        
        if index == x:
            break
        else:
            index += 1
    await ctx.send(embed = em)



# @client.command(aliases=['?', 'helpme'])
# #for other cmds im not even gonna write XD
# async def help(ctx, pg="1"):
#     await open_account(ctx.author)
#     user = ctx.author
#     users = await get_coin2_data()
#     ranklvl = users[str(user.id)]["rank"]
#     if pg == "admin" or pg == "premin" or pg == "all":
#         pg = str(pg)
#     else:
#         pg = int(pg)
#     if pg == 1:
#         embed=discord.Embed(title="List of commands (Page 1):", color=0xff00ff)
#         embed.set_author(name="Kevcore Game help", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#         embed.add_field(name=f"{mainbotprefixSpace}help [page number/rank]", value="Shows this. If a rank is specified, it'll show the rank commands\nAliases: ?, helpme", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}balance [wallet id or @mention]", value="Shows the balance of KCC, Dexa\nAliases: bal, amount", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}profile [wallet id or @mention]", value="Shows the balance of currencies, and extra user perks", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}send <wallet id> <amount> <type of coin>", value="Transfers an amount to another user\nAliases: give, share", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}beg", value="Try to beg for some money\nThere is a 1/3 chance of getting caught\nAliases: mine, gib, givemoney, gamble", inline=False)
#         embed.set_footer(text=f"Page 1. See the next page using {mainbotprefixSpace}help 2")

#         await ctx.send(embed = embed)
                                                                   
#    # embed.add_field(name=f"{mainbotprefixSpace}work", value="Work to get some money. Cooldown: 60s", inline=False)
# #{"623339767756750849": {"coin1": 10449.5, "coin2": 41, "coin3": 1160, "rank": "admin", "hasKCLock": "Yes", "robCounter": 3}, "929595294583242822": {"faucet": 99702, "coin1": 896500, "coin2": 39, "coin3": 10000, "rank": "supply/bot", "hasKCLock": "Infinite", "robCounter": 0, "memberCount": 12}, "639206421707227136": {"coin1": 10000, "coin2": 0, "coin3": 0, "rank": "admin", "hasKCLock": "No", "robCounter": 0}, "646556661615558667": {"coin1": 9927, "coin2": 1, "coin3": 0, "rank": "default", "hasKCLock": "No", "robCounter": 0}, "794389647006105602": {"coin1": 11042.5, "coin2": 11, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "Yes", "robCounter": 1}, "695703574465740851": {"coin1": 0, "coin2": 0, "coin3": 0, "rank": "mod", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "755855419758346360": {"coin1": 20136, "coin2": 21, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": 1, "robCounter": 0}, "705073774298660874": {"coin1": 10000, "coin2": 1, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "889635268070629436": {"coin1": 10000, "coin2": 2, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "452215789307559937": {"coin1": 11008.5, "coin2": 11, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "Yes", "robCounter": 2}, "704406205191159979": {"coin1": 0, "coin2": 0, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}, "488507021667336194": {"coin1": 10000, "coin2": 12, "coin3": 0, "rank": "default", "cmdcd": 0}, "640742876103573514": {"coin1": 0, "coin2": 100, "coin3": 0, "rank": "default", "cmdcd": 0, "hasKCLock": "No", "robCounter": 0}}

#     elif pg == 2:
#         embed=discord.Embed(title="List of commands (Page 2):", color=0xff00ff)
#         embed.add_field(name=f"{mainbotprefixSpace}rob", value="Try to rob someone for some of their money\nThere is a 25% to win a rob. If you are caught by the police, you will gain 1 failed steal. Once you have 3 failed steals, you won't get caught by the police\nAliases: steal, take", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}daily", value="Get your daily coins\nThere's a cooldown of 12 hours", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}buy <itemid> [amount]", value="Buy something from the shop, using itemid", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}faucet [amount to donate]", value="Requests the bot to give some of their KCC to you\nYou can donate by adding a number to the command\nAliases: get_money, minute, minutely", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}deposit <amount>", value="Deposit an amount of your KCC to your bank\nAliases: dep, storeAmount", inline=False)
#         embed.set_footer(text=f"Page 2. See the next page using {mainbotprefixSpace}help 3")

#         await ctx.send(embed = embed)
#     elif pg == 3:
#         embed=discord.Embed(title="List of commands (Page 3):", color=0xff00ff)
#         embed.add_field(name=f"{mainbotprefixSpace}withdraw <amount>", value="Withdraw an amount of your bank to your KCC\nAliases: wd, with", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}supply", value="See the currency supply", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}stats [amount of time]", value="See bot statistics\nYou can choose an amount of time to montior the CPU usage\nOr put 'basic' to not show the resource usage\nAliases: statistics", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}shop [page]", value="See the shop, where you can buy things", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}buy <itemid> [amount]", value="Buy something from the shop, using itemid", inline=False)
#         embed.set_footer(text=f"Page 3. See the next page using {mainbotprefixSpace}help 4")
#         await ctx.send(embed = embed)

#     elif pg == 4:
#         embed=discord.Embed(title="List of commands (Page 4):", color=0xff00ff)
#         embed.add_field(name=f"{mainbotprefixSpace}coinflip <amount>", value="Bet some of your money for a chance at getting KCC!\nAliases: cf, flip, coin", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}leaderboard", value="See the global leaderboard for KCC\nAliases: lb", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}work", value="Work for some money. Cooldown of 5 minutes", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}exchange <from coin> <to coin> <amount of from coin>", value="Exchange a currency to another currency. Run {mainbotprefixSpace}exchange by itself to see the prices.", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}settings <option> <value>", value="Change some settings to your liking. Run {mainbotprefixSpace}settings by itself to see the options/values", inline=False)

#         embed.set_footer(text=f"Page 4. See the next page using kc help 5")
#         await ctx.send(embed = embed)
#     elif pg == 5:
#         embed=discord.Embed(title="List of commands (Page 4):", color=0xff00ff)
#         embed.add_field(name=f"{mainbotprefixSpace}bet <amount>", value="Bet some of your money for a chance at getting KCC!\nThe more you bet, the less chance you'll win\nKevCoin limit is 5x more than the coinflip command\nAliases: gamble", inline=False)
        

#         embed.set_footer(text=f"Page 5. This is the last page\nAdd 'premin' if you have premin to see your commands ")
#         await ctx.send(embed = embed)
#     elif pg == "all":
#         embed=discord.Embed(title="List of all commands:", color=0xff00ff)
#         embed.set_author(name="Kevcore Game help", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#         embed.add_field(name=f"{mainbotprefixSpace}help [page number/rank]", value="Shows this. If a rank is specified, it'll show the rank commands\nAliases: ?, helpme", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}balance [wallet id or @mention]", value="Shows the balance of KCC, Dexa\nAliases: bal, amount", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}profile [wallet id or @mention]", value="Shows the balance of currencies, and extra user perks", inline=False)
#         #embed.add_field(name=f"{mainbotprefixSpace}send <wallet id> <amount> <type of coin>", value="Transfers an amount to another user\nAliases: give, share", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}beg", value="Try to beg for some money\nThere is a 2/15 chance of getting caught\nAliases: mine, gib, givemoney, gamble", inline=False)
#         #embed.add_field(name=f"{mainbotprefixSpace}rob", value="Try to rob someone for some of their money\nThere is a 25% to win a rob. If you are caught by the police, you will gain 1 failed steal. Once you have 3 failed steals, you won't get caught by the police\nAliases: steal, take", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}daily", value="Get your daily coins\nThere's a cooldown of 12 hours", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}buy <itemid> [amount]", value="Buy something from the shop, using itemid", inline=False)
#         #embed.add_field(name=f"{mainbotprefixSpace}faucet [amount to donate]", value="Requests the bot to give some of their KCC to you\nYou can donate by adding a number to the command\nAliases: get_money, minute, minutely", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}deposit <amount>", value="Deposit an amount of your KCC to your bank\nAliases: dep, storeAmount", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}withdraw <amount>", value="Withdraw an amount of your bank to your KCC\nAliases: wd, with", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}supply", value="See the currency supply", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}stats", value="See bot statistics\nAliases: statistics", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}shop [page]", value="See the shop, where you can buy things", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}buy <itemid> [amount]", value="Buy something from the shop, using itemid", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}coinflip <amount>", value="Bet some of your money for a chance at getting KCC!\nAliases: cf, flip, coin", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}leaderboard", value="See the global leaderboard for KCC\nAliases: lb", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}work", value="Work for some money. Cooldown of 5 minutes", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}exchange <from coin> <to coin> <amount of from coin>", value="Exchange a currency to another currency. Run {mainbotprefixSpace}exchange by itself to see the prices.", inline=False)
#         embed.add_field(name=f"{mainbotprefixSpace}settings <option> <value>", value="Change some settings to your liking. Run {mainbotprefixSpace}settings by itself to see the options/values", inline=False)

#         embed.set_footer(text=f"This is the list of all rank default commands")
#         await ctx.send(embed = embed)

#     elif pg == "admin" or pg == "mod":   
#         if ranklvl == "admin" or ranklvl == "mod":     
#             embed=discord.Embed(title="Admin commands:", color=0xff00ff)
#             embed.add_field(name=f"{mainbotprefixSpace}add <amount> <type of coin> [wallet id or mention]", value="Gives an amount to another user\nAliases: admin.add, admin.give, admin.addBal", inline=False)
#             embed.add_field(name=f"{mainbotprefixSpace}set <amount> <type of coin> [wallet id or mention]", value="Sets an amount to another user\nAliases: admin.set", inline=False)
#             embed.add_field(name=f"{mainbotprefixSpace}restart", value="Restarts the program\n(REQUIRES ADMIN)\nAliases: admin.restart, admin.reload, reload", inline=False)
#             embed.add_field(name=f"{mainbotprefixSpace}delete <amount>", value="Deletes a specified amount of messages in the current channel\nAliases: clr, clear, delete, purge", inline=False)
#         else:
#             embed=discord.Embed(title=f"❌ Sorry, but you need at least 'mod' rank to use this argument!", color=0xFF0000)
#             embed.set_author(name="Kevcore Game - help", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#         await ctx.send(embed=embed)
#     elif pg == "premin" or pg == "premium" or pg == "vip":

#         if ranklvl == "premin" or ranklvl == "mod" or ranklvl == "admin":        
#             embed=discord.Embed(title="Premin commands:", color=0xff00ff)
#             embed.add_field(name=f"{mainbotprefixSpace}hourly", value="Like daily, you can get your hourly coins", inline=False)
#             await ctx.send(embed=embed)    
#         else:         
#             embed=discord.Embed(title=f"❌ Sorry, but you need at least 'premin' rank to use this command!", color=0xFF0000)
#             embed.set_author(name="Kevcore Game - help", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#             await ctx.send(embed=embed)
#     else:
#         embed=discord.Embed(title=f"❌ Page '{pg}' isn't found/vaild!\nAvaliable pages: 1-2, premin, all", color=0xFF0000)
#         embed.set_author(name="Kevcore Game - help", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#         await ctx.send(embed=embed)
#     #print when a user runs command
#     print(f"User {ctx.author.name} ({ctx.author.id}) ran 'help' command. pg {pg}")


# @client.event
# async def on_reaction_add(reaction, user):
#     emoji = reaction.emoji

#     if user.bot:
#         return

#     if emoji == "⬅":
#         await ctx.send("left")    

#     elif emoji == "➡":
#         await ctx.send("right")    
   
#     else:
#         return

@client.command(aliases=['addBal', 'admin.add', 'admin.give'])
async def add(ctx, arg1, arg2, walletid: discord.Member=None, IGB=None):
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'add' command. {arg1} {arg2} {walletid} {IGB}")
    if IGB != None:
        IGB = "yes"
    await open_account(ctx.author)
    user = ctx.author
    users = await get_coin2_data()
    ranklvl = users[str(user.id)]["rank"]
    if ranklvl == "admin":
        await open_account(ctx.author)
        user = ctx.author
        users = await get_coin2_data()
        users = await get_coin3_data()
        global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
        if walletid is None:
            walletid = ctx.author
            coin1_amt = users[str(user.id)]["coin1"]
            coin2_amt = users[str(user.id)]["coin2"]
            coin3_amt = users[str(user.id)]["coin3"]
            ranklvl = users[str(user.id)]["rank"]

        else:
            coin1_amt = users[str(walletid.id)]["coin1"]
            coin2_amt = users[str(walletid.id)]["coin2"]
            coin3_amt = users[str(walletid.id)]["coin3"]
            ranklvl = users[str(walletid.id)]["rank"]

        arg1 = float(arg1)
        if arg2 == "KevCoin" or arg2 == "KCC" or arg2 == "kc" or arg2 == "coin1":
            
            users[str(walletid.id)]["coin1"] += arg1
            if IGB == None:
                users[str(929595294583242822)]["coin1"] -= arg1
            else:
                users[str(929595294583242822)]["coin3"] += arg1


            with open("kccData1.json","w") as f:
                json.dump(users,f)
            arg1 = str(arg1)
            embed=discord.Embed(title=f"Given {arg1} KCC to walletid {walletid.id}", color=0x00FF00)
            embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
            await ctx.send(embed=embed)      
                
        elif arg2 == "Dexa" or arg2 == "coin2":
            
            users[str(walletid.id)]["coin2"] += arg1
            if IGB == None:
                users[str(929595294583242822)]["coin2"] -= arg1
            else:
                users[str(929595294583242822)]["oricoin2"] += arg1
            with open("kccData1.json","w") as f:
                json.dump(users,f)
            arg1 = str(arg1)
            embed=discord.Embed(title=f"Given {arg1} {mainbotprefixSpace}to walletid {walletid.id}", color=0x00FF00)
            embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
            await ctx.send(embed=embed)      

        elif arg2 == "bank" or arg2 == "bankBalance" or arg2 == "bank_balance" or arg2 == "coin3":
            
            users[str(walletid.id)]["coin3"] += arg1
            if IGB == None:
                users[str(929595294583242822)]["coin3"] -= arg1
            else:
                users[str(929595294583242822)]["coin3"] += arg1
            with open("kccData1.json","w") as f:
                json.dump(users,f)
            arg1 = str(arg1)
            embed=discord.Embed(title=(f"Given {arg1} KevCoin bank balance to walletid {walletid.id}"), color=0x00FF00)
            embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
            await ctx.send(embed=embed)      
        else:
            await ctx.send("What coin? Can be:\ncoin1, coin2, coin3") 
    else:
        embed=discord.Embed(title=f"❌ Sorry, but you need at least 'mod' rank to use this command!", color=0xFF0000)
        embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
        await ctx.send(embed=embed)

@client.command(aliases=['premin.hourly'])     
@commands.cooldown(1, 3600, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?
async def hourly(ctx):
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'hourly' command")
    await open_account(ctx.author)
    user = ctx.author
    users = await get_coin2_data()
    ranklvl = users[str(user.id)]["rank"]

    if secondint >= 1 or ranklvl == "mod" or ranklvl == "admin":
        global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
        coin1_amt = users[str(929595294583242822)]["coin1"]
        coin2_amt = users[str(929595294583242822)]["coin2"]
        coin3_amt = users[str(929595294583242822)]["coin3"]
        coin1_bot = users[str(929595294583242822)]["coin1"]
        coin2_bot = users[str(929595294583242822)]["coin2"]

        if coin1_bot >= 1000:
            if coin1_amt > 0:
                earnings = 500
                earningsDexa = 0
                # if coin2_bot >= 1:
                #     earningsDexa = 1

                users[str(user.id)]["coin1"] += earnings
                users[str(user.id)]["coin2"] += earningsDexa
                users[str(929595294583242822)]["coin1"] -= earnings
               # users[str(929595294583242822)]["coin2"] -= earningsDexa
                print(f"{earnings}, {earningsDexa} | {coin1_bot}, {coin2_bot}")
                embed=discord.Embed(title="🕒 Hourly reward", description=(ctx.author.mention + f", the KCGame bot gave you:\n+{earnings} KCC"), color=0x00FF00)
                embed.set_author(name="Kevcore Game - hourly")
                embed.set_footer(text=("For more rewards, check out the  faucet command"))
                await ctx.send(embed=embed)        
                with open("kccData1.json","w") as f:
                    json.dump(users,f)
        else:
            embed=discord.Embed(title="KCGame bot has no more cash to give out!", description=("There isn't enough cash for the KCGame bot to give out!"), color=0xff0000)
            embed.set_author(name="Kevcore Game - hourly")
            embed.set_footer(text="Consider asking other people to donate or donate yourself")
            
    else:
        embed=discord.Embed(title=f"❌ Sorry, but you need at least 'premin' rank to use this command!", color=0xFF0000)
        embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
        await ctx.send(embed=embed)
# @client.command(aliases=['admin.set'])      
# async def set(ctx, arg1, arg2, walletid: discord.Member=None):
#     print(f"User {ctx.author.name} ({ctx.author.id}) ran 'give' command")
#     await open_account(ctx.author)
#     user = ctx.author
#     users = await get_coin2_data()
#     ranklvl = users[str(user.id)]["rank"]
#     if ranklvl == "admin":
#         await open_account(ctx.author)
#         user = ctx.author
#         users = await get_coin2_data()
#         users = await get_coin3_data()
#         global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
#         if walletid is None:
#             walletid = ctx.author
#             coin1_amt = users[str(user.id)]["coin1"]
#             coin2_amt = users[str(user.id)]["coin2"]
#             coin3_amt = users[str(user.id)]["coin3"]
        
#         else:
#             coin1_amt = users[str(walletid.id)]["coin1"]
#             coin2_amt = users[str(walletid.id)]["coin2"]
#             coin3_amt = users[str(walletid.id)]["coin3"]
#         arg1 = int(arg1)
#         if arg2 == "KevCoin" or arg2 == "KCC" or arg2 == "kc" or arg2 == "coin1":
            
#             users[str(walletid.id)]["coin1"] = arg1
#             with open("kccData1.json","w") as f:
#                 json.dump(users,f)
#             arg1 = str(arg1)
#             embed=discord.Embed(title=f"Set {arg1} KCC to wallet id {walletid.id}", color=0x00FF00)
#             embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#             await ctx.send(embed=embed)      
                
#         elif arg2 == "Dexa" or arg2 == "coin2":
            
#             users[str(walletid.id)]["coin2"] = arg1
#             with open("kccData1.json","w") as f:
#                 json.dump(users,f)
#             arg1 = str(arg1)
#             embed=discord.Embed(title=f"Set {arg1} {mainbotprefixSpace}to wallet id {walletid.id}", color=0x00FF00)
#             embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#             await ctx.send(embed=embed)      

#         elif arg2 == "bank" or arg2 == "bank_balance" or arg2 == "kcbank" or arg2 == "coin3":
            
#             users[str(walletid.id)]["coin3"] = arg1
#             with open("kccData1.json","w") as f:
#                 json.dump(users,f)
#             arg1 = str(arg1)
#             embed=discord.Embed(title=f"Set the KevCoin Bank balance to {arg1} for wallet id {walletid.id}", color=0x00FF00)
#             embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#             await ctx.send(embed=embed)      
#         else:
#             await ctx.send("What coin? Can be:\ncoin1, coin2, coin3") 
#     else:
#         embed=discord.Embed(title=f"❌ Sorry, but you need at least 'mod' rank to use this command!", color=0xFF0000)
#         embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#         await ctx.send(embed=embed)

# @client.command(aliases=['deposit', 'storeAmount'])
# @commands.cooldown(1, 3, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?
# async def dep(ctx, depAmount=None):
#     print(f"User {ctx.author.name} ({ctx.author.id}) ran 'dep' command\n{depAmount}")
#     if depAmount == None:
#         embed=discord.Embed(title=f"You need an argument (Amount to deposit)!", color=0xFF0000)
#         embed.set_author(name="Error while running command (can't run):")
#         embed.set_footer(text="Error code: dep-noArg1")
#         await ctx.send(embed=embed)   
#     else:
#         await open_account(ctx.author)
#         user = ctx.author
#         users = await get_coin2_data()
#         users = await get_coin3_data()
#         global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
#         coin1_amt = users[str(user.id)]["coin1"]
#         coin2_amt = users[str(user.id)]["coin2"]
#         coin3_amt = users[str(user.id)]["coin3"]

#         ttlKCamt = coin1_amt+coin3_amt
#         ttlKCamt = int(ttlKCamt)
       
#         if depAmount == "all" or depAmount == "max":
#             depAmount = (ttlKCamt/10 - coin3_amt)
#             # depAmount = coin3_amt
#             # depAmount = int(depAmount)        
#             # if depAmount > coin3_amt:
#             #     embed=discord.Embed(title=f"error while running dep", color=0xFF0000)
#             #     embed.set_footer(text="Error code: dep-wdDepAmount>coin3")
#             #     await ctx.send(embed=embed)
#             # elif depAmount < 1:
#             #     embed=discord.Embed(title=f"error while running dep", color=0xFF0000)
#             #     embed.set_footer(text="Error code: dep-wdDepAmount<1")
#             #     await ctx.send(embed=embed)
#             # else:
#             #     # users[str(user.id)]["coin1"] += depAmount
#             #     # users[str(user.id)]["coin3"] -= depAmount
#             #     # embed=discord.Embed(title=f"Success", description=f"<@!{user.id}> withdrawed {depAmount} to their KevCoin balance", color=0x00FF00)
#             #     # embed.set_author(name="Kevcore Game - withdraw")
#             # # embed.set_footer(text="Error code: dep-arg1MoreThanKcBal")
#             #     # await ctx.send(embed=embed)
#             #     with open("kccData1.json","w") as f:
#             #         json.dump(users,f)
#         depAmount = int(depAmount)
#         tooMuch = coin3_amt+depAmount
#         intMaxBank = int(ttlKCamt/10)
#         if depAmount > coin1_amt:
#             embed=discord.Embed(title=f"Deposit amount can't be higher than your KevCoin balance!", color=0xFF0000)
#             embed.set_author(name="Error while running command (can't run):")
#             embed.set_footer(text="Error code: dep-arg1MoreThanKcBal")
#             await ctx.send(embed=embed)
#         elif tooMuch > ttlKCamt/10:
#             embed=discord.Embed(title=f"Maximum amount of bank balance is 10% of your total KCC", description=f"Your current maximum balance for your bank is: {intMaxBank}\nYour current bank balance is {coin3_amt}\nRun '{mainbotprefixSpace}dep all' to deposit the maxmium amount you can have", color=0xFF0000)
#             embed.set_author(name="Error while running command (can't run):")
#             embed.set_footer(text="Error code: dep-arg1MoreThanKcBal")
#             await ctx.send(embed=embed)
#         elif depAmount < 1:
#             embed=discord.Embed(title=f"Deposit amount can't be 0 or less!", color=0xFF0000)
#             embed.set_author(name="Error while running command (denied):")
#             embed.set_footer(text="Error code: dep-arg1LessThan1")
#             await ctx.send(embed=embed)
#         else:
#             users[str(user.id)]["coin1"] -= depAmount
#             users[str(user.id)]["coin3"] += depAmount
#             embed=discord.Embed(title=f"Success", description=f"<@!{user.id}> deposited {depAmount} to their KevCoin bank", color=0x00FF00)
#             embed.set_author(name="Kevcore Game - deposit")
#            # embed.set_footer(text="Error code: dep-arg1MoreThanKcBal")
#             await ctx.send(embed=embed)
#             with open("kccData1.json","w") as f:
#                 json.dump(users,f)

# @client.command(aliases=['withdraw', 'with'])
# @commands.cooldown(1, 1, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?
# async def wd(ctx, depAmount=None):
#     print(f"User {ctx.author.name} ({ctx.author.id}) ran 'wd' command\n{depAmount}")
#     if depAmount == None:
#         embed=discord.Embed(title=f"You need an argument (Amount to withdraw)!", color=0xFF0000)
#         embed.set_author(name="Error while running command (can't run):")
#         embed.set_footer(text="Error code: wd-noArg1")
#         await ctx.send(embed=embed)   
#     else:
#         await open_account(ctx.author)
#         user = ctx.author
#         users = await get_coin2_data()
#         users = await get_coin3_data()
#         global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
#         coin1_amt = users[str(user.id)]["coin1"]
#         coin2_amt = users[str(user.id)]["coin2"]
#         coin3_amt = users[str(user.id)]["coin3"]
#         if depAmount == "all" or depAmount == "max":
#             depAmount = coin3_amt
#         depAmount = int(depAmount)        
#         if depAmount > coin3_amt:
#             embed=discord.Embed(title=f"Withdraw amount can't be higher than your bank balance!", color=0xFF0000)
#             embed.set_author(name="Error while running command (can't run):")
#             embed.set_footer(text="Error code: wd-arg1MoreThanBankBal")
#             await ctx.send(embed=embed)
#         elif depAmount < 1:
#             embed=discord.Embed(title=f"Withdraw amount can't be 0 or less!", color=0xFF0000)
#             embed.set_author(name="Error while running command (denied):")
#             embed.set_footer(text="Error code: wd-arg1LessThan1")
#             await ctx.send(embed=embed)
#         else:
#             users[str(user.id)]["coin1"] += depAmount
#             users[str(user.id)]["coin3"] -= depAmount
#             embed=discord.Embed(title=f"Success", description=f"<@!{user.id}> withdrawed {depAmount} to their KevCoin balance", color=0x00FF00)
#             embed.set_author(name="Kevcore Game - withdraw")
#            # embed.set_footer(text="Error code: dep-arg1MoreThanKcBal")
#             await ctx.send(embed=embed)
#             with open("kccData1.json","w") as f:
#                 json.dump(users,f)












@client.command(aliases=['trade'])
@commands.cooldown(3, 1, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?
async def exchange(ctx, cointypeFrom=None, cointypeTo=None, amt=None):
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'exchange' command")
    await open_account(ctx.author)
    users = await get_coin2_data()
    user = ctx.author
    earnings = 1
    earnornot = 1
    earnornot = random.randrange(1,3)
    earnings = random.randrange(0,100)
    users = await get_coin3_data()
    global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
    coin1_amt = users[str(user.id)]["coin1"]
    coin2_amt = users[str(user.id)]["coin2"]
    coin3_amt = users[str(user.id)]["coin3"]
    coin1_bot = users[str(929595294583242822)]["coin1"]
    coin2_bot = users[str(929595294583242822)]["coin2"]
    coin3_bot = users[str(929595294583242822)]["coin3"]

    if coin1_bot > (coin3_bot/1.5):
        KCliquidity = "HIGH"
    elif coin1_amt > (coin3_amt/3):
        KCliquidity = "MEDIUM"
    else:
        KCliquidity = "LOW"

    ceKcTOSc = users[str(929595294583242822)]["ceKcTOSc"] #orginal: 100k. more = bad
    ceKcTOScAMT = users[str(929595294583242822)]["ceKcTOScAMT"] #Oringal: 1 more = good
    ceKcTOScLiquidity1 = 50000/ceKcTOSc
    ceKcTOScLiquidity2 = ceKcTOScAMT/1
    ceKcTOScLiquidity = (ceKcTOScLiquidity1*ceKcTOScLiquidity2 * 100)
#, "ceKcTOSc": 0, "ceKcTOScAMT": 20, "ceScTOKc": 0, "ceScTOKcAMT": 20
    ceScTOKc = users[str(929595294583242822)]["ceScTOKc"] #orginal: 1
    ceScTOKcAMT = users[str(929595294583242822)]["ceScTOKcAMT"] #Oringal: 5k
    ceScTOKcLiquidity1 = 1/ceScTOKc
    ceScTOKcLiquidity2 = ceScTOKcAMT/5000
    ceScTOKcLiquidity = (ceScTOKcLiquidity1*ceScTOKcLiquidity2 * 100)
    if ceKcTOScLiquidity >= 75:
        ceKCDexaLTXT = "HIGH"
    elif ceKcTOScLiquidity >= 50:
        ceKCDexaLTXT = "MEDIUM"
    elif ceKcTOScLiquidity >= 25:
        ceKCDexaLTXT = "LOW"
    elif ceKcTOScLiquidity >= 0:
        ceKCDexaLTXT = "VERY LOW"
    if coin2_bot <= 0:
        ceKCDexaLTXT = "NONE"

    if ceScTOKcLiquidity >= 75:
        ceDexaKCLTXT = "HIGH"
    elif ceScTOKcLiquidity >= 50:
        ceDexaKCLTXT = "MEDIUM"
    elif ceScTOKcLiquidity >= 25:
        ceDexaKCLTXT = "LOW"
    elif ceScTOKcLiquidity >= 0:
        ceDexaKCLTXT = "VERY LOW"
    if coin2_bot <= 0:
        ceDexaKCLTXT = "NONE"
    if cointypeFrom == None:
        embed=discord.Embed(title="Exchange prices\n", color=0xff00ff)
        embed.set_author(name="Kevcore Game - Exchange")
        embed.add_field(name="KCC → Dexa", value=f"{ceKcTOSc} KC → {ceKcTOScAMT} Dexa\nLiquidity: {ceKcTOScLiquidity}% ({ceKCDexaLTXT})", inline=False)
        embed.add_field(name=f"{mainbotprefixSpace}→ KCC", value=f"{ceScTOKc} Dexa → {ceScTOKcAMT} Kc\nLiquidity: {ceScTOKcLiquidity}% ({ceDexaKCLTXT})", inline=False)
        embed.add_field(name="Exchange Format", value=f'''
{mainbotprefixSpace}exchange <arg1> <arg2> <amount>
⠀⠀⠀arg1 - The currency your trading from ({mainbotprefixSpace}→ kc)
⠀⠀⠀arg2 - The currency your trading from ({mainbotprefixSpace}→ kc)
⠀⠀⠀amount - The amount you of arg1 do you want to trade? (Not arg2!)
For an example, to trade 1 {mainbotprefixSpace}into 1000 (Price) KCC, run {mainbotprefixSpace}exchange {mainbotprefixSpace}{mainbotprefixSpace}1
See above for the prices
        ''')
        embed.set_footer(text="To trade KCC into Dexa, $trade {mainbotprefixSpace}{mainbotprefixSpace}1 \nHigher liquidity = better exchange rates")

        await ctx.send(embed=embed)   
    elif cointypeTo == None:
        embed=discord.Embed(title="From arg check, to arg wrong.", description=("To What type? $trade to see."), color=0xff0000)
        embed.set_author(name="Kevcore Game - exchange")
        await ctx.send(embed=embed)        
    elif amt == None:
        embed=discord.Embed(title="From arg check, to arg check, amt arg wrong.", description=("How many do u wanna trade? see using $trade"), color=0xff0000)
        embed.set_author(name="Kevcore Game - exchange")
        await ctx.send(embed=embed)        
    else:
        if cointypeFrom == "kc" or cointypeFrom == "coin1":
            if cointypeTo == "Dexa":
                amt = int(amt)

                amount = ceKcTOSc*amt #turns 1 into like 10k
                GETamount = ceKcTOScAMT*amt #how much to get
                if amount <= coin1_amt: #if amount less than bal then exchange 
                    if amount < 1:
                        embed=discord.Embed(title="has to be over 0!", description=("amount needs to be 1 or over"), color=0xff0000)
                        embed.set_author(name="Kevcore Game - exchange")
                        await ctx.send(embed=embed)      
                        return 0  
                    if coin2_bot > GETamount: #if bot has more {mainbotprefixSpace}than GETamount (user getting Dexa) then
                        users[str(user.id)]["coin1"] -= amount
                        users[str(user.id)]["coin2"] += GETamount
                        users[str(929595294583242822)]["coin1"] += amount
                        users[str(929595294583242822)]["coin2"] -= GETamount
                        with open("kccData1.json","w") as f:
                            json.dump(users,f)
                        embed=discord.Embed(title=f"Exchanged {amount} KC → {GETamount} Dexa", description=(f"Yay"), color=0x00FF00) #if above code fails then this message wont send
                        embed.set_author(name="Kevcore Game - exchange")
                    #    embed.set_footer(text=("There's a chance (1/3) to get caught while begging\nYou can only use this command 3 times every 30 seconds"))
                        await ctx.send(embed=embed)        

                    else: #no more {mainbotprefixSpace};(
                        embed=discord.Embed(title="KCGame bot has no more cash to give out!", description=("There isn't enough cash for the KCGame bot to give out!"), color=0xff0000)
                        embed.set_author(name="Kevcore Game - exchange")
                        embed.set_footer(text="Consider asking other people to donate or donate yourself")
                        await ctx.send(embed=embed)        
                else: #if not enough then:
                    embed=discord.Embed(title="You don't have enough KCC!", description=(f"You have {coin1_amt} but you need {amount}"), color=0xff0000)
                    embed.set_author(name="Kevcore Game - exchange")
                    embed.set_footer(text="bruh")
                    await ctx.send(embed=embed)                         
            else:
                embed=discord.Embed(title="to currency not found", description=("see $trade. i think u might be trading to 'Dexa'?"), color=0xff0000)
                embed.set_author(name="Kevcore Game - exchange")
                await ctx.send(embed=embed)
        elif cointypeFrom == "Dexa" or cointypeFrom == "coin2":
            if cointypeTo == "kc" or cointypeFrom == "coin1":
                amt = int(amt)

                amount = ceScTOKc*amt #turns 1 into like 10k
                GETamount = ceScTOKcAMT*amt #how much to get
                if amount <= coin2_amt: #if amount less than bal then exchange 
                    if amount < 1:
                        embed=discord.Embed(title="has to be over 0!", description=("amount needs to be 1 or over"), color=0xff0000)
                        embed.set_author(name="Kevcore Game - exchange")
                        await ctx.send(embed=embed)      
                        return 0  
                    if coin1_bot > GETamount: #if bot has more {mainbotprefixSpace}than GETamount (user getting kc) then
                        users[str(user.id)]["coin2"] -= amount
                        users[str(user.id)]["coin1"] += GETamount
                        users[str(929595294583242822)]["coin2"] += amount
                        users[str(929595294583242822)]["coin1"] -= GETamount
                        with open("kccData1.json","w") as f:
                            json.dump(users,f)
                        embed=discord.Embed(title=f"Exchanged {amount} Dexa → {GETamount} kc", description=(f"Yay"), color=0x00FF00) #if above code fails then this message wont send
                        embed.set_author(name="Kevcore Game - exchange")
                    #    embed.set_footer(text=("There's a chance (1/3) to get caught while begging\nYou can only use this command 3 times every 30 seconds"))
                        await ctx.send(embed=embed)        

                    else: #no more {mainbotprefixSpace};(
                        embed=discord.Embed(title="KCGame bot has no more cash to give out!", description=("There isn't enough cash for the KCGame bot to give out!"), color=0xff0000)
                        embed.set_author(name="Kevcore Game - exchange")
                        embed.set_footer(text="Consider asking other people to donate or donate yourself")
                        await ctx.send(embed=embed)        
                else: #if not enough then:
                    embed=discord.Embed(title="You don't have enough Dexa!", description=(f"You have {coin2_amt} but you need {amount}"), color=0xff0000)
                    embed.set_author(name="Kevcore Game - exchange")
                    embed.set_footer(text="bruh")
                    await ctx.send(embed=embed)                         
            else:
                embed=discord.Embed(title="to currency not found", description=("see $trade. i think u might be trading to 'Dexa'?"), color=0xff0000)
                embed.set_author(name="Kevcore Game - exchange")
                await ctx.send(embed=embed)       
        else:
            embed=discord.Embed(title="from currency not found", description=("see $trade"), color=0xff0000)
            embed.set_author(name="Kevcore Game - exchange")
            await ctx.send(embed=embed)                         




















@client.command(aliases=['mine'])
@commands.cooldown(3, 30, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?
async def beg(ctx):
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'beg' command")
    await open_account(ctx.author)
    users = await get_coin2_data()
    user = ctx.author
    earnornot = 1
    earnornot = random.randrange(1,3)
    earnings = random.randrange(0,100)
    users = await get_coin3_data()
    global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
    coin1_amt = users[str(user.id)]["coin1"]
    coin2_amt = users[str(user.id)]["coin2"]
    coin3_amt = users[str(user.id)]["coin3"]
    coin1_bot = users[str(929595294583242822)]["coin1"]
    divPERCENT = coin1_amt/100
    if divPERCENT <= 0.01:
        divPERCENT = 0.01
    divAMT = 1-divPERCENT                                      
    earnings = earnings*divAMT
    if coin1_bot >= 100:
        if earnornot == 1:
            if coin1_amt > 0:
                embed=discord.Embed(title="Oh no!", description=(""+ ctx.author.mention + f" was fined {earnings} KCC for getting caught while begging"), color=0xff0000)
                embed.set_author(name="Kevcore Game - beg")
                embed.set_footer(text="rip")
                users[str(user.id)]["coin1"] -= earnings
                users[str(929595294583242822)]["coin1"] += earnings
                with open("kccData1.json","w") as f:
                    json.dump(users,f)
                print("lol imainge")
            else:
                embed=discord.Embed(title="Oh no!", description=(""+ ctx.author.mention + f" was caught while begging!\nBut because they have no money (or in debt), they was not fined"), color=0xff0000)
                embed.set_author(name="Kevcore Game - beg")
                embed.set_footer(text="imagine having debt")
                print("lol imainge")
            await ctx.send(embed=embed)        

        else:
        
            embed=discord.Embed(title="Reward", description=(f"The KCGame bot gave "+ ctx.author.mention + f" {earnings} KCC!"), color=0x00FF00)
            embed.set_author(name="Kevcore Game - beg")
            embed.set_footer(text=("There's a chance (1/3) to get caught while begging\nYou can only use this command 3 times every 30 seconds"))
            await ctx.send(embed=embed)        
            users[str(user.id)]["coin1"] += earnings
            users[str(929595294583242822)]["coin1"] -= earnings
            with open("kccData1.json","w") as f:
                json.dump(users,f)
    else:
        embed=discord.Embed(title="KCGame bot has no more cash to give out!", description=("There isn't enough cash for the KCGame bot to give out!"), color=0xff0000)
        embed.set_author(name="Kevcore Game - beg")
        embed.set_footer(text="Consider asking other people to donate or donate yourself")
@client.command(aliases=['cf', 'coin', 'flip'])
@commands.cooldown(1, 5, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?

async def coinflip(ctx, amount=None):
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'coinflip' command. set: {amount}")
    await open_account(ctx.author)
    users = await get_coin2_data()
    user = ctx.author
    earnings = 1
    earnornot = 1
    earnornot = random.randrange(1,100)
    users = await get_coin3_data()
    global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
    coin1_amt = users[str(user.id)]["coin1"]
    coin2_amt = users[str(user.id)]["coin2"]
    coin3_amt = users[str(user.id)]["coin3"]
    coin1_bot = users[str(929595294583242822)]["coin1"]
    if coin1_amt > 100:
        kccReduce = 0.01
    elif coin1_amt > 90:
        kccReduce = 0.1
    elif coin1_amt > 80:
        kccReduce = 0.2
    elif coin1_amt > 70:
        kccReduce = 0.3
    elif coin1_amt > 60:
        kccReduce = 0.4
    elif coin1_amt > 50:
        kccReduce = 0.5
    elif coin1_amt > 40:
        kccReduce = 0.6
    elif coin1_amt > 30:
        kccReduce = 0.7
    elif coin1_amt > 20:
        kccReduce = 0.8
    elif coin1_amt > 10:
        kccReduce = 0.9
    else:
        kccReduce = 1
    if amount == None:
        embed=discord.Embed(title="Error while running command (won't run)", description=("Didn't put an amount"), color=0xff0000)
        embed.set_author(name="Kevcore Game - coinflip")
        embed.set_footer(text="Error code: flip-amount=None")
        await ctx.send(embed=embed)        
        coinflip.reset_cooldown(ctx)
    else:
        amount = float(amount)
        if amount < 0:
            embed=discord.Embed(title="Error while running command (denied)", description=("You can't put negatives for the amount!"), color=0xff0000)
            embed.set_author(name="Kevcore Game - coinflip")
            embed.set_footer(text="You can put 0, though\nError code: flip-amount<0")
            await ctx.send(embed=embed)        
            coinflip.reset_cooldown(ctx)
            return 0
        elif amount == 0:
            coinflip.reset_cooldown(ctx)
        elif amount > 1:
            embed=discord.Embed(title="Error while running command (denied)", description=("You can only bet up to 1 KCC"), color=0xff0000)
            embed.set_author(name="Kevcore Game - coinflip")
      #      embed.set_footer(text="")
            await ctx.send(embed=embed)         
            return 0        
        earnings = amount


        if amount <= coin1_amt:
            if coin1_bot >= amount:
                if earnornot >= 50:
                    if coin1_amt > 0:
                        embed=discord.Embed(title="Oh no!", description=(""+ ctx.author.mention + f"'s coin landed on tails\nHe/She lost {earnings} KCC"), color=0xff0000)
                        embed.set_author(name="Kevcore Game - coinflip")
                        embed.set_footer(text="RIP")
                        users[str(user.id)]["coin1"] -= earnings
                        users[str(929595294583242822)]["coin1"] += earnings
                        with open("kccData1.json","w") as f:
                            json.dump(users,f)
                        print("lost set XD")
                        await ctx.send(embed=embed)        

                else:
                                 
                    earnings = earnings*kccReduce
                    embed=discord.Embed(title="Reward", description=(f"The KCGame bot gave "+ ctx.author.mention + f" {earnings} KCC for winning their bet!"), color=0x00FF00)
                    embed.set_author(name="Kevcore Game - coinflip")
                    embed.set_footer(text=("Coin landed on heads, good job!"))
                    await ctx.send(embed=embed)        
                    users[str(user.id)]["coin1"] += earnings
                    users[str(929595294583242822)]["coin1"] -= earnings
                    with open("kccData1.json","w") as f:
                        json.dump(users,f)
                    print("won set XD")

            else:
                embed=discord.Embed(title="KCGame bot has no more cash to give out!", description=("There isn't enough cash for the KCGame bot to give out!"), color=0xff0000)
                embed.set_author(name="Kevcore Game - coinflip")
                embed.set_footer(text="Consider asking other people to donate or donate yourself")
                await ctx.send(embed=embed)        

        else:
            embed=discord.Embed(title="Error while running command (denied)", description=("Amount is higher than your balance!"), color=0xff0000)
            embed.set_author(name="Kevcore Game - coinflip")
            embed.set_footer(text="Error code: flip-amount>coin1_amt")
            await ctx.send(embed=embed)        
            coinflip.reset_cooldown(ctx)

@client.command()
@commands.cooldown(1, 1, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?

async def daily(ctx):
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'daily' command")
    await open_account(ctx.author)
    users = await get_coin2_data()
    user = ctx.author
    global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
    coin1_amt = users[str(user.id)]["coin1"]
    coin2_amt = users[str(user.id)]["coin2"]
    coin3_amt = users[str(user.id)]["coin3"]
    coin1_bot = users[str(929595294583242822)]["coin1"]
    coin2_bot = users[str(929595294583242822)]["coin2"]
    if coin1_amt > 100:
        kccReduce = 0.01
    elif coin1_amt > 90:
        kccReduce = 0.1
    elif coin1_amt > 80:
        kccReduce = 0.2
    elif coin1_amt > 70:
        kccReduce = 0.3
    elif coin1_amt > 60:
        kccReduce = 0.4
    elif coin1_amt > 50:
        kccReduce = 0.5
    elif coin1_amt > 40:
        kccReduce = 0.6
    elif coin1_amt > 30:
        kccReduce = 0.7
    elif coin1_amt > 20:
        kccReduce = 0.8
    elif coin1_amt > 10:
        kccReduce = 0.9
    else:
        kccReduce = 1
         
    #user = 'KEVCORE25'
    print(123)
    if coin1_bot >= 1000:
        print(123)
        if True:
            print(123)
            reptAmt = 0
            earnings = 3

            earningsDexa = 0
            earnings = earnings*kccReduce
            users[str(user.id)]["coin1"] += earnings
            users[str(user.id)]["coin2"] += earningsDexa
            users[str(929595294583242822)]["coin1"] -= earnings
            users[str(929595294583242822)]["coin2"] -= earningsDexa

            print(f"{earnings}, {earningsDexa} | {coin1_bot}, {coin2_bot}")

            with open("kccData1.json","w") as f:
                json.dump(users,f)

            embed=discord.Embed(title="Daily reward", description=(ctx.author.mention + f", the KCGame bot gave you:\n+{earnings} KCC\n+{earningsDexa} Dexa"), color=0x00FF00)
            embed.set_author(name="Kevcore Game - daily")
            embed.set_footer(text=("For more rewards, check out the work and faucet command"))
            await ctx.send(embed=embed)     
    else:
        embed=discord.Embed(title="KCGame bot has no more cash to give out!", description=("There isn't enough cash for the KCGame bot to give out!"), color=0xff0000)
        embed.set_author(name="Kevcore Game - daily")
        embed.set_footer(text="Consider asking other people to donate or donate yourself")
lastDonator = "N\A"
lastDonatorAmount = 0
topDonator = "N\A"
topDonatorAmount = 0
@client.command(aliases=['get_money', 'minute', 'minutely'])
@commands.cooldown(1, 30, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?

async def faucet(ctx, donateint=0):
    await open_account(ctx.author)
    users = await get_coin2_data()
    user = ctx.author
    global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
    coin1user = users[str(user.id)]["coin1"]
    coin1_amt = users[str(929595294583242822)]["coin1"]
    coin2_amt = users[str(929595294583242822)]["coin2"]
    faucet_amt = users[str(929595294583242822)]["faucet"]
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'faucet' command, {donateint}")
    donateint = int(donateint)
    if donateint == 0:
        if faucet_amt > 100:
            if coin1user < 2000:
                earnings = faucet_amt/1000
            else:
                earnings = faucet_amt/10000
            earnings = int(earnings)
            earningsDexa = 1
            global lastDonator, lastDonatorAmount, topDonator, topDonatorAmount
            embed=discord.Embed(title="Faucet reward", description=(ctx.author.mention + f", the KCGame bot gave you:\n+{earnings} KCC"), color=0x00FF00)
            embed.set_author(name="Kevcore Game - Faucet")
            embed.set_footer(text=(f"Top donator to the faucet: {topDonator} ({topDonatorAmount} KC)\nLast donator to the faucet: {lastDonator} ({lastDonatorAmount} KC)\n*not of all time"))
            await ctx.send(embed=embed)        
            users[str(user.id)]["coin1"] += earnings
            users[str(929595294583242822)]["faucet"] -= earnings
            print(f"{earnings} {mainbotprefixSpace}obtained, {faucet_amt} left")

            with open("kccData1.json","w") as f:
                json.dump(users,f)

        else:
            embed=discord.Embed(title="No more KCC!", description=("Sorry " + ctx.author.mention + f", the KCGame bot faucet has lower than 100 KCC!"), color=0xFF0000)
            embed.set_author(name="Kevcore Game - Faucet")
            embed.set_footer(text=("Consider donating to the bot using the send command to help everyone"))
            await ctx.send(embed=embed)    
            donateint.reset_cooldown(ctx)  

    elif donateint > 0:
        if coin1user >= donateint:
            embed=discord.Embed(title="Thanks for donating!", description=(f"Thank you for donating {donateint} KCC to the faucet, "+ctx.author.mention + f"!"), color=0x00FF00)
            embed.set_author(name="Kevcore Game - Faucet")
            embed.set_footer(text=("You just helped many people"))
            await ctx.send(embed=embed)        
            users[str(user.id)]["coin1"] -= donateint
            users[str(929595294583242822)]["faucet"] += donateint
            print(f"{donateint} {mainbotprefixSpace}donated, {faucet_amt} left")      
            with open("kccData1.json","w") as f:
                json.dump(users,f)   
            if lastDonatorAmount < donateint:
                topDonator = user  
                topDonatorAmount = donateint  
            lastDonator = user
            lastDonatorAmount = donateint
        else:          
            embed=discord.Embed(title="Error (Denied)", description=("You don't have enough KCC to donate, " + ctx.author.mention + f"!"), color=0xFF0000)
            embed.set_author(name="Kevcore Game - Faucet")
            embed.set_footer(text=("Thanks for trying to donate, though"))
            await ctx.send(embed=embed)  
        faucet.reset_cooldown(ctx)  

    else:
        embed=discord.Embed(title="Error (Denied)", description=("Donation has to be at least 1 KCC, " + ctx.author.mention + f"!"), color=0xFF0000)
        embed.set_author(name="Kevcore Game - Faucet")
        embed.set_footer(text=("Thanks for trying to donate, though"))
        await ctx.send(embed=embed)      
        faucet.reset_cooldown(ctx)  











@client.command(aliases=['gamble'])
@commands.cooldown(1, 30, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?

async def bet(ctx, amount=None):
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'bet' command. set: {amount}")
    await open_account(ctx.author)
    users = await get_coin2_data()
    user = ctx.author
    earnings = 1
    earnornot = 1

    print(earnornot)
    users = await get_coin3_data()
    global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
    coin1_amt = users[str(user.id)]["coin1"]
    coin2_amt = users[str(user.id)]["coin2"]
    coin3_amt = users[str(user.id)]["coin3"]
    coin1_bot = users[str(929595294583242822)]["coin1"]
    if amount == None:
        embed=discord.Embed(title="Error while running command (won't run)", description=("Didn't put an amount"), color=0xff0000)
        embed.set_author(name="Kevcore Game - bet")
        embed.set_footer(text="Error code: bet-amount=None")
        await ctx.send(embed=embed)        
        bet.reset_cooldown(ctx)
    else:
        amount = int(amount)

        if amount < 1000:
            embed=discord.Embed(title="Error while running command (denied)", description=("You need to put at least 1000 KCC!"), color=0xff0000)
            embed.set_author(name="Kevcore Game - bet")
            embed.set_footer(text="Error code: bet-amount<1000")
            await ctx.send(embed=embed)
            bet.reset_cooldown(ctx)
            return 0
        elif amount > 10000:
            embed=discord.Embed(title="Error while running command (denied)", description=("To prevent the next supply outage, the maxmium amount is 10000 KCC"), color=0xff0000)
            embed.set_author(name="Kevcore Game - coinflip")
            embed.set_footer(text="4.5.2 Bet Command with 10k limit, maybe soon 20k")
            await ctx.send(embed=embed)        
            bet.reset_cooldown(ctx)
            return 0        
        earnings = amount
        earnot = amount*2
        earnot = earnot/1000
        earnot = round(earnot)
        earnornot = random.randint(1,earnot)
        if amount <= coin1_amt:
            if coin1_bot >= amount:
                if earnornot > 1:
                    if coin1_amt > 0:
                        embed=discord.Embed(title="Oh no!", description=(""+ ctx.author.mention + f" lost his bet!\nThey lost {earnings} KCC"), color=0xff0000)
                        embed.set_author(name="Kevcore Game - bet")
                        embed.set_footer(text=f"You had a 1/{earnot} chance of winning")
                        users[str(user.id)]["coin1"] -= earnings
                        users[str(929595294583242822)]["coin1"] += earnings
                        with open("kccData1.json","w") as f:
                            json.dump(users,f)
                        print("lost set XD")
                        await ctx.send(embed=embed)        

                else:
                
                    embed=discord.Embed(title="Reward", description=(f"The KCGame bot gave "+ ctx.author.mention + f" {earnings} KCC for winning their bet!"), color=0x00FF00)
                    embed.set_author(name="Kevcore Game - bet")
                    embed.set_footer(text=(f"Good job, you had a 1/{earnot} chance of winning"))
                    await ctx.send(embed=embed)        
                    users[str(user.id)]["coin1"] += earnings
                    users[str(929595294583242822)]["coin1"] -= earnings
                    with open("kccData1.json","w") as f:
                        json.dump(users,f)
                    print("won set XD")

            else:
                embed=discord.Embed(title="KCGame bot has no more cash to give out!", description=("There isn't enough cash for the KCGame bot to give out!"), color=0xff0000)
                embed.set_author(name="Kevcore Game - bet")
                embed.set_footer(text="Consider asking other people to donate or donate yourself")
                await ctx.send(embed=embed)        
                bet.reset_cooldown(ctx)

        else:
            embed=discord.Embed(title="Error while running command (denied)", description=("Amount is higher than your balance!"), color=0xff0000)
            embed.set_author(name="Kevcore Game - bet")
            embed.set_footer(text="Error code: flip-amount>coin1_amt")
            await ctx.send(embed=embed)        
            bet.reset_cooldown(ctx)





















@client.command()
@commands.cooldown(1, 600, commands.BucketType.user) #when to start cooldown and how much cooldown and is it for the user, server, whole bot, or channel?
async def work(ctx):
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'work' command")
    if isinstance(ctx.channel, discord.channel.DMChannel):

        await open_account(ctx.author)
        users = await get_coin2_data()
        user = ctx.author
        global coin1, coin2, coin3, coin1_amt, coin2_amt, coin3_amt
        coin1user = users[str(user.id)]["coin1"]
        coin1_amt = users[str(929595294583242822)]["coin1"]
        coin2_amt = users[str(929595294583242822)]["coin2"]
        faucet_amt = users[str(929595294583242822)]["faucet"]
        if coin1_amt > 500:
            math1 = random.randrange(10,1000)
            math2 = random.randrange(10,1000)
            answerMath = math1*math2

            embed=discord.Embed(title="Work:", description=(ctx.author.mention + f", what is {math1} x {math2}?"), color=0x00FF00)
            embed.set_author(name="Kevcore Game - work")
            embed.set_footer(text=(f"Try to do it on paper, calculators are cheating"))
            await ctx.send(embed=embed)        
            msg = await client.wait_for('message', timeout=None)
            answerMath = str(answerMath)
            if msg.content == answerMath:
                earnings = random.randrange(500,1000)
                users[str(user.id)]["coin1"] += earnings
                users[str(929595294583242822)]["coin1"] -= earnings
                with open("kccData1.json","w") as f:
                    json.dump(users,f)
                embed=discord.Embed(title="Work reward", description=(ctx.author.mention + f", you solved the math equation and got:\n+{earnings} KCC"), color=0x00FF00)
                embed.set_author(name="Kevcore Game - work")
                embed.set_footer(text=(f"good work lol. hopefully u didnt use a calculator!"))
            else:
                embed=discord.Embed(title="Kevcore Game - Work", description=(ctx.author.mention + f", you didn't solve the math equation\nYou lost your chance at getting KCC"), color=0xFF0000)
                embed.set_author(name="Kevcore Game - work")
                embed.set_footer(text=(f"'so bad la'"))
            await ctx.send(embed=embed)        
        else:
            embed=discord.Embed(title="Kevcore Game - No money left", description=(ctx.author.mention + f", the KCGame bot has no more money to give out!"), color=0xFF0000)
            embed.set_author(name="Kevcore Game - work")
            embed.set_footer(text=(f"Consider asking other people to donate KCC or donate yourself"))
            await ctx.send(embed=embed)        
    else:
        embed=discord.Embed(title="Kevcore Game - Run this command as a DM", description=(ctx.author.mention + f", the work command has issues when ran on a server with active people\nPlease direct message me with the command"), color=0xFF0000)
        embed.set_author(name="Kevcore Game - work")
        embed.set_footer(text=(f"May get fixed later"))
        await ctx.send(embed=embed)
        work.reset_cooldown(ctx)  

# @client.command(aliases=['store'])
# async def shop(ctx):

#     embed=discord.Embed(title="Unknown error", description=(ctx.author.mention + "There was a problem running this command\nI also couldn't find the error"), color=0xff0000)
#     embed.set_author(name="Kevcore Game random error")
#     embed.set_footer(text="Error code: unknownRandomError")
#     await ctx.send(embed=embed)

@client.command(aliases=['reload', 'admin.reload', 'admin.restart'])
async def restart(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_coin2_data()
    ranklvl = users[str(user.id)]["rank"]
    if ranklvl == "admin":
        print(f"!!! User {ctx.author.name} ({ctx.author.id}) successfully ran 'restart' command, which could cause errors!")
        embed=discord.Embed(title=f"Restarting the program...", description=f"Exiting file and trying to open file location:\n||{os.path.abspath(__file__)}||", color=0x00CCFF)
        embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
        embed.set_footer(text=f"Last startup time: {startup} seconds\nWARNING: If the script is being edited while restarting, the bot may crash!")
        await ctx.send(embed=embed, delete_after=3.0)
        os.execl(sys.executable, sys.executable, *sys.argv)

    else:
        embed=discord.Embed(title=f"❌ Sorry, but you need at least 'admin' rank to use this command!", color=0xFF0000)
        embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
        await ctx.send(embed=embed)


@client.command(aliases=['showErrors'])
async def showCommandErrors(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_coin2_data()
    ranklvl = users[str(user.id)]["rank"]
    global showCommandErrorsVar
    if ranklvl == "admin":
        if showCommandErrorsVar == False:
            showCommandErrorsVar = True
            print(f"!!! User {ctx.author.name} ({ctx.author.id}) successfully ran 'showCommandErrors' command now changing to true")
            embed=discord.Embed(title=f"Ok", description=f"Set showCommandErrorsVar to True", color=0x00CCFF)
            embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
            await ctx.send(embed=embed, delete_after=3.0)
        else:
            print(f"!!! User {ctx.author.name} ({ctx.author.id}) successfully ran 'showCommandErrors' command now changing to false")
            showCommandErrorsVar = False

            embed=discord.Embed(title=f"Ok", description=f"Set showCommandErrorsVar to False", color=0x00CCFF)
            embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
            await ctx.send(embed=embed, delete_after=3.0)

    else:
        embed=discord.Embed(title=f"❌ Sorry, but you need at least 'admin' rank to use this command!", color=0xFF0000)
        embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
        await ctx.send(embed=embed)

@client.command(aliases=['del', 'purge', 'clear', 'clr', 'admin.delete', 'admin.purge', 'admin.clear', 'removeMessages', ])
async def delete(ctx,delamount=-1):
    print(f"User {ctx.author.name} ({ctx.author.id}) ran 'send' command\n{delamount}")
    await open_account(ctx.author)
    user = ctx.author
    users = await get_coin2_data()
    ranklvl = users[str(user.id)]["rank"]
    
    if ctx.message.author.guild_permissions.administrator == True or ctx.message.author.guild_permissions.manage_messages == True:
        if delamount > 0:
            embed=discord.Embed(title=f"Deleting messages...", description=f"Trying to delete {delamount} messages...", color=0x00CCFF)
            embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
            await ctx.send(embed=embed, delete_after=120)
            await ctx.channel.purge(limit=delamount+2)

            embed=discord.Embed(title=f"✅ Success", description=f"KCGame bot deleted {delamount} messages in this channel", color=0x00CCFF)
            embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
            await ctx.send(embed=embed, delete_after=5)
        else:
            embed=discord.Embed(title=f"Command requires integer argument higher than 0!", color=0xFF0000)
            embed.set_author(name="Kevcore Game admin - Error (denied)", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
            embed.set_footer(text="error code: del-intArg<1")

            await ctx.send(embed=embed, delete_after=120)        
    else:
        embed=discord.Embed(title=f"❌ Sorry, but you need to have the 'manage messages' permission to use this command!", color=0xFF0000)
        embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
        await ctx.send(embed=embed)        


# @client.command(aliases=['store'])
# async def shop(ctx,page=-1):
#     print(f"User {ctx.author.name} ({ctx.author.id}) ran 'shop' command\n{page}")
#     await open_account(ctx.author)
#     user = ctx.author
#     users = await get_coin2_data()
#     ranklvl = users[str(user.id)]["rank"]

#     embed=discord.Embed(title="Store:", color=0xff00ff)
#     embed.set_author(name="Kevcore Game help", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#     embed.add_field(name="KC Lock (id: lock)", value="When activated, every successful rob will turn into unsucessful robs. If lock blocks a rob, there's a 50% to break\nCost: `1 Dexa`", inline=False)


#    # embed.add_field(name=f"{mainbotprefixSpace}work", value="Work to get some money. Cooldown: 60s", inline=False)

#     embed.set_footer(text=f"To buy, type '{mainbotprefixSpace}buy <item id>'")
#     await ctx.send(embed=embed)    



# @client.command(aliases=['get'])
# async def buy(ctx,itemid="None", amount=1):
#     print(f"User {ctx.author.name} ({ctx.author.id}) ran 'buy' command\n{itemid} {amount}")
#     await open_account(ctx.author)
#     user = ctx.author
#     users = await get_coin2_data()
#     ranklvl = users[str(user.id)]["rank"]
#     coin1 = users[str(user.id)]["coin1"]
#     coin2 = users[str(user.id)]["coin2"]
#     hasKCLockQM = users[str(user.id)]["hasKCLock"]


#    # embed.add_field(name=f"{mainbotprefixSpace}work", value="Work to get some money. Cooldown: 60s", inline=False)


#     something = True
#     if something == True:
#         if itemid == "lock":
#             if coin2 >= 1:
#                 if hasKCLockQM == "Yes":
#                     embed=discord.Embed(title=f"❌ Already have a KC Lock!", description=f"<@{user.id}>, you have 1 `lock`, which is maximum you can hold", color=0xFF0000)
#                     embed.set_author(name="Kevcore Game - buy", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#                     await ctx.send(embed=embed)
#                 else:    
#                     users[str(user.id)]["hasKCLock"] = "Yes"
#                     users[str(user.id)]["coin2"] -= 1
#                     users[str(929595294583242822)]["coin2"] += 1

#                     embed=discord.Embed(title=f"✅ Success", description=f"<@{user.id}> bought `1` `lock` (Item automatically uses)", color=0x00FF00)
#                     embed.set_author(name="Kevcore Game - buy", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#                     await ctx.send(embed=embed)
#                     with open("kccData1.json","w") as f:
#                         json.dump(users,f)
#             else:
#                 embed=discord.Embed(title=f"❌ Not enough Dexa!", description=f"<@{user.id}>, you have `{coin2} Dexa` but the item you bought requires `1 Dexa`", color=0xFF0000)
#                 embed.set_author(name="Kevcore Game - buy", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#                 await ctx.send(embed=embed)
#         elif itemid == "premin":
#             if coin2 >= 10:
#                 global secondint
#                 if secondint >= 1:
#                     embed=discord.Embed(title=f"❌ Already have premin on!", description=f"<@{user.id}>, you have 1 `premin`, which is maximum you can hold", color=0xFF0000)
#                     embed.set_author(name="Kevcore Game - buy", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#                     await ctx.send(embed=embed)
#                 else:   
#                     users[str(user.id)]["coin2"] -= 10
#                     users[str(929595294583242822)]["coin2"] += 10

#                     try:

#                         #global secondint
#                        # secondint = 60
#                         if secondint <= 0:
#                             await ctx.send("I dont think im allowed to do negatives")
#                             raise BaseException
#                         while True:
#                             secondint -= 1
#                             if secondint == 0:
#                                 break
#                             await asyncio.sleep(1)
#                         await ctx.send(f"{ctx.author.mention} your premin ended!")
#                     except ValueError:
#                         await ctx.send("Must be a number!")                    
#                     embed=discord.Embed(title=f"✅ Success", description=f"<@{user.id}> bought `1` `premin` (Item automatically uses)", color=0x00FF00)
#                     embed.set_author(name="Kevcore Game - buy", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#                     await ctx.send(embed=embed)
#                     with open("kccData1.json","w") as f:
#                         json.dump(users,f)
#             else:
#                 embed=discord.Embed(title=f"❌ Not enough Dexa!", description=f"<@{user.id}>, you have `{coin2} Dexa` but the item you bought requires `10 Dexa`", color=0xFF0000)
#                 embed.set_author(name="Kevcore Game - buy", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#                 await ctx.send(embed=embed)
#         else:
#             embed=discord.Embed(title=f"{mainbotprefixSpace}buy requires a vaild item id!", color=0xFF0000)
#             embed.set_author(name="Kevcore Game - Error (denied)", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#             embed.set_footer(text="error code: buy-invaildItemId")

#             await ctx.send(embed=embed, delete_after=120)        
#     else:
#         embed=discord.Embed(title="❌ Sorry, but you need to have the '{something}' permission to use this command!", color=0xFF0000)
#         embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#         await ctx.send(embed=embed, delete_after=10)        


# @client.command(aliases=['test1'])
# async def timer(ctx, seconds):
#     print("test1")
#     try:
#         secondint = int(seconds)
#         if secondint <= 0:
#             await ctx.send("I dont think im allowed to do negatives")
#             raise BaseException
#         message = await ctx.send(f"Timer: {seconds}")
#         while True:
#             secondint -= 1
#             if secondint == 0:
#                 await message.edit(content="Ended!")
#                 break
#             await message.edit(content=f"Timer: {secondint}")
#             await asyncio.sleep(1)
#         await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
#     except ValueError:
#         await ctx.send("Must be a number!")

















async def open_account(user):
    users = await get_coin2_data()
    users = await get_coin3_data()

    if str(user.id) in users:
        return False
    else: 
        users[str(user.id)] = {}
        users[str(user.id)]["coin1"] = 0
        users[str(user.id)]["coin2"] = 0
        users[str(user.id)]["coin3"] = 0
        users[str(user.id)]["rank"] = "default"
        users[str(user.id)]["cmdcd"] = 0
        users[str(user.id)]["hasKCLock"] = "No"
        users[str(user.id)]["robCounter"] = 0
        users[str(user.id)]["userFriendly"] = "default"
        users[str(user.id)]["DMNotifs"] = "Yes"

        users[str(929595294583242822)]["memberCount"] += 1
        users[str(929595294583242822)]["coin3"] += 0


    with open("kccData1.json","w") as f:
        json.dump(users,f)
    return True


async def get_coin2_data():
    with open("kccData1.json","r") as f:
        users = json.load(f)
    return users
async def get_coin3_data():
    with open("kccData1.json","r") as f:
        users = json.load(f)
    return users
# showCommandErrorsVar = True

# if showCommandErrorsVar == True:
#     @client.event #if error while running command AND if its on cooldown then:
#     async def on_command_error(ctx, error):
#         if isinstance(error, commands.CommandOnCooldown):
#             cooldownTimeSec = round(error.retry_after)
#             cooldownTimeMin = 0
#             cooldownTimeHr = 0
#             users = await get_coin2_data()
#             user = ctx.author 
#             userFriendly = users[str(user.id)]["userFriendly"]   
#             while 1:
#                 if cooldownTimeSec >= 60:
#                     cooldownTimeMin += 1
#                     cooldownTimeSec -= 60
#                 elif cooldownTimeMin >= 60:
#                     cooldownTimeHr += 1
#                     cooldownTimeMin -= 60
#                 else:
#                     break
#             if cooldownTimeHr == 0:
#                 cooldownTimeHrTxt = ""
#             else:
#                 if userFriendly == "comfortable":
#                     cooldownTimeHrTxt = f"{cooldownTimeHr} hours, "
#                 else:
#                     cooldownTimeHrTxt = f"{cooldownTimeHr}h, "
#             if cooldownTimeMin == 0:
#                 cooldownTimeMinTxt = ""
#             else:
#                 if userFriendly == "comfortable":
#                     cooldownTimeMinTxt = f"{cooldownTimeMin} minutes, and "
#                 else:
#                     cooldownTimeMinTxt = f"{cooldownTimeMin}m, "

#             if userFriendly == "comfortable":
#                 cooldownTimeSecTxt = f"{cooldownTimeSec} seconds"
#                 msg1 = (f"{ctx.author.mention}, this command is on cooldown!\nYou can use it after")
#             else:
#                 cooldownTimeSecTxt = f"{cooldownTimeSec}s"
#                 msg1 = (f"Chill, {ctx.author.mention}! Wait")

#             embed=discord.Embed(description=f"{msg1} {cooldownTimeHrTxt}{cooldownTimeMinTxt}{cooldownTimeSecTxt}", color=0xff0000)
#             #embed.set_author(name="Kevcore Game - Command cooldown")
#            # embed.set_footer(text="Imagine spamming lmao")
#             await ctx.send(embed=embed)
#         elif isinstance(error, commands.CommandNotFound): #or if the command isnt found then:
#             embed=discord.Embed(description=f"This command doesn't exist (or isn't found)!\nSee '{mainbotprefixSpace}help' for a list of commands", color=0xff0000)
#             embed.set_author(name="Kevcore Game - Error", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#             #embed.set_footer(text="Error code: commandNotFound")
#             await ctx.send(embed=embed)


# async def noPermsMsg(): #show msg when no perms are meet 
    
#     #[[[[!!!!!! however code doesnt use it]]]]


#     embed=discord.Embed(title=f"Sorry, you can't access this command!", color=0xFF0000)
#     embed.set_author(name="Kevcore Game admin", icon_url="https://kevcoremc.github.io/purpletransparentKC.png")
#     await ctx.send(embed=embed)
    
client.run(TOKEN)


