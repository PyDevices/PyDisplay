# -*- coding: utf-8 -*-
# Converted from Chango-Regular.ttf using:
#     ./write_font_converter.py Chango-Regular.ttf 16 -c 0x20-0x7f

MAP = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
BPP = 1
HEIGHT = 17
MAX_WIDTH = 24
_WIDTHS = (
    b"\x06\x08\x0a\x0e\x0d\x18\x10\x06\x08\x08\x0a\x0d\x06\x08\x06\x0b"
    b"\x0e\x0a\x0e\x0d\x0e\x0c\x0e\x0d\x0d\x0d\x06\x06\x0c\x0c\x0b\x0b"
    b"\x18\x11\x10\x0d\x0e\x0e\x0d\x0e\x11\x09\x0b\x11\x0e\x12\x0f\x11"
    b"\x0e\x11\x0f\x0d\x0d\x0e\x0f\x17\x10\x0f\x0e\x08\x0b\x08\x0b\x0c"
    b"\x07\x0d\x0d\x0b\x0d\x0c\x0a\x0d\x0e\x07\x08\x0e\x07\x14\x0e\x0d"
    b"\x0d\x0d\x0b\x0a\x0b\x0e\x0c\x12\x0d\x0c\x0b\x09\x06\x09\x0e\x0b"
)

OFFSET_WIDTH = 2
_OFFSETS = (
    b"\x00\x00\x00\x66\x00\xee\x01\x98\x02\x86\x03\x63\x04\xfb\x06\x0b"
    b"\x06\x71\x06\xf9\x07\x81\x08\x2b\x09\x08\x09\x6e\x09\xf6\x0a\x5c"
    b"\x0b\x17\x0c\x05\x0c\xaf\x0d\x9d\x0e\x7a\x0f\x68\x10\x34\x11\x22"
    b"\x11\xff\x12\xdc\x13\xb9\x14\x1f\x14\x85\x15\x51\x16\x1d\x16\xd8"
    b"\x17\x93\x19\x2b\x1a\x4c\x1b\x5c\x1c\x39\x1d\x27\x1e\x15\x1e\xf2"
    b"\x1f\xe0\x21\x01\x21\x9a\x22\x55\x23\x76\x24\x64\x25\x96\x26\x95"
    b"\x27\xb6\x28\xa4\x29\xc5\x2a\xc4\x2b\xa1\x2c\x7e\x2d\x6c\x2e\x6b"
    b"\x2f\xf2\x31\x02\x32\x01\x32\xef\x33\x77\x34\x32\x34\xba\x35\x75"
    b"\x36\x41\x36\xb8\x37\x95\x38\x72\x39\x2d\x3a\x0a\x3a\xd6\x3b\x80"
    b"\x3c\x5d\x3d\x4b\x3d\xc2\x3e\x4a\x3f\x38\x3f\xaf\x41\x03\x41\xf1"
    b"\x42\xce\x43\xab\x44\x88\x45\x43\x45\xed\x46\xa8\x47\x96\x48\x62"
    b"\x49\x94\x4a\x71\x4b\x3d\x4b\xf8\x4c\x91\x4c\xf7\x4d\x90\x4e\x7e"
)

