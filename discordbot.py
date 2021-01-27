from discord.ext import commands
import os
import traceback
import coin_toss
import dice
import discode_utils

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


def getArgByContext(ctx):
    splited_message = ctx.message.content.split(' ')
    return splited_message[1] if len(splited_message) == 2 else ''


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
    arg = getArgByContext(ctx)
    toss_res = coin_toss.toss(arg)
    await ctx.send(discode_utils.get_mentioned_message(ctx, toss_res))


@bot.command()
async def r(ctx, arg):
    # roll dice
    dice_res = dice.roll(arg)
    await ctx.send(discode_utils.get_mentioned_message(ctx, dice_res))


bot.run(token)
