import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot 
import os

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print('작동시작')

@bot.command()
async def A(ctx):
    await ctx.send('레이드 왔음 @everyone')
    await asyncio.sleep(0.2)
    await ctx.send('레이드 왔음 @everyone')
    await asyncio.sleep(0.2)
    await ctx.send('레이드 왔음 @everyone')
    await asyncio.sleep(0.2)
    await ctx.send('레이드 왔음 @everyone')
    await asyncio.sleep(0.2)
    await ctx.send('레이드 왔음 @everyone')
    await asyncio.sleep(0.2)
    await ctx.send('레이드 왔음 @everyone')
    await asyncio.sleep(0.2)
    await ctx.send('레이드 왔음 @everyone')
    await asyncio.sleep(0.2)
    await ctx.send('레이드 왔음 @everyone')
    await asyncio.sleep(0.2)
    await ctx.send('레이드 왔음 @everyone')

@bot.command()
async def B(ctx):
    await ctx.send('서버초기화 5분전 조인바람 @everyone')
    await asyncio.sleep(0.3)
    await ctx.send('서버초기화 5분전 조인바람 @everyone')
    await asyncio.sleep(0.3)
    await ctx.send('서버초기화 5분전 조인바람 @everyone')
    await asyncio.sleep(0.3)

@bot.command()
async def C(ctx):
    await ctx.send('LIVE ON 비밀번호 노출 조심해주세요 @everyone')
    await asyncio.sleep(0.3)
    await ctx.send('LIVE ON 비밀번호 노출 조심해주세요 @everyone')
    await asyncio.sleep(0.3)
    await ctx.send('LIVE ON 비밀번호 노출 조심해주세요 @everyone')
    await asyncio.sleep(0.3)

@bot.command()
async def D(ctx):
    await ctx.send('@everyone')
    await asyncio.sleep(0.3)
    await ctx.send('@everyone')
    await asyncio.sleep(0.3)
    await ctx.send('@everyone')
    await asyncio.sleep(0.3)

@bot.command()
async def R(ctx):
    await ctx.send('@everyone 레이드 갈 준비해주세요')
    await asyncio.sleep(0.3)
    await ctx.send('@everyone 레이드 갈 준비해주세요')
    await asyncio.sleep(0.3)
    await ctx.send('@everyone 레이드 갈 준비해주세요')
    await asyncio.sleep(0.3)


access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
