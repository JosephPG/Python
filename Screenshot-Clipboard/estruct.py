from ctypes import Structure, POINTER, pointer
from ctypes.wintypes import DWORD, LONG, WORD

class DIB(Structure):
    _fields_ = [("biSize", DWORD), ("biWidth", LONG), ("biHeight", LONG),
                ("biPlanes", WORD), ("biBitCount", WORD), ("biCompression", DWORD),
                ("biSizeImage", DWORD), ("biXPelsPerMeter", LONG), ("biYPelsPerMeter", LONG),
                ("biClrUsed", DWORD), ("biClrImportant", DWORD)]

				
class HEADER(Structure):
    _fields_ = [("type", WORD), ("bfSize", DWORD), ("reserved", DWORD), ("offset", DWORD)]