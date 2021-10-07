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
    if message.content.startswith(';'):
        if message.content[1:].startswith('verify'):
            if get(message.author.roles, name="Verified"):
                await message.reply(
                    embed = discord.Embed(
                        description="You are already verified"
                    )
                )
            else:
                links = [
                    'https://media.discordapp.net/attachments/895477247597740102/895477321434296330/zero.png',
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477490364059658/one.png',
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477339562049556/two.png',
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477393723129977/three.png',
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477453521313802/four.png',
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477439755599872/five.png',
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477374987149332/six.png',
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477356976812093/seven.png',
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477421082562581/eight.png',
                    'https://cdn.discordapp.com/attachments/895477247597740102/895477477164597348/nine.png'
                ]
                randnum = random.randint(0, 9)
                await message.reply(
                    embed = discord.Embed(
                        title="Challenge Started!",
                        description=f"Please check you're DMs {message.author.mention}!"
                    )
                )

                dmch = await message.author.create_dm()

                ms = await dmch.send(
                    embed = discord.Embed(
                        title="PreCAPTCHA",
                        description=f"Click the number below shown in this image. :1234:",
                        color = discord.Colour.blue()
                    ).set_image(
                        url=links[randnum]
                    )
                )
                reactionss = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
                for i in reactionss:
                    await ms.add_reaction(i)
                run = True
                howmany=0
                while run:
                    await asyncio.sleep(1-client.latency)
                    howmany+=1
                    msg = await dmch.fetch_message(ms.id)
                    for i in msg.reactions:
                        if i.count == 2:
                            if i.emoji == reactionss[randnum]:
                                await dmch.send(
                                    embed = discord.Embed(
                                        title="PreCAPTCHA",
                                        description=":white_check_mark: You Won The CAPTCHA Challenge!",
                                        color = discord.Colour.green()
                                    )
                                )
                                verified_role = get(message.guild.roles, name='Verified')
                                await message.author.add_roles(verified_role)
                                run = False
                            else:
                                await dmch.send(
                                    embed = discord.Embed(
                                        title="PreCAPTCHA",
                                        description=":x: You Lost The CAPTCHA Challenge..\n\nMaybe try again next time ..?",
                                        color = discord.Colour.red()
                                    )
                                )
                                run = False
                    if howmany == 30:
                        await dmch.send(
                                embed = discord.Embed(
                                    title="PreCAPTCHA",
                                    description=":x: Verification Has Been Canceled Because It Passed Time Limit (30s).",
                                    color = discord.Colour.red()
                                )
                            )
                        run = False


client.run('TOKEN-HERE')
