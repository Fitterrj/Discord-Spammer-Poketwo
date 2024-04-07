from webserver import keep_alive
import requests

channelID = 1117843631265566840
headers = {
    "authorization":
    "MTExOTY3ODc0NzgyNjcyNDk0NQ.G8TyuZ.wue7ElXneDmmNy0a_Bb5JtF-XQnHTfO16y1N8s"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
