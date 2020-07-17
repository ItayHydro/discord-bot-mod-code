#!/user/bin/python

# importing
import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import random

# setting variable and prefix
client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot's Online(Checked).")
    return await client.change_presence(activity=discord.Activity(type=2, name='Server Guard | -sourcecode'))
# prints when bot's running well and healthy + changing bot's presence

# start of event num. 2
@client.event
async def on_member_join(member):
    print(f'{member} Just joined a server')
# prints a meessage on console when member join a server

# start of event num. 3
@client.event
async def on_member_remove(member):
    print(f'{member} Just left a server')
# prints a message on console when member left

# start of clear command
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    print(f'member has Requested to clear {amount} messages.')
    await ctx.send (f'Successfully cleared {amount} messages.', delete_after = 2)
# end of clear command

# start of clear error
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, you have to be administrator to use this.')
#end of clear error

# creating a command to check if bot is online
@client.command(pass_context=True)
@commands.bot_has_permissions(administrator=True)
async def botcheck(ctx, member):
    print(f'{member} requested botcheck.') # prints the message on the console
    await ctx.send('The bot is running healthy') # sending the message in the channel of the server the bot running in.
# end of botcheck command
# start of sourcecode command
@client.command(pass_context=True)
async def sourcecode(ctx, member):
    print(f'{member} requested sourcecode of the bot.')
    await ctx.send('My source code: https://github.com/ItayHydro/discord-bot-mod-code')
# when a member use 'sourcecode'command, bot will send the message above.
# end of source code command

# start of userinfo command
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s user info" .format(user.display_name), description=" ", color= discord.Color(random.randint(0x000000, 0xFFFFFF)))
    embed.add_field(name="name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Account created at", value=user.created_at.strftime("%a, %#d %b %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined server at", value=user.joined_at.strftime("%a, %#d %b %Y, %I:%M %p UTC"))
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Is the user bot", value=user.bot)

    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send( embed = embed)
# end of userinfo command

# start of kick command
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print(f'Successfully kicked {member}.')
    await ctx.send(f'Successfully kicked {member}.')
# end of kick command

# start of kick error
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, you have to be administrator to use this.')
# end of kick error

# start of ban command
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print(f'Successfully banned {member}.')
    await ctx.send(f'Successfully banned {member}.')
# out of ban command

# start of ban error
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, you have to be administrator to use this.')
# end of ban command

# start of unban command
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Successfully unbanned {user.name}.')
            return
# end of unban command

# start of unban error
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, you have to be administrator to use this.')
# end of unban error

# start of mute command
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please tag a member to mute")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f'{member} has been mute.')
# end of mute command

# start of mute error
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, you have to be administrator to use this.')
# end of mute error

# start of unmute command
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please tag a member to unmute')
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send(f'{member} has been unmuted.')
# end of unmute command

# start unmute error
@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, you have to be administrator to use this.')
# end unmute error

# client TOKEN
client.run('you_wont_see_my_token:)')

