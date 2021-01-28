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
    err_msg = 'パラメーターが間違っています\n'
    err_msg += '例 コマンド : 意味↓\n'
    if '/toss' in ctx.message.content:
        err_msg += '/toss : コインを1回投げる\n'
        err_msg += '/toss 100 : コインを100回投げる\n'
        err_msg += '/toss t : 裏が出るまで投げる\n'
        err_msg += '/toss h : 表が出るまで投げる\n'

    if '/r' in ctx.message.content:
        err_msg += '/r : 6面ダイスを1回投げる\n'
        err_msg += '/r 3d5 : 5面ダイスを3回投げる\n'
        err_msg += '/r d5 : 5面ダイスを1回投げる\n'
        err_msg += '/r 4d : 6面ダイスを4回投げる\n'

    await ctx.send(discode_utils.get_mentioned_message(ctx, err_msg))
    # orig_error = getattr(error, "original", error)
    # error_msg = ''.join(
    #     traceback.TracebackException.from_exception(orig_error).format())
    # await ctx.send(error_msg)


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
async def r(ctx):
    # roll dice
    arg = getArgByContext(ctx)
    dice_res = dice.roll(arg)
    await ctx.send(discode_utils.get_mentioned_message(ctx, dice_res))


bot.run(token)
