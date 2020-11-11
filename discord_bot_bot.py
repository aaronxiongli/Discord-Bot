from googletrans import Translator
import discord
import os
from youtube_search import YoutubeSearch
import googlesearch
import discord.utils
from GoogleNews import GoogleNews
import tenorpy
import math
from discord.ext import commands
from PyDictionary import PyDictionary
from discord.voice_client import VoiceClient
import random
import requests,json
import youtube_dl
import time
from twitter_scraper import get_tweets
import PIL
from PIL import Image
from PIL import ImageFont
from discord.ext import tasks, commands
from PIL import ImageDraw
import praw
import wikipedia
from discord.utils import get
from time import sleep
import pymongo
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
client = commands.Bot(command_prefix = 'e')
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  
web = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe", options=options)
queue = []
youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
@client.event
async def on_ready():
        activity = discord.Game(name="NeuraLink",type=3)
        await client.change_presence(status=discord.Status.online,activity=activity)
@client.command(name='queue', help='This command adds a song to the queue')
async def queue_(ctx, *name):
        print(ctx)
        name=" ".join(name[:])
        global queue
        if "http" in name:
                queue.append(name)
                await ctx.send(f'`{name}` added to queue!')
        else:
                url=YoutubeSearch(name,max_results=1).to_dict()
                suff=url[0]['url_suffix']
                suf=suff.replace(suff[0],"/")
                url="https://www.youtube.com"+suf
                queue.append(url)
                await ctx.send(f'`{url}` added to queue!')
#@client.command()
#async def compile_python(ctx,*code):
#    with open("log.txt","w+") as fil:
#           fil.truncate(0)
#    code=" ".join(code[:])
#    split_code=code.split("|")
#    with open("lol.py","w+") as l:
#        l.truncate(0)
#    with open("lol.py","a+") as f:
#        for i in range(0,len(split_code)):
#            f.write(split_code[i]+"\n")
#    message=os.popen("lol.py").read()
#    await ctx.send(message)
#    print(message)
#    if (len(message)>2000):  
#        with open("log.txt","w") as lol:
#            lol.write(message)
#            await ctx.send(file=discord.File(lol))
#    else:
#        await ctx.send(message)
@client.command()
async def hello(ctx):
        abba=random.choice(['5','1','2','3','4','4','4','4','4','4','4','4','4','4','4','4','4','4'])
        print(abba)
        if abba=='1':
                greet=['Sup gang!','Hey did you see the last SpaceX launch','Man Tesla is awesome!!','OpenAI loves to see projects!','Sometimes I wonder why is the first result on Google for PID Pelvic Inflamatory Disease and not Proportional Integral Derivative Control System!','FunFact: I work 105 hours a week!']
                await ctx.channel.send(random.choice(greet))
        if abba=='2':
                reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
                post = reddit.subreddit('dankmemes')
                latest=post.random()
                await ctx.channel.send("Hey look at this meme. It's so funny!")
                await ctx.channel.send(latest.url)
        if abba=='3':
                with Image.open("D:/Naman/Projects/Discord Bot/itty.png") as f:
                        img=ImageDraw.Draw(f)
                        font = ImageFont.truetype("arial.ttf", 15)
                        img.text((77,250),random.choice(['Skanda','Aryan','Naman']),(0,0,0),font=font)
                        f.save("sitty.png")
                        sleep(2)
                with open("D:/Naman/Projects/Discord Bot/sitty.png","rb") as e:
                        await ctx.channel.send(file=discord.File(e))       
        if abba=='5':
                tenorgif = tenorpy.Tenor()
                await ctx.channel.send(tenorgif.random('elon musk'))
@client.command()
async def covid(ctx):
        web.get("https://www.google.com/search?q=covid+cases&rlz=1C1CHBF_enIN913IN913&oq=covid+cases&aqs=chrome..69i57.1968j0j7&sourceid=chrome&ie=UTF-8")
        Confirmed = web.find_element_by_xpath('/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[4]/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div[1]/table/tbody/tr/td[1]/div[2]/div[1]/span').get_attribute("innerHTML")
        Recovered = web.find_element_by_xpath('/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[4]/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div[1]/table/tbody/tr/td[2]/div[2]/div[1]/span').get_attribute("innerHTML")
        Deaths = web.find_element_by_xpath('/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[4]/div[2]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div[1]/table/tbody/tr/td[3]/div[2]/div[1]/span').get_attribute("innerHTML")
        embed = discord.Embed(colour = discord.Colour.orange())
        embed.set_author(name="Covid cases")
        embed.add_field(name="Confirmed",value=str(Confirmed),inline=False)
        embed.add_field(name="Recovered",value=str(Recovered),inline=False)
        embed.add_field(name="Deaths",value=str(Deaths),inline=False)
        await ctx.send(embed = embed)
@client.command()
async def role(ctx, * role: discord.Role):
        roless = get(ctx.message.guild.roles, name=role)
        await ctx.message.author.add_roles(roless)     
@client.command()
async def hi(ctx):
        await ctx.send(random.choice(["Hello there inferior human.","I dont talk to low IQ people","Ahoy!","Hey nerds"]))
