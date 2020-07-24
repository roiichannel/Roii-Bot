import discord
import time

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzM0NzM4NTA5ODI2NDkwNDQ4.XxkSpg.xSoj3-n6MiCjp2IWl-DQ5ABpZZY'

# 接続に必要なオブジェクトを生成
client = discord.Client()

#変数
maintenance = False

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理

CHANNEL_ID = 735754499767140362 # 任意のチャンネルID(int)

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("Roii-Bot 's startd")

# bot起動時に実行されるイベントハンドラを定義
@client.event
async def on_ready():
    if maintenance:
        await client.change_presence(activity=discord.Game(name="メンテナンス中..."))
        return
    await greet() # 挨拶する非同期関数を実行

@client.event
async def on_message(message):
    if message.content == "R?-Link":
        embed=discord.Embed(title="当Bot運営", url="https://roiiblog.shop/", description="--------------------",color=discord.Colour.blue())
        embed.set_author(name="Roii Bot",icon_url="https://roiiblog.shop/image/icon.png")
        embed.set_footer(text="当Bot運営は ろいぃ～ が運営しております。 \n 不具合等ありましたら @ろいぃ〜 / RealGodGloop所属 RTC開発者 に連絡お願いします。")
        await message.channel.send(embed=embed)
    if message.content == "R?-Ping":
        before = time.monotonic()
        message = await message.channel.send("Pingを計測中...")
        ping = (time.monotonic() - before) * 1000
        await message.delete()
        embed=discord.Embed(title="Ping調査", description="--------------------",color=discord.Colour.blue())
        embed.set_author(name="Roii Bot",icon_url="https://roiiblog.shop/image/icon.png")
        embed.set_footer(text="Roii Bot Pingは {} msです。".format(int(ping)))
        await message.channel.send(embed=embed)
    if message.content == "R?-Ver":
        embed=discord.Embed(title="当Botバージョン情報", description="--------------------",color=discord.Colour.blue())
        embed.set_author(name="Roii Bot",icon_url="https://roiiblog.shop/image/icon.png")
        embed.set_footer(text="Version : 1.0.0 \n Bot_Name : Roii Bot \n development_language : Python \n Developer : Roii   &   Ty")
        await message.channel.send(embed=embed)
        return
    if message.content == "R?-BotStatus":
        users = 0
        for i in client.users:
            users += 1
        users -= 1
        embed=discord.Embed(title="Bot Status", description="--------------------",color=discord.Colour.blue())
        embed.set_author(name="Roii Bot",icon_url="https://roiiblog.shop/image/icon.png ")
        embed.set_footer(text="Bot Status : {}".format(users))
        await message.channel.send(embed=embed)
        await client.change_presence(activity=discord.Game(name="Roii Bot 利用者数 {} 人".format(users)))
        return
    if message.content == "Hey guys!":
        await message.delete()
        await message.channel.send("Pornhub\nxvideo\nS●Xやっふううううううう！\nAAAAAAAAAAAAAAAAAAAAA\nお●ぱいお●ぱいお●ぱいお●ぱいお●ぱいお●ぱい\nくるみ★ぽんちお")
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
