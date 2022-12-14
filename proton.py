import asyncio
import random 
import discord
from discord.ext import commands
from discord.ext import tasks
from googletrans import Translator


client = discord.Client()
prefix = '?'
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")




@bot.event
async def on_ready():
    print("Logged in as : ", bot.user.name)
    print("ID : ", bot.user.id)
    print("NB serveur : ", len(bot.guilds))
    changeStatus.start()


@tasks.loop(seconds=5)
async def changeStatus():
    status = [f"?help | Surveille {len(bot.guilds)} serveurs",
          "?help | A votre service",
          "?help | Version : 1.0",
          "?help | Dรฉveloppeur : HerLocky",
          f"?help | Surveille {len(bot.users)} membres"]
    game = discord.Game(random.choice(status))
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_message(message):
    if message.content == "GG":
        await message.add_reaction('๐')
        await message.add_reaction('๐')
    if message.content == "gg":
        await message.add_reaction('๐')
        await message.add_reaction('๐')
    if message.content == "Gg":
        await message.add_reaction('๐')
        await message.add_reaction('๐')
    if message.content == "<@!785114361252675595>":
        embed = discord.Embed(title="My Prefix", description="prefix config panel", color=255)
        embed.add_field(name="``Prefix de base``", value="?")
        embed.add_field(name="``Prefix de ce serveur``", value="?")
        embed.add_field(name="``?setprefix``", value="pour changer le prefix (non fonctionnel)")
        await message.channel.send(embed=embed)
    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    embed = discord.Embed(title=f"**__{member.name}__ viens de rejoindre le discord !**",
                          description=f"Bienvenue  sur {member.guild.name} {member.guild.member_count} membres sur le serveur",
                          color=65280)
    embed.add_field(name="``Nom``", value=f"{member.name}")
    embed.add_field(name="``Compte crรฉรฉ le``", value=member.created_at.strftime("%d/%m/%Y ร?  %H heures, %M minutes et %S secondes"), inline=True)
    embed.set_image(url=member.avatar_url)
    await discord.utils.get(member.guild.text_channels, name='โญarrivรฉ-dรฉpartโญ').send(embed=embed)


@bot.event
async def on_member_remove(member):
    embed = discord.Embed(title=f"**__{member.name}__ viens de quitter {member.guild.name} !**",
                          description=f"Au-revoir {member.mention}, nous sommes maintenant {member.guild.member_count} membres sur le serveur",
                          color=16711680)
    embed.add_field(name="``Nom``", value=f"{member.name}")
    embed.add_field(name="``Compte crรฉรฉ le``", value=member.created_at.strftime("%d/%m/%Y ร?  %H heures, %M minutes et %S secondes"), inline=True)
    embed.set_image(url=member.avatar_url)
    await discord.utils.get(member.guild.text_channels, name='โญarrivรฉ-dรฉpartโญ').send(embed=embed)


# LOGS