@client.command()
async def roll(ctx):
	await ctx.send(random.randint(1,6))
@client.command()
async def iloveyou(ctx):
        await ctx.send("Everybody does!")
@client.command()
async def tunak(ctx):
	tunak = random.choice(['https://tenor.com/view/tunak-tun-tuktuk-tuk-arabo-gif-7350381','https://tenor.com/view/dancing-dance-mustache-point-daler-mehndi-gif-17362207','https://tenor.com/view/tanuk-gif-10130998'])
	await ctx.send(tunak)
@client.command()
async def timeplease(ctx):
        for i in range (0,3):
                tim = time.strftime('%H:%M:%S')
                await ctx.send(tim)
                sleep(1)        
        await ctx.send("Clock is ticking better do your work!!")
@client.command(pass_context=True)
async def execute(ctx,*args):
        x = " ".join(args[:])
        y = random.choice(["https://tenor.com/view/lego-lego-guillotine-bastille-day-gifs-gif-9146907","https://tenor.com/view/guillotina-guillotine-slice-burger-gif-17494126"])
        await ctx.send("Robespiere here, Send "+x+" to the Guillotin")
        await ctx.send(y)
@client.command(pass_context=True)
async def news(ctx,*args):
        googlenews = GoogleNews()
        x = " ".join(args[:])
        googlenews.setlang('en')
        googlenews.setperiod('d')
        #googlenews.setTimeRange('02/01/2020','02/28/2020')
        googlenews.setencode('utf-8')        
        googlenews.search(x)
        newssss=googlenews.gettext()
        for i in range(0,len(newssss)):
                await ctx.send(newssss[i])
@client.command()
async def ping(ctx):
	embed=discord.Embed(colour=discord.Colour.orange())
	embed.set_author(name="Pong!")
	embed.add_field(name="Latency",value=str(client.latency)+" seconds",inline=False)
	await ctx.send(embed=embed)
@client.command()
async def funfact(ctx):
	fun = ['You are asking me a funfact because you are out of them.','I belong to an alien civilisation.','You are an idiot.','I am wonderful, and i never failed like that Penny next door.']
	await ctx.send(random.choice(fun))
@client.command(pass_context=True)
async def kick(ctx,user: discord.Member,*,reason="You Suck"):
        await ctx.send("Kicking "+ str(user))
        await user.kick(reason=reason)
@client.command(pass_context=True)
async def ban(ctx,user: discord.Member,*,reason=None):
        await ctx.send("Banned "+ str(user))
        await user.ban(reason=reason)         
@client.command(pass_context=True)
async def helpme(ctx,query):
        result = wikipedia.summary(query,sentences=2)
        embed=discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Wikipedia!")
        embed.add_field(name="Your result!",value=result,inline=False)
        await ctx.send(embed=embed)
@client.command(pass_context=True)
async def rot(ctx,angle):
        with Image.open("D:/Naman/Projects/Discord Bot/elon.png") as f:
                img = f.rotate(float(angle))
                i=img.save("e.png")
                with open("D:/Naman/Projects/Discord Bot/e.png","rb") as e:
                        await ctx.send(file=discord.File(e))
@client.command(pass_context=True)
async def communist(ctx,name):
        with Image.open("D:/Naman/Projects/Discord Bot/communism.png") as f:
                img=ImageDraw.Draw(f)
                font = ImageFont.truetype("arial.ttf", 50)
                img.text((45,55),name.upper(),(0,0,0),font=font)
                f.save("comm.png")
                sleep(2)
                with open("D:/Naman/Projects/Discord Bot/comm.png","rb") as e:
                        await ctx.send(file=discord.File(e))
@client.command(pass_context=True)
async def firsttime(ctx,*args):
        x = " ".join(args[:])
        y = x.split(",")
        with Image.open("D:/Naman/Projects/Discord Bot/tooo.png") as f:
                img=ImageDraw.Draw(f)
                font = ImageFont.truetype("arial.ttf", 10)
                font1 = ImageFont.truetype("arial.ttf", 20)
                img.text((10,43),y[0].upper(),(0,0,0),font=font)
                img.text((10,140),y[1].upper(),(0,0,0),font=font1)
                f.save("t.png")
                sleep(2)
                with open("D:/Naman/Projects/Discord Bot/t.png","rb") as e:
                        await ctx.send(file=discord.File(e))                        
@client.command(pass_context=True)
async def spongy(ctx,*args):
        x = " ".join(args[:])
        y = x.split(",")
        z = len(y)
        print(z)
        with Image.open("D:/Naman/Projects/Discord Bot/spongy.png") as f:
                img=ImageDraw.Draw(f)
                font = ImageFont.truetype("arial.ttf", 10)
                k=25
                for i in range (0,z):
                        img.text((25,k),y[i],(0,0,0),font=font)
                        k += 10
                f.save("spn.png")
                sleep(2)
                with open("D:/Naman/Projects/Discord Bot/spn.png","rb") as e:
                        await ctx.send(file=discord.File(e))
