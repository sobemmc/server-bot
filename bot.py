import discord
import asyncio
import random
import datetime
import requests
import os

client = discord.Client()


@client.event
async def on_ready():
    
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('$도움말')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    if message.content.startswith('$도움말'):
      embed = discord.Embed(title="도움말", description="", color=0xAAFFFF)
      embed.add_field(name="$규칙", value="서버 규칙을 알려줌", inline=False)
      embed.add_field(name="$서버정보", value="서버 정보를 알려줌", inline=False)
      embed.add_field(name="$세력", value="현재 세력을 알려줌", inline=False)
      embed.set_footer(text="!SOBI#1919")
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/795588047381987375/845185855068569640/SOBI.png?width=634&height=676")
      await message.channel.send(embed=embed)

    if message.content.startswith('$서버정보'):
      embed = discord.Embed(title="", description="", color=0xAAFFFF)
      embed.add_field(name="이름", value="건축 서버", inline=False)
      embed.add_field(name="게임", value="Minecraft", inline=False)
      embed.add_field(name="주소", value="sobi15.codns.com", inline=False)
      embed.add_field(name="버전", value="1.17", inline=False)
      embed.add_field(name="-", value="-", inline=False)
      embed.add_field(name="이름", value="놀이터 야생 서버(폐지)", inline=False)
      embed.add_field(name="게임", value="~~Minecraft~~", inline=False)
      embed.add_field(name="주소", value="~~sobi15.codns.com~~", inline=False)
      embed.add_field(name="버전", value="~~1.16.4 ~ 1.16.5~~", inline=False)
      embed.set_footer(text="!SOBI#1919")
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/795588047381987375/845185855068569640/SOBI.png?width=634&height=676")
      await message.channel.send(embed=embed)

    if message.content.startswith('$규칙'):
      embed = discord.Embed(title="서버 규칙", description="", color=0xAAFFFF)
      embed.add_field(name="""
- 서버 들어오려면 이 디코섭 필수

- 커맨드 숨기기 금지

- 서버 테러 금지

- 정치, 성, 개인정보 관련 언급 금지

- 서버 내외 특정 인물을 지목하는 욕설 금지

- 특정 장애, 질병, 종교, 단체 언급 및 비하 금지

- 커맨드 블럭 반복형 킬( 무한킬, 반복킬 ) 자제

- 건축할려면 옆에 다른 건축물이 보여야함

- 옆에 다른 건축물이 안보이면 철거

- 욕 금지

- 커맨드 항상활성화 경고
      """, value="""
      잘 지키삼
      """, inline=False)
      embed.set_footer(text="!SOBI#1919")
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/795588047381987375/845185855068569640/SOBI.png?width=634&height=676")
      await message.channel.send(embed=embed)

    if message.content.startswith('$세력'):
      embed = discord.Embed(title="세력",  description="", color=0xAAFFFF)
      embed.add_field(name="솝이 세력", value="""
      - 솝이
      """, inline=False)
      embed.add_field(name="여우 세력", value="""
      - 크시
      - 빌스
      """, inline=False)

      embed.set_footer(text="!SOBI#1919")
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/795588047381987375/845185855068569640/SOBI.png?width=634&height=676")
      await message.channel.send(embed=embed)






client.run(os.environ['token'])
