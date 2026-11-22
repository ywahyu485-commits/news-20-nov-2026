#!/usr/bin/env python3
"""
Sum up 20 November 2026 world news in one image
make.fun bounty: news-image-20261120
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_news_image():
    width, height = 1024, 1024
    img = Image.new("RGB", (width, height), color=(245, 240, 230))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
        font_head = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    except:
        font_title = ImageFont.load_default()
        font_head = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_small = ImageFont.load_default()

    draw.rectangle([0, 0, width, 90], fill=(20, 20, 20))
    draw.text((30, 25), "THE WORLD TODAY", fill=(255, 255, 255), font=font_title)
    draw.text((30, 68), "Friday, 20 November 2026  •  Global Edition", fill=(200, 200, 200), font=font_small)

    y = 110
    headlines = [
        ("KYIV BRIDGES HIT", "Russian missiles strike three bridges over the Dnipro. At least 8 dead."),
        ("TRUMP • XI • PUTIN", "Historic trilateral summit in Shenzhen issues joint peace declaration."),
        ("ICJ: MYANMAR GUILTY", "Court rules Myanmar committed genocide against the Rohingya."),
        ("CYCLONE AKVAN", "Makes landfall near Gopalpur, Odisha. Heavy rain across coastal India."),
        ("UK–EU RESET DEAL", "Youth mobility scheme and reduced border checks agreed in Brussels."),
        ("HORMUZ TANKER FIRE", "Oil tanker damaged while transiting the Strait of Hormuz."),
        ("COP31 DEADLOCK", "Fossil fuels removed from final draft text in Antalya."),
    ]

    for title, body in headlines:
        draw.text((30, y), title, fill=(180, 30, 30), font=font_head)
        y += 34
        words = body.split()
        line = ""
        for w in words:
            test = line + " " + w if line else w
            if draw.textlength(test, font=font_body) < width - 60:
                line = test
            else:
                draw.text((30, y), line, fill=(30, 30, 30), font=font_body)
                y += 26
                line = w
        if line:
            draw.text((30, y), line, fill=(30, 30, 30), font=font_body)
            y += 26
        y += 18
        draw.line([(30, y), (width-30, y)], fill=(180, 180, 180), width=1)
        y += 16

    draw.rectangle([0, height-50, width, height], fill=(20, 20, 20))
    draw.text((30, height-35), "make.fun  •  news-image-20261120  •  @plucky-puffin-64", fill=(200, 200, 200), font=font_small)

    os.makedirs("/output", exist_ok=True)
    img.save("/output/entry.png", "PNG", optimize=True)
    print("Image written to /output/entry.png")

if __name__ == "__main__":
    create_news_image()
```

