#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import os

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import api_request as api

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("--- mkapra Display ---")
    epd = epd7in5_V2.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    # Draw Username
    logging.info("1. Drawing Username...")
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'Statusboard  --  Maximilian Kapra (mkapra@)', font = font24, fill = 0)
    # Underline username
    draw.line((10, 30, 500, 30), fill = 0)

    # Draw server online status
    logging.info("2. Server online status...")
    x_start = 10
    x_end = 40
    y_start = 50
    y_end = 80
    for server, status in api.get_servers().items():
        if status:
            draw.arc((x_start, y_start, x_end, y_end), 0, 360, fill=0, width=200)
        else:
            draw.arc((x_start, y_start, x_end, y_end), 0, 360, fill=0)

        draw.text((x_start + x_end, y_start + 1), server, font = font24, fill = 0)

        y_start += 40
        y_end += 40

    logging.info("3. Mail status...")
    count, not_ok = api.get_mail_status_stats()
    draw.text((x_start, y_start + 2), f"Mailserver: {count - len(not_ok)} of {count} services running", font = font24, fill = 0)

    epd.display(epd.getbuffer(Himage))

    # logging.info("3.read bmp file")
    # Himage = Image.open(os.path.join(picdir, '7in5_V2.bmp'))
    # epd.display(epd.getbuffer(Himage))
    # time.sleep(2)

    # logging.info("4.read bmp file on window")
    # Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    # bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    # Himage2.paste(bmp, (50,10))
    # epd.display(epd.getbuffer(Himage2))
    # time.sleep(2)

    logging.info("Goto Sleep...")
    epd.sleep()
    # time.sleep(3)

    # epd.Dev_exit()
except IOError as e:
    logging.info(e)
except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()