@client.command(pass_context=True)
async def cmm(ctx,*args):
        x = " ".join(args[:])
        y = x.split(",")
        z = len(y)
        print(z)
        with Image.open("D:/Naman/Projects/Discord Bot/cmm.png") as f:
                img=ImageDraw.Draw(f)
                font = ImageFont.truetype("arial.ttf", 10)
                k=97
                for i in range (0,z):
                        img.text((91,k),y[i],(0,0,0),font=font)
                        k += 10
                f.save("cm.png")
                sleep(2)
                with open("D:/Naman/Projects/Discord Bot/cm.png","rb") as e:
                        await ctx.send(file=discord.File(e))
@client.command(pass_context=True)
async def shit(ctx,*args):
        x = " ".join(args[:])
        y = x.split(",")
        z = len(y)
        print(z)
        with Image.open("D:/Naman/Projects/Discord Bot/itty.png") as f:
                img=ImageDraw.Draw(f)
                font = ImageFont.truetype("arial.ttf", 15)
                k=250
                for i in range (0,z):
                        img.text((77,k),y[i],(0,0,0),font=font)
                        k += 10
                f.save("sitty.png")
                sleep(2)
                with open("D:/Naman/Projects/Discord Bot/sitty.png","rb") as e:
                        await ctx.send(file=discord.File(e))
@client.command(pass_context=True)
async def pres(ctx,*args):
        x = " ".join(args[:])
        y = x.split(",")
        z = len(y)
        print(z)
        with Image.open("D:/Naman/Projects/Discord Bot/pres.png") as f:
                img=ImageDraw.Draw(f)
                font = ImageFont.truetype("arial.ttf", 15)
                k=30
                for i in range (0,z):
                        img.text((57,k),y[i],(0,0,0),font=font)
                        k += 10
                f.save("press.png")
                sleep(2)
                with open("D:/Naman/Projects/Discord Bot/press.png","rb") as e:
                        await ctx.send(file=discord.File(e))
@client.command(pass_context=True)
async def ono(ctx,*args):
        x = " ".join(args[:])
        y = x.split(",")
        z = len(y)
        print(z)
        with Image.open("D:/Naman/Projects/Discord Bot/onoo.png") as f:
                img=ImageDraw.Draw(f)
                font = ImageFont.truetype("arial.ttf", 20)
                k=0
                for i in range (0,z):
                        img.text((0,k),y[i],(0,0,0),font=font)
                        k += 20
                f.save("onooo.png")
                sleep(2)
                with open("D:/Naman/Projects/Discord Bot/onooo.png","rb") as e:
                        await ctx.send(file=discord.File(e)) 
@client.command(pass_context=True)
async def dumbo(ctx,*args):
        x = " ".join(args[:])
        y = x.split(",")
        z = len(y)
        print(z)
        with Image.open("D:/Naman/Projects/Discord Bot/dumbo.png") as f:
                img=ImageDraw.Draw(f)
                font = ImageFont.truetype("arial.ttf", 10)
                k=125
                for i in range (0,z):
                        img.text((35,k),y[i],(0,0,0),font=font)
                        k += 10
                f.save("dm.png")
                sleep(2)
                with open("D:/Naman/Projects/Discord Bot/dm.png","rb") as e:
                        await ctx.send(file=discord.File(e)) 
@client.command(pass_context=True)
async def drake(ctx,*args):
        x=" ".join(args[:])
        y=x.split(",")
        print(y)
        with Image.open("D:/Naman/Projects/Discord Bot/nono.png") as f:
                if len(y[1])>14 or len(y[0])>14:
                        img=ImageDraw.Draw(f)
                        font=ImageFont.truetype("arial.ttf", 7)
                        img.text((115,0),y[0].upper(),(0,0,0),font=font,encoding="unic")
                        img.text((115,115),y[1].upper(),(0,0,0),font=font,encoding="unic")
                        f.save("nah.png")
                        sleep(2)
                else:
                        img=ImageDraw.Draw(f)
                        font = ImageFont.truetype("arial.ttf", 14)
                        img.text((115,0),y[0].upper(),(0,0,0),font=font,encoding="unic")
                        img.text((115,115),y[1].upper(),(0,0,0),font=font,encoding="unic")
                        f.save("nah.png")
                        sleep(2)
                with open("D:/Naman/Projects/Discord Bot/nah.png","rb") as e:
                        await ctx.send(file=discord.File(e))
@client.command(pass_context=True)
async def pup(ctx,*args):
        x=" ".join(args[:])
        y=x.split(".")
        first = y[0].split(",")
        second = y[1].split(",")
        with Image.open("D:/Naman/Projects/Discord Bot/pupmeme2.png") as f:
                if len(y[1])>14 or len(y[0])>14:
                        img=ImageDraw.Draw(f)
                        font=ImageFont.truetype("arial.ttf", 15)
                        k=30
                        l=320
                        for i in range(0,len(first)):
                                img.text((230,k),first[i].upper(),(0,0,0),font=font,encoding="unic")
                                k += 17
                        for o in range(0,len(second)):
                                l+=17    
                                img.text((230,l),second[o].upper(),(0,0,0),font=font,encoding="unic")
                        f.save("ppy.png")
                        sleep(2)
                else:
                        img=ImageDraw.Draw(f)
                        font=ImageFont.truetype("arial.ttf", 15)
                        k=0
                        l=290
                        for i in range(0,len(first)):
                                img.text((230,k),first[i].upper(),(0,0,0),font=font,encoding="unic")
                                k += 15
                        for o in range(0,len(second)):
                                l+=15       
                                img.text((230,l),second[o].upper(),(0,0,0),font=font,encoding="unic")
                        f.save("ppy.png")
                        sleep(2)
                with open("D:/Naman/Projects/Discord Bot/ppy.png","rb") as e:
                        await ctx.send(file=discord.File(e))
