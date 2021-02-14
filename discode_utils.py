import discord
from discord.ext import commands


def get_mention(ctx):
    member_id = ctx.author.id
    return f"<@!{member_id}>"


def get_name(ctx):
    return ctx.author


def get_mentioned_message(ctx, message):
    mention = get_mention(ctx)
    return '{}\n{}'.format(mention, message)


def role_to_name_and_id(role):
    return f"{role.name.replace('@','')} : {role.id}"


def get_roles(guild):
    res = "このサーバのロールとID一覧は下記です\n"
    res += '\n'.join(map(role_to_name_and_id, guild.roles))
    return res
