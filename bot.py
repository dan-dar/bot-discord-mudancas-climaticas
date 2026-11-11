  import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def ola(ctx):
    await ctx.send("Olá! Eu sou o bot das mudanças climáticas 🌍")



@bot.command()
async def o_que_sao(ctx):
    await ctx.send("As mudanças climaticas referem-se a alterações significativas e duradouras nos padrões climáticos da Terra, incluindo aumento da temperatura média global, mudanças nos pradões de precitação, aumento do nível do mar e eventos climáticos extremos")


@bot.command()
async def como_ajudar(ctx):
    await ctx.send("Você pode ajudar a combater as mudanças climaticas adotando práticas sustentaveis, como reduzir o consumo de energia, reciclar, plantar árvores e apoiar politicas ambientais. Além disso , você pode se informar sobre esse assunto e compartilhar conhecimento com outras pessoas para aumentar a conscientização")



@bot.command()
async def dicas(ctx):
    await ctx.send("Aqui estão algumas dicas para ajudar a combater as mundanças climaticas:\n"
                   "1. Reduza o consumo de energia: Desligue aparelhos eletrônicos quando não estiverem em uso, utilize lâmpadas de baixo consumo e aproveite a luz natural sempre que possivel.\n"
                   "2. Recicle: Separe corretamente os materiais recicláveis e evite o descarte inadequado de lixo.\n"
                   "3. plante árvores: As árvores ajudam a absorver o dióxido de carbono e contribuem para preservar a biodiversiadade.\n"
                   "4. Apoie politicas ambientais: Participe de campanhas e apoie iniciativas que promovam a proteção do meio ambiente.\n"
                   "5. Informe-se e compartilhe conhecimento: Busque informações sobre as mudanças climaticas e compartilhe com outras pessoas para aumentar a consientização sobre o assunto.")



@bot.command()
async def fontes(ctx):
    await ctx.send("Aqui estão alumas fontes confiaveis sobre mudanças climaticas:\n"
                   "1. Painel Intergovernamental sobre mudanças climaticas (IPPC): https://www.ipcc.ch/\n"
                   "2. NASA - Mudanças climaticas: https://climate.nasa.gov/\n"
                   "3. Organização Meteorologica Mundial (OMM): https://public.wmo.int/en\n"
                   "4. Greenpeace: https://www.greenpeace.org/n")


@bot.command()
async def quiz(ctx):
    perguntas = [
        (
            "1) Qual gás contribui para o aquecimento global?\n"
            "A) Oxigênio\nB) Dióxido de carbono\nC) Hélio",
            "b",
            "O dióxido de carbono é um gás de efeito estufa.",
        ),
        (
            "2) Qual atividade humana aumenta as emissões de gases de efeito estufa?\n"
            "A) Queimar combustíveis fósseis\nB) Separar materiais recicláveis\nC) Usar bicicleta",
            "a",
            "A queima de combustíveis fósseis libera gases de efeito estufa.",
        ),
        (
            "3) Qual atitude ajuda a reduzir as emissões?\n"
            "A) Desperdiçar energia\nB) Usar transporte individual em todos os trajetos\nC) Economizar energia",
            "c",
            "Economizar energia pode ajudar a reduzir as emissões.",
        ),
    ]
    pontos = 0

    await ctx.send("Vamos começar! Responda com A, B ou C. Você tem 30 segundos por pergunta.")

    for pergunta, resposta_correta, explicacao in perguntas:
        await ctx.send(pergunta)
        try:
            resposta = await bot.wait_for(
                "message",
                timeout=30.0,
                check=lambda mensagem: mensagem.author == ctx.author and mensagem.channel == ctx.channel,
            )
        except asyncio.TimeoutError:
            await ctx.send(f"Tempo esgotado! Sua pontuação: {pontos}/{len(perguntas)}.")
            return

        if resposta.content.strip().lower() == resposta_correta:
            pontos += 1
            await ctx.send("Correto!")
        else:
            await ctx.send(f"Resposta incorreta. A resposta certa era {resposta_correta.upper()}. {explicacao}")

    await ctx.send(f"Questionário finalizado! Você acertou {pontos} de {len(perguntas)} perguntas.")


@bot.command()
async def ajuda(ctx):
    await ctx.send("Aqui estão os comandos disponíveis:\n"
                   "!ola - Cumprimenta o usuário\n"
                   "!o_que_sao - Explica o que são mudanças climáticas\n"
                   "!como_ajudar - Fornece informações sobre como ajudar a combater as mudanças climáticas\n"
                   "!dicas - Fornece dicas práticas para combater as mudanças climáticas\n"
                   "!fontes - Fornece fontes confiáveis sobre mudanças climáticas\n"
                   "!quiz - Inicia um questionário sobre mudanças climáticas\n"
                   "!ajuda - Mostra esta mensagem de ajuda")

bot.run(TOKEN)