@client.command(pass_context=True)
async def truck(ctx,*args):
        x=" ".join(args[:])
        y=x.split(".")
        first = y[0].split(",")
        second = y[1].split(",")
        with Image.open("D:/Naman/Projects/Discord Bot/mentos.png") as f:
                if len(y[1])>14 or len(y[0])>14:
                        img=ImageDraw.Draw(f)
                        font=ImageFont.truetype("arial.ttf", 15)
                        k=40
                        l=40
                        for i in range(0,len(first)):
                                img.text((0,k),first[i].upper(),(0,0,0),font=font,encoding="unic")
                                k += 17
                        for o in range(0,len(second)):
                                img.text((210,l),second[o].upper(),(0,0,0),font=font,encoding="unic")
                                l+=17
                        f.save("men.png")
                        sleep(2)
                else:
                        img=ImageDraw.Draw(f)
                        font=ImageFont.truetype("arial.ttf", 15)
                        k=40
                        l=40
                        for i in range(0,len(first)):
                                img.text((0,k),first[i].upper(),(0,0,0),font=font,encoding="unic")
                                k += 15
                        for o in range(0,len(second)):
                                img.text((210,l),second[o].upper(),(0,0,0),font=font,encoding="unic")
                                l+=15
                        f.save("men.png")
                        sleep(2)
                with open("D:/Naman/Projects/Discord Bot/men.png","rb") as e:
                        await ctx.send(file=discord.File(e))                        
@client.command(pass_context=True)                        
async def doggo(ctx,*args):
        x=" ".join(args[:])
        y=x.split(".")
        first = y[0].split(",")
        second = y[1].split(",")
        with Image.open("D:/Naman/Projects/Discord Bot/doggo.png") as f:
                if len(y[1])>14 or len(y[0])>14:
                        img=ImageDraw.Draw(f)
                        font=ImageFont.truetype("arial.ttf", 15)
                        k=150
                        l=150
                        for i in range(0,len(first)):
                                img.text((10,k),first[i].upper(),(0,0,0),font=font,encoding="unic")
                                k += 17
                        for o in range(0,len(second)):
                                img.text((160,l),second[o].upper(),(0,0,0),font=font,encoding="unic")
                                l+=17
                        f.save("doggo1.png")
                        sleep(2)
                else:
                        img=ImageDraw.Draw(f)
                        font=ImageFont.truetype("arial.ttf", 15)
                        k=150
                        l=150
                        for i in range(0,len(first)):
                                img.text((10,k),first[i].upper(),(0,0,0),font=font,encoding="unic")
                                k += 15
                        for o in range(0,len(second)):
                                img.text((155,l),second[o].upper(),(0,0,0),font=font,encoding="unic")
                                l+=15
                        f.save("doggo1.png")
                        sleep(2)
                with open("D:/Naman/Projects/Discord Bot/doggo1.png","rb") as e:
                        await ctx.send(file=discord.File(e))                                                
@client.command(pass_context=True)
async def royalpoo(ctx,*args):
        x=" ".join(args[:])
        y=x.split(",")
        print(y)
        with Image.open("D:/Naman/Projects/Discord Bot/royal.png") as f:
                if len(y[1])>14 or len(y[0])>14:
                        img=ImageDraw.Draw(f)
                        font=ImageFont.truetype("arial.ttf", 7)
                        img.text((125,0),y[0].upper(),(0,0,0),font=font,encoding="unic")
                        img.text((125,105),y[1].upper(),(0,0,0),font=font,encoding="unic")
                        f.save("ryl.png")
                        sleep(2)
                else:
                        img=ImageDraw.Draw(f)
                        font = ImageFont.truetype("arial.ttf", 14)
                        img.text((125,0),y[0].upper(),(0,0,0),font=font,encoding="unic")
                        img.text((125,105),y[1].upper(),(0,0,0),font=font,encoding="unic")
                        f.save("ryl.png")
                        sleep(2)
                with open("D:/Naman/Projects/Discord Bot/ryl.png","rb") as e:
                        await ctx.send(file=discord.File(e))                        
@client.command(pass_context=True)
async def cry(ctx,*args):
        x=" ".join(args[:])
        y=x.split(",")
        print(y)
        with Image.open("D:/Naman/Projects/Discord Bot/cry.png") as f:
                if len(y[1])>14 or len(y[0])>14:
                        img=ImageDraw.Draw(f)
                        font=ImageFont.truetype("arial.ttf", 7)
                        img.text((10,150),y[0].upper(),(0,0,0),font=font,encoding="unic")
                        img.text((170,150),y[1].upper(),(0,0,0),font=font,encoding="unic")
                        f.save("cryyy.png")
                        sleep(2)
                else:
                        img=ImageDraw.Draw(f)
                        font = ImageFont.truetype("arial.ttf", 14)
                        img.text((10,150),y[0].upper(),(0,0,0),font=font,encoding="unic")
                        img.text((150,150),y[1].upper(),(0,0,0),font=font,encoding="unic")
                        f.save("cryyy.png")
                        sleep(2)
                with open("D:/Naman/Projects/Discord Bot/cryyy.png","rb") as e:
                        await ctx.send(file=discord.File(e))                         
