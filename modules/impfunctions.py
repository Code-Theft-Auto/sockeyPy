import random
import aiohttp
import discord
from io import BytesIO


DOGAPI = "http://thedogapi.com/api/images/get.php"
CATAPI = "http://thecatapi.com/api/images/get.php"


def roll_dice():
    return random.randint(1, 6)


async def getCatPicture():
    async with aiohttp.ClientSession( ) as session:
        async with session.get(CATAPI) as response:
            catPicture = await response.read()

            if response.status_code == 200:
                catPicture = BytesIO(catPicture)

        return catPicture


async def getDogPicture():
    async with aiohttp.ClientSession( ) as session:
        async with session.get(DOGAPI) as response:
            dogPicture = await response.read()

            if response.status_code == 200:
                dogPicture = BytesIO(dogPicture)

        return dogPicture



async def meme():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://memes.blademaker.tv/api?lang=en") as response:
            jsonresponse = await response.json()


    title = jsonresponse["title"]
    ups = jsonresponse["ups"]
    image = jsonresponse["image"]
    downs = jsonresponse["downs"]
    embed = discord.Embed(title=f"{title}")
    embed.set_image(url=image)
    embed.set_footer(text=f"👍: {ups} 👎: {downs}")
    return embed


def randnum(a, b):
    return str(random.randint(a, b))