@bot.event
async def on_member_ban(guild, user):
    embed = discord.Embed(title=f"**__{user.name}__ viens d'รชtre banni de {guild.name}**", description=f"",
                          color=16711680)
    embed.add_field(name="``๐Ban``", value=f"{user.name}(ID : {user.id})")
    await discord.utils.get(guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@bot.event
async def on_member_unban(guild, user):
    embed = discord.Embed(title=f"**__{user.name}__ viens d'รชtre debanni de {guild.name}**", description=f"",
                          color=65280)
    embed.add_field(name="``๐Unban``", value=f"{user.name}(ID : {user.id})")
    await discord.utils.get(guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@bot.event
async def on_message_delete(message):
    embed = discord.Embed(title=f"**Message supprimรฉ**", color=16711680)
    embed.add_field(name="``Message Delete``", value=f"**{message.content}**")
    embed.add_field(name="``Auteur du message``", value=f"{message.author}")
    embed.add_field(name="``Channel``", value=f"{message.channel}")
    await discord.utils.get(message.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@bot.event
async def on_guild_role_create(role):
    embed = discord.Embed(title=f"**Nouveau role**", color=65280)
    embed.add_field(name="``Nom du role``", value=f"**{role.name}**")
    await discord.utils.get(role.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@bot.event
async def on_guild_role_delete(role):
    embed = discord.Embed(title=f"**Role delete**", color=16711680)
    embed.add_field(name="``Nom du role``", value=f"**{role.name}**")
    await discord.utils.get(role.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@bot.event
async def on_guild_channel_create(channel):
    embed = discord.Embed(title=f"**Nouveau Channel**", color=65280)
    embed.add_field(name="``Nom du nouveau channel``", value=f"**{channel.name}**")
    await discord.utils.get(channel.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@bot.event
async def on_guild_channel_delete(channel):
    embed = discord.Embed(title=f"**Channel delete**", color=16711680)
    embed.add_field(name="``Nom du channel``", value=f"**{channel.name}**")
    await discord.utils.get(channel.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(title=f"**__{guild.name}__ viens d'ajouter Proton !**", description="", color=65280)
    embed.add_field(name="__Nombre de membres__", value=f"{guild.member_count}")
    embed.add_field(name="__Crรฉรฉ le__", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="__Propriรฉtaire__", value=f"{guild.owner}")
    embed.add_field(name="__Nombre de serveurs__", value=f"{len(bot.guilds)}")
    embed.add_field(name="__Nombre de channels__", value=f"{len(guild.channels)}")

    await bot.get_channel(829344553508536391).send(embed=embed)


@bot.event
async def on_guild_remove(guild):
    embed = discord.Embed(title=f"**Proton n'est plus sur __{guild.name}__ !**", description="", color=16711680)
    embed.add_field(name="__Nombre de membre__", value=f"{guild.member_count}")
    embed.add_field(name="__Crรฉรฉ le__", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="__Propriรฉtaire__", value=f"{guild.owner}")
    embed.add_field(name="__Nombre de serveur__", value=f"{len(bot.guilds)}")

    await bot.get_channel(829344553508536391).send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("โโ?La commande n'existe pasโ?โ")
        await ctx.message.add_reaction('โ')



@bot.command()
async def help(ctx):
    id = str(ctx.author.id)
    if id == '749200546417868831':
        embed = discord.Embed(title="๐HELP", description='''Les diffรฉrentes catรฉgories de commandes de Proton sont : (total de **85 commandes**)
            โบ Administration :computer:
            ``?help_admin`` (**17 commandes**)
            โบ Modules :gear:
            ``?help_modules`` (**6 commandes**)
            โบ Modรฉrations :rotating_light: 
            ``?help_mod`` (**7 commandes**)
            โบ Utils ๐ฑ
            ``?help_utils`` (**22 commandes**)
            โบ Fun :tada:
            ``?help_fun`` (**23 commandes**)
            โบ Bot Owner ๐
            ``?help_owner`` (**3 commandes**)
            ''',
            color=255)
        await ctx.send(embed=embed)
    else : 
        embed = discord.Embed(title="๐HELP", description='''Les diffรฉrentes catรฉgories de commandes de Pee1 sont : (total de **85 commandes**)
            โบ Administration :computer:
            ``?help_admin`` (**17 commandes**)
            โบ Modules :gear:
            ``?help_modules`` (**6 commandes**)
            โบ Modรฉrations :rotating_light: 
            ``?help_mod`` (**7 commandes**)
            โบ Utils ๐ฑ
            ``?help_utils`` (**22 commandes**)
            โบ Fun :tada:
            ``?help_fun`` (**23 commandes**)
            โบ Musique :musical_note:
            ``?help_music`` (**6 commandes**)
            ''',
            color=255)
        await ctx.send(embed=embed)



@bot.command(name="ping", pass_context=True, aliases=["latency", "latence"])
async def ping(ctx):
    
    embed = discord.Embed(title="__**Latence**__", colour=discord.Color.dark_gold(), timestamp=ctx.message.created_at)
    embed.add_field(name="Latence du bot :", value=f"`{round(bot.latency * 1000)} ms`")

    await ctx.send(embed=embed)




@bot.command()
async def help_admin(ctx):
    dictEmbed = {
        "title": ":computer:Administration Help:computer:",
        "description": ''' 
    **Arguments : [obligatoire] (optionnels)**
    ``โ?giveaway [temps en minute] [prix]`` : crรฉer un giveaway.
    ``โ?clear [votre nombre]`` : supprime les messages (1000 d'un coup maximum).
    ``โ?poll [message] ``: crรฉรฉ un sondage.
    ``โ?choice``: crรฉer un sondage ( jusqu'a 9 choix).
    ``โ?loginfo`` : donne les informations sur les logs
    ``โ?embed`` : pour crรฉer un embed personnalisรฉ
    ``โ?text_channel [nom_du_channel]`` : crรฉer un channel textuel personnalisรฉ.
    ``โ?voice_channel [nom_du_channel]`` : crรฉer un channel vocal personnalisรฉ.
    ``โ?add_role [@user] [@role]`` : pour ajouter un grade ร? une personne.
    ``โ?remove_role [@user] [@role]`` : pour retirer un grade ร? une personne.
    ``โ?lock`` : pour verrouiller un channel.
    ``โ?unlock`` : pour dรฉverrouiller un channel.
    ``โ?templock [temps(en minute)]`` : pour verrouiller temporairement un channel.
    ``โ?nick [@user] [nickname]`` : permet de changer le nom de la personne sur le serveur.
    ``โ?readoff`` : permet de rendre invisible le channel
    ``โ?readon`` : permet de rendre visible le channel
    ``โ?slow [temps]`` : permet de mettre un slowmode sur un channel (0 pour desactiver)
    ''',
        "color": 16711680}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@bot.command()
async def help_modules(ctx):
    dictEmbed = {
        "title": ":gear:Modules Help:gear:",
        "description": ''' 
    ``โ?new_enable`` : active le systรจme de bienvenue.
    ``โ?new_disable`` : dรฉsactive le systรจme de bienvenue.
    ``โ?log_enable`` : active le systรจme de log.
    ``โ?log_disable`` : dรฉsactive le systรจme de log.
    ``โ?report_enable`` : active le systรจme de report.
    ``โ?report_disable`` : dรฉsactive le systรจme de report.
    ''',
        "color": 13238245}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@bot.command()
async def help_mod(ctx):
    dictEmbed = {
        "title": ":rotating_light:Moderation Help:rotating_light:",
        "description": '''
    **MODERATION** : 
    **Arguments : [obligatoire] (optionnels)**
    ``โ?mute [@user] [raison]`` : Mute le membre mentionnรฉ.
    ``โ?unmute [@user]`` : Unmute le membre mentionnรฉ.
    ``โ?tempmute [@user] [temps]`` : Mute le membre mentionnรฉ pour un temps donnรฉ.
    ``โ?kick [@user]`` : Kick le membre mentionnรฉ.
    ``โ?ban [@user] [raison]`` : Ban le membre mentionnรฉ.
    ``โ?tempban [@user] [temps]`` : Ban le membre mentionnรฉ pour un temps donnรฉ.
    ``โ?unban [@user]`` : Unban le membre mentionnรฉ.
    ''',
        "color": 11403055}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@bot.command()
async def help_utils(ctx):
    dictEmbed = {
        "title": ":man_frowning:Utils Help:man_frowning:",
        "description": '''
    **Arguments : [obligatoire] (optionnels)**
    ``โ?userinfo (@user)`` : donne des informations sur le membre mentionnรฉ.
    ``โ?roleinfo [@role]`` : donne des informations sur le rรดle mentionnรฉ.
    ``โ?channelinfo [#channel]`` : donne des informations sur le channel mentionnรฉ.
    ``โ?emoteinfo [emoji]`` : donne des informations sur l'emoji en question (:warning:Ne fonctionne que avec les emoji du serveur oรน est exรฉcutรฉe la commande) 
    ``โ?avatar (@user)`` : donne l'avatar du membre mentionnรฉ.
    ``โ?serverinfo`` : donne des informations sur le serveur.
    ``โ?ping`` : Donne le ping du bot.
    ``โ?botinfo`` : donne des informations sur Pee1.
    ``โ?report [@user] [raison]`` : report un membre au staff.
    ``โ?tos`` : donne les conditions gรฉnรฉrales d'utilisation de Pee1.
    ``โ?site`` : donne le site de Pee1.
    ``โ?invite`` : donne le lien d'invitation de Pee1.
    ``โ?support`` : donne le lien du discord de support de pee1.
    ``โ?mcskin [nom du skin]`` : affiche le skin d'un joueur minecraft.
    ``โ?mctex [nom du skin]`` : affiche la texture du skin  d'un joueur minecraft.
    ``โ?staff_list `` : affiche la liste du staff.
    ``โ?translate [language] [message] `` : permet de traduire votre message
    ``โ?youtube [message] `` : permet de faire une recherche youtube
    ``โ?google [message] `` : permet de faire une recherche google
    ``โ?wiki [message] `` : permet de faire une recherche wikipรฉdia
    ``โ?createinvite`` : permet de crรฉer une invitation.
    ``โ?password [nombre de carractรจre] [taille du mdp]`` : permet de gรฉnรฉrer un mot de passe sรฉcuriser.
    ''',
        "color": 14108820}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@bot.command()
async def help_fun(ctx):
    dictEmbed = {
        "title": ":tada:Fun Help:tada:",
        "description": '''
    **Arguments : [obligatoire] (optionnel)**
    ``โ?q`` : Pose une question au bot.
    ``โ?calcul_help``: Liste des calculs que le bot peut faire.
    ``โ?emoji`` : donne un emoji au hasard.
    ``โ?joke`` : vous raconte une blague.
    ``โ?say [message]`` : Fait parler le bot. 
    ``โ?bvn [@user]`` : souhaite la bienvenue a un nouveau membre.
    ``โ?lovecalc (@user)`` : calcule ton amour avec un membre.
    ``โ?qi (@user)`` : calcul ton QI ou celui des autre.
    ``โ?reverse [text]`` : donne un texte le bot te le donnera en verlant.
    ``โ?rps [rock ou paper ou sissors]`` : joue a  123 pierre feuille siceaux.
    ``โ?calin [@user]`` : fait un calin.
    ``โ?kiss [@user]`` : fait un bisous.
    ``โ?clap [@user]`` : pour applaudit.
    ``โ?claque [@user]`` : donne une claque.
    ``โ?pleurer`` : quand tu pleure.
    ``โ?angry`` : quand tu est รฉnerver .
    ``โ?shock`` : quand tu est choquer.
    ``โ?rougir`` : quand tu rougis.
    ``โ?shrug`` : quand tu hausse les รฉpaules.
    ``โ?smile`` : quand tu souris.
    ``โ?thinking`` : quand tu pense.
    ''',
        "color": 16734208}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))



@bot.command()
async def help_owner(ctx):
    id = str(ctx.author.id)
    if id == '749200546417868831':
            embed = discord.Embed(title="๐Owner Help๐", description='''Les diffรฉrentes catรฉgories de commandes de Pee1 sont : (total de **85 commandes**)
            **Arguments : [obligatoire] (optionnel)**
        ``โ?statut [statut]`` : Modifie le statut.
        ``โ?restart``: Pour restart le bot.
        ``โ?stop`` : Pour arreter le bot.
            ''',
            color=255)
            await ctx.send(embed=embed)
    else :
        await ctx.send("Vous n'avez pas la permission d'excuter cette commande, elle est rรฉserver ร? OverGame#1718")




@bot.command()
@commands.has_permissions(manage_messages=True)
async def poll(ctx, *, sujet):
    dictEmbed = {
        "title": "Sondage",
        "description": sujet,
        "footer": {
            "text": f"Auteur : {ctx.author.display_name}"
        }
    }
    message = await ctx.send(embed=discord.Embed.from_dict(dictEmbed))
    await message.add_reaction('๐')
    await message.add_reaction('๐')
    await message.add_reaction('๐คท')


@poll.error
async def poll_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_messages``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?poll sujet)โ?โ")
        raise error


@bot.command()
async def bvn(ctx, user: discord.Member):
    dictEmbed = {
        "title": f"Bienvenue ร? {user.name}",
        "description": f"{ctx.author.mention} souhaite la bienvenue ร? {user.mention}, amuse toi bien sur {ctx.guild.name}",
        "color": 14398228}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@bvn.error
async def bvn_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?bvn @user)โ?โ")
        raise error
    elif isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")


@bot.command()
async def joke(ctx):
    reponses = ["**Que dit-on de quelqu'un qui joue aux jeux vidรฉo quand il est triste ? ||On dit qu il se console||**",
                '**Quel est le dessert prรฉfรฉrรฉ des pompiers ? ||La crรจme brรปlรฉe||**',
                '**Vous connaissez la blague sur les magasins ? ||C est une blague qui a supermarchรฉ||**',
                "**Qu'est ce qui peut faire le tour du monde en restant dans son coin ? ||C est un timbre||**",
                "**Pourquoi les pรชcheurs ne sont pas gros ? ||Parce qu'ils surveillent leur ligne !||**",
                '**Comment appelle-t-on un chien qui a des lunettes ? ||Un optichien||**',
                '**Quel est le point commun entre un dรฉmรฉnageur et un arbitre de football ? ||Ils aiment tous les deux sortir des cartons||**',
                '**Comment appelle-t-on un chat tout terrain ||Un CatCat (4x4)||**',
                "**Donald Duck et Marie Duck se battent, qu'est-ce que cela fait ? ||Un confit de cannard||**",
                "**Que fait un chien sans patte quand on l'appelle ? ||Il ne bouge pas||**",
                ]
    await ctx.send(f'{random.choice(reponses)}')


@bot.command()
async def emoji(ctx):
    reponses = ['**๐**',
                '**๐**',
                '**๐**',
                '**๐คฃ**',
                '**๐**',
                '**๐**',
                '**๐**',
                '**๐**',
                '**๐**',
                '**๐**']
    await ctx.send(f'{random.choice(reponses)}')


@bot.command()
async def calcul_help(ctx):
    dictEmbed = {
        "title": "Calcul help",
        "description": '''
   **Arguments : [obligatoire] (optionnel)**
    ``โ๐ญ?add [a] [b]`` : (remplacer a et b par les chiffres que vous voulez) fait une addition.
    ``โ๐ญ?sous [a] [b]`` : (remplacer a et b par les chiffres que vous voulez) fait une soustraction.
    ``โ๐ญ?multiply [a] [b]`` : (remplacer a et b par les chiffres que vous voulez) fait une multiplication.
    ``โ๐ญ?divise [a] [b]`` : (remplacer a et b par les chiffres que vous voulez) fait une division.
    ``โ๐ญ?puissance [a] [b]`` : (remplacer a et b par les chiffres que vous voulez) calcul les puissances.
    ''',
        "color": 14398228}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@bot.command()
async def tos(ctx):
    dictEmbed = {
        "title": "Bienvenue sur les conditions d'utilisations de Proton",
        "description": '''
    Pour commencer, en utilisant le bot vous accepter toutes ces conditions d'utilisation !

``1.`` Les bugs trouvรฉs devront รชtre rapportรฉs immรฉdiatement.
``2.`` Toutes tentatives d'utilisations de commandes de catรฉgorie Owner est prohibรฉ.
``3.`` Les ToS sont aussi ร? respecter.
``4.`` Le partage de toutes informations ร? propos du personnel ou du bot (IP, mot de passe, ...) est prohibรฉ !
Bonne utilisation du bot :grin:
    ''',
        "color": 14398228}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@bot.command()
async def add(ctx, a: int, b: int):
    embed = discord.Embed(title=f"**Calculator 2000**", description="ADDITION", color=16711680)
    embed.add_field(name="Votre calcul", value=f" {a} + {b}", inline=True)
    embed.add_field(name="``Voici le rรฉsultat``", value=(a + b), inline=True)

    await ctx.send(embed=embed)


@add.error
async def add_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?add chiffre1  chiffre2)โ?โ")
        raise error


@bot.command()
async def multiply(ctx, a: int, b: int):
    embed = discord.Embed(title=f"**Calculator 2000**", description="MULTIPLICATION", color=16711680)
    embed.add_field(name="Votre calcul", value=f" {a} * {b}", inline=True)
    embed.add_field(name="``Voici le rรฉsultat``", value=(a * b), inline=True)

    await ctx.send(embed=embed)


@multiply.error
async def multiply_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?multiply chiffre1  chiffre2)โ?โ")
        raise error


@bot.command()
async def divise(ctx, a: int, b: int):
    embed = discord.Embed(title=f"**Calculator 2000**", description="DIVISION", color=16711680)
    embed.add_field(name="Votre calcul", value=f" {a} / {b}", inline=True)
    embed.add_field(name="``Voici le rรฉsultat``", value=(a / b), inline=True)

    await ctx.send(embed=embed)


@divise.error
async def divise_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?divise chiffre1  chiffre2)โ?โ")
        raise error