@client.command(pass_context=True)
async def knock(ctx,knocked):
        await ctx.send(knocked+"!"+knocked+"!"+knocked+"!")
@client.command()
async def areyoumad(ctx):
	await ctx.send("I am not mad my mom got me tested.")
@client.command(pass_context=True)
async def POWER(ctx,*args):
        name = " ".join(args[:])
        for i in range(0,5):
                await ctx.send("ALL HAIL "+name+"!")
                sleep(2)
@client.command(pass_context=True)
async def gif(ctx,*args):
        tag = " ".join(args[:])
        tenorgif = tenorpy.Tenor()
        await ctx.send(tenorgif.random(tag))
@client.command(pass_context=True)
async def trans(ctx,*args):
        query = " ".join(args[:])
        t=Translator()
        chunks=query.split(',')
        embed=discord.Embed(colour=discord.Colour.orange())
        x=t.translate(chunks[1],src=chunks[0],dest=chunks[2])
        embed.add_field(name=x.text,value=x.pronunciation,inline=False)
        await ctx.send(embed=embed)
@client.command(pass_context=True)
async def twitter(ctx,*args):
		tweets=" ".join(args[:])
		for tweet in get_tweets(tweets,pages=1):
				await ctx.send("https://twitter.com"+tweet['tweetUrl'])
@client.command(pass_context=True)
async def nobody(ctx,*args):
        x=" ".join(args[:])
        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Nobody!!")
        embed.add_field(name="!",value="literaly nobody!",inline=False)
        embed.add_field(name="!",value="I am telling bro nobody!",inline=False)
        embed.add_field(name="!",value="Not even basoor!!!",inline=False)
        embed.add_field(name="!",value=x,inline=False)
        await ctx.send(embed=embed)
@client.command(pass_context=True)
async def weather(ctx,*args):
        city = " ".join(args[:])
        api="4591641ca8555841a53bae52630368ea"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api + "&q=" + city
        response=requests.get(complete_url)
        reply = response.json()
        features=reply["main"]
        temp = features["temp"]
        pressure = features["pressure"]
        humidity = features["humidity"]
        weather = reply["weather"]
        described_weather = weather[0]["description"]
        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Weather!")
        embed.add_field(name="Temperature",value=str(temp)+"K",inline=False)
        embed.add_field(name="Pressure",value=str(pressure)+"hPa",inline=False)
        embed.add_field(name="Humidity",value=str(humidity)+"%",inline=False)
        embed.add_field(name="Weather",value=str(described_weather),inline=False)
        await ctx.send(embed=embed)         
@client.command(pass_context=True)
async def reddit(ctx,sub):
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        post = reddit.subreddit(sub)
        latest=post.random()
        await ctx.send(latest.url)
@client.command(pass_context=True)
async def learnpython(ctx):
        pyembed = discord.Embed(colour=discord.Colour.orange())
        pyembed.set_author(name="Learn Python Basics. You get 10 minutes to respond everytime.")
        pyembed.add_field(name="print",value="Anything followed by this command within quotation marks and brackets will be printed for you.",inline=False)
        pyembed.add_field(name="if",value="Pass parameters like == or != or in and you should receive a value True if notation is true and vice versa NOTE-THE COMMAND IN IDLE IS MORE USEFUL,PLEASE DONT USE QUOTATION MARKS HERE, NO MULTIWORD STRING AND LEAVE SPACES AFTER EVERY WORD!!!",inline=False)
        pyembed.add_field(name="for",value="You can use the for range commands here.NOTE: NOT BRACKETS PLEASE.EXAMPLE: for i in range 0 100 - THIS WILL RETURN A VALUE 100 TIMES.ALSO LEAVE SPACES AFTER EVERY WORD",inline=False)
        pyembed.add_field(name="/ or + or * or -",value="Divide Add Multiply Subtract, TWO VALS ONLY")
        pyembed.add_field(name="quit()",value="Stop the execution.")
        await ctx.send(embed=pyembed)
        player_id = ctx.message.author.id
        while __name__ == "__main__":
                if ctx.message.author.id == player_id:
                        command=await client.wait_for('message',timeout=600)
                        if "print" in command.content:
                                array_1 = command.content.split("(")
                                array_2 = array_1[1].split("'")
                                await ctx.send(array_2[1])
                        if "if" in command.content:
                                array_if_1 = command.content.split(" ")
                                if array_if_1[2] == "==":
                                        if array_if_1[1] == array_if_1[3]:
                                                await ctx.send("True")
                                        else:
                                                await ctx.send("False")                
                                if array_if_1[2] == "!=":
                                        if array_if_1[1] != array_if_1[3]:
                                                await ctx.send("True")
                                        else:
                                                await ctx.send("False")
                                if array_if_1[2] == "in":
                                        if array_if_1[1] in array_if_1[3]:
                                                await ctx.send("True")
                                        else:
                                                await ctx.send("False")
                        if "for" in command.content:
                                array_for = command.content.split(" ")
                                for i in range(int(array_for[4]),int(array_for[5])):
                                        await ctx.send("Here you go with the for loop...")
                        if "/" in command.content:
                                array_div = command.content.split("/")
                                div_res = float(array_div[0])/float(array_div[1])
                                await ctx.send(div_res)
                        if "*" in command.content:
                                array_div = command.content.split("*")
                                mul_res = float(array_div[0])*float(array_div[1])
                                await ctx.send(mul_res)
                        if "+" in command.content:
                                array_div = command.content.split("+")
                                add_res = float(array_div[0])+float(array_div[1])
                                await ctx.send(add_res)
                        if "-" in command.content:
                                array_div = command.content.split("-")
                                sub_res = float(array_div[0])-float(array_div[1])
                                await ctx.send(sub_res)                        
                        if "quit()" in command.content:
                                text = ['Bye! Bye!','Now I better focus on Tesla!Bye!','Now I better focus on SpaceX!Bye!','Now I better focus on Boring Company!Bye!','Now I better focus on OpenAI!Bye!']
                                text_chosen = random.choice(text)
                                await ctx.send(text_chosen)
                                break                                                                       
