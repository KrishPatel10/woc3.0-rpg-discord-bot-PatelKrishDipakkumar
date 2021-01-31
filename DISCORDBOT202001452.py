import discord
from discord.ext import commands
import random
import csv
import pandas as pd


try:
    with open("statis.csv", 'r', newline='') as old:
        rid = csv.reader(old)

except:
    with open("statis.csv", 'w', newline='') as new:
        writ = csv.writer(new)
        writ.writerow(['player id', 'HPPLAYER', 'HPEVIL', 'CLASS', 'LEVEL'])

client = commands.Bot(command_prefix='.')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def start(ctx):

    await ctx.send(f"{ctx.author.name} What you wanna be??\n")
    await ctx.send("🏹ARCHER🏹 \n 🧙MAGE🧙 \n  ⚔️WARRIOR⚔️")
    pid = ctx.author.name
    with open('statis.csv', 'r', newline='') as f:
        csvf = csv.reader(f)

        flag = 1
        clas = '0'

        for row in csvf:
            if row[0] == pid:
                flag = 0


        if flag == 1:
            with open('statis.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                hpp = 100
                hpe = 100
                level = 1

                writer.writerow([pid, hpp, hpe, clas, level])


@client.command()
async def archer(ctx):
    await ctx.send("Do you wanna \n⚔️attack  ⚔️\n 🛡️  evade 🛡️")

    pid = ctx.author.name

    with open('statis.csv', 'r', newline='') as remov:
        remover = csv.reader(remov)

        df = pd.read_csv('statis.csv')

        for row in remover:
            if row[0] == pid:
                df.loc[df["player id"] == pid, "CLASS"] = 'Archer'

        df.to_csv("statis.csv", index=False)


@client.command()
async def warrior(ctx):
    await ctx.send("Do you wanna \n⚔️attack  ⚔️\n 🛡️  evade 🛡️")

    pid = ctx.author.name

    with open('statis.csv', 'r', newline='') as remov:
        remover = csv.reader(remov)

        df = pd.read_csv('statis.csv')

        for row in remover:
            if row[0] == pid:
                df.loc[df["player id"] == pid, "CLASS"] = 'Warrior'

        df.to_csv("statis.csv", index=False)


@client.command()
async def mage(ctx):
    await ctx.send("Do you wanna \n⚔️attack  ⚔️\n 🛡️  evade 🛡️")

    pid = ctx.author.name

    with open('statis.csv', 'r', newline='') as remov:
        remover = csv.reader(remov)

        df = pd.read_csv('statis.csv')

        for row in remover:
            if row[0] == pid:
                df.loc[df["player id"] == pid, "CLASS"] = 'Mage'

        df.to_csv("statis.csv", index=False)


@client.command()
async def attack(ctx):

    hpe = random.randrange(0, 101)
    hpp = random.randrange(0, 101)

    with open('statis.csv', 'r', newline='') as f:
        csvf = csv.reader(f)
        for row in csvf:
            if row[0] == ctx.author.name:
                pid = ctx.author.name
                hpie = int(row[2])
                hpip = int(row[1])
                level = int(row[4])

    await ctx.send("You cut their "+str(hpe)+" HP")
    await ctx.send("They cut your "+str(hpp)+" HP")
    hpev = hpie-hpe
    hppl = hpip-hpp

    if (hpev < 0 and hppl >0):
        await ctx.send("YOU WON!!\n Iam resetting opponent's data!!!\nHURRAY\n LEVEL UP!!!")
        hpev = 100
        level = level + 1

    if (hppl < 0 and hpev>0):
        await ctx.send("YOU LOST!!!\n I am resetting your data!!!\n I am decreasing your level!!!")
        hppl = 100
        level = level-1

    if (hppl < 0 and hpev <0):
        await ctx.send("YOU BOTH DIED!!!\n FIGHT BACK\nI AM REVIVING BOTH OF YOU!!!")
        hppl = 100
        hpev = 100

    with open('statis.csv', 'r', newline='') as remov:
        remover = csv.reader(remov)

        df = pd.read_csv('statis.csv')

        for row in remover:
            if row[0] == pid:
                df.loc[df["player id"] == pid, "HPEVIL"] = str(hpev)
                df.loc[df["player id"] == pid, "HPPLAYER"] = str(hppl)
                df.loc[df["player id"] == pid, "LEVEL"] = str(level)

        df.to_csv("statis.csv", index=False)


@client.command()
async def evade(ctx):
    hpip = 100
    pid = ctx.author.name
    hpe = random.randrange(0, 101)
    hpp = random.randrange(0, 101)

    with open('statis.csv', 'r', newline='') as f:
        csvf = csv.reader(f)

        for row in csvf:
            if row[0] == pid:
                hpip = int(row[1])
                hpie = int(row[2])
                level = int(row[4])

    await ctx.send("They cut your "+str(hpp)+" HP")
    await ctx.send("You cut their "+str(hpe)+" HP")
    hppl = hpip - hpp
    hpev = hpie - hpe

    if (hpev < 0 and hppl > 0):
        await ctx.send("YOU WON!!\n I am resetting opponent's data!!!\n HURRAY\nLEVEL UP!!!!")
        hpev = 100
        level = level + 1

    if (hppl < 0 and hpev >0):
        await ctx.send("YOU LOST!!!\n I am resetting your data!!!\nI am decreasing your level!!!")
        hppl = 100
        level = level-1

    if (hppl < 0 and hpev < 0):
        await ctx.send("YOU BOTH DIED!!!\n FIGHT BACK\nI AM REVIVING BOTH OF YOU!!!")
        hppl =100
        hpev =100

    with open('statis.csv', 'r', newline='') as remov:
        remover = csv.reader(remov)

        df = pd.read_csv('statis.csv')

        for row in remover:
            if row[0] == pid:
                df.loc[df["player id"] == pid, "HPPLAYER"] = str(hppl)
                df.loc[df["player id"] == pid, "HPEVIL"] = str(hpev)
                df.loc[df["player id"] == pid, "LEVEL"] = str(level)

        df.to_csv("statis.csv", index=False)


@client.command()
async def stat(ctx):
    pid = ctx.author.name
    with open('statis.csv', 'r', newline='') as f:
        csvf = csv.reader(f)

        for row in csvf:
            if row[0] == pid:
                hpmy = str(row[1])
                hpev = str(row[2])
                clas = row[3]
                level = str(row[4])

    if clas == 'Archer':
        clas = "🏹ARCHER🏹"

    if clas == "Warrior":
        clas = " ⚔️WARRIOR ⚔️"

    if clas == "Mage":
        clas = "🧙MAGE🧙"

    if int(hpev) < 0:
        hpev = '0'

    if int(hpmy) < 0:
        hpmy = '0'

    if (hpmy != '0') & (hpev != '0'):
        await ctx.send("PLAYER NAME IS: "+pid+"\nPLAYER HP IS: "+hpmy+"\nOPPONENT HP :"+hpev+"\nCLASS IS: "+clas+"\n LEVEL IS: "+level)


@client.command()
async def rule(ctx):
    await ctx.author.send("Command List:\n"
"\'.\' is necessary as prefix of every commands!\n"
".start - 🏁to enter your name in registry and further playing!\n"
'.archer - 🏹to change your class to archer\n'
'.warrior - ⚔to change your class to warrior\n'
'.mage - 🧙to change your class to mage\n'
'.attack - ⚔️to attack on enemies\n'
'.evade - 🛡️to evade the enemies\n'
".stat - 🏁to see your current progress, and current data")


client.run('ODAyMTQwMTQzNDA1MzY3MzI3.YAq5OQ.W9xqeBXZeBTeFY1Fbv7QtJAHQTE')