@bot.command()
async def puissance(ctx, a: int, b: int):
    embed = discord.Embed(title=f"**Calculator 2000**", description="DIVISION", color=16711680)
    embed.add_field(name="Votre calcul", value=f" {a} puissance {b}", inline=True)
    embed.add_field(name="``Voici le rรฉsultat``", value=(a ** b), inline=True)

    await ctx.send(embed=embed)


@puissance.error
async def puissance_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?puissance chiffre1  chiffre2)โ?โ")
        raise error


@bot.command()
async def sous(ctx, a: int, b: int):
    embed = discord.Embed(title=f"**Calculator 2000**", description="SOUSTRACTION", color=16711680)
    embed.add_field(name="Votre calcul", value=f" {a} - {b}", inline=True)
    embed.add_field(name="``Voici le rรฉsultat``", value=(a - b), inline=True)

    await ctx.send(embed=embed)


@sous.error
async def sous_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?sous chiffre1  chiffre2)โ?โ")
        raise error


@bot.command()
async def q(ctx, *, question):
    reponses = ['**Oui :-D**',
                '**Non pas du tout**',
                '**Peut รชtre...**',
                '**Tu as raison**',
                '**Surement !!!**',
                '**Je ne sais pas**',
                '**Je ne peux pas rรฉpondre!**'
                '**Certainement**']
    await ctx.send(f'{random.choice(reponses)}')


@q.error
async def q_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?q question)โ?โ")
        raise error


@bot.command()
async def say(ctx, *, content: str):
    await ctx.message.delete()
    await ctx.send(content)


@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?say message)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx, amount=5):
    def check(ms):
        return ms.channel == ctx.message.channel and ms.author == ctx.message.author

    await ctx.send(content='**Quel sera le titre de cet embed ?**')
    msg = await ctx.bot.wait_for('message', check=check)
    title = msg.content
    await ctx.send(content="**Maintenant, quel sera le texte contenu dans l'embed ?**")
    msg = await ctx.bot.wait_for('message', check=check)
    desc = msg.content
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title=title,
        description=desc,
        color=255,
        timestamp=ctx.message.created_at
    )
    embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)

    await ctx.send(embed=embed)


@embed.error
async def embed_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_messages``)โ?โ")

        raise error


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="Clear", description=f"**{amount} messages** on รฉtรฉ suprimer", color=16711680)
    embed.add_field(name="Author", value=f"**{ctx.author.name}**")
    embed.add_field(name="Channel", value=f"**#{ctx.channel.name}**")
    await discord.utils.get(ctx.guild.text_channels, name='๐pee1-logs๐').send(embed=embed)



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_messages``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?clear nombre de message a delete)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="Clear", description=f"**{amount} messages** on รฉtรฉ suprimer", color=16711680)
    embed.add_field(name="Author", value=f"**{ctx.author.name}**")
    embed.add_field(name="Channel", value=f"**#{ctx.channel.name}**")
    await discord.utils.get(ctx.guild.text_channels, name='๐pee1-logs๐').send(embed=embed)


@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_messages``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?purge nombre de message a delete)โ?โ")
        raise error


@bot.command(aliases=['ui'])
async def userinfo(ctx, user: discord.Member = None):
    user = user or ctx.author
    playinggame = user.activity
    roles = [role for role in user.roles]
    embed = discord.Embed(colour=user.color, timestamp=ctx.message.created_at)

    embed.set_author(
        name=f"User Info - {user}",
        icon_url=user.avatar_url
    )
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text=f"Demandรฉ(e) par {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="๐Nom", value=f"{user.name}", inline=False)
    embed.add_field(name="๐?NickName", value=f"{user.nick}" if user.nick else "Pas de Nickname", inline=False)
    embed.add_field(name=":1234:ใปTag :", value=f"{user.discriminator}", inline=False)
    embed.add_field(name="๐ID", value=f"{user.id}", inline=False)
    embed.add_field(name="๐ผAvatar", value=f"[avatar link]({user.avatar_url})", inline=False)
    embed.add_field(name=":beginner:ใปStatus de jeu :", value=f"{playinggame}", inline=False)
    embed.add_field(name="๐Compte crรฉรฉ le", value=user.created_at.strftime("%d/%m/%Y ร?  %H heures, %M minutes et %S secondes"), inline=False)
    embed.add_field(name="๐Rejoind le",
                    value=user.joined_at.strftime("%d/%m/%Y ร?  %H heures, %M minutes et %S secondes"), inline=False)

    embed.add_field(name="๐Role le plus haut", value=f"{user.top_role.mention}", inline=False)
    embed.add_field(name=f"โRoles ({len(roles)})", value=" ".join({role.mention for role in roles})[0:1000],
                    inline=False)

    embed.add_field(name="๐จโ๐ปBot ?", value="Oui" if user.bot else "Non", inline=False)
    await ctx.send(embed=embed)


@bot.command(aliases=['si'])
async def serverinfo(ctx):
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    embed = discord.Embed(title="ServerInfo", description="Informations sur le serveur", color=0xeee657)
    embed.set_author(name=f"Serveur Info - {ctx.guild.name}")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    roles = [role for role in ctx.guild.roles]
    embed.add_field(name=":ab:Nom", value=f"{ctx.guild.name}", inline=False)
    embed.add_field(name=":id:ID", value=f"{ctx.guild.id}", inline=False)
    embed.add_field(name=":earth_americas:Rรฉgion", value=f"{ctx.guild.region}", inline=False)
    embed.add_field(name=":frame_photo:Icon", value=f"[icon link]({ctx.guild.icon_url})", inline=False)
    embed.add_field(name=":crown:Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name=":octagonal_sign:Niveau de vรฉrification", value=f"{ctx.guild.verification_level}", inline=False)
    embed.add_field(name=":office:Nombre de membre total", value=f"{ctx.guild.member_count}")
    embed.add_field(name=":soon:Crรฉรฉ le",
                    value=ctx.guild.created_at.strftime("%d/%m/%Y ร?  %H heures, %M minutes et %S secondes"),
                    inline=False)
    embed.add_field(name=f":left_right_arrow:Roles ({len(roles)})",
                    value=" ".join({role.mention for role in roles})[0:1024], inline=False)
    embed.add_field(name=f":1234:Nombre d'emojis", value=len(ctx.guild.emojis), inline=False)
    embed.add_field(name=f":firecracker::sparkles:Serveur Boost",
                    value=f"Niveau : **{ctx.guild.premium_tier}** ({ctx.guild.premium_subscription_count} boost)",
                    inline=False)
    embed.add_field(name=f":musical_keyboard:ใปNombre total de salon", value=f"**{allchannels}**", inline=False)
    embed.add_field(name=f":microphone2:ใปSalons vocaux :", value=f"**{allvoice}**", inline=False)
    embed.add_field(name=f":speech_left:ใปSalons textuels :", value=f"**{alltext}**", inline=False)
    embed.set_footer(text=f"Demandรฉ(e) par {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@bot.command(aliases=['a'])
async def avatar(ctx, user: discord.Member = None):
    user = user or ctx.author
    embed = discord.Embed(title="Avatar",
                          description=f"Voici l'avatar de {user.mention} et voici sont lien [avatar link]({user.avatar_url})",
                          color=0xeee657)
    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)


@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?avatar @user)โ?โ")

        raise error


@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title="Proton", description=f'''
            Proton est un bot 100% franรงais de types multifonctions avec ses 72 commandes :
        -Administration- : 17 commandes
        -Modules- : 6 commandes
        -Modรฉration- : 7 commandes
        -Utils- : 22 commandes
        -Fun- : 23 commandes
        Il peut vous etre utile pour tous grace a ses modules prรฉconfigurer vous n'avez rien a faire juste a les activer :wink:!
        **๐ฐStatistiques** :
            โบ __Nombre de serveurs__ : **{len(bot.guilds)}**
            โบ __Nombre de membres__ : **{len(bot.users)}**
            โบ __Ping Moyen__ : **{bot.ws.latency * 1000:.0f} ms**
        **โInformations**
            โบ __Version__ : **5.2**
            โบ __Language de programation__ : [Python](https://www.python.org/)
            โบ __Librairy__ : [discord.py](https://discordpy.readthedocs.io/)
            โบ __Dรฉveloppeur__ : **HerLocky**
        **๐Liens**
            โบ __GitHub__ : [click](https://github.com/Her-Locky/Proton)
            ''', color=0xeee657)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def new_enable(ctx):
    await ctx.message.delete()
    await ctx.guild.create_text_channel('โญarrivรฉ-dรฉpartโญ')
    await ctx.send(
        f"Le channel ``โญarrivรฉ-dรฉpartโญ`` ร? bien รฉtรฉ crรฉรฉ. J'afficherais les messages d'arriver et de dรฉpart dans ce channel(merci de ne pas modifier le nom du channel et les emoji pour รฉviter les problรจmes)")


