"""
Discord.PY CAPTCHA Challenge

Made By : aidangamin (https://github.com/aidangamin or https://twitter.com/AidanGamin)

MY COMMENTS ARE BAD PLEASE MAKE A POST ON TWTR THEN TAG ME AND TELL ME WHAT TO EDIT IF I'M BAD AT EXPLAINING !
"""

import discord
import random
import asyncio
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():
    print("bot ready.")

@client.event
async def on_message(message):
    if message.content.startswith(';'): # Checks for command prefix
        if message.content[1:].startswith('verify'): # Process Commands
            if get(message.author.roles, name="Verified"): # Check if user has role (so they won't use it when they're already verified)
                await message.reply(
                    embed = discord.Embed(
                        description="You are already verified"
                    )
                )
            else:
                links = [ # Image links to distorted/warped images
                    'https://media.discordapp.net/attachments/895477247597740102/895477321434296330/zero.png', # 0
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477490364059658/one.png',    # 1
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477339562049556/two.png',    # 2
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477393723129977/three.png',  # 3
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477453521313802/four.png',   # 4
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477439755599872/five.png',   # 5
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477374987149332/six.png',    # 6
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477356976812093/seven.png',  # 7
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477421082562581/eight.png',  # 8
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477477164597348/nine.png'    # 9
                ]
                randnum = random.randint(0, 9) 
                await message.reply( # I used reply to specify who (the author) is being verified
                    embed = discord.Embed(
                        title="Challenge Started!",
                        description=f"Please check you're DMs {message.author.mention}!" # also mentions the author to specify more.
                    )
                )

                dmch = await message.author.create_dm() # creates a dm channel (its better to use this than doing message.author.send)

                ms = await dmch.send(
                    embed = discord.Embed(
                        title="PreCAPTCHA",
                        description=f"Click the number below shown in this image. :1234:",
                        color = discord.Colour.blue()
                    ).set_image(
                        url=links[randnum]
                    )
                )
                reactionss = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣'] # Adds all reaction
                for i in reactionss:
                    await ms.add_reaction(i)
                run = True
                howmany=0
                while run:
                    await asyncio.sleep(1-client.latency)
                    howmany+=1
                    msg = await dmch.fetch_message(ms.id) # Get message 
                    for i in msg.reactions:
                        if i.count == 2:
                            if i.emoji == reactionss[randnum]: #win
                                await dmch.send(
                                    embed = discord.Embed(
                                        title="PreCAPTCHA",
                                        description=":white_check_mark: You Won The CAPTCHA Challenge!",
                                        color = discord.Colour.green()
                                    )
                                )
                                verified_role = get(message.guild.roles, name='Verified')
                                await message.author.add_roles(verified_role) # Gives author the role if they passed the test
                                run = False
                            else: # Lose
                                await dmch.send(
                                    embed = discord.Embed(
                                        title="PreCAPTCHA",
                                        description=":x: You Lost The CAPTCHA Challenge..\n\nMaybe try again next time ..?",
                                        color = discord.Colour.red()
                                    )
                                )
                                run = False
                    if howmany == 30: # Cancel
                        await dmch.send(
                                embed = discord.Embed(
                                    title="PreCAPTCHA",
                                    description=":x: Verification Has Been Canceled Because It Passed Time Limit (30s).",
                                    color = discord.Colour.red()
                                )
                            )
                        run = False


client.run('TOKEN-HERE') # HEY! If YOU can see this please put token here :), many people keep wondering why their bot doen't work. it doesn't because you forgot the token.
