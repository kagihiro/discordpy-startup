from discord.ext import commands
import os
import traceback
import coin_toss
import dice

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(
        traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def toss(ctx):
    # coin toss
    await ctx.send(coin_toss.toss())


@bot.command()
async def r(ctx):
    # roll dice
    # await ctx.send(dice.roll(ctx))
    await ctx.send(ctx)


bot.run(token)