@new_enable.error
async def new_enable_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``administrator``)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(administrator=True)
async def new_disable(ctx):
    await ctx.message.delete()
    UnePutainDeSimpleVariableTresSimple = discord.utils.get(ctx.guild.text_channels, name='โญarrivรฉ-dรฉpartโญ')
    await UnePutainDeSimpleVariableTresSimple.delete()
    await ctx.send(
        f"Le channel ``โญarrivรฉ-dรฉpartโญ`` ร? bien รฉtรฉ supprimรฉ, le module de message de bienvenue a รฉtรฉ dรฉsactiver sur votre serveur !!")


@new_disable.error
async def new_disable_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``administrator``)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(administrator=True)
async def log_enable(ctx):
    await ctx.message.delete()
    await ctx.guild.create_text_channel('๐proton-logs๐')
    await ctx.send(
        f"Le channel ``๐proton-logs๐`` ร? bien รฉtรฉ crรฉรฉ. J'afficherais les logs dans ce channel(merci de ne pas modifier le nom du channel et les emoji pour รฉviter les problรจmes)")


@log_enable.error
async def log_enable_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``administrator``)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(administrator=True)
async def log_disable(ctx):
    await ctx.message.delete()
    UnePutainDeSimpleVariableTresSimple = discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐')
    await UnePutainDeSimpleVariableTresSimple.delete()
    await ctx.send(
        f"Le channel ``๐proton-logs๐`` ร? bien รฉtรฉ supprimรฉ, le module de log a รฉtรฉ dรฉsactiver sur votre serveur !!")


@log_disable.error
async def log_disable_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``administrator``)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, sujet):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    embed = discord.Embed(title="MUTE", description=f"``{member.name}/ID:{member.id}`` ร? รฉtรฉ mute", color=16711680)
    embed.add_field(name="Mute author", value=f"{ctx.author.name}")
    embed.add_field(name="Raison", value=f"{sujet}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="MUTE", description=f"``{member.name}/ID:{member.id}`` ร? รฉtรฉ mute", color=16711680)
    embed.add_field(name="Mute author", value=f"{ctx.author.name}")
    embed.add_field(name="Raison", value=f"{sujet}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)
    await member.create_dm()
    await member.dm_channel.send(f'''
    **{ctx.guild.name}**: Tu as รฉtรฉ ๐mute !
    **Reason**: {sujet}
    **Staff**: {ctx.author.mention}
    ''')


@bot.command()
@commands.has_permissions(manage_roles=True)
async def addmuterole(ctx):
    await ctx.guild.create_role(name="Muted",
                                permissions=discord.Permissions(
                                    send_messages=False,
                                    speak=False)
                                )
    await ctx.send(
        "Le role **Muted** viens d'รชtre ajouter a votre serveur vous pouvez dรฉsormer utiliser les commandes de mute sans aucun problรจmes")


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_role``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?mute @user la raison)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, sujet):
    await user.kick()
    embed = discord.Embed(title="KICK", description=f"``{user.name}/ID:{user.id}`` ร? รฉtรฉ kick", color=16711680)
    embed.add_field(name="Kick author", value=f"{ctx.author.name}")
    embed.add_field(name="Raison", value=f"{sujet}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="KICK", description=f"``{user.name}/ID:{user.id}`` ร? รฉtรฉ kick", color=16711680)
    embed.add_field(name="Kick author", value=f"{ctx.author.name}")
    embed.add_field(name="Raison", value=f"{sujet}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)
    await user.create_dm()
    await user.dm_channel.send(f'''
    **{ctx.guild.name}: Vous avez รฉtรฉ ๐ขKick
    **Reason**: {sujet}
    **Staff**: {ctx.author.mention}
    ''')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``kick_members``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?kick @user la raison)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, *, sujet):
    await ctx.guild.ban(user)
    embed = discord.Embed(title="BAN", description=f"``{user.name}/ID:{user.id}`` ร? รฉtรฉ banni dรฉfinitivement",
                          color=16711680)
    embed.add_field(name="Ban author", value=f"{ctx.author.name}")
    embed.add_field(name="Raison", value=f"{sujet}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="BAN", description=f"``{user.name}/ID:{user.id}`` ร? รฉtรฉ banni dรฉfinitivement",
                          color=16711680)
    embed.add_field(name="Ban author", value=f"{ctx.author.name}")
    embed.add_field(name="Raison", value=f"{sujet}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)
    await user.create_dm()
    await user.dm_channel.send(f'''
    **{ctx.guild.name}**: Vous avez รฉtรฉ ๐จBan
    **Reason**: {sujet}
    **Staff**: {ctx.author.mention}
    ''')




@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``ban_members``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?ban @user la raison)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    embed = discord.Embed(title="UNMUTE", description=f"``{member.name}/ID:{member.id}`` ร? รฉtรฉ unmute", color=65280)
    embed.add_field(name="Unmute author", value=f"{ctx.author.name}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="UNMUTE", description=f"``{member.name}/ID:{member.id}`` ร? รฉtรฉ unmute", color=65280)
    embed.add_field(name="Unmute author", value=f"{ctx.author.name}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)
    await member.create_dm()
    await member.dm_channel.send(f'''
    **{ctx.guild.name}**: Tu as รฉtรฉ ๐unmute !
    **Reason**: Aucune raison fourni
    **Staff**: {ctx.author.mention}
    ''')


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_role``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?unmute @user)โ?โ")
        raise error


@bot.command()
async def loginfo(ctx):
    dictEmbed = {
        "title": "Log Information",
        "description": '''
    โBan log
    โUnban log
    โMessage delete log
    โMute log
    โUnmute log
    โRole log
    โChannel log
    ''',
        "color": 14398228}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@bot.command()
async def report(ctx, member: discord.Member, *, sujet):
    await ctx.message.delete()
    embed = discord.Embed(title="REPORT",
                          description=f"Report de la part de **{ctx.author.name}** sur ``{member.name}/ID:{member.id}``",
                          color=0xeee657)
    embed.add_field(name="Report info", value=sujet)
    await discord.utils.get(ctx.guild.text_channels, name='๐ฐreports๐ฐ').send(embed=embed)


@report.error
async def report_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?report @user la raison)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(administrator=True)
async def report_enable(ctx):
    await ctx.message.delete()
    await ctx.guild.create_text_channel('๐ฐreports๐ฐ')
    await ctx.send(
        f"Le channel ``๐ฐreports๐ฐ`` ร? bien รฉtรฉ crรฉรฉ. J'afficherais les reports dans ce channel(merci de ne pas modifier le nom du channel et les emoji pour รฉviter les problรจmes)")


@report_enable.error
async def report_enable_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``administrator``)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(administrator=True)
async def report_disable(ctx):
    await ctx.message.delete()
    UnePutainDeSimpleVariableTresSimple = discord.utils.get(ctx.guild.text_channels, name='๐ฐreports๐ฐ')
    await UnePutainDeSimpleVariableTresSimple.delete()
    await ctx.send(
        f"Le channel ``๐ฐreports๐ฐ`` ร? bien รฉtรฉ supprimรฉ, le module de log a รฉtรฉ dรฉsactiver sur votre serveur !!")


@report_disable.error
async def report_disable_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``administrator``)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_roles=True)
async def tempmute(ctx, member: discord.Member, temps: int, *, sujet):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    embed = discord.Embed(title="MUTE", description=f"``{member.name}/ID:{member.id}`` ร? รฉtรฉ mute", color=16711680)
    embed.add_field(name="Mute author", value=f"{ctx.author.name}")
    embed.add_field(name="Temps", value=f"{temps} minutes")
    embed.add_field(name="Raison", value=f"{sujet}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="MUTE", description=f"``{member.name}/ID:{member.id}`` ร? รฉtรฉ mute", color=16711680)
    embed.add_field(name="Mute author", value=f"{ctx.author.name}")
    embed.add_field(name="Temps", value=f"{temps} minutes")
    embed.add_field(name="Raison", value=f"{sujet}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)
    await member.create_dm()
    await member.dm_channel.send(f'''
    **{ctx.guild.name}**: Tu as รฉtรฉ ๐tempmute !
    **Reason**: {sujet}
    **Temps**: {temps} minute(s)
    **Staff**: {ctx.author.mention}
    ''')
    await asyncio.sleep(temps * 60)
    await member.remove_roles(role)
    embed = discord.Embed(title="UNMUTE", description=f"``{member.name}/ID:{member.id}`` ร? รฉtรฉ unmute", color=65280)
    embed.add_field(name="Unmute author", value=f"{ctx.author.name}")
    embed.add_field(name="Raison", value=f"Durรฉe du mute terminer")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)
    await member.create_dm()
    await member.dm_channel.send(f'''
    **{ctx.guild.name}**: Tu as รฉtรฉ ๐unmute !
    **Reason**: Durรฉe de mute terminer
    **Staff**: {ctx.author}
    ''')


@tempmute.error
async def tempmute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_role``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?tempmute @user temps raison)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_channels=True)
async def text_channel(ctx, *, sujet):
    await ctx.guild.create_text_channel(sujet)
    embed = discord.Embed(title="Nouveau Channel textuel", description=f"Nouveau salon {sujet}", color=65280)
    await ctx.send(embed=embed)



