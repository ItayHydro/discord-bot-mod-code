#!/user/bin/python

server_guard_token = '542i0-5ri2-jf0--]f2j3-]ofj2'

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
    return await client.change_presence(activity=discord.Activity(type=3, name='Server Guard | -sourcecode'))
# prints whn bot's running well and healthy + changing bot's presence

# start of event num. 2
memberrole = "Member"
@client.event
async def on_member_join(member):
    print(f'{member} Just joined a server')
    role = get(member.guild.roles, name=memberrole)
    await member.add_roles(role) # adds the role "Member" when a user joins a server
# prints a meessage on console when member join a server

# start of event num. 3
@client.event
async def on_member_remove(member):
    print(f'{member} Just left a server')
# prints a message on console when member left

# start of clear command
@client.command()
@commands.has_permissions(MANAGE_MESSAGES=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    print(f'Member has Requested to clear {amount} messages.')
    await ctx.send (f'Successfully cleared {amount} messages.', delete_after = 2)
# end of clear command

# start of clear error
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, sorry! you must to be an administrator to use the clear command.')
#end of clear error

# creating a command to check if bot is online
@client.command()
@commands.bot_has_permissions(administrator=True)
async def botcheck(ctx):
    print('Requested botcheck command.') # prints the message on the console
    await ctx.send('The bot is running healthy') # sending the message in the channel of the server the bot running in.
# end of botcheck command
# start of sourcecode command
@client.command()
async def sourcecode(ctx):
    print('Requested sourcecode of the bot.')
    await ctx.send("My source code: https://github.com/ItayHydro/discord-bot-mod-code")
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
    embed.add_field(name="Is the user a bot", value=user.bot)

    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send( embed = embed)
    print('Requested userinfo command.')
# end of userinfo command

# start of userinfo error
@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, sorry! you must to be an administrator to use the userinfo command.')
# end of userinfo command

# start of kick command
@client.command()
@commands.has_permissions(KICK_MEMBERS=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print(f'Successfully kicked {member}.')
    await ctx.send(f'Successfully kicked {member}.')
# end of kick command

# start of kick error
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, sorry! you must to be an administrator to use the kick command.')
# end of kick error

@client.command()
@commands.has_permissions(BAN_MEMBERS=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print(f'Successfully banned {member}.')
    await ctx.send(f'Successfully banned {member}.')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, sorry! you must to be an administrator to use the ban command.')

@client.command()
@commands.has_permissions(BAN_MEMBERS=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Successfully unbanned {user.name}#{user.discriminator}')
            print(f'Successfully unbanned {member}.')
            return
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, sorry! you must to be an administrator to use the unban command.')

# start of mute command
@client.command()
@commands.has_permissions(MUTE_MEMBERS=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please tag a member to mute")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    role2 = discord.utils.get(ctx.guild.roles, name="Member")
    await member.remove_roles(role2)
    await ctx.send(f'{member} has been muted.')
    print(f'member {member} has been muted.')
# end of mute command

# start of mute error
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, sorry! you must to be an administrator to use the mute command.')
# end of mute error

# start of unmute command
@client.command()
@commands.has_permissions(MUTE_MEMBERS=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please tag a member to unmute')
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    role2 = discord.utils.get(ctx.guild.roles, name="Member")
    await member.remove_roles(role)
    await member.add_roles(role2)
    await ctx.send(f'{member} has been unmuted.')
    print(f'member {member} has been unmuted.')
# end of unmute command

# start unmute error
@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Missing permissions, sorry! you must to be an administrator to use the unmute command.')
# end unmute error

# client TOKEN
client.run(server_guard_token) # the discord's bot token. *token must be private* DO NOT SHARE THIS WITH ANYONE!!!






















