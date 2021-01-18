from discord.ext import commands


def get_mention(ctx):
    member_id = ctx.author.id
    return f"<@!{member_id}>"


def get_mentioned_message(ctx, message):
    mention = get_mention(ctx)
    return '{}\n{}'.format(mention, message)
