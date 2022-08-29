import random
import discord
from discord.ext import commands
import aiohttp
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw, ImageFont
from io import BytesIO
import os
class Image_Manipulation:
    def __init__(self):
        self.colors = ['aliceblue', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'forestgreen', 'fuchsia', 'gainsboro', 'gold', 'goldenrod', 'gray', 'grey', 'green', 'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgreen', 'lightgray', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 
        'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 
        'slateblue', 'slategray', 'slategrey', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'yellow', 'yellowgreen']
    def sideway_text(self, text, image, width, height, font):
        txt=Image.new('L', (500,50))
        d = ImageDraw.Draw(txt)
        d.text( (0, 0), text,  font=font, fill=255)
        w=txt.rotate(random.randint(10,180),  expand=1)
        image.paste(ImageOps.colorize(w, white=random.choice(self.colors), black="black"), (int(height / random.randint(1, 5)), int(width / random.randint(1,5))), w)
    def __call__(self, image, name):
        width, height = image.size
        font = ImageFont.truetype("arial.ttf", size=int(height / 25))
        self.sideway_text(str(name), image, width, height, font)
        for i in range(0, random.randint(1, 9)):
            self.sideway_text(str(i), image, width, height, font)
        try:
            image = ImageOps.autocontrast(image, cutoff=5)
        except OSError:
            pass
        image = ImageEnhance.Contrast(image).enhance(5)
        image = image.filter(ImageFilter.BLUR)
        image = ImageEnhance.Sharpness(image).enhance(5)
        image = ImageEnhance.Brightness(image).enhance(5)
        image = ImageEnhance.Color(image).enhance(5)
        image = image.filter(ImageFilter.MinFilter(size=5))
        try:
            image = ImageOps.invert(image)
        except OSError:
            pass
        return image
class Images(commands.Cog):
    """Image Manipulation"""
    def __init__(self, bot) -> None:
        self.bot = bot
    @commands.command(name='deepfry', brief='Deepfries an image.', aliases=['deepfryimg', 'deepfryimage'])
    async def deepfry(self, ctx, *, image:discord.Message):
        """>deepfry <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img_ma = Image_Manipulation()
                img = img_ma(img, ctx.author.name)
                img.save('deepfry.png')
                await ctx.send(file=discord.File('deepfry.png'))
                os.remove('deepfry.png')
    @commands.command(name='blur', brief='Blurs an image.', aliases=['blurimg', 'blurimage'])
    async def blur(self, ctx, *, image:discord.Message):
        """>blur <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.GaussianBlur(radius=2))
                img = img.convert('RGB')
                img.save('blur.png')
                await ctx.send(file=discord.File('blur.png'))
                os.remove('blur.png')
    @commands.command(name='emboss', brief='Embosses an image.', aliases=['embossimg', 'embossimage'])
    async def emboss(self, ctx, *, image:discord.Message):
        """>emboss <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.EMBOSS)
                img = img.convert('RGB')
                img.save('emboss.png')
                await ctx.send(file=discord.File('emboss.png'))
                os.remove('emboss.png')
    @commands.command(name='edge', brief='Edges an image.', aliases=['edgeimg', 'edgeimage'])
    async def edge(self, ctx, *, image:discord.Message):
        """>edge <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.FIND_EDGES)
                img = img.convert('RGB')
                img.save('edge.png')
                await ctx.send(file=discord.File('edge.png'))
                os.remove('edge.png')
    @commands.command(name='invert', brief='Inverts an image.', aliases=['invertimg', 'invertimage'])
    async def invert(self, ctx, *, image:discord.Message):
        """>invert <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.INVERT)
                img = img.convert('RGB')
                img.save('invert.png')
                await ctx.send(file=discord.File('invert.png'))
                os.remove('invert.png')
    @commands.command(name='pixelate', brief='Pixelates an image.', aliases=['pixelateimg', 'pixelateimage'])
    async def pixelate(self, ctx, *, image:discord.Message):
        """>pixelate <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.PIXELATE)
                img = img.convert('RGB')
                img.save('pixelate.png')
                await ctx.send(file=discord.File('pixelate.png'))
                os.remove('pixelate.png')
    @commands.command(name='rotate', brief='Rotates an image.', aliases=['rotateimg', 'rotateimage'])
    async def rotate(self, ctx, *, image:discord.Message):
        """>rotate <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.rotate(random.randint(0, 360))
                img = img.convert('RGB')
                img.save('rotate.png')
                await ctx.send(file=discord.File('rotate.png'))
                os.remove('rotate.png')
    @commands.command(name='saturate', brief='Saturates an image.', aliases=['saturateimg', 'saturateimage'])
    async def saturate(self, ctx, *, image:discord.Message):
        """>saturate <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.SATURATE)
                img = img.convert('RGB')
                img.save('saturate.png')
                await ctx.send(file=discord.File('saturate.png'))
                os.remove('saturate.png')
    @commands.command(name='sharpen', brief='Sharpen an image.', aliases=['sharpenimg', 'sharpenimage'])
    async def sharpen(self, ctx, *, image:discord.Message):
        """>sharpen <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.SHARPEN)
                img = img.convert('RGB')
                img.save('sharpen.png')
                await ctx.send(file=discord.File('sharpen.png'))
                os.remove('sharpen.png')
    @commands.command(name='smooth', brief='Smooths an image.', aliases=['smoothimg', 'smoothimage'])
    async def smooth(self, ctx, *, image:discord.Message):
        """>smooth <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.SMOOTH)
                img = img.convert('RGB')
                img.save('smooth.png')
                await ctx.send(file=discord.File('smooth.png'))
                os.remove('smooth.png')
    @commands.command(name='swirl', brief='Swirls an image.', aliases=['swirlimg', 'swirlimage'])
    async def swirl(self, ctx, *, image:discord.Message):
        """>swirl <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.SWIRL)
                img = img.convert('RGB')
                img.save('swirl.png')
                await ctx.send(file=discord.File('swirl.png'))
                os.remove('swirl.png')
    @commands.command(name='tint', brief='Tints an image.', aliases=['tintimg', 'tintimage'])
    async def tint(self, ctx, *, image:discord.Message):
        """>tint <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.TINT)
                img = img.convert('RGB')
                img.save('tint.png')
                await ctx.send(file=discord.File('tint.png'))
                os.remove('tint.png')
    @commands.command(name='vignette', brief='Vignettes an image.', aliases=['vignetteimg', 'vignetteimage'])
    async def vignette(self, ctx, *, image:discord.Message):
        """>vignette <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.VIGNETTE)
                img = img.convert('RGB')
                img.save('vignette.png')
                await ctx.send(file=discord.File('vignette.png'))
                os.remove('vignette.png')
    @commands.command(name='wave', brief='Waves an image.', aliases=['waveimg', 'waveimage'])
    async def wave(self, ctx, *, image:discord.Message):
        """>wave <image>"""
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(image.attachments[0].url) as resp:
                image = await resp.read()
                img = Image.open(BytesIO(image))
                img = img.convert('RGB')
                img = img.resize((250, 250))
                img = img.filter(ImageFilter.WAVE)
                img = img.convert('RGB')
                img.save('wave.png')
                await ctx.send(file=discord.File('wave.png'))
                os.remove('wave.png')
def setup(bot):
    bot.add_cog(Image(bot))
    print('Image cog is loaded.')