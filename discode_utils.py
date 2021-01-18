from discord.ext import commands


def get_mention(ctx):
    member_id = 111111111111111111
    member = ctx.guild.get_member(member_id)
    return member.mention


def get_mentioned_message(ctx, message):
    mention = get_mention(ctx)
    return '{}¥n{}'.format(mention, message)
