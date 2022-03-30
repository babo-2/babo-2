import discord
import requests

id = "618d6c398ea8c940a6e5a6f3"
API_KEY = "48551c9a-c663-4f02-b9b7-e368b2f8c8ee"
url = f"https://api.hypixel.net/guild?key={API_KEY}&id={id}"

staff = ["babo_2", "Bodil-Kwek", "Memicrafters", "Moz", "roncou", "StimmZ"]
exclude = [""]


def get_data(url):
    r = requests.get(url)
    return r.json()


my_secret = 'OTM2MjY2MjY3MDUxMDM2NzAy.YfKr6Q.048NiCIe_3hKH8xXnk21Q65cmjg'


def get_xp(player):
    count = 0
    data = get_data(url)
    success = str(data["success"])
    if success != "True":
        return data["cause"]
    else:
        try:
            data_2 = get_data(
                f"https://api.mojang.com/users/profiles/minecraft/{player}")
        except:
            return "this player doesn't exist"
        uuid = data_2["id"]
        mem = data["guild"]["members"]
        for members in mem:
            if members["uuid"] == uuid:
                for i in members["expHistory"]:
                    if count == 0:
                        date = i
                    if count == 1:
                        date_1 = i
                    if count == 2:
                        date_2 = i
                    if count == 3:
                        date_3 = i
                    if count == 4:
                        date_4 = i
                    if count == 5:
                        date_5 = i
                    if count == 6:
                        date_6 = i
                    count += 1
                xp = members["expHistory"][date] + members["expHistory"][date_1] + members["expHistory"][date_2] + \
                    members["expHistory"][date_3] + members["expHistory"][date_4] + \
                    members["expHistory"][date_5] + \
                    members["expHistory"][date_6]
                return f"{player}'s xp: {xp}"
        return f"{player} is not in your guild"


def get_uuid(player):
    try:
        data_2 = get_data(
            f"https://api.mojang.com/users/profiles/minecraft/{player}")
    except:
        return f"{player} doesn't exist"
    return data_2["id"]


def get_player(uuid):
    try:
        data_2 = get_data(f"https://api.mojang.com/user/profiles/{uuid}/names")
    except:
        return uuid, "doesn't exist"
    for i in data_2:
        name = i
    return name["name"]


client = discord.Client()


@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    data = get_data(url)
    msg = message.content
    send = message.channel.send
    author = str(message.author.name)
    if message.author == client.user:
        return
    if msg.startswith("..get"):
        p = msg.split("..get ").pop(1)
        await send(get_xp(p))
    if msg.startswith("..xp"):
        await send(f"guild xp: {data['guild']['exp']}")
    if msg.startswith("..help"):
        await send("..get <username in your guild>, ..xp, ..help, ..uuid <any username>, ..player or ..user <any uuid>, ..guild")
    if msg.startswith("..player"):
        p = msg.split("..player ").pop(1)
        await send(f"{p}: {get_player(p)}")
    if msg.startswith("..user"):
        p = msg.split("..user ").pop(1)
        await send(f"{p}: {get_player(p)}")
    if msg.startswith("..uuid"):
        p = msg.split("..uuid ").pop(1)
        await send(f"{p}: {get_uuid(p)}")
    if msg.startswith("..guild"):
        print(author)
        if author in staff:
            member = data["guild"]["members"]
            for i in member:
                count = 0
                for d in i["expHistory"]:
                    if count == 0:
                        date = d
                    if count == 1:
                        date_1 = d
                    if count == 2:
                        date_2 = d
                    if count == 3:
                        date_3 = d
                    if count == 4:
                        date_4 = d
                    if count == 5:
                        date_5 = d
                    if count == 6:
                        date_6 = d
                    count += 1
                rank = i["rank"]
                xp = i["expHistory"][date] + i["expHistory"][date_1] + i["expHistory"][date_2] + \
                    i["expHistory"][date_3] + i["expHistory"][date_4] + \
                    i["expHistory"][date_5] + i["expHistory"][date_6]
                p = get_player(i['uuid'])
                if p not in exclude:
                    if xp < 50000:
                        await send(f"{p}:  kick with only: {xp} gexp")
                    if xp < 125000 and rank == "Intermediate" or xp < 125000 and rank == "Pro":
                        await send(f"{p}: {rank}-rookie with: {xp} gexp")
                    if xp < 200000 and xp >= 125000 and rank == "Pro":
                        await send(f"{get_player(i['uuid'])}: Pro-Intermediate with: {xp} gexp")
                    if xp >= 125000 and rank == "Rookie" and xp < 200000:
                        await send(f"{p}: Rookie-Intermediate with: {xp} gexp")
                    if xp >= 200000 and rank == "Intermediate":
                        await send(f"{p}: Intermediate-Pro with: {xp} gexp")
                    if xp >= 200000 and rank == "Rookie":
                        await send(f"{p}: Rookie-Pro with: {xp} gexp")
        else:
            send("only staff can use this command", author)
client.run(my_secret)