_BITMAPS = (
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x61"
    b"\xf9\xf9\xf9\xf8\xf0\xf0\xf0\x00\xf0\xf0\xf0\x00\x00\x00\x00\x00"
    b"\x1d\xc7\x71\xdc\x33\x0c\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x03\x98\x0c\x60\xff\xe3\xff\x8f"
    b"\xfc\x1c\xe1\xff\xc7\xff\x0e\x30\x18\xc0\x67\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\xe0\x07\x00\xff\x1f\xfc\xff\xc7\xf0\x3f\xe0\xff\x81"
    b"\xfe\x47\xf3\xff\x9f\xfc\x7f\x80\x70\x03\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x03\xf0\x3c\x07\xf8\x78\x07\x38\xf0\x07\x39"
    b"\xe0\x07\xfb\xc4\x03\xf7\x9f\x80\x0f\x3f\xc0\x1f\x3b\xc0\x3e\x3b"
    b"\xc0\x7c\x3f\x80\x78\x1f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x70\x03\xfe\x07\xfe\x0f\xc0\x0f\xc0\x07\xff\xc7"
    b"\xff\xcf\xff\x8f\xcf\x8f\xef\x8f\xff\xc7\xff\xc0\x00\x00\x00\x00"
    b"\x00\x00\x00\xe3\x8e\x18\x60\x00\x00\x00\x00\x00\x00\x00\x07\x8f"
    b"\x0f\x1e\x1e\x3c\x3c\x3c\x3c\x3c\x3c\x3c\x1e\x1e\x0f\x0f\x07\xb8"
    b"\x3c\x1e\x1e\x0f\x0f\x0f\x0f\x0f\x8f\x0f\x0f\x0f\x1e\x1e\x3c\x38"
    b"\x00\x00\x00\x60\x18\x16\x8f\xf0\xf8\x3c\x1f\x82\x40\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x0e\x00\x70\x03"
    b"\x81\xff\x8f\xfe\x3f\xe0\x38\x01\xc0\x0e\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x79\xe3\x18\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x01\xf9\xf8\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x79\xe7\x00\x00\x00\x1c\x07\x80\xf0"
    b"\x1c\x07\x80\xf0\x1c\x07\x80\xf0\x3c\x07\x80\xf0\x3c\x07\x80\xf0"
    b"\x3c\x07\x80\x00\x00\x00\x00\x60\x0f\xf0\x7f\xe3\xff\xcf\x9f\x3e"
    b"\x7c\xf9\xf3\xe7\xcf\x9f\x3f\xfc\x7f\xe0\x7f\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x03\xf3\xfc\xff\x1f\xc7\xf1\xfc\x7f\x1f\xc7\xf1"
    b"\xfc\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x40\x1f\xf0\xff\xe3\x3f"
    b"\x80\x7e\x01\xf8\x0f\xc0\x7e\x03\xf0\x3f\xfc\xff\xf3\xff\xc0\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x06\x03\xfe\x3f\xf1\x9f\xc0\x7c\x3f"
    b"\xc1\xff\x01\xfc\x0f\xe7\xff\x3f\xf9\xff\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x3f\x01\xfe\x0f\xf8\x7f\xe3\xbf\x9c\xfe\x7f"
    b"\xfd\xff\xf7\xff\x80\xfe\x03\xf0\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x03\xfe\x3f\xc3\xc0\x3c\x03\xfc\x3f\xe0\x7e\x07\xe7\xfe\x7f"
    b"\xe7\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xc1\xff\x0f"
    b"\xfc\x3f\x01\xff\x87\xff\x1f\xbe\x7c\xf9\xf3\xe3\xff\x07\xf8\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf9\xff\xc0\xfc\x07\xe0"
    b"\x7e\x03\xf0\x3f\x03\xf8\x1f\x81\xfc\x0f\xc0\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x01\x80\x7f\x87\xbc\x7d\xf3\xff\x0f\xf0\xff\xe7\xff"
    b"\x3c\xf9\xff\xcf\xfc\x3f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x03\xf8\x3f\xe3\xef\x9f\x7c\xfb\xf7\xff\x1f\xf8\x0f\xc0\xfc\x3f"
    b"\xc1\xfc\x00\x00\x00\x00\x00\x00\x00\x06\x3c\xf1\x80\x00\x00\x0f"
    b"\x3c\xe0\x00\x00\x00\x00\x18\xf3\xc6\x00\x00\x00\x3c\xf3\xc6\x30"
    b"\x00\x00\x00\x00\x00\x00\x00\x0e\x03\xe0\xfc\x3f\x03\xe0\x1f\x80"
    b"\x7e\x01\xe0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x03\xff\x3f\xf0\x00\x00\x03\xff\x3f\xf3\xff\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x07\xc0\x7e\x03\xf0\x1e"
    b"\x0f\xc7\xc1\xe0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x3f"
    b"\xcf\xf8\x8f\x83\xe0\xf0\x3c\x07\x80\x00\x1e\x03\xc0\x78\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xf0\x00\x7f\xfe\x01\xf0"
    b"\x1f\x83\xc0\x07\x87\x9f\xf3\xc7\xbf\xf3\xcf\x3d\xf3\xcf\x3d\xf3"
    b"\xcf\x3d\xf3\xcf\x3f\xff\x8f\xbe\xff\x07\xc8\x38\x07\xe3\x80\x03"
    b"\xff\x80\x00\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x80\x0f\xe0"
    b"\x07\xf0\x07\xfc\x03\x7f\x03\xbf\x81\x8f\xe1\xff\xf1\xff\xfc\xe0"
    b"\xff\x70\x3f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07"
    b"\xff\x87\xff\xc7\xe7\xc7\xf7\xc7\xff\x87\xff\xc7\xe3\xe7\xe3\xe7"
    b"\xe7\xe7\xff\xc7\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e"
    b"\x03\xfe\x3f\xf3\xfc\x9f\xc1\xfc\x0f\xe0\x7f\x01\xfc\x0f\xff\x3f"
    b"\xf8\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xfc\x3f\xf8"
    b"\xff\xf3\xf9\xef\xe7\xbf\x9e\xfe\x7b\xff\xcf\xff\x3f\xf8\xff\x80"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\xff\xf3\xf8\x0f"
    b"\xe0\x3f\xf0\xff\xe3\xf8\x0f\xe0\x3f\x80\xff\xf3\xff\xc0\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x07\xff\x3f\xfd\xfc\x0f\xe0\x7f\xe3"
    b"\xff\x1f\xc0\xfc\x07\xe0\x3f\x01\xf8\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x01\xff\x8f\xfe\x7f\x89\xfc\x07\xf0\x1f\x9e\x7f\x79"
    b"\xfd\xe7\xff\x8f\xfe\x1f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x0f\xc7\xe7\xe3\xf3\xf1\xf9\xf8\xfe\xfc\x7f\x7f\xff\xbf"
    b"\xff\xdf\xff\xcf\xe7\xe7\xe3\xf3\xf1\xf8\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x07\xf3\xf9\xfc\xfe\x7f\x3f\x9f\xcf\xe7\xf3\xf9\xf8"
    b"\x00\x00\x00\x00\x00\x00\x00\x03\xf0\x7f\x0f\xe1\xfc\x3f\x87\xf0"
    b"\xfc\x1f\x87\xf1\xfc\x3f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x7e\x1e\x3f\x9e\x1f\xde\x0f\xfe\x07\xfe\x03\xff\x81\xff\xe0"
    b"\xff\xf8\x7f\x7e\x3f\xbf\x9f\xcf\xc0\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x7e\x01\xfc\x07\xf0\x1f\xc0\x7f\x01\xfc\x07\xf0"
    b"\x1f\xc0\x7f\xf9\xff\xf7\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x1f\x03\xe7\xe0\xf9\xfc\x7e\x7f\xbf\x9f\xff\xe7\xff"
    b"\xf9\xff\xfe\x77\xdf\x9d\xf7\xe7\x39\xf9\xc6\x7e\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x83\xdf\x87\xbf\xcf\x7f\xfe"
    b"\xff\xfd\xff\xfb\xff\xf7\xff\xef\x7f\xde\x3f\xbc\x3e\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x03\x80\x0f\xf8\x1f\xff\x0f\xff\x8f"
    b"\xe3\xe7\xe0\xf3\xf0\x79\xfc\x7c\xff\xfc\x3f\xfe\x0f\xfe\x03\xfc"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xf1\xff\xe7"
    b"\xff\x9f\xcf\x7f\x3d\xfc\xf7\xff\x9f\xfc\x7f\x01\xfc\x07\xf0\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x1f\xf0\x3f\xfe\x1f"
    b"\xff\x1f\xc7\xcf\xc1\xe7\xe0\xf3\xf8\xf9\xff\xf8\x7f\xfc\x1f\xff"
    b"\x87\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xfc"
    b"\x3f\xfc\x7f\xf8\xfe\x79\xfc\xf3\xf9\xe7\xff\x8f\xfe\x1f\xfc\x3f"
    b"\xbc\x7f\x7c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x07\xfc\x7f"
    b"\xf3\xf9\x1f\xc0\x7f\x81\xfe\x07\xf9\x1f\xcf\xfe\x7f\xf1\xfe\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xfb\xff\xdf\xfe\x3f\x81"
    b"\xfc\x0f\xe0\x7f\x03\xf8\x1f\xc0\xfe\x03\xf0\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x7e\x39\xf8\xe7\xe3\x9f\x8f\x7e\x3d\xf8\xf7"
    b"\xe3\x9f\xfe\x7f\xf8\xff\xc0\xfe\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x7f\x07\x7f\x1c\xfe\x38\xfc\xe1\xfd\xc1\xff\x03\xfe"
    b"\x03\xfc\x07\xf0\x07\xe0\x0f\x80\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x7e\x00\x1c\xfe\x7e\x71\xfc\xfc\xe3\xfb"
    b"\xfd\xc3\xf7\xff\x07\xff\xfe\x07\xfb\xfc\x0f\xf7\xf0\x0f\xef\xe0"
    b"\x1f\x8f\xc0\x1f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x1f\xe3\xdf\xf7\x8f\xff\x07\xfe\x03\xfc\x01\xfe"
    b"\x03\xfe\x07\xff\x07\x7f\x8e\x3f\xdc\x1f\xc0\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x01\xfe\x3d\xfc\x73\xfd\xc3\xff\x03\xfe\x07"
    b"\xf8\x07\xf0\x0f\xe0\x1f\xc0\x3f\x80\x7f\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x0f\xff\x3f\xfc\x1f\xf0\x7f\x83\xfc\x1f\xf0"
    b"\x7f\x83\xfc\x0f\xfe\x3f\xfc\xff\xf0\x00\x00\x00\x00\x00\xfc\xfc"
    b"\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xfc\xfc\xf0"
    b"\x1e\x01\xe0\x3c\x07\x80\x78\x0f\x01\xe0\x1e\x03\xc0\x38\x07\x80"
    b"\xf0\x0e\x01\xe0\x3c\x03\x9f\x9f\x83\x83\x83\x83\x83\x83\x83\x83"
    b"\x83\x83\x83\x83\x83\x9f\x9f\x80\x00\x00\x00\x00\x00\x30\x07\x01"
    b"\xe0\x3e\x0e\xc1\x9c\x71\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x03\xff\x3f\xf0\x00\x00\x00\x60\xe0\xe0\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\xff\x87\xfe\x01\xf1\xff\x9e\x7c\xf3\xe7\xff\x3e\xf8\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\xf8\x07\xc0\x3e\x01\xf0\x0f\xfc\x7f\xf3"
    b"\xff\x9f\x3e\xf9\xe7\xff\x3f\xf9\xff\x80\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x01\xfc\x7f\x9f\x93\xe0\x7c\x0f\xc9\xff"
    b"\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x01\xe0\x1f\x00\xf8\x07\xc7"
    b"\xfe\x7f\xf3\xef\x9e\x7c\xf3\xe7\xff\x3f\xf8\xfb\xc0\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\xff\x9f\x39\xff"
    b"\x9f\xf1\xf0\x1f\xf8\x7f\x80\x00\x00\x00\x00\x00\x00\x03\xe3\xfd"
    b"\xff\x7c\x1f\xcf\xf9\xf0\x7c\x1f\x07\xc1\xf0\x7c\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xcf\xfe\x7d\xf3\xcf"
    b"\x9e\x7c\xff\xe7\xff\x1e\xf9\x07\xcf\xfe\x3f\xe0\x00\x00\x00\x3e"
    b"\x00\xf8\x03\xe0\x0f\x80\x3e\xf8\xff\xf3\xff\xcf\x9f\x3e\x7c\xf9"
    b"\xf3\xe7\xcf\x9f\x00\x00\x00\x00\x00\x00\x00\x1c\x7c\xf8\x03\xe7"
    b"\xcf\x9f\x3e\x7c\xf9\xf0\x00\x00\x00\x00\x07\x0f\x87\x80\x0f\x8f"
    b"\x8f\x8f\x8f\x8f\x8f\x8f\x9f\xbf\x3c\x00\x00\x00\x01\xf0\x07\xc0"
    b"\x1f\x00\x7c\x01\xf3\xc7\xde\x1f\xf0\x7f\xc1\xff\x87\xff\x1f\x7c"
    b"\x7c\xf8\x00\x00\x00\x00\x00\x00\x01\xf3\xe7\xcf\x9f\x3e\x7c\xf9"
    b"\xf3\xe7\xcf\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\xfb\xef\xcf\xff\xfc\xff\xff\xef\x9f\x3e\xf9"
    b"\xf3\xef\x9f\x3e\xf9\xf3\xef\x9f\x3e\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfb\xe3\xff\xcf\xff"
    b"\x3e\x7c\xf9\xf3\xe7\xcf\x9f\x3e\x7c\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xc7\xff\x3e\xf9\xf3\xef\x9f"
    b"\x7d\xf3\xff\x8f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x07\xfe\x3f\xf9\xff\xcf\x9f\x7c\xf3\xff\x9f\xfc\xfb"
    b"\xc7\xc0\x3e\x01\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f"
    b"\xf9\xff\xcf\xbe\x79\xf3\xcf\x9f\xfc\xff\xe3\xff\x00\xf8\x07\xc0"
    b"\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x73\xff\x7f\xcf\x81\xf0"
    b"\x3e\x07\xc0\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x7f\x3f\xcf\x83\xfc\x7f\x87\xef\xfb\xfc\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x0f\x03\xe1\xff\x1f\xe1\xf0\x3e\x07\xc0\xfd\x1f\xe1"
    b"\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07"
    b"\xcf\x9f\x3e\x7c\xf9\xf3\xe7\xcf\x9f\xfe\x7f\xf8\xfb\xe0\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xf1\xdf\x19\xfb"
    b"\x8f\xb0\xff\x07\xe0\x7e\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf3\xc7\x7c\xf9\xdf\x3e"
    b"\xe3\xff\xf8\xff\xfc\x1f\xbf\x07\xef\xc1\xf3\xe0\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\x1c\xfd\xc3"
    b"\xfc\x0f\xc0\x3f\x03\xfc\x3b\xf7\x8f\xc0\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x7e\x3b\xe3\x3f\x71\xf6\x1f\xe0\xfe"
    b"\x0f\xc0\x7c\x07\x83\xf0\x3e\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\xff\x9f\xf0\x7c\x1f\x07\xe1\xf8\x3f\xe7\xfc\x00\x00\x00\x00\x0f"
    b"\x1f\x8f\x8f\x83\xc1\xe0\xf0\x70\x78\x1e\x0f\x07\x83\xc3\xe0\xf8"
    b"\x7e\x0e\x38\xf3\xcf\x3c\xf3\xcf\x3c\xf3\xcf\x3c\xf3\xcf\x38\xf0"
    b"\x7c\x1f\x07\x83\xc1\xe0\xe0\x78\x1e\x1e\x0e\x07\x83\xc1\xe1\xf1"
    b"\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc1\x0f\xcc"
    b"\x3f\xf1\x8f\x80\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x00\x07\xf0\xff\x30\x24\x04\xf8\x9c\x33\x8e\x7f\xce\x79\xc7"
    b"\x3d\xe3\xfc\x00\x00\x00\x00\x00"
)

WIDTHS = memoryview(_WIDTHS)
OFFSETS = memoryview(_OFFSETS)
BITMAPS = memoryview(_BITMAPS)
