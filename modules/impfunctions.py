import random
import requests
import requests as req
from imports import discord
from imports.bs4 import BeautifulSoup
from cryptography.fernet import Fernet

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


def help():

    embed = discord.Embed(title="COMMANDS :", colour=discord.Colour(0x3f2f2f))
    embed.set_thumbnail(url="https://c.tenor.com/bC95JP5b-a0AAAAi/tegan-iversen-socks.gif")
    embed.set_author(name="sockey",icon_url="https://c.tenor.com/bC95JP5b-a0AAAAi/tegan-iversen-socks.gif")
    embed.add_field(name=".ping", value="just returns pong", inline=True)
    embed.add_field(name=".cat", value="sends cute cat pictures", inline=True)
    embed.add_field(name=".dog", value="sends a cute dog picure", inline=True)
    embed.add_field(name=".dice",
                    value="returns a random number between 1 to 6",
                    inline=True)
    embed.add_field(name=".help",
                    value="shows this embed                                ",
                    inline=True)
    embed.add_field(name=".meme", value="sends a meme", inline=True)
    embed.add_field(name=".math",
                    value="""*adds,subtracts,multiplies or divides* 
       eg: $math 35+33 'the ans would be 68'""",
                    inline=False)
    embed.add_field(name=".rnum",
                    value="sends a randum number from given parameters ",
                    inline=True)
    embed.add_field(name=".play `<search query or link>`",
                    value="plays music!",
                    inline=True)
    embed.add_field(name=".join", value="joins a channel", inline=True)
    embed.add_field(name=".skip",
                    value="skips the currnet playing song",
                    inline=True)
    embed.add_field(name=".q", value="shows the queue", inline=True)
    embed.add_field(name=".pause",
                    value="you should understand this",
                    inline=True)
    embed.add_field(name=".resume",
                    value="you should understand this too!!",
                    inline=True)
    embed.add_field(name=".encode `string`",
                    value="encode the string and sends it to you",
                    inline=True)
    embed.add_field(name=".decode `encoded tring`",
                    value="decode the string and sends it to you",
                    inline=True)
    embed.add_field(name=".lofi", value="plays lofi", inline=True)
    embed.add_field(name=".fa `song query`",
                    value="adds songs to a private playlist",
                    inline=True)
    embed.add_field(name=".fv",
                    value="shows the private playlist",
                    inline=True)
    embed.add_field(name=".fd `index`",
                    value="removes the given index from playlist",
                    inline=True)
    embed.add_field(name=".gs `query`",
                    value="searches google and send you the results",
                    inline=True)

    return embed


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


def math_eval(arg):
    try:
        response = eval(arg)
        return response

    except:
        response = "some weird error occured"
        return response


def randnum(a, b):
    return str(random.randint(a, b))


def encrypt(string: str):
    key = Fernet.generate_key()
    f = Fernet(key)
    string = string.encode()
    token = f.encrypt(string)
    return token, key


def decrypt(token: str, key: str):
    key = key.encode()
    f = Fernet(key)
    return f.decrypt(token)


def Getyt(url: str):
    r = req.get(url, "html.parser")

    soup = BeautifulSoup(r.text, "html.parser")
    vidtitle = str(soup.find("title").text)
    vidtitle = vidtitle.replace(" - YouTube", "")
    return vidtitle


