import os
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()

import discord
from discord.ext import commands
from visao_computacional import classificar_imagem

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
FORMATOS_ACEITOS = ('.png', '.jpg', '.jpeg', '.webp', '.bmp')
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    # Verifica se tem alguma imagem anexada na mensagem
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename

            if not file_name.lower().endswith(FORMATOS_ACEITOS):
                await ctx.send("O formato não é aceito")
                continue

            caminho_arquivo = f"./{file_name}"
            
            # Salva a imagem no computador/servidor
            caminho_arquivo = f"./{file_name}"
            await attachment.save(caminho_arquivo)
            await ctx.send(f"Imagem `{file_name}` recebida! A IA está pensando... 🤖")

            # Manda a imagem salva para a IA classificar
            try:
                # Chama a função e recebe a resposta
                classe, confianca = classificar_imagem(caminho_arquivo)
                
                # Transforma a confiança (ex: 0.98) em porcentagem (98.00%)
                porcentagem = confianca * 100
                
                await ctx.send(f"Eu acho que isso é: **{classe}** (Certeza: {porcentagem:.2f}%) 🚀")
            
            except Exception as e:
                await ctx.send("Ops! Tive um problema ao analisar a imagem com a IA.")
                print(f"Erro na IA: {e}")
                
    else:
        await ctx.send('Esquecestes de enviar a imagem jovem padawan') #* M4L2












bot.run("MTQ5ODQ0NDQ3MzY0OTA3MDA5MA.GN613B.bZQeAuWnHAI9JWKGJL0Q8J6qnq8LEN2m1MmJ0Y")