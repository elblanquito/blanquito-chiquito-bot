import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

def get_help_message():
    return (
        "## Hola, soy **Blanquito chikito 💢**\n\n"
        "Un gusto en conocerlos 👋 Soy un bot creado por <@712389088308625471> ¿desdecuando los femboys se volvieron programadores? Estoy aquí para ayudarles en lo que pueda, diganle a blanco que cosas les gustaria que pudiera hacer.\n\n"
        "**Comandos disponibles 📜**\n"
        "• `.saluda` Muestra este mensaje.\n"
        "• `.ayuda` Muestra este mensaje.\n"
        "• `.blanco <mensaje>` Repite el mensaje.\n\n"
        "💌 link de invitacion:\n"
        "https://discord.com/oauth2/authorize?client_id=1530652503916413189"
    )

@bot.command()
async def blanco(ctx, *arg):
    response = ' '.join(arg)
    await ctx.send(response)

@bot.command(aliases=["ayuda", "help"])
async def saluda(ctx):
    await ctx.send(get_help_message(),allowed_mentions=discord.AllowedMentions.none())

@bot.command()
async def tomate(ctx):
    await ctx.send('los tomates son rojos, y pos las verdad estan basten chidos y asi xdd 🍅 emm es mi fruta favorita we jajaja ¿y a ti te gustan?')

@bot.command()
async def suma(ctx, *arg):
    if len(arg) == 0:
        await ctx.send("Claro que se sumar tontito, pasame unos numeros y los sumo :3")
        return

    total = 0
    invalidos = []

    for valor in arg:
        try:
            total += float(valor)
        except ValueError:
            invalidos.append(valor)

    # Si el numero es entero, lo mostramos sin decimales (ej. 10 en vez de 10.0)
    total_mostrado = int(total) if total == int(total) else total


    response = f"Si sumamos todo: {total_mostrado}"
    if total_mostrado == 67:
        response = "SIX SEVENNN!!! 🧨🤲🔥"

    await ctx.send(response)

@bot.command()
async def gato(ctx, *arg):
    try:
        result = requests.get('https://cataas.com/cat/says/' + ' '.join(arg))
        await ctx.send(result.url)
        
    except Exception as e:
        print("Error", e)

@bot.event
async def on_ready():
    print('===============================')
    print('EL bot esta listo!')
    print(f'User: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('===============================')

load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))