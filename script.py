#!/usr/bin/python3

import discord
import time
import asyncio
import VoiceUser
import secrets
client = discord.Client()
active_users = list()
bopping = False
sleep_time = 30
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
        await asyncio.sleep(sleep_time)
        await check_for_bop()

@client.event
async def on_voice_state_update(member, before, after):
    global active_users
    temp = VoiceUser.Voice_User()
    if member != client.user:
        if after.channel != None:
            if before.channel != None:
                for vu in active_users:
                    if member == vu.user:
                        active_users.remove(vu)
            temp.user = member
            temp.channel = after.channel
            active_users.append(temp)
            for vu in active_users:
                if vu.channel.name == after.channel.name:
                    if len(after.channel.members)==1:
                        if not vu.is_alone:
                            temp.time_alone_start = time.perf_counter()
                    vu.is_alone = (len(after.channel.members)==1)
        else:
            for vu in active_users:
                if member == vu.user:
                        active_users.remove(vu)
                if vu.channel.name == before.channel.name:
                    if len(before.channel.members)==1:
                        if not vu.is_alone:
                            temp.time_alone_start = time.perf_counter()
                    vu.is_alone = (len(after.channel.members)==1) ## throwing errors when last user leaves

async def check_for_bop():
    for vu in active_users:
        time_alone = 0
        if vu.is_alone:
            time_alone = time.perf_counter() - vu.time_alone_start
        if time_alone >= sleep_time and not bopping:
            await bop(vu.channel)

async def bop(VC: discord.VoiceChannel):
    global bopping
    bopping = True
    boppage = await VC.connect()
    boppage.play(discord.FFmpegPCMAudio(source=r"home/pi/Documents/Discord/ImportantBot/audio.mp3"))
    while boppage.is_playing():
        await asyncio.sleep(.1)
    await boppage.disconnect()
    bopping = False

client.run(secrets.Token)