@client.command()
async def meme(ctx):
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        post = reddit.subreddit('dankmemes')
        latest=post.random()
        await ctx.send(latest.url)
@client.command()
async def memes(ctx):
        await ctx.send("10 memes for you")
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        for i in range(0,10):
                post = reddit.subreddit('dankmemes')
                latest=post.random()
                await ctx.send(latest.url)
                sleep(2)
@client.command(pass_context=True)
async def google(ctx,*args):
        query = " ".join(args[:])
        answer = search(query,start=0,stop=2,pause=2)
        for res in answer:
                await ctx.send(res)               
@client.command()
async def memebonanza(ctx):
        await ctx.send("100 memes for you")
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        for i in range(0,100):
                post = reddit.subreddit('dankmemes')
                latest=post.random()
                await ctx.send(latest.url)
                sleep(2)
@client.command()
async def memesforlife(ctx):
        await ctx.send("MEME HOUR ACTIVATED")
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        for i in range(0,1800):
                post = reddit.subreddit('dankmemes')
                latest=post.random()
                await ctx.send(latest.url)
                sleep(5)
@client.command(pass_context=True)
async def rememberme(ctx,*name):
        name=" ".join(name[:])
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["elon_members"]
        try:
              edb.delete_one({"idx":ctx.message.author.id})
        except Exception:
                pass        
        edb.insert_one({"idx":ctx.message.author.id,"name":name})
@client.command(pass_context=True)
async def addtomytodo(ctx,*args):
        name = " ".join(args[:])
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["TODO"]
        edb.insert_one({"idx":ctx.message.author.id,"name":name})
@client.command(pass_context=True)
async def appendrulebook(ctx,*args):
        name = " ".join(args[:])
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["rulebook"]
        edb.insert_one({"Added IN":"The Boyz","Rule":name})
@client.command(pass_context=True)
async def rulebook(ctx):
        embed=discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Lex Liber")
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["rulebook"]
        result=edb.find({"Added IN":"The Boyz"})
        for results in result:
                embed.add_field(name="Rule:",value=results["Rule"])
        await ctx.send(embed=embed)          
@client.command(pass_context=True)
async def delete(ctx,*args):
        name = " ".join(args[:])
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["TODO"]
        edb.delete_one({"idx":ctx.message.author.id,"name":name})
@client.command(pass_context=True)
async def whatami(ctx):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["occupation"]
        await ctx.send(edb.find_one({"idx":ctx.message.author.id})["name"])                        
@client.command(pass_context=True)
async def occupation(ctx):
        occ=random.choice(['Physicist','ML Engineer','Engineer at Tesla','Engineer at SpaceX','Biologist','Doctor','Beggar'])
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["occupation"]
        edb.insert_one({"idx":ctx.message.author.id,"name":occ})
        await ctx.send("You have been selected as "+occ)                        
@client.command(pass_context=True)
async def reoccupation(ctx):
        occ=random.choice(['Physicist','ML Engineer','Engineer at Tesla','Engineer at SpaceX','Biologist','Doctor','Beggar'])
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["occupation"]
        try:        
                edb.delete_one({"idx":ctx.message.author.id})
        except Exception:
                pass
        edb.insert_one({"idx":ctx.message.author.id,"name":occ})
        await ctx.send("You have been selected as "+occ)         
@client.command(pass_context=True)
async def TODO(ctx,*args):
        embed=discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="TODO!")
        name = " ".join(args[:])
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["TODO"]
        result=edb.find({"idx":ctx.message.author.id})
        for results in result:
                embed.add_field(name="Your Tasks",value=results["name"])
        await ctx.send(embed=embed)        
