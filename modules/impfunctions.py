import random
import requests
import discord



DOGAPI = "http://thedogapi.com/api/images/get.php"
CATAPI = "http://thecatapi.com/api/images/get.php"


def roll_dice():
    return random.randint(1, 6)


def getCatPicture():
    catPicture = requests.get(CATAPI)
    if catPicture.status_code == 200:
        catPicture = catPicture.url
        return catPicture


def getDogPicture():
    catPicture = requests.get(DOGAPI)
    if catPicture.status_code == 200:
        catPicture = catPicture.url
        return catPicture


def meme():
    response = requests.get("https://memes.blademaker.tv/api?lang=en")
    jsonresponse = response.json()

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



