from discord import FFmpegPCMAudio
from discord.ext import commands
import yt_dlp as youtube_dl

ytdl_format_options = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'noplaylist': True,
    'quiet': True
}

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url):
        if not ctx.author.voice:
            await ctx.send("¡Entra a un canal de voz primero! ( ˶°ㅁ°) !!")
            return

        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()

        ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
        data = ytdl.extract_info(url, download=False)

        if 'entries' in data:  
            data = data['entries'][0]

        audio_url = data['url']
        source = FFmpegPCMAudio(audio_url)
        voice_client.play(source)

        await ctx.send(f"🎵 **Reproduciendo (づ> v <)づ♡** {data['title']}")

async def setup(bot):
    await bot.add_cog(Music(bot))