@text_channel.error
async def text_channel_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_channel``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?text_channel nom du channel)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_channels=True)
async def voice_channel(ctx, *, sujet):
    await ctx.guild.create_voice_channel(sujet)
    embed = discord.Embed(title="Nouveau Channel Vocal", description=f"Nouveau salon {sujet}", color=65280)
    await ctx.send(embed=embed)


@voice_channel.error
async def voice_channel_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_channel``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?voice_channel nom du channel)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_roles=True)
async def add_role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(title="Grade Add",
                          description=f"``{member.name}/ID:{member.id}`` ร? obtenue le grade {role.mention}",
                          color=0xeee657)
    embed.add_field(name="Author", value=f"{ctx.author.name}")

    await ctx.send(embed=embed)


@add_role.error
async def add_role_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_roles``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?add_role @user @role)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_roles=True)
async def remove_role(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    embed = discord.Embed(title="Grade Remove",
                          description=f"``{member.name}/ID:{member.id}`` ร? eu perdu le grade {role.mention}",
                          color=0xeee657)
    embed.add_field(name="Author", value=f"{ctx.author.name}")
    await ctx.send(embed=embed)


@remove_role.error
async def remove_role_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_roles``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?remove_role @user @role)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(administrator=True)
async def giveaway(ctx, temps: int, *, sujet):
    dictEmbed = {
        "title": ":tada: GIVEAWAY :tada:",
        "description": f'''
        Rรฉcompense : **{sujet}**
        
        Auteur du giveaway : {ctx.author.mention}

        Durรฉe du giveaway : ``{temps} minute(s)``
        ''',
        "color": 14398228,
        "footer": {
            "text": f"{ctx.guild.name} giveaway"
        }
    }
    message = await ctx.send(embed=discord.Embed.from_dict(dictEmbed))
    await message.add_reaction("๐")
    await asyncio.sleep(temps * 60)

    message = await ctx.channel.fetch_message(message.id)
    reaction = [reaction for reaction in message.reactions if reaction.emoji == "๐"]
    if not reaction == []:
        users = await reaction[0].users().flatten()
        users = [user for user in users if user.id != ctx.guild.me.id]

        winner = random.choice(users)
    dictEmbed = {
        "title": ":tada: GIVEAWAY TERMINER :tada:",
        "description": f'''
        Le gagant du giveaway est : {winner.mention}

        Voici sa rรฉcompense : **{sujet}**
        ''',
        "color": 14398228,
        "footer": {
            "text": f"{ctx.guild.name} giveaway"
        }
    }
    message = await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@giveaway.error
async def giveaway_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``administrator``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?giveaway temps(minutes) rรฉcompense)โ?โ")
        raise error


@bot.command(aliases=['ri'])
async def roleinfo(ctx, role: discord.Role):
    embed = discord.Embed(title="Role Info", description=f"Role Info - {role.name}", color=0xeee657)
    embed.add_field(name="๐Nom", value=f"{role.name}", inline=False)
    embed.add_field(name="๐ID", value=f"{role.id}", inline=False)
    embed.add_field(name="โPosition", value=str(role.position), inline=False)
    embed.add_field(name="๐งModifiable", value=f"Oui" if role.managed else "Non", inline=False)
    embed.add_field(name="๐Permission", value=f"{role.permissions}", inline=False)
    embed.add_field(name="๐Crรฉer le", value=role.created_at.strftime("%d/%m/%Y"), inline=False)
    embed.add_field(name="๐Couleur", value=f"{role.color}", inline=False)
    embed.add_field(name="โผMention", value=f"{role.mention}", inline=False)
    embed.add_field(name="๐Mentionable", value="Oui" if role.mentionable else "Non", inline=False)
    embed.add_field(name="โAfficher sรฉparรฉment", value="Oui" if role.hoist else "Non", inline=False)
    embed.add_field(name="๐จโ๐ผMembres", value=str(len(role.members)))

    await ctx.send(embed=embed)


@roleinfo.error
async def roleinfo_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le role n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?role @role)โ?โ")

        raise error


@bot.command(aliases=['ei'])
async def emoteinfo(ctx, emoji: discord.Emoji):
    embed = discord.Embed(title="Emoji Info", description=f"Emote Info - {emoji.name}", color=0xeee657)
    embed.add_field(name="๐Nom", value=f"{emoji.name}", inline=False)
    embed.add_field(name="๐ID", value=f"{emoji.id}", inline=False)
    embed.add_field(name="๐งModifiable", value=f"{emoji.managed}", inline=False)
    embed.add_field(name="๐Crรฉer le", value=emoji.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name="โผNitro emoji", value=f"{emoji.animated}")

    await ctx.send(embed=embed)


@emoteinfo.error
async def emoteinfo_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?L'emoji n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?emoteinfo emote)โ?โ")

        raise error


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.User):
    await ctx.guild.unban(user)
    embed = discord.Embed(title="UNBAN", description=f"``{user.name}/ID:{user.id}`` ร? รฉtรฉ unban", color=65280)
    embed.add_field(name="UnBan author", value=f"{ctx.author.name}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="UNBAN", description=f"``{user.name}/ID:{user.id}`` ร? รฉtรฉ unban", color=65280)
    embed.add_field(name="UnBan author", value=f"{ctx.author.name}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``ban_members``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?unban @user)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(ban_members=True)
async def tempban(ctx, user: discord.User, temps: int, *, sujet):
    await ctx.guild.ban(user)
    embed = discord.Embed(title="BAN", description=f"``{user}/ID:{user.id}`` ร? รฉtรฉ banni pendant {temps}",
                          color=16711680)
    embed.add_field(name="Ban author", value=f"{ctx.author.name}")
    embed.add_field(name="Temps", value=f"{temps} jour(s)")
    embed.add_field(name="Raison", value=f"{sujet}")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="BAN", description=f"Vous avez รฉtรฉ banni de {ctx.guild.name}", color=16711680)
    embed.add_field(name="Ban author", value=f"{ctx.author.name}")
    embed.add_field(name="Temps", value=f"{temps} jour(s)")
    embed.add_field(name="Raison", value=f"{sujet}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)
    await user.create_dm()
    await user.dm_channel.send(f'''
    **{ctx.guild.name}**: Vous avez รฉtรฉ ๐จtempban
    **Reason**: {sujet}
    **Temps**: {sujet} jour(s)
    **Staff**: {ctx.author.mention}
    ''')
    await asyncio.sleep(temps * 3600)
    await ctx.guild.unban(user)
    embed = discord.Embed(title="UNBAN", description=f"``{user.name}/ID:{user.id}`` ร? รฉtรฉ unban", color=65280)
    embed.add_field(name="UnBan author", value=f"{ctx.author.name}")
    embed.add_field(name="Raison", value=f"Durรฉe du ban terminer")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@tempban.error
async def tempban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``ban_members``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?tempban @user temps(en jours) la raison)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=True, send_messages=False)
    embed = discord.Embed(title="Channel Locked",
                          description=f"``Le channel **{ctx.channel}** est dรฉsormรฉ vรฉrouiller``", color=16711680)
    embed.add_field(name="Lock author", value=f"**{ctx.author.name}**")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="Channel locked", description=f"``Le channel **{ctx.channel}** est dรฉsormรฉ vรฉrouiller``", color=16711680)
    embed.add_field(name="Author", value=f"{ctx.author.name}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_channel``)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=None, send_messages=None)
    embed = discord.Embed(title="Channel Unlocked",
                          description=f"``Le channel **{ctx.channel}** est dรฉsormรฉ dรฉvรฉrouiller``", color=65280)
    embed.add_field(name="Unlock author", value=f"**{ctx.author.name}**")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="Channel Unlocked", description=f"``Le channel **{ctx.channel}** est dรฉsormรฉ dรฉvรฉrouiller``", color=65280)
    embed.add_field(name="Author", value=f"{ctx.author.name}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_channel``)โ?โ")
        raise error


@bot.command()
@commands.has_permissions(manage_channels=True)
async def templock(ctx, temps: int):
    await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=True, send_messages=False)
    embed = discord.Embed(title="Channel locked",
                          description=f"``Le channel **{ctx.channel}** est dรฉsormรฉ vรฉrouiller``", color=16711680)
    embed.add_field(name="Lock author", value=f"**{ctx.author.name}**")
    embed.add_field(name="Temps", value=f"Le channel est vรฉrouillez pour {temps} minute(s)")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="Channel locked", description=f"``Le channel **{ctx.channel}** est dรฉsormรฉ vรฉrouiller``", color=16711680)
    embed.add_field(name="Author", value=f"{ctx.author.name}")
    embed.add_field(name="Temps", value=f"Le channel est vรฉrouillez pour {temps} minute(s)", inline=False)
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)
    await asyncio.sleep(temps * 60)
    await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=None, send_messages=None)
    embed = discord.Embed(title="Channel Unlocked",
                          description=f"``Le channel **{ctx.channel}** est dรฉsormรฉ dรฉvรฉrouiller``", color=65280)
    embed.add_field(name="Unlock author", value=f"**{ctx.author.name}**")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="Channel Unlocked", description=f"``Le channel **{ctx.channel}** est dรฉsormรฉ dรฉvรฉrouiller``", color=65280)
    embed.add_field(name="Author", value=f"{ctx.author.name}")
    await discord.utils.get(ctx.guild.text_channels, name='๐proton-logs๐').send(embed=embed)


@templock.error
async def templock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_channel``)โ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?templock temps(en minutes))โ?โ")
        raise error


@bot.command()
async def reverse(ctx, *, text: str):
    t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f"๐ {t_rev}")