@client.command(pass_context=True)
async def whoami(ctx):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client["discord"]
        edb=db["elon_members"]
        dicti=edb.find_one({"idx":ctx.message.author.id})
        await ctx.send("You are "+dicti["name"])        
@client.command()
async def space(ctx):
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        post = reddit.subreddit('space')
        latest=post.random()
        await ctx.send(latest.url)
@client.command()
async def elon(ctx):
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        post = reddit.subreddit('elonmusk')
        latest=post.random()
        await ctx.send(latest.url)
@client.command()
async def pewds(ctx):
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        post = reddit.subreddit('pewdiepie')
        latest=post.random()
        await ctx.send(latest.url)   
@client.command()
async def dani(ctx):
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        post = reddit.subreddit('DaniDev')
        latest=post.random()
        await ctx.send(latest.url)       
@client.command()
async def dota(ctx):
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        post = reddit.subreddit('dota2')
        latest=post.random()
        await ctx.send(latest.url)        
@client.command()
async def amlonely(ctx):
        sad = ['Sad did your crush dump you? Here is some hot beverage :tea:','Sad you have no friends.Here is some hot beverage :tea:','Here is some hot beverage :tea:','I love you :heart:']
        await ctx.send(random.choice(sad))
@client.command()
async def read_budget_discord(ctx):
        client=pymongo.MongoClient('mongodb+srv://budgetdiscord:discord@cluster0.bn3df.mongodb.net/budgetdiscord?retryWrites=true&w=majority')
        database=client.messages
        messages=database.messages
        discovered=[]
        embed=discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Your shitty messages at that silly platform")
        for x in messages.find():
                if x in discovered:
                        pass
                else:
                        username=str(x.get("username"))
                        message=str(x.get("message"))
                        embed.add_field(name=username,value=message,inline=False)
        await ctx.send(embed=embed)
@client.command()
async def send_budget_discord(ctx,*args):
        args=" ".join(args[:])
        mes=args.split(":")
        username=mes[0]
        message=mes[1]
        client=pymongo.MongoClient('mongodb+srv://budgetdiscord:discord@cluster0.bn3df.mongodb.net/budgetdiscord?retryWrites=true&w=majority')
        database=client.messages
        messages=database.messages
        messages.insert_one({"username":username,"message":message})
@client.command(pass_context=True)
async def reddits(ctx,sub):
        reddit = praw.Reddit(client_id='Yfc5FKaKBtgY1w',client_secret='0o_zidhe8Oas3pq0p5Xq7ZPuxVg', password='shellyhatespenny',user_agent='Shelly', username='Shelly_Cooper69')
        for i in range(0,10):
                post = reddit.subreddit(sub)
                latest=post.random()
                await ctx.send(latest.url)
                sleep(2)
@client.command(pass_context=True)
async def dictionary(ctx,word):
        dictionary=PyDictionary()
        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Result")
        embed.add_field(name="Meaning",value=dictionary.meaning(word))
        embed.add_field(name="Synonym",value=dictionary.synonym(word))
        embed.add_field(name="Antonym",value=dictionary.antonym(word))
        await ctx.send(embed=embed)
@client.command(pass_context=True)
async def mathgame(ctx):
        embed=discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name="Someone not liking maths should be executed!!!")
        embed.add_field(name="Rules",value="First to answer correct is correct sorry no pointing system my creator is dumb.")
        embed.add_field(name="Thats it enjoy",value="I will sleep for 5 seconds then we can start")
        await ctx.send(embed=embed)
        sleep(5)
        questions=['multiply','divide','square root','cube','basoor']
        while True:
                curr_ques=random.choice(questions)
                if "multiply" in curr_ques:
                        x = random.randint(1,1000)
                        y = random.randint(1,1000)
                        res = x*y
                        await ctx.send("multiply "+str(x)+"*"+str(y))
                        run = True
                        while run:
                                answer = await client.wait_for('message',timeout=600)
                                if str(res) in answer.content:
                                        await ctx.send("You got it correct "+str(ctx.message.author))
                                        run = False
                                        questions.remove('multiply') 
                if "divide" in curr_ques:
                        x = random.randint(1,1000)
                        y = random.randint(1,1000)
                        res = round(x/y)
                        await ctx.send("divide "+str(x)+"/"+str(y))
                        run = True
                        while run:
                                answer = await client.wait_for('message',timeout=600)
                                if str(res) in answer.content:
                                        await ctx.send("You got it correct "+str(ctx.message.author))
                                        run = False
                                        questions.remove('divide')
                if "square root" in curr_ques:
                        x = random.randint(1,1000)
                        res = round(math.sqrt(x))
                        await ctx.send("square root of "+str(x))
                        run = True
                        while run:
                                answer = await client.wait_for('message',timeout=600)
                                if str(res) in answer.content:
                                        await ctx.send("You got it correct "+str(ctx.message.author))
                                        run = False
                                        questions.remove('square root')
                if "basoor" in curr_ques:
                        x = random.randint(1,100)
                        res = x**2
                        await ctx.send("square of "+str(x))
                        run = True
                        while run:
                                answer = await client.wait_for('message',timeout=600)
                                if str(res) in answer.content:
                                        await ctx.send("You got it correct "+str(ctx.message.author))
                                        run = False
                                        questions.remove('basoor')
                if "cube" in curr_ques:
                        x = random.randint(1,100)
                        res = x**3
                        await ctx.send("cube of "+str(x))
                        run = True
                        while run:
                                answer = await client.wait_for('message',timeout=600)
                                if str(res) in answer.content:
                                        await ctx.send("You got it correct "+str(ctx.message.author))
                                        run = False
                                        questions.remove('cube')
