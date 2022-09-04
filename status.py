import discord
import requsets
from bs4 import BeautifulSoup
from datetime import datetime

bot = commands.Bot(command_prefix='?')

if fuck.status_code == 200 :
  a = "사이트 사용가능."
else :
  a = "사이트 사용불가능(업데이트중)"

@bot.event
async def on_ready():
    print('봇이 켜졌습니다.')

@bot.event
async def on_ready():


  await bot.change_presence(status=discord.Status.idle) 
  await bot.change_presence(activity=discord.Game(name="상태 표시중"))

@bot.command()
async def 상태 (ctx):
  msg = await ctx.send("https://linore.rocot.xyz/%22)
  fuck = requests.get('https://linore.rocot.xyz/%27)
  while True :
    ti = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    embed = discord.Embed(Colour = 00000)
    embed.add_field(name= ti +'사이트 상태' , value=a, inline=False)
    embed.set_footer(text='2시간마다 갱신됩니다.')
    await msg.edit(embed=embed)
    time.sleep(7200)
    
    token('')