@reverse.error
async def reverse_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?reverse texteโ?โ")
        raise error


@bot.command(aliases=['lc', 'love'])
async def lovecalc(ctx, *, user: discord.Member = None):
    user = user or ctx.author

    random.seed(user.id)
    r = random.randint(1, 100)
    hot = r / 1.17

    emoji = "๐, l'amour n'est pas prรฉsent ici"
    if hot > 25:
        emoji = "โค, l'amour risque d'รชtre dificile mais l'amitier est prรฉsent"
    if hot > 50:
        emoji = "๐, une relation est possible"
    if hot > 75:
        emoji = "๐, c'est l'amour de ta vie cours le/la rejoindre"

    embed = discord.Embed(
        description=f'''
    **{user.mention}** ton niveau d'amour avec {ctx.author.mention} est de **{hot:.2f}%**
    **{emoji}**
    ''',
        color=0xeee657
    )

    await ctx.send(embed=embed)


@lovecalc.error
async def lovecalc_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?lovecalc @user)โ?โ")
        raise error


@bot.command(aliases=['flip', 'coin'])
async def coinflip(ctx):
    coinsides = ['Pile', 'Face']
    await ctx.send(f"**{ctx.author.name}** lance une piรจce. Et tombe sur : **{random.choice(coinsides)}**!")


@bot.command(aliases=['inv', 'bot_invite'])
async def invite(ctx):
    embed = discord.Embed(title="Pee1", description="Voici le lien pour inviter Proton", color=0xeee657)
    embed.add_field(name="Invite le bot",
                    value="[INVITE LINK](https://discord.com/oauth2/authorize?client_id=785114361252675595&scope=bot&permissions=8)")
    await ctx.send(embed=embed)


@bot.command(aliases=['bot_support'])
async def support(ctx):
    embed = discord.Embed(title="Pee1", description="Voici le lien du support du bot", color=0xeee657)
    embed.add_field(name="Support", value="[DISCORD SUPPORT](https://discord.gg/zY6tAgb6YA)")

    await ctx.send(embed=embed)


@bot.command(aliases=['website'])
async def site(ctx):
    embed = discord.Embed(title="Pee1", description="Voici le site de Proton", color=0xeee657)
    embed.add_field(name="Site web", value="[SITE](https://proton-bot.tk)")

    await ctx.send(embed=embed)


@bot.command()
async def qi(ctx, *, user: discord.Member = None):
    user = user or ctx.author

    random.seed(user.id)
    r = random.randint(-60, 250)
    hot = r / 1.17

    emoji = ""
    if hot < 0:
        emoji = "Mais... mais... mais il est pas intelligent lui ?! En dessous de 0 ?? La loose ! Mais non je rigole, c'est le bot qui a (encore) du buguer :unamused:"
    if hot > 0:
        emoji = "Bon, t'es pas trรจs trรจs intรฉligent toi dit donc!"
    if hot > 78:
        emoji = "Bon, t'es pas dรฉbile mais... c'est la l'extra-intelligence non plus quoi !"
    if hot > 100:
        emoji = "Mais on a affaire ร? un bรฉbรฉ gรฉnie on dirait ! **WOUHOU** !"
    if hot > 250:
        emoji = "**OMG** ! Permettez moi de vous appeler *MAรTRE* ! Ah non, pardon, c'est juste un bug, je retire ce que je viens de dire :P"

    embed = discord.Embed(
        description=f'''
    Son QI est de **{hot:.2f}**!
    {emoji}
    ''',
        color=0xeee657
    )
    embed.set_author(
        name=f"Voici le QI de {user} !",
        icon_url=user.avatar_url
    )

    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def choice(ctx, *, text):
    text = text.split("|")
    try:
        text[1] = text[1]
    except:
        return await ctx.send(
            "Veuillez sรฉparer la question et la rรฉponse (par exemple `` !poll [Votre question] |[Choix1]|[Choix2]|[ect...] '')``)")

    try:
        if text[10]:
            return await ctx.send("Veuillez fournir moins de 9 rรฉponses.")
    except:
        pass

    reactions = []
    fmt = ""
    count = 0
    for x in text[1:len(text)]:
        count = count + 1
        numstr = ""
        if count == 1:
            numstr = "one"
            reactions.append("1โฃ")
        if count == 2:
            numstr = "two"
            reactions.append("2โฃ")
        if count == 3:
            numstr = "three"
            reactions.append("3โฃ")
        if count == 4:
            numstr = "four"
            reactions.append("4โฃ")
        if count == 5:
            numstr = "five"
            reactions.append("5โฃ")
        if count == 6:
            numstr = "six"
            reactions.append("6โฃ")
        if count == 7:
            numstr = "seven"
            reactions.append("7โฃ")
        if count == 8:
            numstr = "eight"
            reactions.append("8๏ฟฝ๏ฟฝ๏ฟฝ")
        if count == 9:
            numstr = "nine"
            reactions.append("9โฃ")
        fmt = fmt + f":{numstr}: - {text[count]}\n"

    em = discord.Embed(title=f":bar_chart: | {text[0]}", description=f"{fmt}", colour=0x363940,
                       timestamp=ctx.message.created_at)

    msg = await ctx.send(embed=em)
    for x in reactions:
        await msg.add_reaction(x)

    await ctx.message.delete()


@choice.error
async def choice_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``manage_messages``)โ?โ")

        raise error


@bot.command()
@commands.has_permissions(change_nickname=True)
async def nick(ctx, member: discord.Member, nick):
    member = member or ctx.author
    await member.edit(nick=nick)
    await ctx.send(f'Le nickname de : **{member.name}** est devenue : **{nick}**')


@nick.error
async def nick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("โโ?Le membre n'a pas รฉtรฉ trouverโ?โ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("โโ?Il manque un ou plusieur argument a la commande(?nick user nickname)โ?โ")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "โโ?Vous n'avez pas la permission de faire cette commande( nรฉcรฉsite la permission ``change_nickname``)โ?โ")

        raise error


@bot.command()
async def funytext_help(ctx):
    dictEmbed = {
        "title": "FunyText help",
        "description": '''
   **Arguments : [obligatoire] (optionnel)**
    ``โ?chinese [texte]`` : permet d'รฉcrire en caractรจre chinois, (ne pas utiliser les majuscules)
    ``โ?gotic [texte]`` : permet d'รฉcrire en caractรจre gotic, (ne pas utiliser les majuscules)
    ``โ?russian [texte]`` : permet d'รฉcrire en caractรจre russe, (ne pas utiliser les majuscules)
    ``โ?greek [texte]`` : permet d'รฉcrire en caractรจre grec, (ne pas utiliser les majuscules)
    ``โ?africa [texte]`` : permet d'รฉcrire en caractรจre africain, (ne pas utiliser les majuscules)
    ``โ?fasion [texte]`` : permet d'รฉcrire en caractรจre fasion, (ne pas utiliser les majuscules)
    ''',
        "color": 14398228}
    await ctx.send(embed=discord.Embed.from_dict(dictEmbed))


@bot.command()
async def gotic(ctx, *text):
    chineseChar = "ฮฑฮฒcฮดฮตลฆฤhฮนjฮบlสฯรธฯฯฦฆ$โ?uฯฯฯฯz"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))


@bot.command()
async def russian(ctx, *text):
    chineseChar = "ฮะฯพรฮลฆGHลJะลMะะคPวชะฏSTUVะจะะZ"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))


@bot.command()
async def greek(ctx, *text):
    chineseChar = "ฮปฯฯdฮตาษขะฝฮนฯณฮบlฯปฯฯฯฯะณsฯฯvัฯฐฯz"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))


@bot.command()
async def chinese(ctx, *text):
    chineseChar = "ไธนไนฆๅๅๅทณไธๅๅปพๅทฅไธฟ็ไน็ชๅๅฃๅฐธQๅฐบไธไธๅตVๅฑฑไนYไน"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))


@bot.command()
async def africa(ctx, *text):
    chineseChar = "aษcษษฦghijklmลษpqrstuสwxษฃz"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))


@bot.command()
async def fasion(ctx, *text):
    chineseChar = "ฤษฦฤฮตโฑษ?ษงรฏสากโษฑลฯรพาฉลลลงลณโััฮณแบ"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))


@bot.command()
async def mcskin(ctx):
    def check(ms):
        return ms.channel == ctx.message.channel and ms.author == ctx.message.author

    await ctx.send(content='Quel est le nom du skin ?')
    msg = await ctx.bot.wait_for('message', check=check)
    title = msg.content
    embed = discord.Embed(
        title=f'Skin : {title}',
        description=f'Voici le skin de : **{title}**',
        color=0x295192,
        timestamp=ctx.message.created_at
    )
    embed.set_image(url=('https://mc-heads.net/body/' + (title)))
    await ctx.send(embed=embed)


@bot.command()
async def mctex(ctx):
    def check(ms):
        return ms.channel == ctx.message.channel and ms.author == ctx.message.author

    await ctx.send(content='```Quel est le nom du skin ?```')
    msg = await ctx.bot.wait_for('message', check=check)
    title = msg.content
    embed = discord.Embed(title=f'Texture: {title}', description=f"Voici le skin de : **{title}**", color=0x295192, )
    embed.add_field(name=f"Tรฉlรฉcharge le skin de {title}",
                    value=f'Clique sur le lien pour tรฉlรฉcharger la texture du skin de {title}: https://minotar.net/download/' + (
                        title))
    embed.set_image(url='https://minotar.net/skin/' + (title))
    await ctx.send(embed=embed)


