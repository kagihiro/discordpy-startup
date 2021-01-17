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
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視
    if message.author.bot:
        return
    # 「/toss」と発言したらトス結果が返る処理
    if ('/t' in message.content):
        await message.channel.send(coin_toss.toss())
    if ('/r' in message.content):
        await message.channel.send(dice.roll(message.content.split()[1]))


bot.run(token)