@client.command(name='play', help='This command plays songs')
async def play(ctx):
    global queue

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        print(queue)
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])
@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()
@client.command(name='join', help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()
@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()
@client.command(pass_context=True)
async def about(ctx):
        embed = discord.Embed(
                colour=discord.Colour.orange()
                )
        lol = discord.Embed(
                colour=discord.Colour.orange()
                )
        embed.set_author(name="Elon here to help you.Have Fun!!!")
        embed.add_field(name="roll",value="Rolls a dice :game_die:",inline=False)
        embed.add_field(name="reddits",value="Get 10 posts from your favourite subreddit! :smiley:",inline=False)
        embed.add_field(name="reddit",value="Get a post from your favourite subreddit :smile:",inline=False)
        embed.add_field(name="helpme",value="Use wikipedia to get answer to your queries :wink:",inline=False)
        embed.add_field(name="elon",value="Get Elon Musk :nerd:",inline=False)
        embed.add_field(name="pewds",value="Get PewDiePie :smiley:",inline=False)
        embed.add_field(name="areyoumad",value="No! :-1:",inline=False)
        embed.add_field(name="meme",value="Get one meme :smiley:",inline=False)
        embed.add_field(name="memes",value="Whats better than a meme TEN MEMES!!! :sunglasses:",inline=False)
        embed.add_field(name="memebonanza",value="Whats better than a meme HUNDRED MEMES!!! :sunglasses:",inline=False)
        embed.add_field(name="memesforlife",value="150 minutes of memes :sunglasses:",inline=False)
        embed.add_field(name="amlonely",value="Get emotional support :sob:",inline=False)
        embed.add_field(name="dota",value="To get a Dota 2 post :video_game:",inline=False)
        embed.add_field(name="hi",value="Get a greeting! :wave:",inline=False)
        embed.add_field(name="funfact",value="Get a funfact :nerd:",inline=False)
        embed.add_field(name="ban",value="Ban members :stop_sign:",inline=False)
        embed.add_field(name="kick",value="Kick members :athletic_shoe:",inline=False)
        embed.add_field(name="knock",value="To give someone my classic three knocks :clap:",inline=False)
        embed.add_field(name="trans",value="Translate:secret:",inline=False)
        embed.add_field(name="ping",value="Check bot's latency! :table_tennis:",inline=False)
        embed.add_field(name="weather",value="Check your city's weather :cloud:",inline=False)
        embed.add_field(name="twitter",value="Check your favourite celeb's recent Twitter posts :bird:",inline=False)
        embed.add_field(name="tunak",value=".",inline=False)
        embed.add_field(name="dictionary",value="Get the meaning synonym and antonym",inline=False)
        embed.add_field(name="google",value="I think the command tells what happens",inline=False)
        lol.add_field(name="gif",value="Send GIFS",inline=False)
        lol.add_field(name="learnpython",value="Learn python basics a bit different from IDLE but still explains the concept",inline=False)
        lol.add_field(name="rot",value="Rotate Elon by a certain angle",inline=False)
        lol.add_field(name="communist",value="Join CP",inline=False)
        lol.add_field(name="drake",value="Drake meme",inline=False)
        lol.add_field(name="cry",value="Chad meme",inline=False)
        lol.add_field(name="spongy",value="Spongebob meme",inline=False)
        lol.add_field(name="dumbo",value=".",inline=False)
        lol.add_field(name="royalpoo",value="royalpoo memes",inline=False)
        lol.add_field(name="firsttime",value="first time memes",inline=False)
        lol.add_field(name="mathgame",value="Math Probs.Didn't your teacher tell maths is everywhere",inline=False)
        lol.add_field(name="occupation",value="Gives you a job.Bye Bye Unemployment",inline=False)
        lol.add_field(name="reoccupation",value="Not happy with you job no problem take another one",inline=False)
        lol.add_field(name="whatami",value="Tells your occupation",inline=False)
        lol.add_field(name="rememberme",value="Remembers your name",inline=False)
        lol.add_field(name="whoami",value="Tells your name",inline=False)
        lol.add_field(name="queue",value="Make a playlist",inline=False)
        lol.add_field(name="join",value="Join voice channel",inline=False)
        lol.add_field(name="play",value="Play playlist",inline=False)
        lol.add_field(name="pause",value="Pause playlist",inline=False)
        lol.add_field(name="resume",value="Resume playlist",inline=False)
        lol.add_field(name="stop",value="Stop playlist",inline=False)
        await ctx.send(embed=embed)
        await ctx.send(embed=lol)
client.run('NzM1MzgzMzY0ODM1NjA2NjEx.XxfdaA.4694YNQWEC9OTy9Wd1Gwxq6ejDM')	