@bot.command()
async def staff_list(ctx):
    """ Check which mods are online on current guild """
    message = ""
    online, idle, dnd, offline = [], [], [], []

    for user in ctx.guild.members:
        if ctx.channel.permissions_for(user).manage_messages or \
                ctx.channel.permissions_for(user).ban_members:
            if not user.bot and user.status is discord.Status.online:
                online.append(f"**{user}**")
            if not user.bot and user.status is discord.Status.idle:
                idle.append(f"**{user}**")
            if not user.bot and user.status is discord.Status.dnd:
                dnd.append(f"**{user}**")
            if not user.bot and user.status is discord.Status.offline:
                offline.append(f"**{user}**")

    if online:
        message += f"๐ข {', '.join(online)}\n"
    if idle:
        message += f"๐ก {', '.join(idle)}\n"
    if dnd:
        message += f"๐ด {', '.join(dnd)}\n"
    if offline:
        message += f":white_circle: {', '.join(offline)}\n"

    await ctx.send(f"Listes du staff de **{ctx.guild.name}**\n{message}")


@bot.command()
async def translate(ctx, lang, *, args):
    t = Translator()
    a = t.translate(args, dest=lang)
    embed = discord.Embed(title="**TRADUCTION**", description=f"Message traduit en __**{lang}**__ ", color=0x363940,
                          timestamp=ctx.message.created_at)
    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/768px-Google_Translate_logo.svg.png")
    embed.add_field(name="**:bulb:  | Message ร? traduire :**", value=args, inline=False)
    embed.add_field(name=f"** :speech_balloon:   | Message traduit en  :**", value=a.text, inline=False)
    embed.set_footer(text=f"Demandรฉ par {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, *, search):
    while ' ' in search:
        search = search.replace(' ', '+')

    embed = discord.Embed(title="**YOUTUBE**", description="Nouvelle recherche pour : " + search, color=0x363940,
                          timestamp=ctx.message.created_at)
    embed.set_thumbnail(
        url="https://www.dbxr.be/wp-content/uploads/2018/09/kisspng-youtube-live-computer-icons-music-youtube-logo-5ac17f36b9c318-9648962215226304547609.png")
    embed.add_field(name="**๐ | Recherche :**", value=search, inline=False)
    embed.add_field(name="**๐ฐ | Rรฉsultat :**", value="https://www.youtube.com/results?search_query=" + search)
    embed.set_footer(text=f"Demandรฉ par {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


@bot.command()
async def google(ctx, *, search):
    while ' ' in search:
        search = search.replace(' ', '+')

    embed = discord.Embed(title="**GOOGLE**", description="Nouvelle recherche pour : " + search, color=0x363940,
                          timestamp=ctx.message.created_at)
    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/1200px-Google_%22G%22_Logo.svg.png")
    embed.add_field(name="**๐ | Recherche :**", value=search, inline=False)
    embed.add_field(name="**๐ฐ | Rรฉsultat :**", value="https://google.fr/?q=" + search)
    embed.set_footer(text=f"Demandรฉ par {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


@bot.command()
async def wiki(ctx, *, search_term):
    while ' ' in search_term:
        search_term = search_term.replace(' ', '+')

    embed = discord.Embed(title="**WIKIPEDIA**", description="Nouvelle recherche pour : " + search_term, color=0x363940,
                          timestamp=ctx.message.created_at)
    embed.set_thumbnail(
        url="https://images.squarespace-cdn.com/content/v1/58b8350dd1758e709661be23/1490070758334-R8TE5PTSB41TBY00B88P/ke17ZwdGBToddI8pDm48kLaXHMAa4yZAGUJNi8h2zcR7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QHyNOqBUUEtDDsRWrJLTm7yCen1CO98SR0OrrKKRz6WbUvghyx11l6rAD7IoGJLnziUokrLsmdvcfVQwGRKyP/Wikipedia-logo-v2.svg.png?format=500w")
    embed.add_field(name="**๐ | Recherche :**", value=search_term, inline=False)
    embed.add_field(name="**๐ฐ | Rรฉsultat :**", value="https://wikipedia.org/w/index.php?search=" + search_term)
    embed.set_footer(text=f"Demandรฉ par {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def readoff(ctx):
    try:
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=False)
        await ctx.send("๐ **| Salon dรฉsormais invisible jusqu'ร? nouvel ordre !**")
        embed = discord.Embed(title="Modification Channel", description=f"๐ **| Salon dรฉsormais invisible jusqu'ร? nouvel ordre !**", color=16711680)
        embed.add_field(name="Author", value=f"{ctx.author.name}")
        embed.add_field(name="Channel", value=f"{ctx.channel}")
        await discord.utils.get(ctx.guild.text_channels, name='๐pee1-logs๐').send(embed=embed)
    except Exception:
        await ctx.send("๐ซ **| Ce salon est dรฉjร? invisible.**")
        return


@bot.command()
@commands.has_permissions(manage_channels=True)
async def readon(ctx):
    try:
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=True)
        await ctx.send("๐ต **| Salon dรฉsormais visible !**")
        embed = discord.Embed(title="Modification Channel", description=f"๐ต **| Salon dรฉsormais visible !**", color=65280)
        embed.add_field(name="Author", value=f"{ctx.author.name}")
        embed.add_field(name="Channel", value=f"{ctx.channel}")
        await discord.utils.get(ctx.guild.text_channels, name='๐pee1-logs๐').send(embed=embed)
    except Exception:
        await ctx.send("๐ซ **| Ce salon est dรฉjร? visible.**")
    


@bot.command()
@commands.has_permissions(manage_messages=True)
async def slow(ctx, delay):
    slomo_embed = discord.Embed(title="**Un slowmode de **" + str(delay) + " secondes ร? รฉtรฉ activรฉ par un modรฉrateur.",
                                color=0x363940, timestamp=ctx.message.created_at)
    slomo_embed.set_footer(text=f'Appliquรฉ par {ctx.author}', icon_url=ctx.author.avatar_url)

    await ctx.channel.purge(limit=1)
    await ctx.channel.edit(slowmode_delay=delay)
    await ctx.send(content=None, embed=slomo_embed)
    embed = discord.Embed(title="Modification Channel", description=f"slowmode de " + str(delay) + " secondes activรฉ", color=65280)
    embed.add_field(name="Author", value=f"{ctx.author.name}")
    embed.add_field(name="Channel", value=f"{ctx.channel}")
    await discord.utils.get(ctx.guild.text_channels, name='๐pee1-logs๐').send(embed=embed)


@bot.command()
async def rps(ctx, arg):
    rpschoice = [
        "rock",
        "paper",
        "scissors",
    ]
    choicebot = random.choice(rpschoice)

    await ctx.send(f"**:eyes: | Je choisis : {choicebot}**")

    if arg == "r" or arg == "rock":
        if choicebot == "rock":
            await ctx.send("**:lock: | Egalitรฉ !**")
        elif choicebot == "paper":
            await ctx.send(f"**:tada: | J'ai gagnรฉ !**")
        else:
            await ctx.send(f"**:tada: | Tu as gagnรฉ !**")
    elif arg == "p" or arg == "paper":
        if choicebot == "rock":
            await ctx.send("**:tada: | Tu as gagnรฉ !**")
        elif choicebot == "paper":
            await ctx.send(f"**:lock: | Egalitรฉ !**")
        else:
            await ctx.send(f"**:tada: | J'ai gagnรฉ !**")
    elif arg == "s" or arg == "scissors":
        if choicebot == "rock":
            await ctx.send("**:tada: | J'ai gagnรฉ !**")
        elif choicebot == "paper":
            await ctx.send(f"**:tada: | Tu as gagnรฉ !**")
        else:
            await ctx.send(f"**:lock: | Egalitรฉ !**")
    else:
        await ctx.send(f"**:cloud: | Ce choix n'existe pas.**")


# a voir
@bot.command()
async def calin(ctx, member: discord.Member):
    await ctx.send(f"{ctx.message.author.mention} **fait un cรขlin ร?** {member.mention} ๐ ")
    await ctx.send(random.choice(["https://giphy.com/gifs/QFPoctlgZ5s0E",
                                  "https://giphy.com/gifs/Y8wCpaKI9PUBO",
                                  "https://giphy.com/gifs/JUwliZWcyDmTQZ7m9L",
                                  "https://giphy.com/gifs/3bqtLDeiDtwhq",
                                  "https://giphy.com/gifs/l2QDM9Jnim1YVILXa",
                                  "https://giphy.com/gifs/rSNAVVANV5XhK",
                                  "https://giphy.com/gifs/yziFo5qYAOgY8",
                                  "https://giphy.com/gifs/DjczAlIcyK1Co",
                                  "https://giphy.com/gifs/VXP04aclCaUfe",
                                  "https://tenor.com/FQNP.gif",
                                  "https://tenor.com/7Wko.gif",
                                  "https://tenor.com/QWw1.gif", ]))


@bot.command()
async def clap(ctx, member: discord.Member):
    await ctx.send(f"{ctx.message.author.mention} **applaudi** ๐ ")
    await ctx.send(random.choice(["https://giphy.com/gifs/klQrJUcrfMsTK",
                                  "https://giphy.com/gifs/vQB6Rf1M9hsjK",
                                  "https://giphy.com/gifs/KsPC9t0ToZhqU",
                                  "https://i.gifer.com/7ddb.gif",
                                  "https://tenor.com/bbPUh.gif",
                                  "https://tenor.com/be6kV.gif",
                                  "https://tenor.com/behUB.gif",
                                  "https://tenor.com/66ti.gif",
                                  "https://tenor.com/bmbic.gif",
                                  "https://tenor.com/Tws9.gif",
                                  "https://tenor.com/uWAq.gif", ]))


@bot.command()
async def claque(ctx, member: discord.Member):
    await ctx.send(f"{ctx.message.author.mention} **frappe** {member.mention} ๐ ")
    await ctx.send(random.choice(["https://tenor.com/E1MC.gif",
                                  "https://tenor.com/xhlc.gif",
                                  "https://tenor.com/bbHX6.gif",
                                  "https://tenor.com/T3nh.gif",
                                  "https://tenor.com/8ps1.gif",
                                  "https://tenor.com/T3n1.gif",
                                  "https://tenor.com/wtQ8.gif",
                                  "https://tenor.com/HyAC.gif",
                                  "https://tenor.com/bkOur.gif",
                                  "https://tenor.com/6sAc.gif",
                                  "https://tenor.com/bmv00.gif", ]))


# CATรGORIE รMOTIONS


@bot.command()
async def pleurer(ctx):
    await ctx.send(f"{ctx.message.author.mention} **est entrain de pleurer... ๐ฅ**")
    await ctx.send(random.choice(["https://giphy.com/gifs/ROF8OQvDmxytW",
                                  "https://giphy.com/gifs/4NuAILyDbmD16",
                                  "https://giphy.com/gifs/AI7yqKC5Ov0B2",
                                  "https://giphy.com/gifs/87HkPDUOtN0TC",
                                  "https://giphy.com/gifs/yHeHqyoRLBBSM",
                                  "https://giphy.com/gifs/RUZZqXiGgTyec",
                                  "https://giphy.com/gifs/59d1zo8SUSaUU",
                                  "https://tenor.com/vUP8.gif",
                                  "https://tenor.com/vvmF.gif",
                                  "https://tenor.com/vt2y.gif",
                                  "https://tenor.com/xSzl.gif",
                                  "https://tenor.com/7pvS.gif", ]))


@bot.command()
async def angry(ctx):
    await ctx.send(f"{ctx.message.author.mention} **est en colรจre ๐ก**")
    await ctx.send(random.choice(["https://giphy.com/gifs/k63gNYkfIxbwY",
                                  "https://giphy.com/gifs/TEJe85dPYW0Uw",
                                  "https://giphy.com/gifs/X3VrxPijowGC4",
                                  "https://giphy.com/gifs/TEqzDIP8FDbnG",
                                  "https://giphy.com/gifs/2pTl1XyGnkflu",
                                  "https://giphy.com/gifs/ejhkhcFuR0zni",
                                  "https://giphy.com/gifs/9w9Z2ZOxcbs1a",
                                  "https://giphy.com/gifs/T3Vvyi6SHJtXW",
                                  "https://giphy.com/gifs/UUjkoeNhnn0K4", ]))


@bot.command()
async def shock(ctx):
    await ctx.send(f"{ctx.message.author.mention} **est choquรฉ ๐ฒ**")
    await ctx.send(random.choice(["https://giphy.com/gifs/3o7btN8AC43aOlKL6M",
                                  "https://giphy.com/gifs/zgGrSqSi3SSqs",
                                  "https://giphy.com/gifs/13lRBLnBpXXsS4",
                                  "https://giphy.com/gifs/ckNPhjpC1C7jAOdjVX",
                                  "https://giphy.com/gifs/BDN8BqYikeV2g",
                                  "https://giphy.com/gifs/HkUey32gK29RS",
                                  "https://giphy.com/gifs/3og0IHCELv0TRg3afK",
                                  "https://giphy.com/gifs/mm1QxNmKWPupO", ]))


@bot.command()
async def rougir(ctx):
    await ctx.send(f"{ctx.message.author.mention} ** rougi(e) ๐**")
    await ctx.send(random.choice(["https://tenor.com/LN7I.gif",
                                  "https://tenor.com/bd9B5.gif",
                                  "https://tenor.com/7pij.gif",
                                  "https://tenor.com/TgQ9.gif",
                                  "https://tenor.com/xm9S.gif",
                                  "https://tenor.com/2TWP.gif",
                                  "https://tenor.com/6Clt.gif",
                                  "https://tenor.com/EGSz.gif",
                                  "https://tenor.com/xUjU.gif",
                                  "https://tenor.com/xIfR.gif", ]))


@bot.command()
async def shrug(ctx):
    await ctx.send(f"{ctx.message.author.mention} **hausse les รฉpaules** :person_shrugging:")
    await ctx.send(random.choice(["https://tenor.com/baJXt.gif",
                                  "https://tenor.com/9wVw.gif",
                                  "https://tenor.com/6HAF.gif",
                                  "https://tenor.com/ZIsy.gif",
                                  "https://tenor.com/be3cF.gif",
                                  "https://tenor.com/wUnM.gif",
                                  "https://tenor.com/5rCO.gif",
                                  "https://tenor.com/bfviE.gif"
                                  "https://tenor.com/H6uP.gif", ]))


@bot.command()
async def smile(ctx):
    await ctx.send(f"{ctx.message.author.mention} **souri** :smile:")
    await ctx.send(random.choice(["https://tenor.com/beqAZ.gif",
                                  "https://tenor.com/zowN.gif",
                                  "https://tenor.com/ya9o.gif",
                                  "https://tenor.com/2aaI.gif",
                                  "https://tenor.com/6Gc0.gif",
                                  "https://tenor.com/Zqqm.gif",
                                  "https://tenor.com/H2r4.gif",
                                  "https://tenor.com/PzBz.gif",
                                  "https://tenor.com/bfG3V.gif",
                                  "https://tenor.com/usZY.gif",
                                  "https://tenor.com/wuOu.gif",
                                  "https://tenor.com/AbDb.gif",
                                  "https://tenor.com/HlMg.gif", ]))


@bot.command()
async def thinking(ctx):
    await ctx.send(f"{ctx.message.author.mention} **rรฉflรฉchi** :thinking:")
    await ctx.send(random.choice(["https://tenor.com/5FxL.gif",
                                  "https://tenor.com/bgSGM.gif",
                                  "https://tenor.com/bgSGM.gif",
                                  "https://tenor.com/1P4R.gif",
                                  "https://tenor.com/4CnT.gif",
                                  "https://tenor.com/Yoa9.gif",
                                  "https://tenor.com/bm5xf.gif",
                                  "https://tenor.com/bjkoo.gif",
                                  "https://tenor.com/bicea.gif",
                                  "https://tenor.com/bmPwW.gif",
                                  "https://tenor.com/XXdw.gif", ]))


@bot.command(aliases=['chi'])
async def channelinfo(ctx, *, channel: discord.TextChannel = None):
    if not channel:
        channel = ctx.channel
    embed = discord.Embed(title="Channel info", description=f"Informations sur le channel {channel.name}",
                          color=0xeee657)
    embed.add_field(name="๐?ใปNom du salon :", value=f"{channel.name}", inline=False)
    embed.add_field(name="๐ใปID du salon :", value=f"{channel.id}", inline=False)
    embed.add_field(name=":tools:ใปSalon crรฉรฉ le ", value=channel.created_at.strftime("%d/%m/%Y"), inline=False)
    embed.add_field(name="๐ฐใปSujet du salon :", value=f"[icon link]({ctx.guild.icon_url})", inline=False)
    embed.add_field(name="โฐใปDurรฉe du slowmode :", value=f"{channel.slowmode_delay}", inline=False)
    embed.set_footer(text=f"Demandรฉ(e) par {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@bot.command()
async def kiss(ctx, member: discord.Member):
    await ctx.send(f"{ctx.message.author.mention} **fait un bisous ร?** {member.mention} :kiss: ")
    await ctx.send(random.choice(["https://giphy.com/gifs/G3va31oEEnIkM",
                                  "https://giphy.com/gifs/nyGFcsP0kAobm",
                                  "https://giphy.com/gifs/bGm9FuBCGg4SY",
                                  "https://giphy.com/gifs/vUrwEOLtBUnJe",
                                  "https://giphy.com/gifs/zkppEMFvRX5FC",
                                  "https://giphy.com/gifs/bm2O3nXTcKJeU",
                                  "https://giphy.com/gifs/hnNyVPIXgLdle",
                                  "https://giphy.com/gifs/ofF5ftkB75n2",
                                  "https://tenor.com/Z93A.gif",
                                  "https://tenor.com/6fqy.gif",
                                  "https://tenor.com/xRO8.gif",
                                  "https://tenor.com/uX8n.gif", ]))


@bot.command()
async def createinvite(ctx, max_uses: int = 0, max_age: int = 0, *, temporary: bool = 0):
    embed = discord.Embed(title=f"{str(ctx.author)}, here is your invite!", color=0xff1493)
    invite = await ctx.guild.text_channels[0].create_invite(max_uses=max_uses, max_age=max_age, temporary=temporary)
    embed = discord.Embed(color=0x363940, timestamp=ctx.message.created_at)
    embed.description = f":incoming_envelope: : Expire aprรจs {invite.max_uses} utilisation(s).\n\nโฐ : Expire dans {invite.max_age} secondes.\n\n:question: : Temporaire : {invite.temporary}\n\n"
    embed.set_footer(text=f'Demandรฉ par {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name=f":link:  Ton inivitation :", value=invite)
    await ctx.send(embed=embed)


@bot.command()
async def password(ctx, lenght: int = None, number: int = None):
    if not lenght or not number:
        await ctx.send(embed=discord.Embed(
            description=f'Veuillez indiquer la longueur du mot de passe et le nombre de caractรจres qu il contient..',
            color=0x363940, timestamp=ctx.message.created_at))

    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for x in range(number):
        password = ''

        for i in range(lenght):
            password += random.choice(chars)

        await ctx.author.send(
            embed=discord.Embed(description=f'**๐ | Mot de passe gรฉnรฉrรฉ :\n\n{password}**', color=0x363940,
                                timestamp=ctx.message.created_at))
        await ctx.send(embed=discord.Embed(description=f'**โ | Mot de passe envoyรฉ avec succรจs!**', color=0x363940,
                                           timestamp=ctx.message.created_at))
        returnr


    




bot.run("")
