# Authentication_by_reaction.py

import discord
import datetime
import asyncio

client = discord.Client()

accept_msg = "" #id
accept_ch = "" #id
accept_role = "" #str

kick_content = """同意していただけなかったので、キックさせていただきました。
再入室はこちらからできます。
"""

kick_faile = """次のユーザーのキックをトライしましたが、Discordの権限のエラーでキックができませんでした。
対象者: <@{0}> (ID: {0})
理由: {1}
対処: {2}
"""

class control_reaction():
    @asyncio.coroutine
    def reaction_remove(self, msg_id, ch_id, emoji, user_id):
        try:
            emoji = '{}:{}'.format(emoji.name, emoji.id)
        except:
            pass
        yield from client.http.remove_reaction(msg_id, ch_id, emoji, user_id)

@client.event
async def on_ready():
    print("Let's ready!")
    # Add target message to client.messages(deque object).
    msg = await client.get_message(client.get_channel(accept_ch), accept_msg)
    client.messages.append(msg)
    print("Complete!")

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.id == accept_msg:
        if reaction.emoji == "✅":
            role = discord.utils.get(user.server.roles, name=accept_role)
            await client.add_roles(user, role)
            del role
        elif reaction.emoji == "❌":
            m = await client.send_message(user, kick_content)
            try:
                await client.kick(user)
            except discord.errors.Forbidden:
                # Permission error for kick. Send details to the owner.
                await client.delete_message(m)
                content = kick_faile.format(user.id, "規約同意確認で不同意を選択。", "送信したメッセージを削除。")
                await client.send_message(reaction.message.server.owner, content)
                del content
            except Exception as e:
                print("err\n", e)
            del m
            await client.remove_reaction(reaction.message, "❌", user)

@client.event
async def on_reaction_remove(reaction, user):
    if reaction.message.id == accept_msg:
        if reaction.emoji == "✅":
            try:
                role = discord.utils.get(user.server.roles, name=accept_role)
                await client.remove_roles(user, role)
            except AttributeError:
                pass
            except Exception as e:
                print("err:\n", e)

@client.event
async def on_member_remove(member):
    await control_reaction().reaction_remove(msg_id=accept_msg, ch_id=accept_ch, emoji="✅", user_id=member.id)

client.run("Token")
